# CLEANUP_REPORT

## Summary

Stone AI Investment Manager has been consolidated to one runnable V12 line.

No investment strategy, target allocation, data source, or report body logic was added or rewritten. The cleanup only changed project structure, entry points, report output paths, and legacy file placement.

## Current Entry

- Unique main program: `src/main.py`
- One-click local run: `python src/main.py`
- Root compatibility entry: `main.py`
- Root `main.py` only forwards to `src.main.main`

## GitHub Actions

- Workflow file: `.github/workflows/daily.yml`
- Current command: `python src/main.py`
- Artifact path: `reports/latest/`
- Workflow count for report generation: one workflow, `daily.yml`
- Result: GitHub Actions will run the latest code after this cleaned project is committed and pushed.

## Kept Current Files

- `src/main.py`
- `main.py`
- `src/config/`
- `src/data/`
- `src/portfolio/`
- `src/risk/`
- `src/strategy/`
- `src/reports/`
- `src/analysis/`
- `src/ai/`
- `src/journal/`
- `src/macro/`
- `src/notifier/`
- `src/services/`
- `src/system/`
- `utils/data_loader.py`
- `utils/logger.py`
- `data/portfolio.csv`
- `data/market_data.csv`
- `data/investment_log.csv`
- `data/config.yaml`
- `.github/workflows/daily.yml`
- `requirements.txt`
- `README.md`

## Moved To Current Architecture

- `src/portfolio.py` -> `src/portfolio/__init__.py`
- `agents/portfolio_agent.py` -> `src/portfolio/agent.py`
- `agents/market_agent.py` -> `src/data/market_agent.py`
- `agents/risk_agent.py` -> `src/risk/agent.py`
- `agents/decision_agent.py` -> `src/strategy/decision_agent.py`
- `agents/rebalance_advisor.py` -> `src/strategy/rebalance_advisor.py`
- `agents/report_agent.py` -> `src/reports/report_agent.py`
- `src/data_sources/` -> `src/data/sources/`

## Archived Legacy Files

- `run.py` -> `archive/legacy_versions/run.py`
- `scripts/final_check.py` -> `archive/legacy_versions/scripts/final_check.py`
- `scripts/deploy_check.py` -> `archive/legacy_versions/scripts/deploy_check.py`
- `utils/market_data_provider.py` -> `archive/legacy_versions/utils/market_data_provider.py`
- `agents/` empty legacy directory -> `archive/legacy_versions/agents_empty_dir/`
- Python cache snapshots -> `archive/legacy_versions/`
- Previous root reports -> `reports/archive/pre_cleanup_20260708/`

## Latest Report Output

The current run writes only these four latest files:

- `reports/latest/daily_report.md`
- `reports/latest/today_action.md`
- `reports/latest/weekly_report.md`
- `reports/latest/chatgpt_brief.md`

Historical reports are stored under:

- `reports/archive/`

## Verification

Command executed:

```powershell
python src/main.py
```

Result:

- Program completed successfully.
- Generated only one latest report set in `reports/latest/`.
- `reports/` root contains no loose `.md` report files.
- GitHub Actions calls `python src/main.py`.
- Old active imports were checked; current source no longer imports `agents`, `run`, `utils.market_data_provider`, or `src.data_sources`.

## Remaining Notes

- Email sending failed in the local environment with a Windows socket permission error. This does not affect report generation.
- The current local folder is not a Git repository, so this cleanup was not committed or pushed from this workspace.
- `archive/legacy_versions/` intentionally remains available for inspection, but it is not imported by the current runtime or called by GitHub Actions.

