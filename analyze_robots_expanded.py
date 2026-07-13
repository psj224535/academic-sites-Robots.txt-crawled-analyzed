import os
import json
import re

bots_to_check = {
    "training_bots": ["GPTBot", "ClaudeBot", "CCBot", "Google-Extended"],
    "ai_search_bots": ["OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"],
    "user_rag_bots": ["ChatGPT-User", "Perplexity-User"],
    "traditional_bots": ["Googlebot"]
}

def parse_robots_txt(content):
    policies = {}
    current_agents = []
    
    for line in content.split('\n'):
        line = line.split('#')[0].strip()
        if not line:
            continue
            
        lower_line = line.lower()
        if lower_line.startswith('user-agent:'):
            agent = line[11:].strip()
            if policies.get("last_was_agent", False):
                current_agents.append(agent)
            else:
                current_agents = [agent]
            
            for a in current_agents:
                if a not in policies:
                    policies[a] = {'disallow': [], 'allow': []}
            policies["last_was_agent"] = True
        elif lower_line.startswith('disallow:'):
            policies["last_was_agent"] = False
            path = line[9:].strip()
            for a in current_agents:
                if a in policies:
                    policies[a]['disallow'].append(path)
        elif lower_line.startswith('allow:'):
            policies["last_was_agent"] = False
            path = line[6:].strip()
            for a in current_agents:
                if a in policies:
                    policies[a]['allow'].append(path)
        else:
            policies["last_was_agent"] = False
            
    if "last_was_agent" in policies:
        del policies["last_was_agent"]
    return policies

def analyze_bot_status(bot_name, policies):
    bot_policy = None
    for agent, rules in policies.items():
        if agent.lower() == bot_name.lower():
            bot_policy = rules
            break
            
    if not bot_policy:
        return "Not Mentioned"
        
    disallows = bot_policy.get('disallow', [])
    disallows = [d for d in disallows if d]
    if len(disallows) == 1 and disallows[0] == '/':
        return "Blocked"
    elif '/' in disallows:
        return "Blocked"
    elif len(disallows) > 0:
        return "Partially Blocked"
    else:
        return "Allowed"

def analyze_scope(policies):
    asterisk_policy = policies.get('*', {'disallow': [], 'allow': []})
    disallows = asterisk_policy.get('disallow', [])
    
    is_fulltext_pdf_blocked = False
    is_abstract_blocked = False
    is_internal_search_blocked = False
    
    for path in disallows:
        path_lower = path.lower()
        if any(kw in path_lower for kw in ['pdf', 'fulltext', 'download', 'epub']):
            is_fulltext_pdf_blocked = True
        if any(kw in path_lower for kw in ['abs', 'abstract', 'summary', 'article']):
            is_abstract_blocked = True
        if any(kw in path_lower for kw in ['search', 'query', 'scholar']):
            is_internal_search_blocked = True
            
    return is_fulltext_pdf_blocked, is_abstract_blocked, is_internal_search_blocked

def get_default_policy(policies):
    asterisk = policies.get('*', {})
    disallows = asterisk.get('disallow', [])
    disallows = [d for d in disallows if d]
    if not disallows:
        return "Allow All"
    if '/' in disallows:
        return "Disallow All"
    return "Specific Paths Blocked"

def process_file(filepath, name, category, url, status="success"):
    if status != "success":
        empty_bots = {group: {bot: "Fetch Failed" for bot in bots} for group, bots in bots_to_check.items()}
        return {
            "platform_name": name,
            "platform_category": category,
            "default_policy_asterisk": "Unknown",
            "bot_policies": empty_bots,
            "scope_restrictions": {
                "is_fulltext_pdf_blocked": False,
                "is_abstract_blocked": False,
                "is_internal_search_blocked": False
            },
            "notable_features": f"Failed to fetch robots.txt ({status})"
        }

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    policies = parse_robots_txt(content)
    
    bot_policies_out = {}
    for group, bots in bots_to_check.items():
        bot_policies_out[group] = {}
        for bot in bots:
            bot_policies_out[group][bot] = analyze_bot_status(bot, policies)
            
    fulltext_blocked, abstract_blocked, search_blocked = analyze_scope(policies)
    
    notable = []
    for group, bots in bots_to_check.items():
        for bot in bots:
            b_status = bot_policies_out[group][bot]
            if b_status in ["Blocked", "Partially Blocked"]:
                 notable.append(f"{bot} is {b_status}")
            elif b_status == "Allowed":
                 notable.append(f"{bot} is explicitly Allowed")
                 
    if len(notable) > 0:
         notable_str = ", ".join(notable)
    else:
         notable_str = "No explicit bot rules found."
         
    return {
        "platform_name": name,
        "platform_category": category,
        "default_policy_asterisk": get_default_policy(policies),
        "bot_policies": bot_policies_out,
        "scope_restrictions": {
            "is_fulltext_pdf_blocked": fulltext_blocked,
            "is_abstract_blocked": abstract_blocked,
            "is_internal_search_blocked": search_blocked
        },
        "notable_features": notable_str
    }

def main():
    with open('raw_robots_expanded/metadata.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)
        
    results = []
    for name, info in metadata.items():
        if info['status'] == 'success':
            filepath = os.path.join('raw_robots_expanded', f"{name}.txt")
            if os.path.exists(filepath):
                res = process_file(filepath, name, info['category'], info['url'], "success")
                results.append(res)
        else:
            res = process_file("", name, info['category'], info['url'], info['status'])
            results.append(res)
                
    with open('analysis_results_expanded.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)

if __name__ == '__main__':
    main()
