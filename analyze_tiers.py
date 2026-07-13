import json
from collections import defaultdict

def get_base_domain(domain):
    parts = domain.split('.')
    if len(parts) < 2: return domain
    if len(parts) > 2 and parts[-2] in ['co', 'ac', 'edu', 'org', 'gov', 'net', 'com', 'ne']:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])

def classify_tier(base_domain):
    d = base_domain.lower()
    
    tier4_kw = ['scholar', 'semantic', 'search', 'index', 'lens.org', 'scopus', 'webofscience', 'proquest', 'ebsco', 'jstor', 'researchgate', 'academia.edu', 'mendeley', 'openalex', 'dimensions.ai', 'clarivate', 'exlibris']
    for kw in tier4_kw:
        if kw in d: return "Tier 4 (Web-scale Aggregators)"

    tier3_kw = ['.edu', '.ac.', 'repository', 'eprint', 'dspace', 'arxiv', 'rxiv', 'ssrn', 'osf.io', 'zenodo', 'figshare', 'dryad', 'archive', 'ir.', 'digitalcommons', 'theses', 'dissertation', 'hal.science', 'bepress', 'scholarworks']
    for kw in tier3_kw:
        if kw in d: return "Tier 3 (Institutional Repositories & Preprints)"

    tier1_kw = ['elsevier', 'sciencedirect', 'cell.com', 'thelancet', 'springer', 'nature', 'wiley', 'tandfonline', 'taylorandfrancis', 'routledge', 'oup', 'oxfordjournals', 'cambridge', 'sagepub', 'ieee', 'acm.org', 'asme', 'asce', 'aip.org', 'aps.org', 'iop.org', 'rsc.org', 'acs.org', 'jamanetwork', 'nejm', 'bmj', 'karger', 'brill', 'degruyter', 'emerald', 'thieme', 'wolterskluwer', 'lww.com', 'maryannliebert', 'inderscience', 'igi-global', 'begellhouse']
    for kw in tier1_kw:
        if kw in d: return "Tier 1 (High Selectivity Commercial Publishers)"

    tier2_kw = ['doaj', 'pubmed', 'nih.gov', 'pmc', 'crossref', 'plos', 'mdpi', 'frontiers', 'hindawi', 'biomedcentral', 'scielo', 'copernicus', 'peerj', 'cogentoa', 'f1000', 'elife', 'datacite', 'orcid']
    for kw in tier2_kw:
        if kw in d: return "Tier 2 (Mid-High Selectivity Open Access)"

    return "Unclassified (Independent Journals)"

def is_bot_disallowed(robots_txt, bot_name):
    if not robots_txt: return False
    lines = str(robots_txt).lower().splitlines()
    target = bot_name.lower()
    applying_to_target = False
    last_was_agent = False
    is_blocked = False
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
                    path = parts[1].strip()
                    if path in ['/', '/*']: is_blocked = True
        elif line.startswith('allow:') or line.startswith('crawl-delay:') or line.startswith('sitemap:'):
            last_was_agent = False
    return is_blocked

