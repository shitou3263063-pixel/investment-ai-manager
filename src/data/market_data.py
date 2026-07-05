from __future__ import annotations
import pandas as pd
import yfinance as yf
from datetime import datetime


def flatten_watchlist(settings: dict) -> dict:
    result = {}
    for _, group in settings.get('watchlist', {}).items():
        for name, ticker in group.items():
            result[name] = ticker
    return result


def fetch_market_snapshot(settings: dict) -> pd.DataFrame:
    rows = []
    for name, ticker in flatten_watchlist(settings).items():
        try:
            hist = yf.download(ticker, period='1mo', interval='1d', progress=False, auto_adjust=True)
            if hist.empty:
                raise ValueError('empty data')
            close = float(hist['Close'].iloc[-1])
            prev = float(hist['Close'].iloc[-2]) if len(hist) > 1 else close
            ma20 = float(hist['Close'].tail(20).mean())
            change_pct = (close / prev - 1) * 100 if prev else 0
            trend = '上涨' if close >= ma20 else '弱势/震荡'
            rows.append({
                'name': name,
                'ticker': ticker,
                'close': round(close, 4),
                'change_pct': round(change_pct, 2),
                'ma20': round(ma20, 4),
                'trend': trend,
                'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        except Exception as e:
            rows.append({'name': name, 'ticker': ticker, 'close': None, 'change_pct': None, 'ma20': None, 'trend': '数据获取失败', 'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'error': str(e)})
    return pd.DataFrame(rows)
