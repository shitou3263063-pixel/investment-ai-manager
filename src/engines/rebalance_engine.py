from __future__ import annotations
import pandas as pd


def generate_rebalance_advice(portfolio_summary: pd.DataFrame, settings: dict) -> pd.DataFrame:
    targets = settings.get('target_allocation', {})
    threshold = float(settings.get('rebalance_threshold', 0.05))
    total = portfolio_summary['amount_cny'].sum()
    rows = []
    actual_map = dict(zip(portfolio_summary['category'], portfolio_summary['actual_ratio']))
    amount_map = dict(zip(portfolio_summary['category'], portfolio_summary['amount_cny']))
    for category, target in targets.items():
        actual = float(actual_map.get(category, 0))
        gap = actual - float(target)
        action = '保持'
        amount = 0
        if gap > threshold:
            action = '考虑降低'
            amount = gap * total
        elif gap < -threshold:
            action = '考虑增加'
            amount = -gap * total
        rows.append({'category': category, 'actual_ratio': round(actual, 4), 'target_ratio': round(float(target), 4), 'gap': round(gap, 4), 'action': action, 'suggest_amount_cny': round(amount, 0), 'current_amount_cny': round(float(amount_map.get(category, 0)), 0)})
    return pd.DataFrame(rows)
