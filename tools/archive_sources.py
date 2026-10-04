"""Find an Internet Archive (Wayback Machine) copy of every source the site cites.

  python3 tools/archive_sources.py            # look up sources not yet in research/archives.json
  python3 tools/archive_sources.py --all      # look them all up again

Reads the citations in research/timeline.json and research/airframes.json and writes
research/archives.json: {url: {"wayback": ..., "captured": "YYYY-MM-DD"}}. The site links each
source to its archived copy as well, and for sources listed in OFFLINE the archived copy becomes
the main link. Only reads from the Wayback Machine; it never asks it to capture anything.
"""
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research/archives.json"
UA = "Article121/0.1 (+https://github.com/ralphte/article121)"

# Sources the weekly link check (links.yml) finds unreachable, with the reason, as of the date given.
OFFLINE = {
    "habu.org": "TLS certificate expired (checked 2026-10-04)",
    "sr-71.org": "site returns 503 to every request (checked 2026-10-04)",
    "https://www.rocketcenter.com/tour/ac/A12Oxcart": "page removed, 404 (checked 2026-10-04)",
}


def offline_reason(url):
    host = urllib.parse.urlsplit(url).hostname or ""
    for k, why in OFFLINE.items():
        if url == k or host == k or host.endswith("." + k):
            return why
    return None


def in_archive(url):
    """Sources hosted by the Internet Archive itself need no copy (and the Wayback Machine refuses them)."""
    host = urllib.parse.urlsplit(url).hostname or ""
    return host == "archive.org" or host.endswith(".archive.org")


def cited_urls():
    urls = []
    for f in ("research/timeline.json", "research/airframes.json"):
        for rec in json.loads((ROOT / f).read_text()):
            urls += [s["url"].strip() for s in rec.get("sources", []) if s.get("url")]
    urls += [s["url"].strip() for s in json.loads((ROOT / "research/machine.json").read_text())["sources"].values()]
    return sorted(set(urls))


def _get_json(q):
    for attempt in range(5):
        try:
            req = urllib.request.Request(q, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
            return json.loads(body) if body.strip() else []
        except Exception as e:  # the archive rate-limits and goes "temporarily offline" now and then
            if attempt == 4:
                print(f"  lookup failed: {e}", file=sys.stderr)
                return None
            time.sleep(8 * (attempt + 1))


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def lookup(url):
    """Latest capture: the Wayback Machine answers /web/<date>/<url> with a redirect to the capture
    nearest that date. The CDX index gives the same answer far more slowly, so it is the fallback."""
    today = time.strftime("%Y%m%d")
    for attempt in range(4):
        try:
            req = urllib.request.Request(f"https://web.archive.org/web/{today}/{url}", method="HEAD", headers={"User-Agent": UA})
            _opener.open(req, timeout=60)
            break  # 200 without a redirect: not expected, treat as unknown
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location", "")
            m = re.match(r"https?://web\.archive\.org/web/(\d{14})/(.+)$", loc)
            if e.code in (301, 302, 307) and m:
                ts, original = m.groups()
                return {"wayback": f"https://web.archive.org/web/{ts}/{original}", "captured": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"}
            if e.code in (403, 404):
                return None
            time.sleep(6 * (attempt + 1))
        except Exception:
            time.sleep(6 * (attempt + 1))
    q = "https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(
        {"url": url, "output": "json", "fl": "timestamp,original", "filter": "statuscode:200", "limit": "-1"})
    rows = _get_json(q)
    if not rows or len(rows) < 2:
        return None
    ts, original = rows[-1]
    return {"wayback": f"https://web.archive.org/web/{ts}/{original}", "captured": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"}


def main():
    have = json.loads(OUT.read_text()) if OUT.exists() else {}
    redo = "--all" in sys.argv
    urls = cited_urls()
    todo = [u for u in urls if not in_archive(u) and (redo or "wayback" not in have.get(u, {}))]
    print(f"{len(urls)} cited URLs, looking up {len(todo)}")
    for i, u in enumerate(todo, 1):
        rec = lookup(u)
        if rec:
            have[u] = rec
        elif redo:
            have.pop(u, None)
        print(f"[{i}/{len(todo)}] {'ok  ' + rec['captured'] if rec else 'none'}  {u}")
        time.sleep(0.8)
    for u in urls:
        why = offline_reason(u)
        if why:
            have.setdefault(u, {})["offline"] = why
        elif u in have:
            have[u].pop("offline", None)
    out = {u: have[u] for u in sorted(have) if u in set(urls)}
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    missing = [u for u in urls if "wayback" not in out.get(u, {}) and not in_archive(u)]
    hosted = sum(in_archive(u) for u in urls)
    print(f"archived copies for {len(urls) - hosted - len(missing)} of {len(urls) - hosted} (plus {hosted} hosted by the Internet Archive itself); none for {len(missing)}")
    for u in missing:
        print("  no copy:", u, "(offline)" if offline_reason(u) else "")


if __name__ == "__main__":
    main()
