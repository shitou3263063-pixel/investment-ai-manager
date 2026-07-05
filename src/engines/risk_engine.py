from __future__ import annotations
import pandas as pd


def calculate_risk_score(portfolio_summary: pd.DataFrame, market_df: pd.DataFrame) -> dict:
    equity_ratio = portfolio_summary.loc[portfolio_summary['category'].str.contains('equity'), 'actual_ratio'].sum()
    gold_ratio = portfolio_summary.loc[portfolio_summary['category'].eq('gold'), 'actual_ratio'].sum()
    cash_ratio = portfolio_summary.loc[portfolio_summary['category'].eq('cash'), 'actual_ratio'].sum()

    vix_row = market_df[market_df['name'].eq('VIX')]
    vix = None if vix_row.empty else vix_row.iloc[0].get('close')

    score = 50
    score += min(equity_ratio * 60, 30)
    if vix and vix > 25:
        score += 15
    elif vix and vix > 18:
        score += 7
    if gold_ratio > 0.22:
        score += 5
    if cash_ratio < 0.05:
        score += 8
    score = max(0, min(100, round(score)))

    level = '低' if score < 45 else '中等' if score < 70 else '偏高'
    return {'risk_score': score, 'risk_level': level, 'vix': vix, 'equity_ratio': round(float(equity_ratio), 4), 'gold_ratio': round(float(gold_ratio), 4), 'cash_ratio': round(float(cash_ratio), 4)}
