from src.portfolio import load_portfolio, load_targets, analyze_portfolio
from src.market import update_market_data
from src.decision import make_decision
from src.report import generate_report, save_report
from src.services.wecom_service import send_daily_report
from src.services.email_service import send_email_if_configured


def main():
    portfolio = load_portfolio()
    targets = load_targets()
    portfolio_analysis = analyze_portfolio(portfolio, targets)

    market_rows = update_market_data()
    decision = make_decision(portfolio_analysis, market_rows)

    report = generate_report(portfolio_analysis, market_rows, decision)
    save_report(report)

    print("Stone AI Pro V4.0 运行成功！")
    print(f"总资产：{portfolio_analysis['total']:,.0f} 元")
    print(f"市场风险评分：{decision['risk_score']}/100")
    print("日报已生成：reports/daily_report.md")

    send_daily_report()

    send_email_if_configured(
        "Stone AI Investment Manager 日报",
        report,
    )


if __name__ == "__main__":
    main()
