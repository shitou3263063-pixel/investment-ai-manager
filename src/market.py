import csv
from pathlib import Path
import time

SYMBOLS = {
    "S&P 500": "^GSPC",
    "Nasdaq 100": "^NDX",
    "VIX": "^VIX",
    "Gold ETF": "GLD",
    "TLT": "TLT",
    "USD Index": "DX-Y.NYB",
    "VOO": "VOO",
    "NVDA": "NVDA",
    "GOOGL": "GOOGL",
    "BABA": "BABA",
    "XLF": "XLF",
    "IBKR": "IBKR"
}

def _safe_change_from_yfinance(ticker):
    import yfinance as yf
    data = yf.download(ticker, period="5d", interval="1d", progress=False, auto_adjust=False, threads=False)
    if len(data) < 2:
        return None, "数据不足"
    last_close = float(data["Close"].iloc[-1])
    prev_close = float(data["Close"].iloc[-2])
    change = (last_close - prev_close) / prev_close * 100
    return round(change, 2), "自动获取"

def fetch_market_data():
    rows = []
    try:
        for name, ticker in SYMBOLS.items():
            change = None
            note = ""
            for attempt in range(2):
                try:
                    change, note = _safe_change_from_yfinance(ticker)
                    break
                except Exception as e:
                    note = f"获取失败：{e}"
                    time.sleep(1.5)
            rows.append({
                "name": name,
                "ticker": ticker,
                "change": 0.0 if change is None else change,
                "note": note
            })
            time.sleep(0.3)
    except Exception as e:
        rows.append({"name": "Market Data", "ticker": "", "change": 0.0, "note": f"yfinance不可用：{e}"})
    return rows

def save_market_data(rows, path="data/market_data.csv"):
    Path("data").mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "ticker", "change", "note"])
        writer.writeheader()
        writer.writerows(rows)

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

def update_market_data(path="data/market_data.csv"):
    rows = fetch_market_data()
    good_rows = [r for r in rows if not str(r.get("note","")).startswith("获取失败")]
    if len(good_rows) >= 3:
        save_market_data(rows, path)
        return rows

    cached = load_cached_market_data(path)
    if cached:
        for r in cached:
            r["note"] = "使用缓存数据"
        return cached

    save_market_data(rows, path)
    return rows
