# `robots.txt` Analysis Results

> [!NOTE]
> This report summarizes the `robots.txt` policies for 11 academic platforms across 5 categories. It details their default policies, explicit blocks/allowances for various AI bots, and content scope restrictions.

## 1. Overview of Platforms & Scope Restrictions

| Platform                   | Category              | Default Policy (`*`) | Fulltext Blocked | Abstract Blocked | Search Blocked |
| -------------------------- | --------------------- | ---------------------- | :--------------: | :--------------: | :------------: |
| **Elsevier**         | Commercial_Publisher  | Allow All              |        ❌        |        ❌        |       ❌       |
| **Springer**         | Commercial_Publisher  | Disallow All           |        ✅        |        ✅        |       ✅       |
| **Wiley**            | Commercial_Publisher  | Specific Paths Blocked |        ✅        |        ❌        |       ✅       |
| **PLOS**             | Open_Access_Publisher | Specific Paths Blocked |        ❌        |        ✅        |       ✅       |
| **ACM**              | Open_Access_Publisher | Specific Paths Blocked |        ❌        |        ❌        |       ✅       |
| **PubMed**           | Academic_Database     | Specific Paths Blocked |        ✅        |        ✅        |       ✅       |
| **Semantic_Scholar** | Academic_Database     | Specific Paths Blocked |        ❌        |        ❌        |       ✅       |
| **arXiv**            | Preprint_Repository   | Specific Paths Blocked |        ❌        |        ❌        |       ✅       |
| **bioRxiv**          | Preprint_Repository   | Specific Paths Blocked |        ❌        |        ❌        |       ✅       |
| **ResearchGate**     | Academic_SNS          | Specific Paths Blocked |        ✅        |        ❌        |       ✅       |
| **Academia**         | Academic_SNS          | Disallow All           |        ❌        |        ❌        |       ❌       |

*(✅ = True/Blocked, ❌ = False/Not Blocked)*

---

## 2. Bot Policies: Training Bots

| Platform                   |   GPTBot   | ClaudeBot |   CCBot   | Google-Extended |
| -------------------------- | :--------: | :--------: | :--------: | :-------------: |
| **Elsevier**         |     -     |     -     |     -     |        -        |
| **Springer**         | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |   🚫 Blocked   |
| **Wiley**            | 🚫 Blocked |     -     |     -     |   🚫 Blocked   |
| **PLOS**             |     -     |     -     |     -     |        -        |
| **ACM**              | 🚫 Blocked |     -     | 🚫 Blocked |   🚫 Blocked   |
| **PubMed**           |     -     |     -     |     -     |        -        |
| **Semantic_Scholar** |     -     |     -     |     -     |        -        |
| **arXiv**            |     -     |     -     |     -     |        -        |
| **bioRxiv**          | 🚫 Blocked | 🚫 Blocked | 🚫 Blocked |        -        |
| **ResearchGate**     |     -     |     -     |     -     |        -        |
| **Academia**         | 🚫 Blocked |     -     |     -     |   🚫 Blocked   |

*(Note: `-` indicates "Not Mentioned")*

---

## 3. Bot Policies: AI Search & User RAG Bots

| Platform                   | OAI-SearchBot | Claude-SearchBot | PerplexityBot | ChatGPT-User |
| -------------------------- | :-----------: | :--------------: | :-----------: | :----------: |
| **Elsevier**         |       -       |        -        |       -       |      -      |
| **Springer**         |       -       |        -        |  🚫 Blocked  |  🚫 Blocked  |
| **Wiley**            |       -       |        -        |       -       |      -      |
| **PLOS**             |       -       |        -        |       -       |      -      |
| **ACM**              |       -       |        -        |       -       |  🚫 Blocked  |
| **PubMed**           |       -       |        -        |       -       |      -      |
| **Semantic_Scholar** |       -       |        -        |       -       |      -      |
| **arXiv**            |       -       |        -        |       -       |      -      |
| **bioRxiv**          |       -       |        -        |  🚫 Blocked  |  🚫 Blocked  |
| **ResearchGate**     |       -       |        -        |       -       |      -      |
| **Academia**         | ⚠️ Partial |   ⚠️ Partial   | ⚠️ Partial | ⚠️ Partial |

---

## 4. Notable Features & Highlights

> [!IMPORTANT]
> The following platforms have distinct or aggressive strategies against AI scraping:

- **Springer**: Extremely restrictive. Blocks almost all training (`GPTBot`, `ClaudeBot`, `CCBot`), AI search (`PerplexityBot`), and RAG bots (`ChatGPT-User`). Content paths are heavily blocked for all agents.
- **ACM**: Blocks specific training bots (`GPTBot`, `CCBot`, `Google-Extended`) and user bots (`ChatGPT-User`), while leaving some others unmentioned.
- **bioRxiv**: Strong blocks against specific AI bots including `GPTBot`, `ClaudeBot`, `CCBot`, `PerplexityBot`, and `ChatGPT-User`.
- **Academia.edu**: Explicitly blocks `GPTBot` and `Google-Extended`, and imposes *partial blocks* on AI Search bots (`OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`) and user bots (`ChatGPT-User`, `Googlebot`).
- **Common Patterns**: Most platforms (except Elsevier and Academia) block internal search paths (e.g., `/search`, `/query`) for default agents to prevent traditional and AI scraping of search results.
