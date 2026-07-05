from __future__ import annotations
from src.utils.config import load_settings
from src.data.portfolio import load_portfolio, portfolio_summary
from src.data.market_data import fetch_market_snapshot
from src.engines.risk_engine import calculate_risk_score
from src.engines.rebalance_engine import generate_rebalance_advice
from src.engines.dca_engine import dca_advice
from src.engines.event_engine import macro_event_check
from src.services.report_service import build_daily_report, save_report
from src.services.email_service import send_email_if_configured
from src.services.wecom_service import send_daily_report


def main():
    settings = load_settings()
    portfolio = load_portfolio()
    summary = portfolio_summary(portfolio)
    market = fetch_market_snapshot(settings)
    risk = calculate_risk_score(summary, market)
    rebalance = generate_rebalance_advice(summary, settings)
    dca = dca_advice(market)
    events = macro_event_check(market)
    report = build_daily_report(portfolio, summary, market, risk, rebalance, dca, events)
   path = save_report(report)
save_report(report, 'weekly_report.md')

print(f'Report generated: {path}')

send_daily_report()

send_email_if_configured(
    'Stone AI Investment Manager Pro V10 日报',
    report
)

if __name__ == '__main__':
    main()
