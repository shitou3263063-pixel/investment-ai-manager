import csv
from collections import defaultdict


def load_csv(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def get_value(row, *keys, default=""):
    for key in keys:
        if key in row and row[key] not in ("", None):
            return row[key]
    return default


def load_portfolio(path="data/portfolio.csv"):
    rows = load_csv(path)

    return [{
        "asset": get_value(r, "Asset", "asset"),
        "category": get_value(r, "Category", "category"),
        "value": float(get_value(r, "Value", "value", "amount_cny", default=0)),
        "ticker": get_value(r, "Ticker", "ticker"),
    } for r in rows]


def load_targets(path="config/target_allocation.csv"):
    rows = load_csv(path)
    return {
        get_value(r, "Category", "category"): float(get_value(r, "Target", "target", default=0))
        for r in rows
    }


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
            "diff_value": diff * total,
        })

    holdings = [
        {**i, "ratio": i["value"] / total if total else 0}
        for i in items
    ]

    return {
        "total": total,
        "categories": sorted(categories, key=lambda x: abs(x["diff_ratio"]), reverse=True),
        "holdings": sorted(holdings, key=lambda x: x["value"], reverse=True),
    }