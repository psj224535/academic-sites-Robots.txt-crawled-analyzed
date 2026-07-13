# 🛡️ Global Academic Domain AI Defense Statistics (Root Domain Deduplicated)

To prevent statistical distortion caused by subdomain bloat (e.g., `top.sagepub.com`, `jpl.sagepub.com`), all domains were consolidated into their top-level root domains (e.g., `sagepub.com`) representing a single organizational entity.

> **Evaluation Rule:** Even if a single publisher operates 100 subdomains, it is counted as 1 entity. If any of its subdomains returned a 403 Forbidden or explicitly blocked GPTBot in `robots.txt`, the entire entity is considered to have 'AI defense mechanisms enabled'.

## Tier 1 (High Selectivity Commercial Publishers)
- **Total Consolidated Entities**: 91
- **[Level 1 Defense] WAF Firewall Block (HTTP 403)**: 9 entities (**9.9%**)
  - **[Level 2 Defense] Explicit robots.txt Disallow**:
    - **GPTBot**: 10 entities blocked (11.0%)
    - **ChatGPT-User**: 10 entities blocked (11.0%)
    - **OAI-SearchBot**: 6 entities blocked (6.6%)
    - **Google-Extended**: 9 entities blocked (9.9%)

👉 **[Comprehensive Insight]**: Combines WAF blocking (9.9%) and robots.txt blocking (11.0%) to form a robust multi-layered active defense.

## Tier 2 (Mid-High Selectivity Open Access)
- **Total Consolidated Entities**: 25
- **[Level 1 Defense] WAF Firewall Block (HTTP 403)**: 2 entities (**8.0%**)
  - **[Level 2 Defense] Explicit robots.txt Disallow**:
    - **GPTBot**: 2 entities blocked (8.0%)
    - **ChatGPT-User**: 2 entities blocked (8.0%)
    - **OAI-SearchBot**: 2 entities blocked (8.0%)
    - **Google-Extended**: 2 entities blocked (8.0%)

👉 **[Comprehensive Insight]**: Combines WAF blocking (8.0%) and robots.txt blocking (8.0%) to form a robust multi-layered active defense.

## Tier 3 (Institutional Repositories & Preprints)
- **Total Consolidated Entities**: 1101
- **[Level 1 Defense] WAF Firewall Block (HTTP 403)**: 57 entities (**5.2%**)
  - **[Level 2 Defense] Explicit robots.txt Disallow**:
    - **GPTBot**: 37 entities blocked (3.4%)
    - **ChatGPT-User**: 35 entities blocked (3.2%)
    - **OAI-SearchBot**: 31 entities blocked (2.8%)
    - **Google-Extended**: 32 entities blocked (2.9%)

👉 **[Comprehensive Insight]**: Combines WAF blocking (5.2%) and robots.txt blocking (3.4%) to form a robust multi-layered active defense.

## Tier 4 (Web-scale Aggregators)
- **Total Consolidated Entities**: 63
- **[Level 1 Defense] WAF Firewall Block (HTTP 403)**: 1 entities (**1.6%**)
  - **[Level 2 Defense] Explicit robots.txt Disallow**:
    - **GPTBot**: 4 entities blocked (6.3%)
    - **ChatGPT-User**: 3 entities blocked (4.8%)
    - **OAI-SearchBot**: 2 entities blocked (3.2%)
    - **Google-Extended**: 3 entities blocked (4.8%)

👉 **[Comprehensive Insight]**: Combines WAF blocking (1.6%) and robots.txt blocking (6.3%) to form a robust multi-layered active defense.

## Unclassified (Independent Journals)
- **Total Consolidated Entities**: 5900
- **[Level 1 Defense] WAF Firewall Block (HTTP 403)**: 207 entities (**3.5%**)
  - **[Level 2 Defense] Explicit robots.txt Disallow**:
    - **GPTBot**: 207 entities blocked (3.5%)
    - **ChatGPT-User**: 179 entities blocked (3.0%)
    - **OAI-SearchBot**: 133 entities blocked (2.3%)
    - **Google-Extended**: 163 entities blocked (2.8%)

👉 **[Comprehensive Insight]**: Combines WAF blocking (3.5%) and robots.txt blocking (3.5%) to form a robust multi-layered active defense.


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


## 📋 [Appendix] Tier 1 & 2 Detailed Domain Verification List

### 🏛️ Tier 1 Detailed Domains
**1. Firewall (WAF 403) Blocked Entities (Total 9):**
`bmj.com`, `sagepub.com`, `acm.org`, `wiley.com`, `aip.org`, `elsevier.com`, `springerpub.com`, `wolterskluwer.com`, `wileyonlinelibrary.com`

**2. robots.txt Explicit GPTBot Disallow (Total 7):**
`springeropen.com`, `ieee.org`, `springer.com`, `thieme-connect.de`, `sciencedirect.com`, `thieme-connect.com`, `elsevier.es`

**3. Allowed Entities (5 randomly extracted / Total 75):**
`sagepub.net`, `amigosdanatureza.org.br`, `globalhealthsciencegroup.com`, `rsc.org`, `springer.de`

### 🔓 Tier 2 Detailed Domains
**1. Firewall (WAF 403) Blocked Entities (Total 2):**
`mdpi.com`, `scielo.cl`

**2. robots.txt Explicit GPTBot Disallow (Total 2):**
`biomedcentral.com`, `datacite.org`

**3. Allowed Entities (All / Total 22):**
`nih.gov`, `plosone.org`, `frontiersin.org`, `plosmedicine.org`, `plospathogens.org`, `earthsciencefrontiers.net.cn`, `doaj.org`, `scielo.br`, `hindawi.com`, `elifesciences.org`, `plosbiology.org`, `f1000research.com`, `plosgenetics.org`, `plos.org`, `scielo.org.za`, `scielo.org.pe`, `scielo.org.ar`, `peerj.com`, `plosntds.org`, `frontiersinzoology.com`, `europepmc.org`, `scielo.org`

