import json
from analyze_tiers import classify_tier

with open("hybrid_pipeline_results.json", "r") as f:
    data = json.load(f)

t1_total = 0
t1_200 = 0
t1_403 = 0
t1_timeout = 0
t1_gptbot_mention = 0
t1_general_block = 0

for item in data:
    if classify_tier(item["domain"]).startswith("Tier 1"):
        t1_total += 1
        status = item.get("status")
        if status == 200:
            t1_200 += 1
            content = str(item.get("content", "")).lower()
            if "gptbot" in content:
                t1_gptbot_mention += 1
        elif status == 403:
            t1_403 += 1
        elif status == "Timeout":
            t1_timeout += 1

print(f"Tier 1 Total: {t1_total}")
print(f"Tier 1 200 OK: {t1_200}")
print(f"Tier 1 403 Forbidden: {t1_403}")
print(f"Tier 1 Timeout: {t1_timeout}")
print(f"Tier 1 200 OK & Mentions GPTBot: {t1_gptbot_mention}")
