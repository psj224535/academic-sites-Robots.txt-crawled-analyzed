# 🛡️ 전 세계 학술 도메인 티어별 AI 방어 통계 (WAF + Robots.txt 통합 분석)

단순히 `robots.txt`만 분석한 것이 아니라, **방화벽(WAF) 단에서의 403 강제 차단율**까지 결합하여 각 학술 티어(Tier)별 AI 봇 대응 전략과 실제 방어력을 입체적으로 분석한 최종 통계입니다.

## Tier 1 (고도 선별형 상업 출판사)

- **수집 시도된 총 도메인 수**: 879개
- **[1단계 방어] WAF/방화벽 강제 차단 (HTTP 403)**: 413개 (**47.0%**)
- **[2단계 방어] robots.txt 접근 허용 (HTTP 200)**: 401개
  - **접근 허용 도메인 중 AI 봇 명시적 차단율 (Disallow: /)**:
    - **GPTBot**: 74곳 차단 (18.5%)
    - **ChatGPT-User**: 74곳 차단 (18.5%)
    - **OAI-SearchBot**: 70곳 차단 (17.5%)
    - **Google-Extended**: 74곳 차단 (18.5%)

👉 **[종합] 실질적인 AI 크롤링 불가율 (방화벽 + robots.txt)**: **55.4%**

## Tier 2 (심사 완료 오픈형)

- **수집 시도된 총 도메인 수**: 132개
- **[1단계 방어] WAF/방화벽 강제 차단 (HTTP 403)**: 2개 (**1.5%**)
- **[2단계 방어] robots.txt 접근 허용 (HTTP 200)**: 119개
  - **접근 허용 도메인 중 AI 봇 명시적 차단율 (Disallow: /)**:
    - **GPTBot**: 99곳 차단 (83.2%)
    - **ChatGPT-User**: 99곳 차단 (83.2%)
    - **OAI-SearchBot**: 99곳 차단 (83.2%)
    - **Google-Extended**: 99곳 차단 (83.2%)

👉 **[종합] 실질적인 AI 크롤링 불가율 (방화벽 + robots.txt)**: **76**

-> biomedcentral.com이 98개 였음. 근데 다 bot 차단중이었던 것. 

-> 학술 사이트 도메인 모음 데이터 선별시 주의 사항 : 과하게 중복되는 주소가 있을 수 있다. 

## Tier 3 (기관 보관/프리프린트)

- **수집 시도된 총 도메인 수**: 1625개
- **[1단계 방어] WAF/방화벽 강제 차단 (HTTP 403)**: 62개 (**3.8%**)
- **[2단계 방어] robots.txt 접근 허용 (HTTP 200)**: 953개
  - **접근 허용 도메인 중 AI 봇 명시적 차단율 (Disallow: /)**:
    - **GPTBot**: 38곳 차단 (4.0%)
    - **ChatGPT-User**: 37곳 차단 (3.9%)
    - **OAI-SearchBot**: 32곳 차단 (3.4%)
    - **Google-Extended**: 34곳 차단 (3.6%)

👉 **[종합] 실질적인 AI 크롤링 불가율 (방화벽 + robots.txt)**: **6.2%**

## Tier 4 (포괄적 크롤링형)

- **수집 시도된 총 도메인 수**: 149개
- **[1단계 방어] WAF/방화벽 강제 차단 (HTTP 403)**: 8개 (**5.4%**)
- **[2단계 방어] robots.txt 접근 허용 (HTTP 200)**: 108개
  - **접근 허용 도메인 중 AI 봇 명시적 차단율 (Disallow: /)**:
    - **GPTBot**: 12곳 차단 (11.1%)
    - **ChatGPT-User**: 10곳 차단 (9.3%)
    - **OAI-SearchBot**: 9곳 차단 (8.3%)
    - **Google-Extended**: 10곳 차단 (9.3%)

👉 **[종합] 실질적인 AI 크롤링 불가율 (방화벽 + robots.txt)**: **13.4%**

## Unclassified (미분류 개별 저널)

- **수집 시도된 총 도메인 수**: 7215개
- **[1단계 방어] WAF/방화벽 강제 차단 (HTTP 403)**: 221개 (**3.1%**)
- **[2단계 방어] robots.txt 접근 허용 (HTTP 200)**: 4335개
  - **접근 허용 도메인 중 AI 봇 명시적 차단율 (Disallow: /)**:
    - **GPTBot**: 254곳 차단 (5.9%)
    - **ChatGPT-User**: 224곳 차단 (5.2%)
    - **OAI-SearchBot**: 178곳 차단 (4.1%)
    - **Google-Extended**: 209곳 차단 (4.8%)

👉 **[종합] 실질적인 AI 크롤링 불가율 (방화벽 + robots.txt)**: **6.6%**

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
