#!/usr/bin/env python3
"""Pull the waxfreq* catalogue from elasticStage and rewrite releases.json.

Run it by hand:   python3 scripts/update-releases.py
or let the GitHub workflow in .github/workflows/update-releases.yml run it daily.

It identifies itself honestly. If elasticStage's bot protection declines the
request, the script exits 1 and leaves releases.json untouched; in that case
either edit releases.json by hand or ask elasticStage for API access.
"""
import datetime
import json
import pathlib
import sys
import urllib.request

PAGE_ID = "78746b10-9d09-460d-a8cf-dba6dfa20308"   # the waxfreq* page on elasticStage
API = f"https://elasticstage.com/api/release_groups?media=Vinyl,CD&page={PAGE_ID}"
OUT = pathlib.Path(__file__).resolve().parent.parent / "releases.json"

req = urllib.request.Request(API, headers={
    "Accept": "application/json",
    "User-Agent": "waxfreq-site-updater/1.0 (artist site; updates releases.json from the public catalogue)",
})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())["data"]
except Exception as e:  # blocked, offline, or the response shape changed
    print(f"update-releases: could not read the elasticStage API ({e}); releases.json left as is", file=sys.stderr)
    sys.exit(1)

releases = []
for d in data:
    releases.append({
        "title": d.get("title"),
        "format": d.get("format"),
        "media": d.get("media") or [],
        "year": d.get("year"),
        "date": d.get("original_release_date"),
        "genre": (d.get("main_genre") or {}).get("name"),
        "subgenre": (d.get("sub_genre") or {}).get("name"),
        "url": d.get("url"),
        "image": d.get("image"),
    })
releases.sort(key=lambda r: r.get("date") or "", reverse=True)

doc = {
    "source": "https://elasticstage.com/waxfreq",
    "updated": datetime.date.today().isoformat(),
    "releases": releases,
}
OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
print(f"update-releases: wrote {len(releases)} release(s) to {OUT.name}")
