def assess_market(market_rows):
    risk = 50
    alerts = []

    for r in market_rows:
        name = r["name"]
        change = r["change"]

        if name == "Nasdaq 100" and change <= -3:
            risk += 20
            alerts.append(f"纳斯达克大跌 {change:.2f}%，触发风险提醒。")
        elif name == "S&P 500" and change <= -2:
            risk += 15
            alerts.append(f"标普500明显下跌 {change:.2f}%。")

        if name == "VIX" and change >= 15:
            risk += 20
            alerts.append(f"VIX 飙升 {change:.2f}%，市场恐慌情绪上升。")

        if name == "Gold ETF" and abs(change) >= 2:
            risk += 8
            alerts.append(f"黄金明显波动 {change:.2f}%。")

    return min(risk, 100), alerts

def make_decision(portfolio_analysis, market_rows):
    risk, alerts = assess_market(market_rows)
    actions = []
    risks = []

    for row in portfolio_analysis["categories"]:
        cat = row["category"]
        current = row["current_ratio"]
        diff = row["diff_ratio"]

        if abs(diff) >= 0.03:
            if diff > 0:
                actions.append(f"{cat} 高于目标 {diff:.2%}，后续可分批降低，不建议一次性操作。")
            else:
                actions.append(f"{cat} 低于目标 {abs(diff):.2%}，可优先用新增资金逐步补足。")

        if cat == "Gold" and current > 0.15:
            risks.append("黄金仓位超过 15%，暂不建议继续加仓。")
        if cat == "HK Stocks" and current > 0.08:
            risks.append("港股高于目标配置，继续观察，不主动大幅补仓。")
        if cat == "Cash" and current < 0.05:
            risks.append("现金低于 5%，暂停所有加仓。")

    actions.append("长期策略：以持有为主，不因单日波动频繁交易。")

    if risk >= 80:
        level = "B级：建议本周重点关注"
        final = "市场风险偏高，今日不主动加仓，优先保持现金和债券防守。"
    elif risk >= 60:
        level = "C级：继续观察"
        final = "市场风险中等，继续持有，不做大幅调仓。"
    else:
        level = "D级：不要操作"
        final = "市场风险可控，继续执行长期配置和定投计划。"

    return {
        "risk_score": risk,
        "alerts": alerts,
        "actions": actions,
        "risks": risks,
        "level": level,
        "final": final
    }
