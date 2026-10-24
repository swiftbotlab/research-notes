# Pull @clipsbykes data from tikwm (public TikTok mirror API). Output -> ./raw/.
import json, time, urllib.request, urllib.parse, sys, os
OUT = "./raw"
# tikwm.com mirrors TikTok public stats. Its /api/ (single video) works with plain requests; the user/search/comment
# endpoints may sit behind a Cloudflare check: open tikwm.com once in a browser and put that browser's user-agent and
# cookie string in session.json as {"ua": ..., "cookie": ...}.
try:
    _cf = json.load(open("./session.json"))
except FileNotFoundError:
    _cf = {"ua": "Mozilla/5.0", "cookie": ""}
UA = {"user-agent": _cf["ua"], "cookie": _cf["cookie"], "referer": "https://www.tikwm.com/"}
def get(path, **q):
    url = "https://www.tikwm.com" + path + "?" + urllib.parse.urlencode(q)
    for i in range(5):
        try:
            r = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read())
            if r.get("code") == 0:
                return r
            print("api", r.get("code"), r.get("msg"), file=sys.stderr)
        except Exception as e:
            print("err", e, file=sys.stderr)
        time.sleep(2 + 2 * i)
    return None
ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
what = sys.argv[1]
if what == "info":
    r = get("/api/user/info", unique_id="clipsbykes")
    json.dump({"t": ts, **r}, open(f"{OUT}/user_info_{ts}.json", "w")); print(json.dumps(r["data"])[:800])
elif what == "posts":
    allv, cursor = [], 0
    for page in range(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
        r = get("/api/user/posts", unique_id="clipsbykes", count=35, cursor=cursor)
        if not r: break
        vids = r["data"].get("videos", [])
        allv += vids
        print(page, len(vids), r["data"].get("cursor"), r["data"].get("hasMore"), file=sys.stderr)
        if not r["data"].get("hasMore"): break
        cursor = r["data"]["cursor"]; time.sleep(1.2)
    json.dump({"t": ts, "videos": allv}, open(f"{OUT}/posts_{ts}.json", "w")); print(len(allv))
elif what == "comments":
    vid = sys.argv[2]; url = f"https://www.tiktok.com/@x/video/{vid}"
    allc, cursor = [], 0
    for page in range(20):
        r = get("/api/comment/list/", url=url, count=50, cursor=cursor)
        if not r: break
        cs = r["data"].get("comments", []) or []
        allc += cs
        print(page, len(cs), r["data"].get("cursor"), r["data"].get("hasMore"), r["data"].get("total"), file=sys.stderr)
        if not r["data"].get("hasMore"): break
        cursor = r["data"]["cursor"]; time.sleep(1.2)
    json.dump({"t": ts, "vid": vid, "comments": allc}, open(f"{OUT}/comments_{vid}_{ts}.json", "w")); print(len(allc))
elif what == "video":
    vid = sys.argv[2]
    r = get("/api/", url=f"https://www.tiktok.com/@x/video/{vid}")
    d = r["data"]; keep = {k: d.get(k) for k in ["id","title","play_count","digg_count","comment_count","share_count","download_count","collect_count","create_time","region"]}
    with open(f"{OUT}/snapshots.jsonl", "a") as f: f.write(json.dumps({"t": ts, "unix": int(time.time()), **keep}) + "\n")
    print(json.dumps(keep))
