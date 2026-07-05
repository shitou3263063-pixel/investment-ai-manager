from __future__ import annotations
import pandas as pd
from src.utils.config import DATA_DIR


def load_portfolio(path=None) -> pd.DataFrame:
    path = path or DATA_DIR / 'portfolio.csv'
    df = pd.read_csv(path)
    df['amount_cny'] = pd.to_numeric(df['amount_cny'], errors='coerce').fillna(0)
    return df


def portfolio_summary(df: pd.DataFrame) -> pd.DataFrame:
    total = df['amount_cny'].sum()
    summary = df.groupby('category', as_index=False)['amount_cny'].sum()
    summary['actual_ratio'] = summary['amount_cny'] / total
    return summary.sort_values('amount_cny', ascending=False)
