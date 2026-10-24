# Reproduce the key numbers in README.md from the CSVs in ../data (needs numpy).
#   python3 scripts/analyze.py
import csv, os, numpy as np

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
T = "7698896779714071830"


def rows(name):
    return list(csv.DictReader(open(os.path.join(D, name), encoding="utf-8")))


cat = rows("clipsbykes_catalog_2026-10-23.csv")
for r in cat:
    for k in ("plays", "likes", "comments", "shares", "saves", "downloads"):
        r[k] = int(r[k])
t = [r for r in cat if r["video_id"] == T][0]
R = [r for r in cat if r["plays"] >= 10000 and min(r["likes"], r["comments"], r["shares"], r["saves"]) > 0]
print(f"catalog: {len(cat)} videos, {len(R)} with 10k+ plays and non-zero counts")

print("\n1) Target vs log-log fit of the account's other videos (10k+ plays)")
for xk, yk in [("plays", "likes"), ("plays", "saves"), ("plays", "shares"), ("plays", "comments"), ("likes", "shares"), ("likes", "saves"), ("likes", "comments")]:
    O = [r for r in R if r["video_id"] != T]
    X, Y = np.log10([r[xk] for r in O]), np.log10([r[yk] for r in O])
    b, a = np.polyfit(X, Y, 1)
    sd = (Y - (a + b * X)).std(ddof=2)
    pred = 10 ** (a + b * np.log10(t[xk]))
    print(f"   {yk:>8} given {xk:<6} predicted {pred:9.0f}  actual {t[yk]:7d}  z = {(np.log10(t[yk]) - np.log10(pred)) / sd:+.2f}")

print("\n2) Likes per comment, account's own viral tier")
for lo in (100000, 500000):
    g = [r for r in cat if r["plays"] >= lo and r["comments"] > 0 and r["video_id"] != T]
    lc = np.array([r["likes"] / r["comments"] for r in g])
    print(f"   {lo:>7}+ plays: n={len(g)} median {np.median(lc):.0f}  p90 {np.percentile(lc, 90):.0f}  max {lc.max():.0f}")
print(f"   target: {t['likes'] / t['comments']:.0f}")

print("\n3) Same-vlog clips on @clipsbykes (posted 20 Oct 23:00 - 21 Oct 03:00 UTC, 50k+ plays)")
for r in cat:
    if "2026-10-20T23" <= r["posted_utc"] <= "2026-10-21T03" and r["plays"] >= 50000:
        print(f"   {r['posted_utc']} plays {r['plays']:>8} likes/comment {r['likes'] / max(1, r['comments']):6.0f}  saves per 100 likes {100 * r['saves'] / r['likes']:.1f}  {r['caption'][:40]}")

print("\n4) Other accounts, clips posted within the first hour of the vlog (20 Oct 23:00-24:00 UTC)")
for r in rows("kimchi_search_uploads_other_accounts.csv"):
    if r["same_vlog_first_hour"] == "1" and int(r["comments"]) > 0:
        print(f"   {r['account']:>16} plays {int(r['plays']):>7} likes/comment {int(r['likes']) / int(r['comments']):6.0f}  like rate {100 * int(r['likes']) / int(r['plays']):.1f}%  {r['caption'][:40]}")

print("\n5) Target over time (data/target_snapshots.csv)")
S = rows("target_snapshots.csv")
for s in S:
    l, c, sv = int(s["likes"]), int(s["comments"]), int(s["saves"])
    print(f"   h{float(s['hours_since_post']):6.2f} {s['source'][:38]:<38} likes {l:6d} comments {c:4d} saves {sv:5d}  saves/100 likes {100 * sv / l:.2f}  likes/comment {l / c:.0f}")
P = [s for s in S if s["plays"]]
a, b = P[0], P[-1]
dp, dl = int(b["plays"]) - int(a["plays"]), int(b["likes"]) - int(a["likes"])
print(f"   marginal like rate {a['source'][:20]} -> last read: {100 * dl / dp:.2f}% of {dp} new plays (lifetime {100 * int(b['likes']) / int(b['plays']):.2f}%)")
own = [s for s in S if s["source"].startswith("tikwm")]
if len(own) > 1:
    a, b = own[0], own[-1]
    dp, dl = int(b["plays"]) - int(a["plays"]), int(b["likes"]) - int(a["likes"])
    print(f"   marginal like rate over our own reads ({float(b['hours_since_post']) - float(a['hours_since_post']):.2f} h): {100 * dl / dp:.2f}% of {dp} new plays")
