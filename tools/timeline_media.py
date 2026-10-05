"""Fetch and prepare the Chronology's media, listed in research/timeline-media.json.

  uv run --with pillow python tools/timeline_media.py [--only id,id] [--force] [--local dir]

--local names a folder of files already downloaded during the research (matched by file name).

For each item the master is downloaded to research/timeline-media/raw/ (gitignored), then:
  image     a web still, sRGB JPEG, at most 1800 px on the long edge  -> design/img/timeline/<id>.jpg
  document  the chosen PDF page at 150 dpi in greyscale                -> design/img/timeline/<id>.jpg
  video     H.264 MP4, at most 720 lines, fast start                   -> research/timeline-media/web/<id>.mp4
            and a poster frame                                         -> design/img/timeline/<id>.jpg
  audio     128 kbps MP3                                               -> research/timeline-media/web/<id>.mp3
The manifest gets each item's file, src (video and audio), master URL and duration. Items that
fail are reported and left without a file, so the import skips them. Then upload:
  tools/r2 copy research/timeline-media/web r2:article121-files/timeline
  tools/r2 copy research/timeline-media/raw r2:article121-files/masters/timeline
Needs curl, pdftoppm (poppler), ffmpeg, ffprobe and yt-dlp.
"""
import json
import mimetypes
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research/timeline-media.json"
RAW = ROOT / "research/timeline-media/raw"
WEB = ROOT / "research/timeline-media/web"
STILLS = ROOT / "design/img/timeline"
VIDEOS = ROOT / "research/videos"
LOCAL = Path(sys.argv[sys.argv.index("--local") + 1]) if "--local" in sys.argv else Path("/nonexistent")
FILES = "https://files.article121.com"
UA = "Article121-archive/1.0 (+https://article121.com/about/)"
Image.MAX_IMAGE_PIXELS = None


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def ext_of(url, fallback):
    m = re.search(r"\.([A-Za-z0-9]{2,5})(?:[?#]|$)", url.split("/")[-1])
    return (m.group(1).lower() if m else fallback).replace("jpeg", "jpg")


def download(it):
    """Fetch the master once; returns its path."""
    old = list(RAW.glob(f"{it['id']}.*"))
    if old:
        return old[0]
    url = it.get("fetch") or ""
    cat = it.get("catalog_id")
    if cat:
        v = CATALOG[cat]
        if v.get("local_file"):
            src = VIDEOS / v["local_file"] if not Path(v["local_file"]).is_absolute() else Path(v["local_file"])
            if not src.exists():
                src = VIDEOS / "raw" / Path(v["local_file"]).name
            dst = RAW / f"{it['id']}{src.suffix}"
            dst.symlink_to(src.resolve())
            return dst
        url = v.get("download_url") or url
    if not url:                                      # a photo the project already holds
        for tok in re.findall(r"[\w./-]+\.(?:jpe?g|png|tiff?)", it.get("held_by_project") or ""):
            for base in (ROOT, ROOT / "design", ROOT / "research/systems/media"):
                src = base / tok
                if src.exists():
                    dst = RAW / f"{it['id']}{src.suffix.lower()}"
                    dst.symlink_to(src.resolve())
                    return dst
        raise ValueError("no file to fetch")
    if "youtube.com" in url or "youtu.be" in url:
        run(["yt-dlp", "-q", "--no-playlist", "-f", "bv*[height<=1080]+ba/b", "--merge-output-format", "mp4",
             "-o", str(RAW / f"{it['id']}.%(ext)s"), url])
        return next(RAW.glob(f"{it['id']}.*"))
    url = url.split("#")[0]
    fallback = {"document": "pdf", "audio": "mp3", "video": "mp4"}.get(it["kind"], "jpg")
    dst = RAW / f"{it['id']}.{ext_of(url, fallback)}"
    local = LOCAL / Path(url).name                   # copies saved during the research
    if local.exists():
        dst.write_bytes(local.read_bytes())
        return dst
    # some government hosts refuse scripts (media.defense.gov, nro.gov): fall back to the Wayback
    # Machine's copy of the same file, fetched raw (id_)
    for u in (url, f"https://web.archive.org/web/2024id_/{url}"):
        try:
            run(["curl", "-sSfL", "--retry", "6", "--retry-delay", "8", "--max-time", "1800", "-A", UA, "-o", str(dst), u])
        except subprocess.CalledProcessError:
            continue
        if dst.stat().st_size >= 2000:
            return dst
    dst.unlink(missing_ok=True)
    raise ValueError(f"could not fetch {url}")


