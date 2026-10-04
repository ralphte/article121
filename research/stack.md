# SR-71 site stack research (verified 2026-10-04)

Method: npm registry (curl), GitHub releases API, official docs fetched today. Items marked (UNVERIFIED) come from search snippets only.

## 1. Astro
- Latest stable: **astro 7.3.5** (published 2026-09-24). npm dist-tags: latest 7.3.5, beta 7.4.0-beta.1, alpha 7.0.0-alpha.2, legacy 4.16.19. Source: https://registry.npmjs.org/astro
- Timeline: 6.0.0 on 2026-03-10; 7.0.0 on 2026-06-22; 7.1.0 07-16; 7.2.0 08-06; 7.3.0 09-03. Requires Node >=22.12.0.
- Content collections: `src/content.config.ts`, `defineCollection({ loader: glob({pattern, base}), schema: z.object(...) })`, `import { z } from 'astro/zod'` (Zod 4), `getCollection`/`getEntry`, `render()`. Legacy collections API removed in 6. https://docs.astro.build/en/guides/content-collections/
- Images: `<Image/>` and `<Picture/>` from astro:assets, sharp default, AVIF/WebP via Picture, responsive images via `image.layout` (stable since 5.10, no flag), `image.responsiveStyles`. Local images in src/ only get optimised. https://docs.astro.build/en/guides/images/
- View transitions: `<ClientRouter />` (replaces `<ViewTransitions />`, removed in 6) or native cross-document view transitions (no JS). `transition:persist` keeps islands/canvas alive; re-init scripts on `astro:page-load`. https://docs.astro.build/en/guides/view-transitions/
- Static output is default; no adapter needed.
- 5 to 6 breaking: Node 22+, Vite 7, Zod 4, Shiki 4, legacy content API removed, ViewTransitions removed, image default cropping + no upscaling, getImage() client-side throws, endpoints with extension reject trailing slash, import.meta.env always inlined. https://docs.astro.build/en/guides/upgrade-to/v6/
- 6 to 7 breaking: Vite 8, Rust compiler stable and strict about HTML (unclosed tags error), Satteri replaces remark/rehype by default (install @astrojs/markdown-remark for plugins), compressHTML default 'jsx', src/fetch.ts reserved, @astrojs/db removed, astro:transitions internals removed. https://docs.astro.build/en/guides/upgrade-to/v7/
- Related: @astrojs/cloudflare 14.3.3 (only for SSR), @astrojs/sitemap 3.7.4, sharp 0.35.5.

## 2. Three.js
- Latest: **r186 = npm three 0.186.1** (r186 released 2026-09-08 per npm, GitHub release tagged 2026-09-24). @types/three 0.186.0. Prior: r185 2026-06-25, r184 2026-04-16.
- r186 notes: CommonJS builds deprecated, minified builds removed, PCFSoftShadowMap removed for WebGPURenderer, Object3D.dispose(), new Gaussian splat loader (TSL). Migration: https://github.com/mrdoob/three.js/wiki/Migration-Guide
- WebGPURenderer: official docs call it a "new alternative"; auto-falls back to WebGL 2 backend (`forceWebGL` option). WebGLRenderer remains fully supported and is the safe default. TSL is the node shader language for WebGPURenderer (and works on its WebGL2 backend). MDN BCD: WebGPU Chrome 144 (Windows/macOS/ChromeOS, Linux Intel Gen12+), Safari 26, Firefox 141 on Windows and 145+ on Apple silicon macOS. https://threejs.org/docs/pages/WebGPURenderer.html
- Advice for this site: WebGLRenderer for max reach and simplicity; WebGPURenderer+TSL only if you want compute/node post effects.
- glTF compression (UNVERIFIED as an official ranking; gltf-transform docs list both without ranking): meshopt (simple, fast decode, good with gzip/brotli) or Draco for pure geometry; KTX2 (ETC1S small, UASTC quality) for textures; use `gltf-transform optimize`. @gltf-transform/cli 4.5.1, meshoptimizer 1.3.0. https://gltf-transform.dev/cli
- Astro integration: plain island (vanilla `<script>` or client:visible component) is lightest. Threlte 8.6.1 (Svelte) and @react-three/fiber 9.8.1 are fine if you already use Svelte/React; not needed for a handful of scenes. With ClientRouter use transition:persist or dispose on astro:before-swap.

