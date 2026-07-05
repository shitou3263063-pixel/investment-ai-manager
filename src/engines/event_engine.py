from __future__ import annotations
from datetime import date

IMPORTANT_EVENTS = [
    '美联储 FOMC 利率决议',
    '美国 CPI 通胀数据',
    '美国 PPI 数据',
    '美国非农就业数据',
    'VIX 恐慌指数异常',
    '美债收益率快速上行',
]


def macro_event_check(market_df):
    notes = []
    vix_row = market_df[market_df['name'].eq('VIX')]
    if not vix_row.empty and vix_row.iloc[0].get('close'):
        vix = float(vix_row.iloc[0]['close'])
        if vix >= 25:
            notes.append(f'VIX={vix:.1f}，市场恐慌升温，暂停追涨。')
        elif vix >= 18:
            notes.append(f'VIX={vix:.1f}，风险中等，控制新仓。')
        else:
            notes.append(f'VIX={vix:.1f}，市场风险暂未明显升温。')
    notes.append('宏观日历建议后续接入 Trading Economics / FRED / 财经日历 API。')
    return {'date': str(date.today()), 'watch_events': IMPORTANT_EVENTS, 'notes': notes}
