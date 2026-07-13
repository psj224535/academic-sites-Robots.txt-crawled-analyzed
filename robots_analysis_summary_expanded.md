# Expanded `robots.txt` Analysis Results

> [!NOTE]
> This report summarizes the `robots.txt` policies for ~40 academic platforms across 5 categories. It details their default policies, explicit blocks/allowances for various AI bots, and content scope restrictions.

## 1. Overview of Platforms & Scope Restrictions

| Platform | Category | Default Policy (`*`) | Fulltext Blocked | Abstract Blocked | Search Blocked |
|----------|----------|----------------------|:---:|:---:|:---:|
| **Elsevier** | Commercial_Publisher | Allow All | ❌ | ❌ | ❌ |
| **Springer** | Commercial_Publisher | Disallow All | ✅ | ✅ | ✅ |
| **Wiley** | Commercial_Publisher | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **Taylor_Francis** | Commercial_Publisher | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **Sage** | Commercial_Publisher | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **OUP** | Commercial_Publisher | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **Cambridge** | Commercial_Publisher | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **Nature** | Commercial_Publisher | Specific Paths Blocked | ❌ | ✅ | ✅ |
| **Science** | Commercial_Publisher | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **IEEE_Xplore** | Commercial_Publisher | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **Emerald** | Commercial_Publisher | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **De_Gruyter** | Commercial_Publisher | Specific Paths Blocked | ❌ | ✅ | ✅ |
| **PLOS** | Open_Access_Publisher | Specific Paths Blocked | ❌ | ✅ | ✅ |
| **MDPI** | Open_Access_Publisher | Unknown | ❌ | ❌ | ❌ |
| **ACM** | Open_Access_Publisher | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **Hindawi** | Open_Access_Publisher | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **Frontiers** | Open_Access_Publisher | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **eLife** | Open_Access_Publisher | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **BMC** | Open_Access_Publisher | Unknown | ❌ | ❌ | ❌ |
| **PeerJ** | Open_Access_Publisher | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **PubMed** | Academic_Database | Specific Paths Blocked | ✅ | ✅ | ✅ |
| **Semantic_Scholar** | Academic_Database | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **Web_of_Science** | Academic_Database | Allow All | ❌ | ❌ | ❌ |
| **Scopus** | Academic_Database | Unknown | ❌ | ❌ | ❌ |
| **Google_Scholar** | Academic_Database | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **JSTOR** | Academic_Database | Specific Paths Blocked | ❌ | ✅ | ❌ |
| **EBSCO** | Academic_Database | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **ProQuest** | Academic_Database | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **DBLP** | Academic_Database | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **arXiv** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **bioRxiv** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **medRxiv** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **Zenodo** | Preprint_Repository | Unknown | ❌ | ❌ | ❌ |
| **SSRN** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **OSF** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **ChemRxiv** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ✅ |
| **PsyArXiv** | Preprint_Repository | Allow All | ❌ | ❌ | ❌ |
| **Research_Square** | Preprint_Repository | Specific Paths Blocked | ❌ | ❌ | ❌ |
| **ResearchGate** | Academic_SNS | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **Academia** | Academic_SNS | Disallow All | ❌ | ❌ | ❌ |
| **Mendeley** | Academic_SNS | Specific Paths Blocked | ✅ | ❌ | ✅ |
| **ORCID** | Academic_SNS | Specific Paths Blocked | ❌ | ❌ | ✅ |

*(✅ = True/Blocked, ❌ = False/Not Blocked)*

## 2. Bot Policies: Training Bots

| Platform | GPTBot | ClaudeBot | CCBot | Google-Extended |
|----------|:---:|:---:|:---:|:---:|
| **Elsevier** | - | - | - | - |
| **Springer** | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |
| **Wiley** | 🚫 Blocked | - | - | 🚫 Blocked |
| **Taylor_Francis** | 🚫 Blocked | - | - | - |
| **Sage** | 🚫 Blocked | - | 🚫 Blocked | 🚫 Blocked |
| **OUP** | - | - | - | - |
| **Cambridge** | - | - | - | - |
| **Nature** | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |
| **Science** | 🚫 Blocked | - | 🚫 Blocked | 🚫 Blocked |
| **IEEE_Xplore** | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |
| **Emerald** | - | - | - | - |
| **De_Gruyter** | 🚫 Blocked | - | 🚫 Blocked | 🚫 Blocked |
| **PLOS** | - | - | - | - |
| **MDPI** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **ACM** | 🚫 Blocked | - | 🚫 Blocked | 🚫 Blocked |
| **Hindawi** | 🚫 Blocked | - | - | 🚫 Blocked |
| **Frontiers** | - | - | - | - |
| **eLife** | - | - | - | - |
| **BMC** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **PeerJ** | - | - | - | - |
| **PubMed** | - | - | - | - |
| **Semantic_Scholar** | - | - | - | - |
| **Web_of_Science** | - | - | - | - |
| **Scopus** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **Google_Scholar** | - | - | - | - |
| **JSTOR** | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |
| **EBSCO** | - | - | - | - |
| **ProQuest** | 🚫 Blocked | - | - | - |
| **DBLP** | - | - | - | - |
| **arXiv** | - | - | - | - |
| **bioRxiv** | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked | - |
| **medRxiv** | - | - | - | - |
| **Zenodo** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **SSRN** | 🚫 Blocked | - | - | 🚫 Blocked |
| **OSF** | ⚠️ Partial | - | - | - |
| **ChemRxiv** | 🚫 Blocked | - | - | - |
| **PsyArXiv** | - | - | - | - |
| **Research_Square** | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |
| **ResearchGate** | - | - | - | - |
| **Academia** | 🚫 Blocked | - | - | 🚫 Blocked |
| **Mendeley** | - | - | - | - |
| **ORCID** | - | - | - | - |

