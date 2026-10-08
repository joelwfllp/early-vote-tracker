"""Bake the NC and Maine pipeline outputs into one self-contained dashboard page.

Usage: python3 build.py   (after ~/nc-early-vote/run.py and ~/maine-early-vote/run.py)
Writes dashboard.html next to this file; publish it as the Early Vote Tracker artifact.
"""
import csv, json
from pathlib import Path

HERE = Path(__file__).parent
NC, ME = Path.home() / "nc-early-vote" / "out", Path.home() / "maine-early-vote" / "out"


def rows(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def num(v):
    try:
        x = float(v)
        return int(x) if x.is_integer() and "." not in str(v) else x
    except (TypeError, ValueError):
        return v


race = json.loads((NC / "race_series.json").read_text())
nc = {
    "asof": race["asof"], "days_out": race["days_out"],
    "comparison": [{k: num(v) for k, v in r.items()} for r in rows(NC / "comparison_2022_vs_2026.csv")],
    "quartile": [{k: num(v) for k, v in r.items()} for r in rows(NC / "quartile_per100k_same_days_out.csv")],
    "race": race["groups"],
}

me_raw = json.loads((ME / "dashboard_me.json").read_text())
# Compact the daily series: {cd|how|party|yr: [[days_out, per100k, cum], ...]}
daily = {}
for r in me_raw["daily"]:
    daily.setdefault(f'{r["cd"]}|{r["how"]}|{r["party"]}|{r["yr"]}', []).append([r["days_out"], r["per100k"], r["cum"]])
me = {"asof": me_raw["asof"], "days_out": me_raw["days_out"], "reg_asof": me_raw["reg_asof"],
      "same_days_out": me_raw["same_days_out"], "history": me_raw["history"], "daily": daily}

page = (HERE / "template.html").read_text().replace("/*__DATA__*/null", json.dumps({"nc": nc, "me": me}, separators=(",", ":")))
(HERE / "dashboard.html").write_text(page)
# Standalone copy for GitHub Pages (the artifact host adds the document skeleton; Pages does not).
(HERE / "docs").mkdir(exist_ok=True)
(HERE / "docs" / "index.html").write_text(
    '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n' + page + "\n</html>\n")
print(f"Wrote {HERE / 'dashboard.html'} ({len(page) / 1024:.0f} KB). NC through {nc['asof']}, ME through {me['asof']}.")
