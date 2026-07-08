# Stone AI Investment Manager Pro V12

个人投资管理辅助系统。系统只读取资产、采集市场数据、生成报告和发送提醒；不自动交易，不接入券商下单权限，不承诺收益，所有内容仅供投资辅助，不构成投资建议。

## 唯一运行入口

```powershell
python src/main.py
```

根目录 `main.py` 仅作为兼容转发入口：

```powershell
python main.py
```

## 当前目录约定

- `src/main.py`：唯一主程序入口
- `src/config/`：配置相关代码
- `src/data/`：数据采集与市场数据路由
- `src/portfolio/`：持仓读取与资产配置分析
- `src/risk/`：风险评分
- `src/strategy/`：定投、再平衡、执行计划与决策
- `src/reports/`：日报、周报和行动清单生成
- `reports/latest/`：最新一次运行输出
- `reports/archive/`：历史报告归档
- `archive/legacy_versions/`：旧入口、旧检查脚本和历史缓存归档

## 最新输出

每次运行只生成一套最新报告：

```text
reports/latest/daily_report.md
reports/latest/today_action.md
reports/latest/weekly_report.md
reports/latest/chatgpt_brief.md
```

## 依赖安装

```powershell
python -m pip install -r requirements.txt
```

## 可选环境变量

本地可使用 `.env`，GitHub Actions 使用 Secrets：

```text
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
EMAIL_TO=
OPENAI_API_KEY=
FRED_API_KEY=
ALPHA_VANTAGE_API_KEY=
FINNHUB_API_KEY=
```

## GitHub Actions

`.github/workflows/daily.yml` 只调用：

```bash
python src/main.py
```

并上传：

```text
reports/latest/
```

