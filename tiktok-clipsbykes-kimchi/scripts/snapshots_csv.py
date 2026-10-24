import json, csv
B = '.'; T0 = 1792539116
out = [dict(source='Rasmr screenshot (posted on X 2026-10-21 14:14 UTC; upper bound on time)', utc='2026-10-21T14:14Z', hours_since_post=round((1792592094 - T0) / 3600, 2), plays='', likes=48800, comments=56, shares='', saves=2305, downloads=''),
       dict(source='claim 9047 published read (2026-10-23 13:48 UTC)', utc='2026-10-23T13:48Z', hours_since_post=round((1792763280 - T0) / 3600, 2), plays=1040070, likes=89177, comments=95, shares=1369, saves=4200, downloads=208)]
snaps = [dict(t='20261023T233543Z', unix=1792798543, play_count=1082765, digg_count=92813, comment_count=101, share_count=1414, collect_count=4367, download_count=222)]
snaps += [json.loads(l) for l in open(B + '/raw/snapshots.jsonl') if '7698896779714071830' in l]
for s in snaps:
    out.append(dict(source='tikwm read (ours)', utc=s['t'], hours_since_post=round((s['unix'] - T0) / 3600, 2), plays=s['play_count'], likes=s['digg_count'], comments=s['comment_count'], shares=s['share_count'], saves=s['collect_count'], downloads=s['download_count']))
with open(B + '/data/target_snapshots.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
ctl = {}
for l in open(B + '/raw/snapshots.jsonl'):
    d = json.loads(l)
    if d['id'] != '7698896779714071830': ctl.setdefault(d['id'], []).append(d)
with open(B + '/data/control_snapshots.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['video_id', 'utc', 'plays', 'likes', 'comments', 'shares', 'saves', 'downloads'])
    for k, v in ctl.items():
        for d in v: w.writerow([k, d['t'], d['play_count'], d['digg_count'], d['comment_count'], d['share_count'], d['collect_count'], d['download_count']])
print(len(out), 'rows')
