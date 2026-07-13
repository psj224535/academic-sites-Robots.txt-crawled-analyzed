import json
import random

def get_base_domain(domain):
    parts = domain.split('.')
    if len(parts) < 2: return domain
    if len(parts) > 2 and parts[-2] in ['co', 'ac', 'edu', 'org', 'gov', 'net', 'com', 'ne']:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])

def classify_tier(base_domain):
    d = base_domain.lower()
    tier1_kw = ['elsevier', 'sciencedirect', 'cell.com', 'thelancet', 'springer', 'nature', 'wiley', 'tandfonline', 'taylorandfrancis', 'routledge', 'oup', 'oxfordjournals', 'cambridge', 'sagepub', 'ieee', 'acm.org', 'asme', 'asce', 'aip.org', 'aps.org', 'iop.org', 'rsc.org', 'acs.org', 'jamanetwork', 'nejm', 'bmj', 'karger', 'brill', 'degruyter', 'emerald', 'thieme', 'wolterskluwer', 'lww.com', 'maryannliebert', 'inderscience', 'igi-global', 'begellhouse']
    for kw in tier1_kw:
        if kw in d: return "Tier 1"

    tier2_kw = ['doaj', 'pubmed', 'nih.gov', 'pmc', 'crossref', 'plos', 'mdpi', 'frontiers', 'hindawi', 'biomedcentral', 'scielo', 'copernicus', 'peerj', 'cogentoa', 'f1000', 'elife', 'datacite', 'orcid']
    for kw in tier2_kw:
        if kw in d: return "Tier 2"
    return "Other"

def is_gptbot_blocked(robots_txt):
    if not robots_txt: return False
    lines = str(robots_txt).lower().splitlines()
    target = "gptbot"
    applying_to_target = False
    last_was_agent = False
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'): continue
        if line.startswith('user-agent:'):
            agent = line.split(':', 1)[1].strip()
            if not last_was_agent: applying_to_target = False
            if agent == target or agent == '*': applying_to_target = True
            last_was_agent = True
        elif line.startswith('disallow:'):
            last_was_agent = False
            if applying_to_target:
                parts = line.split(':', 1)
                if len(parts) > 1:
                    if parts[1].strip() in ['/', '/*']: return True
        elif line.startswith('allow:') or line.startswith('crawl-delay:') or line.startswith('sitemap:'):
            last_was_agent = False
    return False

with open("hybrid_pipeline_results.json", "r") as f:
    data = json.load(f)

consolidated = {}
for item in data:
    bd = get_base_domain(item["domain"])
    tier = classify_tier(bd)
    if tier not in ["Tier 1", "Tier 2"]: continue
    
    if bd not in consolidated:
        consolidated[bd] = {"tier": tier, "waf": False, "gptbot": False}
        
    status = item.get("status")
    if status == 403:
        consolidated[bd]["waf"] = True
    elif status == 200:
        if is_gptbot_blocked(item.get("content", "")):
            consolidated[bd]["gptbot"] = True

t1_waf = [k for k, v in consolidated.items() if v["tier"] == "Tier 1" and v["waf"]]
t1_gpt = [k for k, v in consolidated.items() if v["tier"] == "Tier 1" and not v["waf"] and v["gptbot"]]
t1_ok = [k for k, v in consolidated.items() if v["tier"] == "Tier 1" and not v["waf"] and not v["gptbot"]]

t2_waf = [k for k, v in consolidated.items() if v["tier"] == "Tier 2" and v["waf"]]
t2_gpt = [k for k, v in consolidated.items() if v["tier"] == "Tier 2" and not v["waf"] and v["gptbot"]]
t2_ok = [k for k, v in consolidated.items() if v["tier"] == "Tier 2" and not v["waf"] and not v["gptbot"]]

random.seed(42)

out = "\n\n## 📋 [부록] Tier 1 & 2 상세 기관 도메인 리스트 (검증용)\n\n"
out += "### 🏛️ Tier 1 도메인 상세\n"
out += f"**1. 방화벽(WAF 403) 차단 기관 (총 {len(t1_waf)}개):**\n"
out += ", ".join([f"`{d}`" for d in t1_waf]) + "\n\n"
out += f"**2. robots.txt GPTBot 명시적 차단 기관 (총 {len(t1_gpt)}개):**\n"
out += ", ".join([f"`{d}`" for d in t1_gpt]) + "\n\n"
out += f"**3. AI 접근을 허용하는 기타 기관 (임의 추출 5개 / 총 {len(t1_ok)}개):**\n"
out += ", ".join([f"`{d}`" for d in random.sample(t1_ok, min(5, len(t1_ok)))]) + "\n\n"

out += "### 🔓 Tier 2 도메인 상세\n"
out += f"**1. 방화벽(WAF 403) 차단 기관 (총 {len(t2_waf)}개):**\n"
out += ", ".join([f"`{d}`" for d in t2_waf]) + "\n\n"
out += f"**2. robots.txt GPTBot 명시적 차단 기관 (총 {len(t2_gpt)}개):**\n"
out += ", ".join([f"`{d}`" for d in t2_gpt]) + "\n\n"
out += f"**3. AI 접근을 허용하는 기타 기관 (전체 / 총 {len(t2_ok)}개):**\n"
out += ", ".join([f"`{d}`" for d in t2_ok]) + "\n\n"

with open("tier_analysis_results_v4.md", "a") as f:
    f.write(out)

