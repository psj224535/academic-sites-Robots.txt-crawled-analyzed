import json
from collections import defaultdict

def classify_tier(domain):
    d = domain.lower()
    
    tier4_kw = [
        'scholar', 'semantic', 'search', 'index', 'lens.org', 'scopus', 'webofscience', 
        'proquest', 'ebsco', 'jstor', 'researchgate', 'academia.edu', 'mendeley', 
        'openalex', 'dimensions.ai', 'clarivate', 'exlibris'
    ]
    for kw in tier4_kw:
        if kw in d: return "Tier 4 (포괄적 크롤링형)"

    tier3_kw = [
        '.edu', '.ac.', 'repository', 'eprint', 'dspace', 'arxiv', 'rxiv', 'ssrn', 
        'osf.io', 'zenodo', 'figshare', 'dryad', 'archive', 'ir.', 'digitalcommons', 
        'theses', 'dissertation', 'hal.science', 'bepress', 'scholarworks'
    ]
    for kw in tier3_kw:
        if kw in d: return "Tier 3 (기관 보관/프리프린트)"

    tier1_kw = [
        'elsevier', 'sciencedirect', 'cell.com', 'thelancet', 'springer', 'nature', 
        'wiley', 'tandfonline', 'taylorandfrancis', 'routledge', 'oup', 'oxfordjournals', 
        'cambridge', 'sagepub', 'ieee', 'acm.org', 'asme', 'asce', 'aip.org', 'aps.org', 
        'iop.org', 'rsc.org', 'acs.org', 'jamanetwork', 'nejm', 'bmj', 'karger', 'brill', 
        'degruyter', 'emerald', 'thieme', 'wolterskluwer', 'lww.com', 'maryannliebert', 
        'inderscience', 'igi-global', 'begellhouse'
    ]
    for kw in tier1_kw:
        if kw in d: return "Tier 1 (고도 선별형 상업 출판사)"

    tier2_kw = [
        'doaj', 'pubmed', 'nih.gov', 'pmc', 'crossref', 'plos', 'mdpi', 'frontiers', 
        'hindawi', 'biomedcentral', 'scielo', 'copernicus', 'peerj', 'cogentoa', 
        'f1000', 'elife', 'datacite', 'orcid'
    ]
    for kw in tier2_kw:
        if kw in d: return "Tier 2 (심사 완료 오픈형)"

    return "Unclassified (미분류 개별 저널)"

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
    tiers = [
        "Tier 1 (고도 선별형 상업 출판사)", 
        "Tier 2 (심사 완료 오픈형)", 
        "Tier 3 (기관 보관/프리프린트)", 
        "Tier 4 (포괄적 크롤링형)",
        "Unclassified (미분류 개별 저널)"
    ]
    
    stats = {
        tier: {
            "total": 0,
            "status_200": 0,
            "status_403": 0,
            "status_other": 0,
            "bots": {bot: 0 for bot in bots_to_check}
        } for tier in tiers
    }

    for item in data:
        domain = item["domain"]
        tier = classify_tier(domain)
        status = item.get("status")
        
        stats[tier]["total"] += 1
        
        if status == 200:
            stats[tier]["status_200"] += 1
            robots_content = item.get("content", "")
            for bot in bots_to_check:
                if is_bot_disallowed(robots_content, bot):
                    stats[tier]["bots"][bot] += 1
        elif status == 403:
            stats[tier]["status_403"] += 1
        else:
            stats[tier]["status_other"] += 1

    report = "# 🛡️ 전 세계 학술 도메인 티어별 AI 방어 통계 (WAF + Robots.txt 통합 분석)\n\n"
    report += "단순히 `robots.txt`만 분석한 것이 아니라, **방화벽(WAF) 단에서의 403 강제 차단율**까지 결합하여 각 학술 티어(Tier)별 AI 봇 대응 전략과 실제 방어력을 입체적으로 분석한 최종 통계입니다.\n\n"
    
    for tier in tiers:
        s = stats[tier]
        t = s["total"]
        if t == 0: continue
        
        t_403 = s["status_403"]
        t_200 = s["status_200"]
        
        rate_403 = (t_403 / t) * 100
        
        report += f"## {tier}\n"
        report += f"- **수집 시도된 총 도메인 수**: {t}개\n"
        report += f"- **[1단계 방어] WAF/방화벽 강제 차단 (HTTP 403)**: {t_403}개 (**{rate_403:.1f}%**)\n"
        report += f"- **[2단계 방어] robots.txt 접근 허용 (HTTP 200)**: {t_200}개\n"
        
        if t_200 > 0:
            report += "  - **접근 허용 도메인 중 AI 봇 명시적 차단율 (Disallow: /)**:\n"
            for bot in bots_to_check:
                blocked = s["bots"][bot]
                pct = (blocked / t_200) * 100
                report += f"    - **{bot}**: {blocked}곳 차단 ({pct:.1f}%)\n"
                
            # 통합 차단율 (403 방화벽 차단 + robots.txt GPTBot 차단)
            gpt_robots = s["bots"]["GPTBot"]
            total_block_rate = ((t_403 + gpt_robots) / t) * 100
            report += f"\n👉 **[종합] 실질적인 AI 크롤링 불가율 (방화벽 + robots.txt)**: **{total_block_rate:.1f}%**\n\n"
        else:
            report += "\n"

    famous_examples = """
## 🏢 각 티어별 대표 도메인 예시 (Top 10)

### 🏛️ Tier 1 (고도 선별형 상업 출판사)
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

### 🔓 Tier 2 (심사 완료 오픈형)
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

### 🏫 Tier 3 (기관 보관/프리프린트)
1. **arXiv** (`arxiv.org`)
2. **bioRxiv** (`biorxiv.org`)
3. **Zenodo** (`zenodo.org`)
4. **Figshare** (`figshare.com`)
5. **SSRN** (`ssrn.com`)
6. **OSF** (`osf.io`)
7. **MIT DSpace** (`dspace.mit.edu` 등 `.edu`)
8. **Cambridge/Oxford Repositories** (`.ac.uk`)
9. **Digital Commons** (`digitalcommons.*`)
10. **HAL Science** (`hal.science`)

### 🕸️ Tier 4 (포괄적 크롤러 / 어그리게이터)
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

    with open("tier_analysis_results_v3.md", "w") as f:
        f.write(report)
        
    print("Analysis complete. Saved to tier_analysis_results_v3.md")

if __name__ == "__main__":
    analyze()
