from __future__ import annotations
from datetime import datetime
from pathlib import Path
import pandas as pd
from src.utils.config import REPORTS_DIR


def df_to_md(df: pd.DataFrame) -> str:
    if df is None or df.empty:
        return '无数据'
    return df.to_markdown(index=False)


def build_daily_report(portfolio_df, summary_df, market_df, risk, rebalance_df, dca_rows, event_info) -> str:
    today = datetime.now().strftime('%Y-%m-%d')
    total = portfolio_df['amount_cny'].sum()
    dca_df = pd.DataFrame(dca_rows)
    decision = '今日不建议频繁交易，以持有、观察、按纪律定投为主。'
    if risk['risk_level'] == '偏高':
        decision = '今日风险偏高：暂停追涨，优先保留现金，等待回撤或重大数据落地。'
    elif any(rebalance_df['action'].isin(['考虑降低', '考虑增加'])):
        decision = '组合存在偏离：只做小幅再平衡，不做一次性大调仓。'

    return f'''# Stone AI Investment Manager Pro V10 日报

日期：{today}

## 一句话结论

{decision}

## 组合总览

总资产估算：{total:,.0f} CNY

{df_to_md(summary_df)}

## 市场扫描

{df_to_md(market_df[['name','ticker','close','change_pct','ma20','trend']])}

## 风险评分

- 风险分：{risk['risk_score']}/100
- 风险等级：{risk['risk_level']}
- VIX：{risk.get('vix')}
- 股票占比：{risk['equity_ratio']:.2%}
- 黄金占比：{risk['gold_ratio']:.2%}
- 现金占比：{risk['cash_ratio']:.2%}

## 再平衡建议

{df_to_md(rebalance_df)}

## 定投提醒

{df_to_md(dca_df)}

## 宏观事件监控

关注事件：{', '.join(event_info['watch_events'])}

监控结论：

{chr(10).join('- ' + x for x in event_info['notes'])}

## 操作纪律

1. 不预测短期涨跌，只根据估值、仓位、风险和现金纪律行动。
2. 单日不做大额调仓，除非组合偏离目标超过阈值。
3. 重大宏观事件前暂停追涨。
4. 下跌时分批，不一次性满仓。
5. 所有建议仅用于辅助决策，不构成投资建议。
'''


def save_report(content: str, filename='daily_report.md') -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / filename
    path.write_text(content, encoding='utf-8')
    return path
