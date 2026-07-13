import urllib.request
import os
import json

urls = {
    "Elsevier": ("Commercial_Publisher", "https://www.elsevier.com/robots.txt"),
    "Springer": ("Commercial_Publisher", "https://link.springer.com/robots.txt"),
    "Wiley": ("Commercial_Publisher", "https://onlinelibrary.wiley.com/robots.txt"),
    "PLOS": ("Open_Access_Publisher", "https://journals.plos.org/robots.txt"),
    "MDPI": ("Open_Access_Publisher", "https://www.mdpi.com/robots.txt"),
    "ACM": ("Open_Access_Publisher", "https://dl.acm.org/robots.txt"),
    "PubMed": ("Academic_Database", "https://pubmed.ncbi.nlm.nih.gov/robots.txt"),
    "Semantic_Scholar": ("Academic_Database", "https://www.semanticscholar.org/robots.txt"),
    "arXiv": ("Preprint_Repository", "https://arxiv.org/robots.txt"),
    "bioRxiv": ("Preprint_Repository", "https://www.biorxiv.org/robots.txt"),
    "Zenodo": ("Preprint_Repository", "https://zenodo.org/robots.txt"),
    "ResearchGate": ("Academic_SNS", "https://www.researchgate.net/robots.txt"),
    "Academia": ("Academic_SNS", "https://www.academia.edu/robots.txt")
}

os.makedirs("raw_robots", exist_ok=True)

metadata = {}

for name, (category, url) in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8', errors='replace')
            with open(f"raw_robots/{name}.txt", "w", encoding='utf-8') as f:
                f.write(content)
            metadata[name] = {"category": category, "url": url, "status": "success"}
        print(f"Success: {name}")
    except Exception as e:
        metadata[name] = {"category": category, "url": url, "status": f"failed: {e}"}
        print(f"Failed: {name} - {e}")

with open("raw_robots/metadata.json", "w", encoding='utf-8') as f:
    json.dump(metadata, f, indent=4)
