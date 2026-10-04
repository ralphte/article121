# Article 121: plan

Prepared 4 October 2026. Status: awaiting a design decision.

## 1. Mission and ground rules

Article 121 documents the Lockheed A-12, YF-12, M-21/D-21 and SR-71 in the highest quality the public record allows. It shows history; it does not claim it.

1. **Free forever.** No ads, no accounts, no paywall, no tracking. Hosting is designed to cost about the price of the domain.
2. **Every claim has a source.** Events, figures, airframe records and images all reference at least one source record. The build fails without one.
3. **Credit, never ownership.** The creator and archive appear on the image itself, with a link to the original.
4. **Originals stay original.** No AI upscaling, colourising or restoration of historical photographs. If a cleaned copy is ever shown, the original sits beside it and the change is labelled.
5. **Preserve what is fading.** Every source URL is captured to the Wayback Machine. Legacy fan and veteran sites are credited, and mirrored only with written permission.
6. **Corrections in the open.** Each page links to a GitHub issue form. Fixes land as public commits.

## 2. Site map

| Section | Contents | Signature interaction |
|---|---|---|
| Home | Mission, the story in six chapters | The Climb |
| Timeline | Every dated event, 1956 to the museum era | Zoomable multi-lane timeline |
| Programs | Archangel, OXCART, KEDLOCK, TAGBOARD, SENIOR BOWL, SENIOR CROWN, NASA | Per-program timelines |
| Register | One page per airframe (51 entries in the fact pack) | Survivors map and globe |
| The Machine | Airframe, titanium, J58, JP-7, inlet, navigation, pressure suits | 3D exploded view, inlet simulator |
| Missions | Publicly documented operations and record flights | Animated route maps |
| People | Engineers, crews, ground crews, oral histories | Cross-links to airframes and events |
| Archive | Photographs and film at full resolution | Deep zoom with provenance panel |
| Documents | Declassified CIA, NRO and USAF records, manuals, NASA papers | Reader with passages linked to events |
| Sources | Every source, its rights tier and archive copy | Filter by archive and licence |

## 3. Signature pieces

- **The Climb.** Home page. Scroll drives a sortie from a twilight runway to 85,000 ft with live altitude, Mach and ground speed. The sky darkens to black at cruise. History chapters sit at each altitude. (Prototype A.)
- **The Timeline.** One zoomable track from 1956 onward, a lane per program. Drag to scrub, pinch to zoom, select a mark to open the cited entry.
- **The Register and map.** Every airframe built, its story, photos and fate. A globe flies to each survivor's museum.
- **The Machine.** A properly modelled aircraft with exploded view, the J58 inlet explainer (prototype C) and a skin temperature map at cruise.
- **Record flights.** The 6 March 1990 Los Angeles to Washington flight replayed on a map at true pace beside an airliner on the same route.
- **Deep-zoom archive.** Full-resolution scans with creator, date, catalogue number and licence beside each.

## 4. Design directions

Three live prototypes are in `design/`. They share one placeholder aircraft model (`design/blackbird.js`) and the same public-domain photos.

- **A, Altitude.** Cinematic. The scroll is the climb.
- **B, Declassified.** Archival. A released case file; dark mode is a microfilm reader.
- **C, Blueprint.** Engineering. Line drawings with real dimensions; whiteprint by day, blueprint by night.

Recommendation: A as the shell and home page, C's drawing language for The Machine and the Register, B's case-file treatment for the Documents room. One type system, one set of colour tokens and one navigation tie them together. If one look is preferred, choose A.

## 5. Citation system

```
Archive or document
  -> Source record (title, publisher, URL, rights tier, Wayback snapshot, accessed date)
  -> Content entry (event, airframe, photo) referencing one or more sources
  -> Build checks: schema (no source, no build), weekly link check, Wayback capture
  -> Page: numbered markers on claims, credit line on every image, source drawer
  -> Reader correction via GitHub issue form -> content entry
```

Content lives in Astro content collections with Zod schemas:

```ts
// src/content.config.ts
const events = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/events' }),
  schema: z.object({
    date: z.string(),
    precision: z.enum(['day', 'month', 'year', 'approx']),
    title: z.string(),
    program: z.enum(['context', 'archangel', 'oxcart', 'kedlock', 'tagboard', 'senior-bowl', 'senior-crown', 'nasa', 'legacy']),
    airframes: z.array(reference('airframes')).default([]),
    sources: z.array(reference('sources')).min(1),
    notes: z.string().optional(), // where sources disagree, say so
  }),
});
```

