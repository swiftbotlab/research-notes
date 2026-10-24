import json, numpy as np, datetime as dt
rows = json.load(open('./rows.json'))
T = '7698896779714071830'
R = [r for r in rows if r['p'] >= 10000 and r['l'] > 0 and r['c'] > 0 and r['sv'] > 0 and r['s'] > 0]
print('videos >=10k plays:', len(R))
def fit(xk, yk, excl=T):
    X = np.log10([r[xk] for r in R if r['id'] != excl]); Y = np.log10([r[yk] for r in R if r['id'] != excl])
    b, a = np.polyfit(X, Y, 1); res = Y - (a + b * X); sd = res.std(ddof=2)
    t = [r for r in rows if r['id'] == T][0]
    pred = 10 ** (a + b * np.log10(t[xk])); z = (np.log10(t[yk]) - np.log10(pred)) / sd
    allres = {r['id']: (np.log10(r[yk]) - (a + b * np.log10(r[xk]))) / sd for r in R}
    pct = 100 * np.mean([v <= z for v in allres.values()])
    return dict(slope=round(b, 3), pred=round(pred), actual=t[yk], z=round(z, 2), pct=round(pct, 1)), allres
out = {}
for xk, yk, name in [('p', 'l', 'likes|plays'), ('p', 'c', 'comments|plays'), ('p', 'sv', 'saves|plays'), ('p', 's', 'shares|plays'), ('p', 'd', 'downloads|plays'),
                     ('l', 'c', 'comments|likes'), ('l', 'sv', 'saves|likes'), ('l', 's', 'shares|likes')]:
    if yk == 'd':
        continue
    o, allres = fit(xk, yk); out[name] = o; print(name, o)
    big = sorted(allres.items(), key=lambda kv: -abs(kv[1]))[:3]
    print('   most extreme:', [(k[-6:], round(v, 2)) for k, v in big])
# the 'bought likes' signature: high likes|plays AND low saves|likes AND low comments|likes
_, zl = fit('p', 'l'); _, zs = fit('l', 'sv'); _, zc = fit('l', 'c')
sig = sorted(R, key=lambda r: -(zl[r['id']] - zs[r['id']] - zc[r['id']]))[:8]
print('top "bought-like signature" scores (z_likes|plays - z_saves|likes - z_comments|likes):')
for r in sig:
    print(f"  {dt.datetime.utcfromtimestamp(r['t']):%Y-%m-%d} {r['id']} p={r['p']} score={zl[r['id']]-zs[r['id']]-zc[r['id']]:.2f} zl={zl[r['id']]:.2f} zs={zs[r['id']]:.2f} zc={zc[r['id']]:.2f} {r['title'][:40]}")
t = [r for r in R if r['id'] == T][0]
rank = sorted(R, key=lambda r: -(zl[r['id']] - zs[r['id']] - zc[r['id']])).index(t) + 1
print('target signature rank', rank, 'of', len(R))
# absurd small-video like rates
odd = [r for r in rows if r['p'] >= 1000 and r['l'] / r['p'] > 0.2]
print('videos with like rate >20% (>=1k plays):', len(odd))
# monthly medians
import collections
m = collections.defaultdict(list)
for r in rows: m[dt.datetime.utcfromtimestamp(r['t']).strftime('%Y-%m')].append(r)
for k in sorted(m):
    v = m[k]; P = [x['p'] for x in v]; LR = [x['l'] / x['p'] for x in v if x['p'] > 0]
    print(k, 'n', len(v), 'median plays', int(np.median(P)), 'max', max(P), 'median like-rate %.3f' % np.median(LR), 'kimchi', sum(x['kim'] for x in v))
json.dump(out, open('./catalog_fit.json', 'w'))
