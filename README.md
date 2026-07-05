# Stone AI Investment Manager Pro V10

这是一个私人 AI 投资管家骨架版本，目标是每天自动生成可执行的投资日报和周报。

## V10 已包含

- 自动读取持仓：`data/portfolio.csv`
- 自动联网获取市场行情：Yahoo Finance / yfinance
- 宏观事件监控：VIX + 事件清单，后续可接入财经日历 API
- 根据资产配置生成再平衡建议
- 自动生成日报：`reports/daily_report.md`
- 自动生成周报：`reports/weekly_report.md`
- GitHub Actions 每天自动运行
- 邮件通知：通过 SMTP 环境变量配置
- 定投提醒
- 风险评分
- 黄金、债券、美元、美股、港股联动监控
- 预留 OpenAI API 扩展入口

## 本地运行

```bash
pip install -r requirements.txt
python -m src.main
```

运行后查看：

```text
reports/daily_report.md
```

## 修改你的持仓

打开：

```text
data/portfolio.csv
```

按真实金额修改 `amount_cny`。

## 修改目标配置

打开：

```text
config/settings.yaml
```

重点修改：

```yaml
target_allocation:
  us_equity: 0.18
  hk_cn_equity: 0.16
  china_equity: 0.08
  bonds: 0.36
  gold: 0.16
  cash: 0.06
```

## GitHub Actions 自动运行

项目已内置：

```text
.github/workflows/daily-investment-report.yml
```

上传到 GitHub 后，它会每天自动运行，也可以手动点击 `Run workflow`。

## 邮件通知设置

在 GitHub 仓库：

```text
Settings → Secrets and variables → Actions → New repository secret
```

添加：

```text
SMTP_HOST
SMTP_PORT
SMTP_USER
SMTP_PASSWORD
EMAIL_TO
```

Gmail 用户建议使用“应用专用密码”，不要直接使用邮箱登录密码。

## 给 Codex 的启动指令

```text
请把这个项目升级并运行成 Stone AI Investment Manager Pro V10。

要求：
1. 安装 requirements.txt。
2. 执行 python -m src.main。
3. 如果报错，请自动修复，直到 reports/daily_report.md 可以正常生成。
4. 检查 data/portfolio.csv 是否能读取我的持仓。
5. 检查 config/settings.yaml 的目标配置是否生效。
6. 检查 GitHub Actions 文件是否能每天自动运行。
7. 不要接入真实交易，不要自动买卖，只生成建议和提醒。
```

## 免责声明

本项目仅用于投资研究、风险监控和个人决策辅助，不构成投资建议，也不应自动执行真实交易。
