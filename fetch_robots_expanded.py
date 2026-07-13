import urllib.request
import os
import json
import ssl
import time

urls = {
    # Commercial Publisher
    "Elsevier": ("Commercial_Publisher", "https://www.elsevier.com/robots.txt"),
    "Springer": ("Commercial_Publisher", "https://link.springer.com/robots.txt"),
    "Wiley": ("Commercial_Publisher", "https://onlinelibrary.wiley.com/robots.txt"),
    "Taylor_Francis": ("Commercial_Publisher", "https://www.tandfonline.com/robots.txt"),
    "Sage": ("Commercial_Publisher", "https://journals.sagepub.com/robots.txt"),
    "OUP": ("Commercial_Publisher", "https://academic.oup.com/robots.txt"),
    "Cambridge": ("Commercial_Publisher", "https://www.cambridge.org/robots.txt"),
    "Nature": ("Commercial_Publisher", "https://www.nature.com/robots.txt"),
    "Science": ("Commercial_Publisher", "https://www.science.org/robots.txt"),
    "IEEE_Xplore": ("Commercial_Publisher", "https://ieeexplore.ieee.org/robots.txt"),
    "Emerald": ("Commercial_Publisher", "https://www.emerald.com/robots.txt"),
    "De_Gruyter": ("Commercial_Publisher", "https://www.degruyter.com/robots.txt"),

    # Open Access Publisher
    "PLOS": ("Open_Access_Publisher", "https://journals.plos.org/robots.txt"),
    "MDPI": ("Open_Access_Publisher", "https://www.mdpi.com/robots.txt"),
    "ACM": ("Open_Access_Publisher", "https://dl.acm.org/robots.txt"),
    "Hindawi": ("Open_Access_Publisher", "https://www.hindawi.com/robots.txt"),
    "Frontiers": ("Open_Access_Publisher", "https://www.frontiersin.org/robots.txt"),
    "eLife": ("Open_Access_Publisher", "https://elifesciences.org/robots.txt"),
    "BMC": ("Open_Access_Publisher", "https://www.biomedcentral.com/robots.txt"),
    "PeerJ": ("Open_Access_Publisher", "https://peerj.com/robots.txt"),

    # Academic Database
    "PubMed": ("Academic_Database", "https://pubmed.ncbi.nlm.nih.gov/robots.txt"),
    "Semantic_Scholar": ("Academic_Database", "https://www.semanticscholar.org/robots.txt"),
    "Web_of_Science": ("Academic_Database", "https://www.webofscience.com/robots.txt"),
    "Scopus": ("Academic_Database", "https://www.scopus.com/robots.txt"),
    "Google_Scholar": ("Academic_Database", "https://scholar.google.com/robots.txt"),
    "JSTOR": ("Academic_Database", "https://www.jstor.org/robots.txt"),
    "EBSCO": ("Academic_Database", "https://www.ebsco.com/robots.txt"),
    "ProQuest": ("Academic_Database", "https://www.proquest.com/robots.txt"),
    "DBLP": ("Academic_Database", "https://dblp.org/robots.txt"),

    # Preprint Repository
    "arXiv": ("Preprint_Repository", "https://arxiv.org/robots.txt"),
    "bioRxiv": ("Preprint_Repository", "https://www.biorxiv.org/robots.txt"),
    "medRxiv": ("Preprint_Repository", "https://www.medrxiv.org/robots.txt"),
    "Zenodo": ("Preprint_Repository", "https://zenodo.org/robots.txt"),
    "SSRN": ("Preprint_Repository", "https://papers.ssrn.com/robots.txt"),
    "OSF": ("Preprint_Repository", "https://osf.io/robots.txt"),
    "ChemRxiv": ("Preprint_Repository", "https://chemrxiv.org/robots.txt"),
    "PsyArXiv": ("Preprint_Repository", "https://psyarxiv.com/robots.txt"),
    "Research_Square": ("Preprint_Repository", "https://www.researchsquare.com/robots.txt"),

    # Academic SNS
    "ResearchGate": ("Academic_SNS", "https://www.researchgate.net/robots.txt"),
    "Academia": ("Academic_SNS", "https://www.academia.edu/robots.txt"),
    "Mendeley": ("Academic_SNS", "https://www.mendeley.com/robots.txt"),
    "ORCID": ("Academic_SNS", "https://orcid.org/robots.txt")
}

os.makedirs("raw_robots_expanded", exist_ok=True)

metadata = {}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

for name, (category, url) in urls.items():
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
            content = response.read().decode('utf-8', errors='replace')
            with open(f"raw_robots_expanded/{name}.txt", "w", encoding='utf-8') as f:
                f.write(content)
            metadata[name] = {"category": category, "url": url, "status": "success"}
        print(f"Success: {name}")
    except Exception as e:
        metadata[name] = {"category": category, "url": url, "status": f"failed: {e}"}
        print(f"Failed: {name} - {e}")
    time.sleep(1) # Polite delay

with open("raw_robots_expanded/metadata.json", "w", encoding='utf-8') as f:
    json.dump(metadata, f, indent=4)
