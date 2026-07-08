# SYNC_REPORT

## Check Time

2026-07-08

## Current Local Project

- Path: `C:\Users\12120\Documents\最强大脑`
- Git status command: failed
- Failure: `fatal: not a git repository (or any of the parent directories): .git`
- Note: this folder contains a `.git` directory, but it is not a valid Git repository.

## Required Git Commands In Current Project

### git status

Result:

```text
fatal: not a git repository (or any of the parent directories): .git
```

### git remote -v

Result:

```text
fatal: not a git repository (or any of the parent directories): .git
```

### git branch --show-current

Result:

```text
fatal: not a git repository (or any of the parent directories): .git
```

### git log --oneline -5

Result:

```text
fatal: not a git repository (or any of the parent directories): .git
```

## Nearby GitHub Repository Found

- Path: `C:\Users\12120\Documents\GitHub\investment-ai-manager`
- Branch: `main`
- Upstream: `origin/main`
- Remote:

```text
origin  https://github.com/shitou3263063-pixel/investment-ai-manager.git (fetch)
origin  https://github.com/shitou3263063-pixel/investment-ai-manager.git (push)
```

- Working tree: clean
- Current HEAD:

```text
89ab4a0e165f2ac5a10d4e114103976d51d0e708
```

- Recent commits:

```text
89ab4a0 Fix Gmail SMTP sending
4cfb053 Enable Gmail SMTP in GitHub Actions
0af710e Enable Gmail daily report
94c7b73 Enable Gmail daily report
d4058ce Improve WeCom error logging
```

## Uncommitted Changes

- Current project `C:\Users\12120\Documents\最强大脑`: cannot be determined by Git because the folder is not a valid Git repository.
- Nearby GitHub repo `C:\Users\12120\Documents\GitHub\investment-ai-manager`: no uncommitted changes.

## Commit And Push

- Requested commit message: `cleanup: consolidate Stone AI stable version`
- Commit executed: no
- Push executed: no
- Reason: the current local project folder is not a valid Git repository, so `git add`, `git commit`, and `git push` cannot be safely executed there.

## GitHub Actions Status

For the nearby GitHub repo:

- `.github/workflows/daily-investment-report.yml` calls `python -m src.main`
- `.github/workflows/daily.yml` calls `python main.py`
- Both upload `reports/`

For the cleaned current project:

- `.github/workflows/daily.yml` calls `python src/main.py`
- It uploads `reports/latest/`

Because the cleaned current project has not been committed and pushed to the actual GitHub repository, GitHub Actions will not run the cleaned latest code yet.

## Final Sync Status

- Local branch: unavailable in `C:\Users\12120\Documents\最强大脑`
- Remote repository: unavailable in current project; nearby repo uses `https://github.com/shitou3263063-pixel/investment-ai-manager.git`
- Has uncommitted changes: unknown for current project because Git repository is invalid
- Push successful: no
- Will GitHub Actions run latest cleaned code: no
- Failure reason: current project folder is not a valid Git repository; actual GitHub repo is a separate clean folder and does not contain the cleaned files from `最强大脑`.