*(Note: `-` indicates "Not Mentioned")*

## 3. Bot Policies: AI Search & User RAG Bots

| Platform | OAI-SearchBot | Claude-SearchBot | PerplexityBot | ChatGPT-User |
|----------|:---:|:---:|:---:|:---:|
| **Elsevier** | - | - | - | - |
| **Springer** | - | - | 🚫 Blocked | 🚫 Blocked |
| **Wiley** | - | - | - | - |
| **Taylor_Francis** | - | - | - | - |
| **Sage** | - | - | - | - |
| **OUP** | - | - | - | - |
| **Cambridge** | - | - | - | 🚫 Blocked |
| **Nature** | - | - | 🚫 Blocked | 🚫 Blocked |
| **Science** | - | - | - | 🚫 Blocked |
| **IEEE_Xplore** | - | - | 🚫 Blocked | - |
| **Emerald** | - | - | - | - |
| **De_Gruyter** | - | - | - | - |
| **PLOS** | - | - | - | - |
| **MDPI** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **ACM** | - | - | - | 🚫 Blocked |
| **Hindawi** | - | - | - | - |
| **Frontiers** | - | - | - | - |
| **eLife** | - | - | - | - |
| **BMC** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **PeerJ** | - | - | - | - |
| **PubMed** | - | - | - | - |
| **Semantic_Scholar** | - | - | - | - |
| **Web_of_Science** | - | - | - | - |
| **Scopus** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **Google_Scholar** | - | - | - | - |
| **JSTOR** | - | - | - | - |
| **EBSCO** | - | - | - | - |
| **ProQuest** | ✅ Allowed | - | - | 🚫 Blocked |
| **DBLP** | - | - | - | - |
| **arXiv** | - | - | - | - |
| **bioRxiv** | - | - | 🚫 Blocked | 🚫 Blocked |
| **medRxiv** | - | - | - | - |
| **Zenodo** | ❌ Failed | ❌ Failed | ❌ Failed | ❌ Failed |
| **SSRN** | - | - | - | 🚫 Blocked |
| **OSF** | - | - | ⚠️ Partial | - |
| **ChemRxiv** | - | - | - | - |
| **PsyArXiv** | - | - | - | - |
| **Research_Square** | - | - | 🚫 Blocked | 🚫 Blocked |
| **ResearchGate** | - | - | - | - |
| **Academia** | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial |
| **Mendeley** | - | - | - | - |
| **ORCID** | - | - | - | - |

## 4. Notable Features & Highlights

> [!IMPORTANT]
> The following platforms have distinct or aggressive strategies against AI scraping:

- **Springer**: GPTBot is Blocked, ClaudeBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, PerplexityBot is Blocked, ChatGPT-User is Blocked
- **Wiley**: GPTBot is Blocked, Google-Extended is Blocked
- **Taylor_Francis**: GPTBot is Blocked
- **Sage**: GPTBot is Blocked, CCBot is Blocked, Google-Extended is Blocked
- **Cambridge**: ChatGPT-User is Blocked
- **Nature**: GPTBot is Blocked, ClaudeBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, PerplexityBot is Blocked, ChatGPT-User is Blocked
- **Science**: GPTBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, ChatGPT-User is Blocked
- **IEEE_Xplore**: GPTBot is Blocked, ClaudeBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, PerplexityBot is Blocked, Perplexity-User is Blocked
- **De_Gruyter**: GPTBot is Blocked, CCBot is Blocked, Google-Extended is Blocked
- **MDPI**: ❌ Failed to fetch (`robots.txt` blocked by WAF or returns 404).
- **ACM**: GPTBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, ChatGPT-User is Blocked
- **Hindawi**: GPTBot is Blocked, Google-Extended is Blocked
- **eLife**: Googlebot is Partially Blocked
- **BMC**: ❌ Failed to fetch (`robots.txt` blocked by WAF or returns 404).
- **Scopus**: ❌ Failed to fetch (`robots.txt` blocked by WAF or returns 404).
- **JSTOR**: GPTBot is Blocked, ClaudeBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, Googlebot is Partially Blocked
- **ProQuest**: GPTBot is Blocked, OAI-SearchBot is explicitly Allowed, ChatGPT-User is Blocked
- **arXiv**: Googlebot is Partially Blocked
- **bioRxiv**: GPTBot is Blocked, ClaudeBot is Blocked, CCBot is Blocked, PerplexityBot is Blocked, ChatGPT-User is Blocked
- **Zenodo**: ❌ Failed to fetch (`robots.txt` blocked by WAF or returns 404).
- **SSRN**: GPTBot is Blocked, Google-Extended is Blocked, ChatGPT-User is Blocked
- **OSF**: GPTBot is Partially Blocked, PerplexityBot is Partially Blocked
- **ChemRxiv**: GPTBot is Blocked
- **Research_Square**: GPTBot is Blocked, ClaudeBot is Blocked, CCBot is Blocked, Google-Extended is Blocked, PerplexityBot is Blocked, ChatGPT-User is Blocked
- **Academia**: GPTBot is Blocked, Google-Extended is Blocked, OAI-SearchBot is Partially Blocked, Claude-SearchBot is Partially Blocked, PerplexityBot is Partially Blocked, ChatGPT-User is Partially Blocked, Googlebot is Partially Blocked