from src.portfolio import load_portfolio, load_targets, analyze_portfolio
from src.market import update_market_data
from src.decision import make_decision
from src.report import generate_report, save_report
from pathlib import Path
import csv

def load_cached_market_data(path="data/market_data.csv"):
    if not Path(path).exists():
        return []
    with open(path, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    return [{
        "name": r.get("name", ""),
        "ticker": r.get("ticker", ""),
        "change": float(r.get("change", 0) or 0),
        "note": r.get("note", "缓存数据")
    } for r in rows]

def main():
    portfolio = load_portfolio()
    targets = load_targets()
    portfolio_analysis = analyze_portfolio(portfolio, targets)

    try:
        market_rows = update_market_data()
    except Exception as e:
        print(f"市场数据更新失败，使用缓存数据：{e}")
        market_rows = load_cached_market_data()

    decision = make_decision(portfolio_analysis, market_rows)

    report = generate_report(portfolio_analysis, market_rows, decision)
    save_report(report)

    print("Stone AI Pro V3.1 运行成功！")
    print(f"总资产：{portfolio_analysis['total']:,.0f} 元")
    print(f"市场风险评分：{decision['risk_score']}/100")
    print("日报已生成：reports/daily_report.md")

if __name__ == "__main__":
    main()