def still(src, dst, grey=False):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    im = im.convert("L" if grey else "RGB")
    im.thumbnail((1800, 1800), Image.LANCZOS)
    im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
    return im.size


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)]).stdout
    s = round(float(out.strip() or 0))
    return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def process(it, force=False):
    sid = it["id"]
    dst = STILLS / f"{sid}.jpg"
    master = download(it)
    it["master"] = f"{FILES}/masters/timeline/{master.name}"
    kind = it["kind"]
    if kind == "image" and master.suffix.lower() == ".pdf":
        kind = "document"                            # a photograph published only inside a PDF
    if kind == "image" and (force or not dst.exists()):
        it["size"] = list(still(master, dst))
    elif kind == "document" and (force or not dst.exists()):
        pages = int(re.search(r"Pages:\s+(\d+)", run(["pdfinfo", str(master)]).stdout).group(1))
        p = it.get("page") or 1
        p = p if 1 <= p <= pages else 1
        it["page"] = p
        tmp = RAW / f"{sid}-page"
        run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "150", "-gray", "-png", "-singlefile", str(master), str(tmp)])
        it["size"] = list(still(f"{tmp}.png", dst, grey=True))
        Path(f"{tmp}.png").unlink()
    elif kind == "video":
        out = WEB / f"{sid}.mp4"
        clip = it.get("clip")                        # [start, end] in seconds: the part that shows the event
        cut = ["-ss", str(clip[0]), "-to", str(clip[1])] if clip else []
        if force or not out.exists():
            run(["ffmpeg", "-y", "-v", "error", *cut, "-i", str(master), "-vf", "scale=-2:'min(720,ih)'", "-c:v", "libx264",
                 "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-ac", "2",
                 "-movflags", "+faststart", str(out)])
        it["duration"] = duration(out)
        if force or not dst.exists():
            secs = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(out)]).stdout)
            at = it.get("poster_at", max(1.0, secs * 0.15))   # a frame chosen by eye, else 15 percent in
            run(["ffmpeg", "-y", "-v", "error", "-ss", f"{at:.1f}", "-i", str(out), "-frames:v", "1", "-q:v", "3", str(dst)])
        it["src"] = f"{FILES}/timeline/{out.name}"
    elif kind == "audio":
        out = WEB / f"{sid}.mp3"
        if force or not out.exists():
            secs = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(master)]).stdout)
            speech = ["-ac", "1", "-b:a", "64k"] if secs > 1200 else ["-b:a", "128k"]   # long talks: speech quality
            run(["ffmpeg", "-y", "-v", "error", "-i", str(master), "-vn", "-c:a", "libmp3lame", *speech, str(out)])
        it["duration"] = duration(out)
        it["src"] = f"{FILES}/timeline/{out.name}"
    if dst.exists():
        it["file"] = f"img/timeline/{dst.name}"
    it.pop("error", None)
    return sid


def main():
    args = sys.argv[1:]
    only = set(args[args.index("--only") + 1].split(",")) if "--only" in args else None
    force = "--force" in args
    for d in (RAW, WEB, STILLS):
        d.mkdir(parents=True, exist_ok=True)
    data = json.loads(MANIFEST.read_text())
    global CATALOG
    CATALOG = {v["id"]: v for v in json.loads((VIDEOS / "catalog.json").read_text())}
    items = [it for it in data["items"] if not only or it["id"] in only]
    for it in items:
        it.pop("error", None)                        # a fresh attempt
    # downloads in parallel, processing (ffmpeg) in order
    def fetch(it):
        try:
            download(it)
        except Exception as e:                       # reported below, after processing
            it["error"] = f"download: {e}"
    with ThreadPoolExecutor(3) as ex:
        list(ex.map(fetch, [it for it in items if it["kind"] in ("image", "document", "audio")]))
    failed = []
    for it in items:
        if it.get("error"):
            failed.append((it["id"], it["error"]))
            continue
        try:
            process(it, force)
            print("ok", it["id"], it.get("duration") or it.get("size"), flush=True)
        except Exception as e:
            msg = getattr(e, "stderr", "") or str(e)
            it["error"] = msg.strip()[-300:]
            failed.append((it["id"], it["error"]))
            print("FAILED", it["id"], it["error"], flush=True)
    MANIFEST.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(items) - len(failed)} ready, {len(failed)} failed")
    for sid, err in failed:
        print("  ", sid, err[:200])


if __name__ == "__main__":
    main()
