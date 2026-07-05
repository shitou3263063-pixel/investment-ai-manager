import csv
from collections import defaultdict

def load_csv(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def load_portfolio(path="data/portfolio.csv"):
    rows = load_csv(path)
    items = []
    for r in rows:
        items.append({
            "asset": r["Asset"],
            "category": r["Category"],
            "value": float(r["Value"]),
            "ticker": r.get("Ticker", "")
        })
    return items

def load_targets(path="config/target_allocation.csv"):
    rows = load_csv(path)
    return {r["Category"]: float(r["Target"]) for r in rows}

def analyze_portfolio(items, targets):
    total = sum(i["value"] for i in items)
    by_category = defaultdict(float)
    for i in items:
        by_category[i["category"]] += i["value"]

    categories = []
    for category, value in by_category.items():
        current = value / total if total else 0
        target = targets.get(category, 0)
        diff = current - target
        categories.append({
            "category": category,
            "value": value,
            "current_ratio": current,
            "target_ratio": target,
            "diff_ratio": diff,
            "diff_value": diff * total
        })

    holdings = []
    for i in items:
        holdings.append({
            **i,
            "ratio": i["value"] / total if total else 0
        })

    return {
        "total": total,
        "categories": sorted(categories, key=lambda x: abs(x["diff_ratio"]), reverse=True),
        "holdings": sorted(holdings, key=lambda x: x["value"], reverse=True)
    }
