import csv
from pathlib import Path

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

def fetch_market_data():
    rows = []
    try:
        import yfinance as yf
        for name, ticker in SYMBOLS.items():
            try:
                data = yf.download(ticker, period="5d", interval="1d", progress=False, auto_adjust=False)
                if len(data) >= 2:
                    last_close = float(data["Close"].iloc[-1])
                    prev_close = float(data["Close"].iloc[-2])
                    change = (last_close - prev_close) / prev_close * 100
                    rows.append({
                        "name": name,
                        "ticker": ticker,
                        "change": round(change, 2),
                        "note": "自动获取"
                    })
                else:
                    rows.append({"name": name, "ticker": ticker, "change": 0.0, "note": "数据不足"})
            except Exception as e:
                rows.append({"name": name, "ticker": ticker, "change": 0.0, "note": f"获取失败：{e}"})
    except Exception as e:
        rows.append({"name": "Market Data", "ticker": "", "change": 0.0, "note": f"yfinance不可用：{e}"})
    return rows

def save_market_data(rows, path="data/market_data.csv"):
    Path("data").mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "ticker", "change", "note"])
        writer.writeheader()
        writer.writerows(rows)

def update_market_data(path="data/market_data.csv"):
    rows = fetch_market_data()
    save_market_data(rows, path)
    return rows
