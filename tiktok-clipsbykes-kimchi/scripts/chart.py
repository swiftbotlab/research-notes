import json, math, datetime as dt
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

BASE = "."
SURF, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1"
BLUE, ORANGE, GRAY = "#2a78d6", "#eb6834", "#b9b8b2"
T0 = 1792539116  # target createTime (UTC 2026-10-20 23:31:56)
TID = "7698896779714071830"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10.5, "axes.edgecolor": MUTED, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.titlecolor": INK, "axes.titleweight": "bold", "axes.titlesize": 12})

rows = json.load(open(f"{BASE}/rows.json"))
S = json.load(open(f"{BASE}/search_compact.json"))
fit = json.load(open(f"{BASE}/catalog_fit.json"))
snaps = [json.loads(l) for l in open(f"{BASE}/raw/snapshots.jsonl") if TID in l]
first = {"unix": 1792798543, "play_count": 1082765, "digg_count": 92813, "comment_count": 101, "share_count": 1414, "collect_count": 4367, "download_count": 222}
snaps = [first] + snaps
last = snaps[-1]

fig = plt.figure(figsize=(16, 11.2), dpi=110, facecolor=SURF)
gs = fig.add_gridspec(2, 3, left=0.05, right=0.975, top=0.83, bottom=0.16, wspace=0.42, hspace=0.45, width_ratios=[1, 1, 1.05])
fig.text(0.05, 0.955, "@clipsbykes \"Kimchi just wanted to flex on Gunna\": is the engagement botted?", fontsize=19, weight="bold", color=INK)
fig.text(0.05, 0.915, "Verdict: the likes, saves and comments look organic, with no bot signature (about 80% confidence). The reach is real but engineered: a paid per-view\n"
         "clip account, one of 57+ same-day Kimchi clips from 40+ accounts, with Gunna as the hook. Data: TikTok public stats via tikwm, read 23-24 Oct 2026 UTC.",
         fontsize=11.5, color=INK2, va="top")

def style(ax):
    ax.set_facecolor(SURF)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.grid(True, color=GRID, lw=0.8, zorder=0); ax.set_axisbelow(True)

# A: likes vs comments, log-log
ax = fig.add_subplot(gs[0, 0:2]); style(ax)
cat = [r for r in rows if r["p"] >= 10000 and r["c"] > 0 and r["id"] != TID]
ax.scatter([r["l"] for r in cat], [r["c"] for r in cat], s=16, c=GRAY, edgecolors="none", zorder=2, label=f"@clipsbykes, its other {len(cat)} videos with 10k+ plays")
ctrl = [v for v in S if v["author"] != "clipsbykes" and v["comment_count"] > 0 and "kimchi" in v["title"].lower() and (v["play_count"] >= 100000 or (1792537200 <= v["create_time"] <= 1792540800 and "kimchi" in v["title"].lower()))]
same = [v for v in ctrl if 1792537200 <= v["create_time"] <= 1792540800]
other = [v for v in ctrl if v not in same]
ax.scatter([v["digg_count"] for v in other], [v["comment_count"] for v in other], s=46, marker="D", c="none", edgecolors=BLUE, linewidths=1.6, zorder=3,
           label=f"Other accounts: Kimchi clips with 100k+ plays ({len(other)})")
ax.scatter([v["digg_count"] for v in same], [v["comment_count"] for v in same], s=52, c=BLUE, edgecolors=SURF, linewidths=1.5, zorder=4,
           label=f"Other accounts: Kimchi clips posted in the same hour ({len(same)})")
ax.scatter([last["digg_count"]], [last["comment_count"]], s=170, c=ORANGE, edgecolors=SURF, linewidths=2, zorder=5, label="Target video")
xs = np.array([30, 600000])
for k in (100, 300, 1000):
    ax.plot(xs, xs / k, ls=(0, (4, 3)), lw=1, color=MUTED, zorder=1)
    ax.text(640000, 600000 / k, f"{k}:1", color=MUTED, fontsize=9, ha="left", va="center", clip_on=False)
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(150, 600000); ax.set_ylim(0.3, 9000)
ax.set_xlabel("Likes (log scale)"); ax.set_ylabel("Comments (log scale)")
ax.set_title("A. 900+ likes per comment is high, not unique: another account's upload of the same\n     Gunna scene runs 1,017:1 (dashed lines: likes per comment)", loc="left")
ax.annotate(f"Target: {last['digg_count']:,} likes / {last['comment_count']} comments", (last["digg_count"], last["comment_count"]), xytext=(18, -62),
            textcoords="offset points", fontsize=10, color=INK, ha="left", bbox=dict(boxstyle="round,pad=0.25", fc=SURF, ec=GRID), arrowprops=dict(arrowstyle="-", color=INK2, lw=1))
