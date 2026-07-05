from __future__ import annotations


def dca_advice(market_df):
    rows = []
    for name in ['VOO', 'QQQ', 'HS300', 'HangSengTech', 'TLT', 'GOLD']:
        item = market_df[market_df['name'].eq(name)]
        if item.empty:
            continue
        row = item.iloc[0]
        if row.get('trend') == '数据获取失败':
            advice = '等待数据恢复'
        elif row.get('change_pct') is not None and row.get('change_pct') < -2:
            advice = '可小额定投，禁止满仓抄底'
        else:
            advice = '按计划定投/观察'
        rows.append({'asset': name, 'ticker': row.get('ticker'), 'trend': row.get('trend'), 'change_pct': row.get('change_pct'), 'advice': advice})
    return rows
