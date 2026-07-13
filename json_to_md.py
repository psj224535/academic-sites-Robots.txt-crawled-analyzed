import json

def bool_to_emoji(val):
    if val is True: return "✅"
    if val is False: return "❌"
    return str(val)

def bot_status(status):
    if status == "Blocked": return "🚫 Blocked"
    if status == "Partially Blocked": return "⚠️ Partial"
    if status == "Allowed": return "✅ Allowed"
    if status == "Fetch Failed": return "❌ Failed"
    return "-"

with open('analysis_results_expanded.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md = []
md.append("# Expanded `robots.txt` Analysis Results")
md.append("\n> [!NOTE]\n> This report summarizes the `robots.txt` policies for ~40 academic platforms across 5 categories. It details their default policies, explicit blocks/allowances for various AI bots, and content scope restrictions.")

md.append("\n## 1. Overview of Platforms & Scope Restrictions")
md.append("\n| Platform | Category | Default Policy (`*`) | Fulltext Blocked | Abstract Blocked | Search Blocked |")
md.append("|----------|----------|----------------------|:---:|:---:|:---:|")

for row in data:
    md.append(f"| **{row['platform_name']}** | {row['platform_category']} | {row['default_policy_asterisk']} | {bool_to_emoji(row['scope_restrictions']['is_fulltext_pdf_blocked'])} | {bool_to_emoji(row['scope_restrictions']['is_abstract_blocked'])} | {bool_to_emoji(row['scope_restrictions']['is_internal_search_blocked'])} |")

md.append("\n*(✅ = True/Blocked, ❌ = False/Not Blocked)*\n")

md.append("## 2. Bot Policies: Training Bots")
md.append("\n| Platform | GPTBot | ClaudeBot | CCBot | Google-Extended |")
md.append("|----------|:---:|:---:|:---:|:---:|")
for row in data:
    bots = row['bot_policies']['training_bots']
    md.append(f"| **{row['platform_name']}** | {bot_status(bots['GPTBot'])} | {bot_status(bots['ClaudeBot'])} | {bot_status(bots['CCBot'])} | {bot_status(bots['Google-Extended'])} |")
md.append("\n*(Note: `-` indicates \"Not Mentioned\")*\n")

md.append("## 3. Bot Policies: AI Search & User RAG Bots")
md.append("\n| Platform | OAI-SearchBot | Claude-SearchBot | PerplexityBot | ChatGPT-User |")
md.append("|----------|:---:|:---:|:---:|:---:|")
for row in data:
    ai_s = row['bot_policies']['ai_search_bots']
    rag = row['bot_policies']['user_rag_bots']
    md.append(f"| **{row['platform_name']}** | {bot_status(ai_s['OAI-SearchBot'])} | {bot_status(ai_s['Claude-SearchBot'])} | {bot_status(ai_s['PerplexityBot'])} | {bot_status(rag['ChatGPT-User'])} |")

md.append("\n## 4. Notable Features & Highlights")
md.append("\n> [!IMPORTANT]\n> The following platforms have distinct or aggressive strategies against AI scraping:\n")
for row in data:
    if "Failed" in row['notable_features']:
        md.append(f"- **{row['platform_name']}**: ❌ Failed to fetch (`robots.txt` blocked by WAF or returns 404).")
    elif row['notable_features'] != "No explicit bot rules found.":
        md.append(f"- **{row['platform_name']}**: {row['notable_features']}")

with open('/Users/psj/.gemini/antigravity-ide/brain/3c0612d8-0dea-4c04-9bb8-d90f4af7df02/robots_analysis_summary_expanded.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

with open('robots_analysis_summary_expanded.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(md))