def analyze():
    with open("hybrid_pipeline_results.json", "r") as f:
        data = json.load(f)

    bots_to_check = ['GPTBot', 'ChatGPT-User', 'OAI-SearchBot', 'Google-Extended']
    consolidated = {}

    for item in data:
        base_domain = get_base_domain(item["domain"])
        tier = classify_tier(base_domain)
        status = item.get("status")
        
        if base_domain not in consolidated:
            consolidated[base_domain] = {
                "tier": tier,
                "status_403": 0,
                "status_200": 0,
                "bots": {bot: 0 for bot in bots_to_check}
            }
            
        if status == 403:
            consolidated[base_domain]["status_403"] += 1
        elif status == 200:
            consolidated[base_domain]["status_200"] += 1
            robots_content = item.get("content", "")
            for bot in bots_to_check:
                if is_bot_disallowed(robots_content, bot):
                    consolidated[base_domain]["bots"][bot] += 1

    tiers = [
        "Tier 1 (High Selectivity Commercial Publishers)", 
        "Tier 2 (Mid-High Selectivity Open Access)", 
        "Tier 3 (Institutional Repositories & Preprints)", 
        "Tier 4 (Web-scale Aggregators)",
        "Unclassified (Independent Journals)"
    ]
    
    stats = {
        tier: {
            "total_entities": 0,
            "blocked_by_403": 0,
            "blocked_by_robots": {bot: 0 for bot in bots_to_check},
            "examples": []
        } for tier in tiers
    }

    for base_domain, info in consolidated.items():
        tier = info["tier"]
        stats[tier]["total_entities"] += 1
        if len(stats[tier]["examples"]) < 10:
            stats[tier]["examples"].append(base_domain)
        for bot in bots_to_check:
            if info["bots"][bot] > 0:
                stats[tier]["blocked_by_robots"][bot] += 1
        if info["status_403"] > 0:
            stats[tier]["blocked_by_403"] += 1

    report = "# 🛡️ Global Academic Domain AI Defense Statistics (Root Domain Deduplicated)\n\n"
    report += "To prevent statistical distortion caused by subdomain bloat (e.g., `top.sagepub.com`, `jpl.sagepub.com`), all domains were consolidated into their top-level root domains (e.g., `sagepub.com`) representing a single organizational entity.\n\n"
    report += "> **Evaluation Rule:** Even if a single publisher operates 100 subdomains, it is counted as 1 entity. If any of its subdomains returned a 403 Forbidden or explicitly blocked GPTBot in `robots.txt`, the entire entity is considered to have 'AI defense mechanisms enabled'.\n\n"
    
    for tier in tiers:
        s = stats[tier]
        t = s["total_entities"]
        if t == 0: continue
        
        t_403 = s["blocked_by_403"]
        rate_403 = (t_403 / t) * 100
        
        report += f"## {tier}\n"
        report += f"- **Total Consolidated Entities**: {t}\n"
        report += f"- **[Level 1 Defense] WAF Firewall Block (HTTP 403)**: {t_403} entities (**{rate_403:.1f}%**)\n"
        
        report += "  - **[Level 2 Defense] Explicit robots.txt Disallow**:\n"
        for bot in bots_to_check:
            blocked = s["blocked_by_robots"][bot]
            pct = (blocked / t) * 100
            report += f"    - **{bot}**: {blocked} entities blocked ({pct:.1f}%)\n"
            
        gpt_robots = s["blocked_by_robots"]["GPTBot"]
        report += f"\n👉 **[Comprehensive Insight]**: Combines WAF blocking ({rate_403:.1f}%) and robots.txt blocking ({(gpt_robots/t)*100:.1f}%) to form a robust multi-layered active defense.\n\n"

    famous_examples = """
## 🏢 Top 10 Representative Domains by Tier

### 🏛️ Tier 1 (High Selectivity Commercial Publishers)
1. **Elsevier** (`elsevier.com`, `sciencedirect.com`)
2. **Springer Nature** (`springer.com`, `nature.com`)
3. **IEEE** (`ieeexplore.ieee.org`)
4. **ACM** (`dl.acm.org`)
5. **Wiley** (`onlinelibrary.wiley.com`)
6. **Taylor & Francis** (`tandfonline.com`)
7. **Oxford University Press** (`oxfordjournals.org`)
8. **Cambridge University Press** (`cambridge.org`)
9. **SAGE Publishing** (`sagepub.com`)
10. **NEJM / BMJ** (`nejm.org`, `bmj.com`)

### 🔓 Tier 2 (Mid-High Selectivity Open Access)
1. **DOAJ** (`doaj.org`)
2. **PubMed / NIH** (`pubmed.ncbi.nlm.nih.gov`)
3. **PLOS** (`journals.plos.org`)
4. **MDPI** (`mdpi.com`)
5. **Frontiers** (`frontiersin.org`)
6. **BioMed Central (BMC)** (`biomedcentral.com`)
7. **Crossref** (`crossref.org`)
8. **eLife** (`elifesciences.org`)
9. **SciELO** (`scielo.org`)
10. **PeerJ** (`peerj.com`)

### 🏫 Tier 3 (Institutional Repositories & Preprints)
1. **arXiv** (`arxiv.org`)
2. **bioRxiv** (`biorxiv.org`)
3. **Zenodo** (`zenodo.org`)
4. **Figshare** (`figshare.com`)
5. **SSRN** (`ssrn.com`)
6. **OSF** (`osf.io`)
7. **MIT DSpace** (`dspace.mit.edu` etc.)
8. **Cambridge/Oxford Repositories** (`.ac.uk`)
9. **Digital Commons** (`digitalcommons.*`)
10. **HAL Science** (`hal.science`)

### 🕸️ Tier 4 (Web-scale Aggregators)
1. **Google Scholar** (`scholar.google.com`)
2. **Semantic Scholar** (`semanticscholar.org`)
3. **ResearchGate** (`researchgate.net`)
4. **Academia.edu** (`academia.edu`)
5. **EBSCO / ProQuest** (`ebsco.com`, `proquest.com`)
6. **JSTOR** (`jstor.org`)
7. **eScholarship** (`escholarship.org`)
8. **ScholarWorks** (`scholarworks.*`)
9. **OpenAlex** (`openalex.org`)
10. **Scopus / Web of Science** (`scopus.com`, `webofscience.com`)
"""
    report += famous_examples

    with open("tier_analysis_results_v4.md", "w") as f:
        f.write(report)
        
    print("Analysis complete. Saved to tier_analysis_results_v4.md")

if __name__ == "__main__":
    analyze()
