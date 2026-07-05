from datetime import datetime
from pathlib import Path

def money(x):
    return f"{x:,.0f} 元"

def pct(x):
    return f"{x:.2%}"

def generate_report(portfolio_analysis, market_rows, decision):
    lines = []
    lines.append("# Stone AI Investment Manager Pro V4.0 日报")
    lines.append("")
    lines.append(f"日期：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"总资产：{money(portfolio_analysis['total'])}")
    lines.append(f"市场风险评分：{decision['risk_score']}/100")
    lines.append(f"操作等级：{decision['level']}")
    lines.append("")
    lines.append("## 一、市场数据")
    lines.append("| 指标 | 代码 | 日涨跌幅 | 备注 |")
    lines.append("|---|---|---:|---|")
    for r in market_rows:
        lines.append(f"| {r['name']} | {r.get('ticker','')} | {r['change']:.2f}% | {r.get('note','')} |")

    lines.append("")
    lines.append("## 二、资产配置")
    lines.append("| 类别 | 金额 | 当前占比 | 目标占比 | 偏离 |")
    lines.append("|---|---:|---:|---:|---:|")
    for r in portfolio_analysis["categories"]:
        lines.append(f"| {r['category']} | {money(r['value'])} | {pct(r['current_ratio'])} | {pct(r['target_ratio'])} | {pct(r['diff_ratio'])} |")

    lines.append("")
    lines.append("## 三、重大事件监控")
    if decision["alerts"]:
        for a in decision["alerts"]:
            lines.append(f"- 🚨 {a}")
    else:
        lines.append("- 今日没有触发重大市场事件。")

    lines.append("")
    lines.append("## 四、风险提示")
    if decision["risks"]:
        for r in decision["risks"]:
            lines.append(f"- {r}")
    else:
        lines.append("- 当前没有紧急风险提示。")

    lines.append("")
    lines.append("## 五、今日操作建议")
    for a in decision["actions"]:
        lines.append(f"- {a}")

    lines.append("")
    lines.append("## 六、一句话结论")
    lines.append("")
    lines.append(f"**{decision['final']}**")
    lines.append("")
    lines.append("> 本报告用于投资辅助和风险管理，不构成收益保证。")
    return "\n".join(lines)

def save_report(content, path="reports/daily_report.md"):
    Path("reports").mkdir(exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")
