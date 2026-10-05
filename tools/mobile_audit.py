"""Mobile audit of the site in Playwright WebKit (Safari's engine), emulating iPhones and an iPad.

  uv run --with playwright python tools/mobile_audit.py https://preview.article121.com out/ [--pages /,/timeline/] [--devices se,15,15l,ipad]

Reports, per device and page: anything wider than the screen, controls under 24 px (and how many
under 44 px), text under 11 px, the routing bar's height and console errors; saves a screenshot of
each. Needs `uv run --with playwright python -m playwright install webkit` once.
"""
import asyncio, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

PAGES = ["/", "/timeline/", "/register/", "/register/60-6924/", "/machine/", "/sources/", "/about/"]
DEVICES = {"se": "iPhone SE", "15": "iPhone 15 Pro", "15l": "iPhone 15 Pro landscape", "ipad": "iPad Mini"}

PROBE = r"""() => {
  const vw = window.innerWidth, out = { vw, docW: document.documentElement.scrollWidth, overflow: [], small: [], tiny: [], banner: null };
  const clipped = (el) => { for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) { const s = getComputedStyle(p); if (/(auto|hidden|scroll|clip)/.test(s.overflowX)) return true; } return false; };
  const desc = (el) => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (!r.width || getComputedStyle(el).visibility === 'hidden') continue;
    if (r.right > vw + 1 && !clipped(el)) out.overflow.push(desc(el) + ' right=' + Math.round(r.right));
  }
  const inText = (el) => el.tagName === 'A' && el.closest('p, li, figcaption, dd') && !el.closest('nav') && el.textContent.trim().length > 2;
  for (const el of document.querySelectorAll('a, button, input, select, summary, [role=button], label')) {
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    const s = getComputedStyle(el); if (s.visibility === 'hidden' || s.display === 'none') continue;
    if (inText(el)) continue;
    const m = Math.min(r.width, r.height);
    if (m < 24) out.tiny.push(desc(el) + ` ${Math.round(r.width)}x${Math.round(r.height)} "${el.textContent.trim().slice(0, 24)}"`);
    else if (m < 44) out.small.push(desc(el));
  }
  const fonts = {};
  for (const el of document.querySelectorAll('body *')) {
    if (!el.childNodes.length || ![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize); if (fs < 11) { const k = desc(el) + ' ' + fs.toFixed(1) + 'px'; fonts[k] = (fonts[k] || 0) + 1; }
  }
  out.smallText = Object.entries(fonts).sort((a, b) => b[1] - a[1]).slice(0, 8);
  const b = document.querySelector('.banner'); if (b) out.banner = Math.round(b.getBoundingClientRect().height);
  out.overflow = [...new Set(out.overflow)].slice(0, 12);
  const count = (a) => Object.entries(a.reduce((m, x) => (m[x.split(' ')[0]] = (m[x.split(' ')[0]] || 0) + 1, m), {})).sort((a, b) => b[1] - a[1]).slice(0, 10);
  out.tinyByKind = count(out.tiny); out.smallByKind = count(out.small); out.tinyExamples = out.tiny.slice(0, 6);
  delete out.tiny; delete out.small;
  return out;
}"""


async def main():
    a = sys.argv[1:]
    base, outdir = a[0].rstrip("/"), Path(a[1]); outdir.mkdir(parents=True, exist_ok=True)
    pages = a[a.index("--pages") + 1].split(",") if "--pages" in a else PAGES
    devs = a[a.index("--devices") + 1].split(",") if "--devices" in a else list(DEVICES)
    report = {}
    async with async_playwright() as p:
        wk = await p.webkit.launch()
        for dk in devs:
            ctx = await wk.new_context(**p.devices[DEVICES[dk]])
            for path in pages:
                page = await ctx.new_page()
                errs = []
                page.on("pageerror", lambda e: errs.append("pageerror: " + str(e)[:200]))
                page.on("console", lambda m: errs.append(f"{m.type}: {m.text[:200]}") if m.type in ("error", "warning") else None)
                await page.goto(base + path, wait_until="load", timeout=90000)
                await page.wait_for_timeout(2500)
                res = await page.evaluate(PROBE)
                res["errors"] = [e for e in errs if "cloudflareinsights" not in e and "interest-cohort" not in e][:8]
                name = f"{dk}{path.strip('/').replace('/', '_') or '_home'}"
                await page.screenshot(path=str(outdir / f"{name}.png"))
                report[f"{dk} {path}"] = res
                await page.close()
            await ctx.close()
        await wk.close()
    (outdir / "report.json").write_text(json.dumps(report, indent=1))
    for k, v in report.items():
        print(f"\n== {k}: vw {v['vw']} docW {v['docW']} banner {v['banner']}px")
        if v["overflow"]: print("  overflow:", v["overflow"][:6])
        if v["tinyByKind"]: print("  targets <24px:", v["tinyByKind"][:6], v["tinyExamples"][:3])
        if v["smallByKind"]: print("  targets <44px:", v["smallByKind"][:6])
        if v["smallText"]: print("  text <11px:", v["smallText"][:4])
        if v["errors"]: print("  errors:", v["errors"][:4])


asyncio.run(main())
