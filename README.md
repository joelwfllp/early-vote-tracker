# Early Vote Tracker (dashboard)

Public site (GitHub Pages): https://joelwfllp.github.io/early-vote-tracker/ (repo joelwfllp/early-vote-tracker, served from `docs/`).
Published artifact: https://claude.ai/artifact/3q6MzCVQe1fcw8jWUgvjay (private until shared from its Share menu).

Daily update:
1. `cd ~/nc-early-vote && .venv/bin/python run.py > results_<date>.md` (also writes out/race_series.json)
2. `cd ~/maine-early-vote && .venv/bin/python run.py`
3. `python3 ~/early-vote-dashboard/build.py` -> dashboard.html
4. Republish dashboard.html to the artifact URL above (Claude: Artifact publish with this file path / url).
5. `git add -A && git commit -m "Update <date>" && git push` (build.py also writes docs/index.html for Pages).

NC study page (docs/nc-early-vote-signal/), also daily, after step 1:
`cd ~/nc-early-vote/retro && for s in elliott_groups early_years one_prior demo_share stratified stratified_active stratified_active_robust swing_check build_findings_html; do ../.venv/bin/python $s.py; done`
then `cp ../out/retro_findings.html ~/early-vote-dashboard/docs/nc-early-vote-signal/index.html` before the commit in step 5.

`template.html` is the page; `build.py` injects the data at `/*__DATA__*/null`.