cec = [v for v in same if v["video_id"] == "7698897443185888542"][0]
ax.annotate("same Gunna scene, other account\n(4,069 likes / 4 comments)", (cec["digg_count"], cec["comment_count"]), xytext=(-30, -42), textcoords="offset points",
            fontsize=9, color=INK2, ha="right", bbox=dict(boxstyle="round,pad=0.2", fc=SURF, ec=GRID), arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
own = [r for r in rows if r["id"] == "7698926886654676246"][0]
ax.annotate("@clipsbykes, same vlog\n(9,447 likes / 5 comments)", (own["l"], own["c"]), xytext=(26, -40), textcoords="offset points",
            fontsize=9, color=INK2, ha="left", bbox=dict(boxstyle="round,pad=0.2", fc=SURF, ec=GRID), arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.legend(loc="upper left", frameon=True, facecolor=SURF, edgecolor=GRID, framealpha=1, fontsize=9, labelcolor=INK2)

# B: catalog z-scores
ax = fig.add_subplot(gs[0, 2]); style(ax)
names = [("likes|plays", "Likes | plays"), ("saves|plays", "Saves | plays"), ("shares|plays", "Shares | plays"), ("comments|plays", "Comments | plays"),
         ("shares|likes", "Shares | likes"), ("saves|likes", "Saves | likes"), ("comments|likes", "Comments | likes")]
z = [fit[k]["z"] for k, _ in names]
y = np.arange(len(names))[::-1]
ax.axvspan(-2, 2, color="#f1f0ec", zorder=0); ax.axvspan(-1, 1, color="#e9e8e3", zorder=0)
ax.barh(y, z, height=0.55, color=ORANGE, zorder=3)
ax.axvline(0, color=INK2, lw=1)
ax.set_yticks(y); ax.set_yticklabels([n for _, n in names]); ax.set_xlim(-3, 3)
for yi, zi in zip(y, z):
    ax.text(zi + (0.08 if zi >= 0 else -0.08), yi, f"{zi:+.2f}", va="center", ha="left" if zi >= 0 else "right", fontsize=9.5, color=INK)
ax.set_xlabel("z-score vs log-log fit of the account's\n361 other videos with 10k+ plays (shaded: 1 sd, 2 sd)")
ax.set_title("B. Against the full catalog (866 videos)\n     every metric is within 1.3 sd", loc="left")

# C: ratio stability over time (saves per 100 likes and likes per comment)
ax = fig.add_subplot(gs[1, 0]); style(ax)
pts = [(14.7, 48800, 56, 2305, "Rasmr screenshot\n(by 14:14 UTC 21 Oct)"), ((1792763280 - T0) / 3600, 89177, 95, 4200, "Rival read\n13:48 UTC 23 Oct"),
       ((last["unix"] - T0) / 3600, last["digg_count"], last["comment_count"], last["collect_count"], "Our\nread")]
hx = [p[0] for p in pts]; sv = [100 * p[3] / p[1] for p in pts]
ax.plot(hx, sv, color=ORANGE, lw=2, marker="o", ms=9, mec=SURF, mew=2, zorder=3)
for (h, l, c, s, lab), v in zip(pts, sv):
    ax.text(h, v + 0.35, f"{v:.2f}", ha="center", fontsize=10, color=INK)
    ax.text(h + (0 if h < 20 else (1 if h > 70 else -1)), 3.0, lab, ha="center" if h < 20 else ("left" if h > 70 else "right"), fontsize=8, color=INK2)
ax.set_ylim(2.6, 6.2); ax.set_xlim(0, 84)
ax.text(2, 5.85, "Likes per comment: %s" % "  ->  ".join(f"{p[1]/p[2]:.0f}" for p in pts), fontsize=9, color=INK2)
ax.set_xlabel("Hours since posting"); ax.set_ylabel("Saves per 100 likes")
ax.set_title("C. Saves per 100 likes stays flat from hour 15\n     to hour 73: no like-only burst was layered on", loc="left")

# D: marginal like rate per interval vs lifetime
ax = fig.add_subplot(gs[1, 1]); style(ax)
life = 100 * last["digg_count"] / last["play_count"]
a, b = (1040070, 89177), (last["play_count"], last["digg_count"])
tail = 100 * (b[1] - a[1]) / (b[0] - a[0])
own0 = snaps[0]; own = 100 * (last["digg_count"] - own0["digg_count"]) / max(1, last["play_count"] - own0["play_count"])
bars = [("Lifetime\n(all plays)", life), ("New plays, 13:48 to\n%s UTC (day 3)" % dt.datetime.utcfromtimestamp(last["unix"]).strftime("%H:%M"), tail),
        ("New plays during\nour own reads (%.1f h)" % ((last["unix"] - own0["unix"]) / 3600), own)]
xb = np.arange(len(bars))
ax.bar(xb, [v for _, v in bars], width=0.55, color=[GRAY, ORANGE, ORANGE], zorder=3)
for xi, (_, v) in zip(xb, bars): ax.text(xi, v + 0.2, f"{v:.1f}%", ha="center", fontsize=11, color=INK, weight="bold")
ax.set_xticks(xb); ax.set_xticklabels([n for n, _ in bars], fontsize=9)
ax.set_ylim(0, 11.5); ax.set_ylabel("Likes per 100 plays")
ax.set_title("D. Fresh day-3 viewers like at the lifetime rate.\n     Bought likes would leave the tail far lower", loc="left")
ax.text(-0.3, 10.6, "If 30%% of likes were bought, the organic tail\nwould run near %.1f%%." % (life * 0.7), fontsize=8.5, color=INK2)

# E: paid clipping evidence (text panel)
ax = fig.add_subplot(gs[1, 2]); ax.axis("off")
ax.set_title("E. Where the reach comes from", loc="left")
txt = ("PAID PER VIEW. Content Rewards (Whop) lists \"Orangie's\nCampaign\" by \"Memecoin Clippers (orangie)\": $1 per 1k views,\n"
       "13 Aug - 30 Sep 2026, $4,500 budget spent. Its top 5 clips\nare @clipsbykes posts. Clipper \"kesv1\" ranks #1: 49 approved\n"
       "clips, 3.1M paid views, $2,647 earned.\n\n"
       "A SAME-DAY FLOOD. In the 24 h after the vlog, 40+ other\naccounts posted 57+ Kimchi clips, 26 of them the Gunna\n"
       "scene. 6 used an identical caption (\"Kimchi, the trader who\nmade $40m on the Trump coin, had to ask Gunna...\").\n"
       "@clipsbykes itself posted 16 Kimchi clips that day.\n\n"
       "THE HOOK IS GUNNA. Top comments ask who these people\nare, or mock Kimchi (\"The greatest AI larp dev of 2024/5\").")
ax.text(0.0, 0.97, txt, va="top", fontsize=9.3, color=INK2, linespacing=1.42, transform=ax.transAxes)

fig.text(0.05, 0.088, "What would have meant bots: a like rate far off the account's norm; saves, comments and shares drifting apart from likes over time; a day-3 tail liking at a\n"
         "fraction of the lifetime rate; fresh or default-name commenter accounts. None of these shows up. Limits: TikTok's private analytics (traffic source,\n"
         "watch time) are not public. A drip-fed package that buys likes, saves and comments in natural proportions cannot be fully excluded.", fontsize=10, color=INK2, va="top")
fig.text(0.05, 0.02, "Sources: tikwm.com public API (TikTok stats, 866-video catalog, comments), TikTok search, Wayback Machine, contentrewards.com campaign page, x.com/rasmr_eth.  "
         "Full report, data and scripts: github.com/swiftbotlab/research-notes", fontsize=8.8, color=MUTED)
out = f"{BASE}/kimchi_clipsbykes_summary.png"
import os; os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out, facecolor=SURF); print(out, life, tail, own, len(snaps))
