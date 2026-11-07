#!/usr/bin/env python3
"""
Generates assets/stats-dashboard.svg for the GitHub profile README.

Data comes straight from the GitHub GraphQL API (no third-party stat services).
Standard library only, so the workflow needs no `pip install`.

Usage:
  python scripts/generate_stats.py               # live data (needs GH_TOKEN)
  python scripts/generate_stats.py --placeholder # neutral card, no numbers
  python scripts/generate_stats.py --mock        # fake data, for layout testing only
"""
import datetime as dt
import json
import os
import random
import sys
import urllib.request
from xml.sax.saxutils import escape

LOGIN = os.environ.get("GH_LOGIN", "Karunpoojari7")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = os.environ.get("OUT", "assets/stats-dashboard.svg")
API = "https://api.github.com/graphql"

MONO = "font-family=\"'Courier New', Consolas, monospace\""
SANS = "font-family=\"'Segoe UI', Helvetica, Arial, sans-serif\""
GREENS = ["#101c19", "#0b4d36", "#0f7a53", "#00b574", "#00ff9c"]


# ----------------------------------------------------------------- data ----
def gql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        API,
        data=body,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        res = json.load(r)
    if "errors" in res:
        raise RuntimeError(json.dumps(res["errors"]))
    return res["data"]


PROFILE_Q = """
query($login:String!){
  user(login:$login){
    createdAt
    followers{ totalCount }
    publicRepos: repositories(privacy:PUBLIC, ownerAffiliations:OWNER){ totalCount }
    repositories(first:100, privacy:PUBLIC, ownerAffiliations:OWNER, isFork:false){
      nodes{
        stargazerCount
        languages(first:8, orderBy:{field:SIZE, direction:DESC}){
          edges{ size node{ name color } }
        }
      }
    }
  }
}"""

