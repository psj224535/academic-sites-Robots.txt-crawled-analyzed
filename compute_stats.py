import json

with open('analysis_results_expanded.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out failed ones
valid_data = [d for d in data if "Failed to fetch" not in d['notable_features']]

# Group by category
categories = {}
for d in valid_data:
    cat = d['platform_category']
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(d)

md = []
md.append("# Category Statistics: AI Bot & Scope Restrictions\n")
md.append("This document summarizes the percentage of platforms within each category that actively **Block (or Partially Block)** specific content scopes and bots. *(Failed sites are excluded from totals)*.\n")

def fmt_stat(count, total):
    if total == 0: return "-"
    pct = (count / total) * 100
    return f"{count}/{total} ({pct:.1f}%)"

# Table 1: Scope Restrictions
md.append("## 1. Scope Restrictions by Category\n")
md.append("| Category | Total Sites | Fulltext Blocked | Abstract Blocked | Search Blocked |")
md.append("|----------|:---:|:---:|:---:|:---:|")

for cat, sites in categories.items():
    total = len(sites)
    full = sum(1 for s in sites if s['scope_restrictions']['is_fulltext_pdf_blocked'])
    abs_ = sum(1 for s in sites if s['scope_restrictions']['is_abstract_blocked'])
    search = sum(1 for s in sites if s['scope_restrictions']['is_internal_search_blocked'])
    md.append(f"| **{cat}** | {total} | {fmt_stat(full, total)} | {fmt_stat(abs_, total)} | {fmt_stat(search, total)} |")

# Table 2: Training Bots
md.append("\n## 2. Training Bots Blocked by Category\n")
md.append("Includes 'Blocked' and 'Partially Blocked' statuses.\n")
md.append("| Category | Total Sites | GPTBot | ClaudeBot | CCBot | Google-Extended |")
md.append("|----------|:---:|:---:|:---:|:---:|:---:|")

def is_blocked(status):
    return status in ["Blocked", "Partially Blocked"]

for cat, sites in categories.items():
    total = len(sites)
    gpt = sum(1 for s in sites if is_blocked(s['bot_policies']['training_bots']['GPTBot']))
    claude = sum(1 for s in sites if is_blocked(s['bot_policies']['training_bots']['ClaudeBot']))
    cc = sum(1 for s in sites if is_blocked(s['bot_policies']['training_bots']['CCBot']))
    google = sum(1 for s in sites if is_blocked(s['bot_policies']['training_bots']['Google-Extended']))
    md.append(f"| **{cat}** | {total} | {fmt_stat(gpt, total)} | {fmt_stat(claude, total)} | {fmt_stat(cc, total)} | {fmt_stat(google, total)} |")

# Table 3: Search & RAG Bots
md.append("\n## 3. AI Search & User RAG Bots Blocked by Category\n")
md.append("Includes 'Blocked' and 'Partially Blocked' statuses.\n")
md.append("| Category | Total Sites | OAI-SearchBot | Claude-SearchBot | PerplexityBot | ChatGPT-User |")
md.append("|----------|:---:|:---:|:---:|:---:|:---:|")

for cat, sites in categories.items():
    total = len(sites)
    oai = sum(1 for s in sites if is_blocked(s['bot_policies']['ai_search_bots']['OAI-SearchBot']))
    cl_search = sum(1 for s in sites if is_blocked(s['bot_policies']['ai_search_bots']['Claude-SearchBot']))
    perp = sum(1 for s in sites if is_blocked(s['bot_policies']['ai_search_bots']['PerplexityBot']))
    gpt_user = sum(1 for s in sites if is_blocked(s['bot_policies']['user_rag_bots']['ChatGPT-User']))
    md.append(f"| **{cat}** | {total} | {fmt_stat(oai, total)} | {fmt_stat(cl_search, total)} | {fmt_stat(perp, total)} | {fmt_stat(gpt_user, total)} |")

artifact_path = "/Users/psj/.gemini/antigravity-ide/brain/3c0612d8-0dea-4c04-9bb8-d90f4af7df02/category_statistics.md"
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))
with open('category_statistics.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(md))
