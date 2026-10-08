# Early Vote Tracker (dashboard)

Public site (GitHub Pages): https://joelwfllp.github.io/early-vote-tracker/ (repo joelwfllp/early-vote-tracker, served from `docs/`).
Published artifact: https://claude.ai/artifact/3q6MzCVQe1fcw8jWUgvjay (private until shared from its Share menu).

Daily update:
1. `cd ~/nc-early-vote && .venv/bin/python run.py > results_<date>.md` (also writes out/race_series.json)
2. `cd ~/maine-early-vote && .venv/bin/python run.py`
3. `python3 ~/early-vote-dashboard/build.py` -> dashboard.html
4. Republish dashboard.html to the artifact URL above (Claude: Artifact publish with this file path / url).
5. `git add -A && git commit -m "Update <date>" && git push` (build.py also writes docs/index.html for Pages).

`template.html` is the page; `build.py` injects the data at `/*__DATA__*/null`.
