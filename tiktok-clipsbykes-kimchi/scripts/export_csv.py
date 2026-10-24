import json, csv, glob, re, datetime as dt
B = '.'; O = B + '/data'
iso = lambda t: dt.datetime.fromtimestamp(t, dt.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
V = json.load(open(sorted(glob.glob(B + '/raw/posts_*.json'))[-1]))['videos']
with open(O + '/clipsbykes_catalog_2026-10-23.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['video_id', 'posted_utc', 'plays', 'likes', 'comments', 'shares', 'saves', 'downloads', 'duration_s', 'kimchi_in_caption', 'caption'])
    for v in sorted(V, key=lambda v: v['create_time']):
        w.writerow([v['video_id'], iso(v['create_time']), v['play_count'], v['digg_count'], v['comment_count'], v['share_count'], v['collect_count'], v['download_count'], v['duration'], int('kimchi' in v['title'].lower()), v['title'].strip()])
S = json.load(open(B + '/search_compact.json'))
with open(O + '/kimchi_search_uploads_other_accounts.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['video_id', 'account', 'posted_utc', 'plays', 'likes', 'comments', 'shares', 'saves', 'downloads', 'duration_s', 'same_vlog_first_hour', 'caption'])
    for v in sorted(S, key=lambda v: -v['play_count']):
        if v['author'] == 'clipsbykes': continue
        w.writerow([v['video_id'], v['author'], iso(v['create_time']), v['play_count'], v['digg_count'], v['comment_count'], v['share_count'], v['collect_count'], v['download_count'], v['duration'],
                    int(1792537200 <= v['create_time'] <= 1792540800), v['title'].strip()])
for vid, name in [('7698896779714071830', 'target'), ('7668432497927015702', 'clipsbykes_2.58M_2026-07-30'), ('7649946596624583939', 'clipsbykes_kimchi_1.46M_2026-06-11'),
                  ('7654344038698552598', 'clipsbykes_kimchi_0.98M_2026-06-22'), ('7655417605502635286', 'clipsbykes_1.89M_2026-06-25'), ('7698898058687286542', 'doomclippr_same_vlog'), ('7698900879138753813', 'sulqs1_same_vlog')]:
    d = json.load(open(sorted(glob.glob(f'{B}/raw/comments_{vid}_*.json'))[-1]))
    with open(f'{O}/comments_{name}.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['comment_posted_utc', 'commenter_region', 'commenter_account_age_days_approx', 'default_style_handle', 'comment_likes', 'replies', 'text'])
        for c in sorted(d['comments'], key=lambda c: c['create_time']):
            u = c['user']; uid = int(u['id']); created = uid >> 32
            age = round((c['create_time'] - created) / 86400) if uid > 10**17 and created > 1420070400 else ''
            w.writerow([iso(c['create_time']), u.get('region', ''), age, int(bool(re.fullmatch(r'user\d{6,}', u.get('unique_id', '')))), c['digg_count'], c['reply_total'], c['text'].strip()])
print('ok')
