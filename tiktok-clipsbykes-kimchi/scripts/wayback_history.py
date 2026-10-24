import json, re, sys, urllib.request, time
caps = [("20250904165816", "https://www.tiktok.com/@clipsbykes"), ("20250907093552", "https://www.tiktok.com/@clipsbykes"),
        ("20251020062557", "https://www.tiktok.com/@clipsbykes"), ("20261013210224", "https://www.tiktok.com/@clipsbykes"),
        ("20261016185920", "https://www.tiktok.com/@clipsbykes/video/7676167509199867158"), ("20261011185816", "https://www.tiktok.com/@clipsbykes/video/7695200006583651607"),
        ("20260328000836", "https://www.tiktok.com/@clipsbykes/video/7611309647097580822"), ("20260511120455", "https://www.tiktok.com/@clipsbykes/video/7611309647097580822?lang=en"),
        ("20260327094648", "https://www.tiktok.com/@clipsbykes/video/7617921418046524694"), ("20260423125222", "https://www.tiktok.com/@clipsbykes/video/7619856626110975254"),
        ("20260331095312", "https://www.tiktok.com/@clipsbykes/video/7621275617060752662"), ("20260401191101", "https://www.tiktok.com/@clipsbykes/video/7620551989679705366")]
out = []
for ts, u in caps:
    url = f"https://web.archive.org/web/{ts}id_/{u}"
    try:
        h = urllib.request.urlopen(urllib.request.Request(url, headers={"user-agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
    except Exception as e:
        print(ts, "err", e); continue
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>', h, re.S)
    rec = {"wayback": ts, "url": u}
    if m:
        d = json.loads(m.group(1)).get("__DEFAULT_SCOPE__", {})
        ud = d.get("webapp.user-detail", {}).get("userInfo")
        if ud: rec["user_stats"] = ud.get("stats")
        it = d.get("webapp.video-detail", {}).get("itemInfo", {}).get("itemStruct")
        if it: rec["video_stats"] = it.get("stats"); rec["vid"] = it.get("id"); rec["createTime"] = it.get("createTime"); rec["authorStats"] = it.get("authorStats")
    else:
        for k in ["followerCount", "heartCount", "videoCount", "playCount", "diggCount"]:
            mm = re.search(r'"%s":(\d+)' % k, h)
            if mm: rec[k] = int(mm.group(1))
    print(json.dumps(rec)); out.append(rec); time.sleep(1)
json.dump(out, open("./raw/wb/wayback.json", "w"))