## 3. GSAP, Lenis, scroll-driven CSS
- GSAP **3.15.0** (2026-04-13). Licence "Standard 'no charge' license": all plugins incl. ScrollTrigger, SplitText, MorphSVG free incl. commercial use. Only restriction: no use in no-code visual animation builders competing with Webflow. https://gsap.com/community/standard-license/ . Your belief is confirmed.
- Lenis **1.3.26** (2026-08-05); 2.0.0-dev.5 on dev tag only.
- CSS scroll-driven animations (animation-timeline), per MDN BCD data: Chrome/Edge 115+, Safari 26+, Firefox only "preview" (flag/Nightly; a search snippet says still flagged in Firefox 152, UNVERIFIED). Not Baseline. Use `@supports (animation-timeline: scroll())` with GSAP ScrollTrigger fallback. https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline

## 4. Search, deep zoom, maps
- Pagefind **1.5.2** (2026-04-12); 1.5.0 added Component UI (modal) replacing Default UI. Run `npx pagefind --site dist` after build. astro-pagefind 2.0.1 wrapper exists. https://pagefind.app/docs/
- OpenSeadragon **6.1.1** (2026-09-09). DZI/IIIF pre-generation: libvips `vips dzsave` (sharp also has `.tile()` with DZ layout) is the standard; no Astro-specific convention found. Generate in a prebuild script or in CI, not in the repo (UNVERIFIED how common in Astro sites).
- MapLibre GL JS **6.12.0** (2026-10-03). OpenFreeMap: free public instance, no keys, no limits stated, commercial OK, attribution (auto in MapLibre). https://openfreemap.org/ . Protomaps/PMTiles: single-file, HTTP range requests from any static host or R2, spec v3; npm pmtiles 4.5.0. https://docs.protomaps.com/pmtiles/

## 5. Hosting
- Cloudflare Pages vs Workers: Cloudflare's Astro guide documents only Workers static assets (wrangler.json `assets.directory ./dist`, no adapter for static). Docs push Workers as the broader feature set; no explicit Pages deprecation found. Pick Workers static assets for new projects. https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/ and https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/
- Limits (both): 20,000 files/deploy on Free (100,000 Paid), **25 MiB max per file**. Static asset requests are free and unlimited (no bandwidth cap stated). Pages builds: 500/month free, 20 min timeout. https://developers.cloudflare.com/workers/platform/limits/ , https://developers.cloudflare.com/pages/platform/limits/ , https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/
- R2: free 10 GB-month storage, 1M Class A, 10M Class B per month; then $0.015/GB-month, $4.50/M Class A, $0.36/M Class B; **egress free**. Infrequent Access $0.01/GB. https://developers.cloudflare.com/r2/pricing/
- GitHub Pages: published site max 1 GB; repo 1 GB recommended (<5 GB strongly); soft 100 GB/month bandwidth; 10 min deploy timeout; 100 MiB hard file block, 50 MiB warn; not for commercial/SaaS. https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits , https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- Netlify Free: credit based, 300 credits/month (about $2); bandwidth 20 credits/GB (so roughly 15 GB/month if nothing else), 15 credits per production deploy. Poor fit for image-heavy. https://www.netlify.com/pricing/
- Recommendation for 5 to 20 GB of images: keep the GitHub repo small (code, content, small/optimised web assets, originals NOT committed). Host HTML/JS/CSS plus optimised images under 25 MiB each on Cloudflare Workers static assets (watch the 20,000 file cap, DZI tile pyramids burn files fast, so use PMTiles-style single files or IIIF/DZI in R2). Put heavy assets (hi-res originals, DZI/tile packs, glTF, video) in an R2 public bucket with custom domain: 10 GB free then about $0.15 per 10 GB/month, zero egress. 20 GB costs about $0.15/month. Fetch/optimise at build time or in CI from R2 rather than committing. GitHub Pages is the fallback only for a small site (1 GB cap, 100 GB soft bandwidth).

## 6. Link rot
- lychee-action **v2.9.0** (2026-07-09), use `lycheeverse/lychee-action@v2` with `args: --cache`, `fail: false` or true; pin SHA; `.lycheeignore`; issues:write permission if auto-filing issues. lychee core **v0.24.2** (2026-05-01). https://github.com/lycheeverse/lychee-action
- Wayback Save Page Now 2 (SPN2): authenticate with archive.org S3 keys, header `authorization: LOW accesskey:secret` (keys at https://archive.org/account/s3.php). Authenticated limits reported by a search result: 12 concurrent captures, 100,000 captures/day, 10 per URL per day (UNVERIFIED, from search snippet; official Google doc at https://docs.google.com/document/d/1Nsv52MvSjbLb2PCpHlat0gkzw0EvtSgpKHu4mk0MnrA did not render for fetch). Unauthenticated GET /save/ returned HTTP 429 from my test, so use keys. Status endpoint: https://web.archive.org/save/status/system (returned ok).

## Gaps
Firefox scroll-driven stable status, SPN2 exact limits, DZI-in-Astro prevalence and Cloudflare Pages deprecation status were not confirmed from primary docs.