Disagreements between sources are shown, not hidden: the fact pack already records several (Article 121's first-flight date, the 1976 altitude record airframe, the 1990 average speed).

## 6. Sources and rights

See `research/sources.md` for the full survey, verified API endpoints and credit-line formats.

Rights tiers, stored with every asset:

| Tier | Covers | Action |
|---|---|---|
| A, Mirror | U.S. government works, CC0, "no known restrictions" | Host the master, credit anyway |
| B, Mirror under licence | CC BY, CC BY-SA, GPL | Host with the credit and licence link required |
| C, Link only | Copyrighted photos, fan-site pages, Lockheed Martin material, books | Link plus Wayback copy, summarise in our own words |
| D, Permission | Legacy fan sites, crew collections, museum archives, private scans | Written request; host only after a yes |

Rules: check captions on government sites for contractor or "courtesy" credits; declassified is not the same as public domain; do not use agency seals or the Skunk Works logo as decoration; do not rely on fair use for images; record every permission in a register (evidence kept privately, not in the public repo).

## 7. Stack and hosting

Versions checked 4 October 2026 (`research/stack.md`).

| Layer | Choice |
|---|---|
| Site | Astro 7.3, static output, content collections, `<Picture>` with AVIF and WebP |
| 3D | Three.js r186, WebGLRenderer; glTF with meshopt and KTX2 via gltf-transform |
| Motion | GSAP 3.15 with ScrollTrigger (free for all use), Lenis 1.3; CSS scroll-driven animation where supported |
| Search | Pagefind 1.5 |
| Deep zoom | OpenSeadragon 6.1, DZI tiles generated with libvips at build, stored on R2 |
| Maps | MapLibre GL 6.12 with Protomaps PMTiles on R2 |
| Hosting | Cloudflare Workers static assets (free, unlimited static requests) |
| Large files | Cloudflare R2: originals, tiles, models. 10 GB free, then $0.015 per GB-month, no egress fees |
| CI | GitHub Actions: build and schema checks on pull requests, weekly lychee link check, Wayback capture, deploy on merge |
| Analytics | None |

Running cost: about $11 a year for the domain; hosting $0; R2 about $0.15 a month at 20 GB.

Repository stays small: code, content and optimised images. Masters and tile packs go to R2, never into git.

Performance and access budgets: Largest Contentful Paint under 2.5 s on a mid-range phone over 4G; no page ships 3D unless it is the point of the page; every animation has a `prefers-reduced-motion` path; every WebGL scene has a static fallback image; all content is readable without JavaScript.

## 8. The 3D aircraft

No museum or agency has released an open 3D scan of any Blackbird (Smithsonian 3D, NASA 3D Resources and Sketchfab CC0 all checked). Plan:

1. Ship a credited CC BY 4.0 mesh from Sketchfab for the web viewer.
2. Ask the author of the photogrammetry scan of the Smithsonian SR-71A for permission, and ask the Smithsonian Digitization Program Office whether 61-7972 is on their list.
3. Fallback: a custom model built in Blender from the published three-view drawings, released under CC BY-SA with the site.

## 9. Roadmap

1. **Approve.** Choose a direction, register article121.com, confirm licences.
2. **Foundation.** Astro project, design tokens, content schemas with the citation rule, CI, deploy. Live skeleton on the domain.
3. **Harvest.** Ingest scripts (Smithsonian Open Access, NASA Image Library, CIA, NARA, DVIDS, Commons, Library of Congress, Internet Archive). Source register. Convert the fact pack into content entries.
4. **Signature pieces.** The Climb, the Timeline, the Register and map, The Machine.
5. **Depth.** Documents reader, missions, people, deep-zoom archive, permission requests to legacy sites.
6. **Launch.** Accessibility audit, performance budgets, reduced-motion paths, share cards.

## 10. Decisions needed

| Decision | Recommendation |
|---|---|
| Design direction | A shell, C for engineering, B for documents |
| Repository owner | `ralphte/article121` to start; a dedicated organisation later for co-maintainers |
| Licences | Text CC BY-SA 4.0, data CC0 1.0, code MIT |
| Hosting | Cloudflare Workers static assets plus R2 |
| 3D model | CC BY mesh now, permission request for a scan |
| Outreach to legacy sites | Yes; each request approved before sending |
| Analytics | None |

## 11. Accounts and keys needed later

Free keys, requested when the harvest phase starts: api.data.gov (Smithsonian), NARA Catalog API, DVIDS API, Flickr API. Archive.org S3 keys for Save Page Now. Stored in 1Password, never in the repo.
