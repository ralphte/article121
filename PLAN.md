# Article 121: plan

Prepared 4 October 2026. Status: round 3. Direction chosen: the black file, a dark classified case file led by real photographs.

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
| Home | The case file: mission, summary, exhibits | Folder opening, Exhibit A loupe |
| Timeline | Every dated event, 1956 to the museum era | Zoomable multi-lane timeline |
| Programs | Archangel, OXCART, KEDLOCK, TAGBOARD, SENIOR BOWL, SENIOR CROWN, NASA | Per-program timelines |
| Register | Where they are now: a file for every airframe built (51 records) | Card index and globe |
| The Machine | Airframe, titanium, J58, JP-7, inlet, navigation, pressure suits | 3D exploded view, inlet simulator |
| Missions | Publicly documented operations and record flights | Animated route maps |
| People | Engineers, crews, ground crews, oral histories | Cross-links to airframes and events |
| Archive | Photographs and film at full resolution | Deep zoom with provenance panel |
| Documents | Declassified CIA, NRO and USAF records, manuals, NASA papers | Reader with passages linked to events |
| Sources | Every source, its rights tier and archive copy | Filter by archive and licence |

## 3. Signature pieces

- **The case file.** Home page. A full-bleed photograph with the title unredacted on load, a black folder that opens in 3D, Exhibit A inspected with a loupe at full resolution.
- **The Timeline.** One zoomable track from 1956 onward, a lane per program. Drag to scrub, pinch to zoom, select a mark to open the cited entry.
- **Where they are now.** Every airframe built, its story, photos and fate, chosen from a card index. A globe turns to each survivor's museum. (Prototype built.)
- **The Machine.** The J58 inlet explainer, cutaway drawings and engine photographs. A 3D aircraft only once a model matches the real one.
- **Record flights.** The 6 March 1990 Los Angeles to Washington flight replayed on a map at true pace beside an airliner on the same route.
- **Deep-zoom archive.** Full-resolution scans with creator, date, catalogue number and licence beside each.

## 4. Design direction

**Chosen (round 3): the black file.** The classified, declassified case file is the identity of the whole site, finished like the aircraft: surfaces in the SR-71's blue-black, titanium-grey and white-stencil type, and one accent, the red of its walkway markings, used for the classification line, stamps and losses. Wide, low display type (Archivo expanded) echoes the airframe; B612 Mono, the Airbus cockpit face, carries data; Courier Prime is kept for the typed documents themselves. Case-file devices stay: file numbers, stamps, redactions that lift. The design system is `design/casefile.css`.

Round 2 rules from the owner's feedback:

- **Photographs lead.** Real, high-resolution photographs are the main content. Exhibits can be inspected with a loupe and opened full screen with zoom; the full site serves deep-zoom tiles of the original scans.
- **3D only where it adds something a photograph cannot.** The folder that opens on the home page, the register globe, the inlet explainer. No 3D aircraft until a model matches the photographs beside it.
- **Where they are now.** A register with a file for every airframe built, selectable from a card index, with photos of that exact airframe (identified by serial), record card, career, fate, chronology, source disagreements and sources, and a globe turned to its museum.

Live prototypes in `design/`: `casefile.html` (home) and `register.html` (register). Earlier rounds are kept for reference: `declassified.html` (round 2, light paper), `altitude.html` and `blueprint.html` (round 1); the J58 inlet explainer from `blueprint.html` carries forward into The Machine.

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

## 8. 3D policy

3D is used only where it adds information or atmosphere a photograph cannot: the opening folder, the register globe, the inlet explainer. No 3D aircraft appears until a model matches the photographs beside it. No museum or agency has released an open 3D scan of any Blackbird (Smithsonian 3D, NASA 3D Resources and Sketchfab CC0 all checked). If a model is wanted later: ask the author of the photogrammetry scan of the Smithsonian SR-71A for permission, ask the Smithsonian Digitization Program Office whether 61-7972 is on their list, or build one in Blender from the published three-view drawings.

Status, 4 October 2026: the model is being built in Blender from NASA Dryden's three-view (EG-0075-02), scaled to NASA's fuselage stations, with cross-sections from the Lockheed section sheet (`model/`). v0.3 adds the canopy; outline scores against the drawing are 97.6 percent (plan) and 95.4 percent (side). It stays off the public site until it matches the photographs beside it; files are at files.article121.com/models/.

## 9. Roadmap

1. **Approve.** Choose a direction, register article121.com, confirm licences.
2. **Foundation.** Astro project, design tokens, content schemas with the citation rule, CI, deploy. Live skeleton on the domain.
3. **Harvest.** Ingest scripts (Smithsonian Open Access, NASA Image Library, CIA, NARA, DVIDS, Commons, Library of Congress, Internet Archive). Source register. Convert the fact pack into content entries.
4. **Signature pieces.** The case-file home, the Register, the Timeline, the light table with deep zoom, The Machine. Built so far: home, Register (51 airframes), Chronology, Sources, About, and The Machine (data plate, inlet explainer, J58, cockpits with the pilot's panel explorer, heat, fuel, escape), all on preview.article121.com.
5. **Depth.** Documents reader, missions, people, deep-zoom archive, permission requests to legacy sites.
6. **Launch.** Accessibility audit, performance budgets, reduced-motion paths, share cards.

## 10. Decisions needed

| Decision | Recommendation |
|---|---|
| Design direction | Decided: the case file, photo-led |
| Repository owner | `ralphte/article121` to start; a dedicated organisation later for co-maintainers |
| Licences | Text CC BY-SA 4.0, data CC0 1.0, code MIT |
| Hosting | Cloudflare Workers static assets plus R2 |
| 3D model | CC BY mesh now, permission request for a scan |
| Outreach to legacy sites | Yes; each request approved before sending |
| Analytics | None |

## 11. Accounts and keys needed later

Free keys, requested when the harvest phase starts: api.data.gov (Smithsonian), NARA Catalog API, DVIDS API, Flickr API. Archive.org S3 keys for Save Page Now. Stored in 1Password, never in the repo.