CONTRIB_Q = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    contributionsCollection(from:$from, to:$to){
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar{ weeks{ contributionDays{ date contributionCount } } }
    }
  }
}"""


def fetch_live():
    now = dt.datetime.now(dt.timezone.utc)
    p = gql(PROFILE_Q, {"login": LOGIN})["user"]
    created = dt.datetime.fromisoformat(p["createdAt"].replace("Z", "+00:00")).date()

    days, commits, prs, issues = {}, 0, 0, 0
    start, end = created, now.date()
    while start <= end:
        stop = min(start + dt.timedelta(days=364), end)  # API max span is 1 year
        v = {
            "login": LOGIN,
            "from": f"{start.isoformat()}T00:00:00Z",
            "to": f"{stop.isoformat()}T23:59:59Z",
        }
        c = gql(CONTRIB_Q, v)["user"]["contributionsCollection"]
        commits += c["totalCommitContributions"]
        prs += c["totalPullRequestContributions"]
        issues += c["totalIssueContributions"]
        for w in c["contributionCalendar"]["weeks"]:
            for d in w["contributionDays"]:
                days[d["date"]] = d["contributionCount"]  # dict -> no double counting
        start = stop + dt.timedelta(days=1)

    langs = {}
    stars = 0
    for r in p["repositories"]["nodes"]:
        stars += r["stargazerCount"]
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            cur = langs.get(n, [0, e["node"]["color"] or "#8B949E"])
            cur[0] += e["size"]
            langs[n] = cur

    return {
        "placeholder": False,
        "updated": now.strftime("%Y-%m-%d %H:%M UTC"),
        "joined": created,
        "days": {dt.date.fromisoformat(k): v for k, v in days.items()},
        "commits": commits,
        "prs": prs,
        "issues": issues,
        "repos": p["publicRepos"]["totalCount"],
        "stars": stars,
        "followers": p["followers"]["totalCount"],
        "langs": langs,
    }


def mock():
    today = dt.datetime.now(dt.timezone.utc).date()
    random.seed(7)
    days = {}
    for i in range(500):
        d = today - dt.timedelta(days=i)
        days[d] = 0 if (i > 20 and random.random() < 0.35) else random.randint(1, 9)
    return {
        "placeholder": False,
        "updated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "joined": today - dt.timedelta(days=499),
        "days": days, "commits": 812, "prs": 14, "issues": 3, "repos": 27,
        "stars": 0, "followers": 2,
        "langs": {"TypeScript": [520000, "#3178c6"], "Python": [210000, "#3572A5"],
                  "HTML": [90000, "#e34c26"], "PowerShell": [40000, "#012456"],
                  "JavaScript": [30000, "#f1e05a"], "CSS": [9000, "#563d7c"]},
    }


def placeholder():
    return {"placeholder": True, "updated": "AWAITING FIRST RUN", "days": {}, "langs": {}}


# ------------------------------------------------------------- analysis ----
def streaks(days, today):
    """Current + longest streak. A streak is still alive if today is empty but yesterday was not."""
    def n(d):
        return days.get(d, 0)

    best, best_rng, run, run_start = 0, None, 0, None
    for d in sorted(days):
        if days[d] > 0:
            if run == 0:
                run_start = d
            run += 1
            if run > best:
                best, best_rng = run, (run_start, d)
        else:
            run = 0

    cur_end = today if n(today) > 0 else today - dt.timedelta(days=1)
    cur, d = 0, cur_end
    while n(d) > 0:
        cur += 1
        d -= dt.timedelta(days=1)
    cur_rng = (cur_end - dt.timedelta(days=cur - 1), cur_end) if cur else None
    return cur, cur_rng, best, best_rng


def fmt_d(d):
    return d.strftime("%b %-d") if d else "-"


def fmt_rng(r):
    return f"{fmt_d(r[0])} - {fmt_d(r[1])}" if r else "no active streak"


# ------------------------------------------------------------ rendering ----
def render(d):
    ph = d["placeholder"]
    today = dt.datetime.now(dt.timezone.utc).date()
    days = d["days"]
    dash = "-"

    if ph:
        total = cur = best = last30 = None
        cur_rng = best_rng = None
        vals = {k: dash for k in ("commits", "prs", "repos", "stars", "followers")}
        joined_txt = "run the workflow once"
        avg_txt = "to load live data"
    else:
        total = sum(days.values())
        cur, cur_rng, best, best_rng = streaks(days, today)
        last30 = sum(v for k, v in days.items() if (today - k).days < 30)
        vals = {k: f"{d[k]:,}" for k in ("commits", "prs", "repos", "stars", "followers")}
        joined_txt = f"since {d['joined'].strftime('%b %-d, %Y')}"
        avg_txt = f"avg {last30 / 30:.1f} per day"

    def num(v):
        return dash if v is None else f"{v:,}"

    o = []
    w, h = 900, 466
    o.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="GitHub activity dashboard for {LOGIN}">
<defs>
<pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="#00FF9C" stroke-opacity="0.04"/></pattern>
<linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00FF9C"/><stop offset="0.5" stop-color="#2389E8"/><stop offset="1" stop-color="#00FF9C"/></linearGradient>
<clipPath id="cp"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12"/></clipPath>
</defs>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="#080D12"/>
<g clip-path="url(#cp)"><rect width="{w}" height="{h}" fill="url(#grid)"/>
<rect width="{w}" height="38" fill="#0D1A17"/><line x1="0" y1="38" x2="{w}" y2="38" stroke="#00FF9C" stroke-opacity="0.25"/></g>
<circle cx="24" cy="19" r="6" fill="#FF5F56"/><circle cx="44" cy="19" r="6" fill="#FFBD2E"/><circle cx="64" cy="19" r="6" fill="#27C93F"/>
<text x="450" y="24" text-anchor="middle" {MONO} font-size="12" fill="#7FA89A">karun@karun-lab: ~/github-activity</text>
<circle cx="{878 - (len(d["updated"]) + 8) * 7.1 - 10:.1f}" cy="19" r="3.5" fill="#00FF9C"><animate attributeName="opacity" values="1;0.25;1" dur="1.8s" repeatCount="indefinite"/></circle>
<text x="878" y="23" text-anchor="end" {MONO} font-size="10" fill="#00FF9C" letter-spacing="1">UPDATED {escape(d["updated"])}</text>''')

    # ---- metric tiles
    tiles = [
        ("TOTAL CONTRIBUTIONS", num(total), "", joined_txt, "#00FF9C"),
        ("CURRENT STREAK", num(cur), "days", fmt_rng(cur_rng) if not ph else "to load live data", "#2389E8"),
        ("LONGEST STREAK", num(best), "days", fmt_rng(best_rng) if not ph else "to load live data", "#A78BFA"),
        ("LAST 30 DAYS", num(last30), "", avg_txt, "#22D3EE"),
    ]
    for i, (lab, val, unit, sub, col) in enumerate(tiles):
        x, y = 18 + i * 220, 54
        o.append(f'<rect x="{x}" y="{y}" width="204" height="88" rx="8" fill="#0A1218" stroke="{col}" stroke-opacity="0.4"/>')
        o.append(f'<rect x="{x}" y="{y}" width="4" height="88" rx="2" fill="{col}"/>')
        o.append(f'<text x="{x+18}" y="{y+24}" {MONO} font-size="10" fill="{col}" letter-spacing="1.6">{lab}</text>')
        u = f'<tspan font-size="13" fill="#7FA89A" font-weight="400"> {unit}</tspan>' if unit else ""
        o.append(f'<text x="{x+18}" y="{y+60}" {SANS} font-size="34" font-weight="700" fill="#E6EDF3">{val}{u}</text>')
        o.append(f'<text x="{x+18}" y="{y+78}" {MONO} font-size="10" fill="#7C8F9C">{escape(sub)}</text>')

    # ---- heatmap panel
    px, py, pw, ph_ = 18, 158, 520, 214
    o.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph_}" rx="8" fill="#0A1218" stroke="#00FF9C" stroke-opacity="0.25"/>')
    o.append(f'<text x="{px+20}" y="{py+26}" {MONO} font-size="10" fill="#00FF9C" letter-spacing="1.6">ACTIVITY  /  LAST 26 WEEKS</text>')
    week0 = today - dt.timedelta(days=(today.weekday() + 1) % 7) - dt.timedelta(weeks=25)  # Sunday-aligned
    recent = [v for k, v in days.items() if (today - k).days < 26 * 7]
    mx = max(recent) if recent else 0
    for c in range(26):
        for r in range(7):
            dd = week0 + dt.timedelta(days=c * 7 + r)
            if dd > today:
                continue
            v = days.get(dd, 0)
            lvl = 0 if v <= 0 or mx == 0 else min(4, max(1, -(-v * 4 // mx)))
            o.append(f'<rect x="{px+20+c*18}" y="{py+42+r*18}" width="14" height="14" rx="3" fill="{GREENS[lvl]}"/>')
    o.append(f'<text x="{px+20}" y="{py+196}" {MONO} font-size="9" fill="#5C6F7E">LESS</text>')
    for i, gc in enumerate(GREENS):
        o.append(f'<rect x="{px+54+i*18}" y="{py+187}" width="12" height="12" rx="3" fill="{gc}"/>')
    o.append(f'<text x="{px+54+5*18+6}" y="{py+196}" {MONO} font-size="9" fill="#5C6F7E">MORE</text>')

    # ---- languages panel
    lx, lw = 554, 328
    o.append(f'<rect x="{lx}" y="{py}" width="{lw}" height="{ph_}" rx="8" fill="#0A1218" stroke="#2389E8" stroke-opacity="0.3"/>')
    o.append(f'<text x="{lx+20}" y="{py+26}" {MONO} font-size="10" fill="#2389E8" letter-spacing="1.6">TOP LANGUAGES  /  BY CODE SIZE</text>')
    langs = sorted(d["langs"].items(), key=lambda kv: -kv[1][0])[:5]
    tot = sum(v[0] for v in d["langs"].values()) or 1
    if not langs:
        o.append(f'<text x="{lx+20}" y="{py+70}" {SANS} font-size="13" fill="#7C8F9C">Waiting for the first workflow run.</text>')
    for i, (name, (size, color)) in enumerate(langs):
        y = py + 54 + i * 29
        pct = size * 100 / tot
        o.append(f'<text x="{lx+20}" y="{y}" {SANS} font-size="12.5" fill="#C9D4DC">{escape(name)}</text>')
        o.append(f'<text x="{lx+lw-20}" y="{y}" text-anchor="end" {MONO} font-size="11" fill="#9FB3C8">{pct:.1f}%</text>')
        o.append(f'<rect x="{lx+20}" y="{y+7}" width="{lw-40}" height="5" rx="2.5" fill="#142029"/>')
        o.append(f'<rect x="{lx+20}" y="{y+7}" width="{max(3, (lw-40)*pct/100):.1f}" height="5" rx="2.5" fill="{escape(color)}"/>')
    o.append(f'<text x="{lx+20}" y="{py+ph_-12}" {MONO} font-size="9" fill="#5C6F7E">PUBLIC, NON-FORK REPOS</text>')

    # ---- footer strip
    fy = 386
    o.append(f'<rect x="18" y="{fy}" width="864" height="48" rx="8" fill="#0A1218" stroke="#00FF9C" stroke-opacity="0.2"/>')
    items = [("COMMITS", vals["commits"]), ("PULL REQUESTS", vals["prs"]), ("PUBLIC REPOS", vals["repos"]),
             ("STARS EARNED", vals["stars"]), ("FOLLOWERS", vals["followers"])]
    cw = 864 / len(items)
    for i, (lab, val) in enumerate(items):
        cx = 18 + cw * i + cw / 2
        o.append(f'<text x="{cx:.1f}" y="{fy+22}" text-anchor="middle" {MONO} font-size="16" font-weight="bold" fill="#00FF9C">{val}</text>')
        o.append(f'<text x="{cx:.1f}" y="{fy+38}" text-anchor="middle" {MONO} font-size="9" fill="#7C8F9C" letter-spacing="1.4">{lab}</text>')
        if i:
            o.append(f'<line x1="{18+cw*i:.1f}" y1="{fy+10}" x2="{18+cw*i:.1f}" y2="{fy+38}" stroke="#00FF9C" stroke-opacity="0.15"/>')

    o.append(f'<text x="450" y="{h-14}" text-anchor="middle" {MONO} font-size="9" fill="#5C6F7E">Counted by GitHub rules: default branch only, UTC days, private activity only if enabled in profile settings.</text>')
    o.append(f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="none" stroke="url(#bd)" stroke-width="1.5"><animate attributeName="stroke-opacity" values="1;0.4;1" dur="4s" repeatCount="indefinite"/></rect>')
    o.append("</svg>")
    return "\n".join(o)


def main():
    if "--placeholder" in sys.argv:
        data = placeholder()
    elif "--mock" in sys.argv:
        data = mock()
    else:
        if not TOKEN:
            sys.exit("GH_TOKEN is not set. Use --placeholder or --mock for offline runs.")
        data = fetch_live()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(data))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
