# Article 121

A free, ad-free, fully cited archive of the Lockheed Blackbirds: the A-12 OXCART, YF-12, M-21 and D-21, and SR-71.

Article 121 was the CIA's designation for the first A-12 airframe, serial 60-6924, which made its official first flight on 30 April 1962.

## What this is

- A history site that collects the best public photographs, documents and records of the Blackbird family and presents them well.
- Every claim, figure and image carries its source. The build refuses content without one.
- Nothing here is ours. We credit the photographers, archives and authors whose work we show, and link back to them.
- There will never be ads, accounts, tracking or a charge for access.

## Status

Planning and design. See [PLAN.md](PLAN.md) and the design prototypes in [`design/`](design/).

| Prototype | Idea |
|---|---|
| [`design/altitude.html`](design/altitude.html) | Scroll is altitude: a 3D Blackbird climbs from the runway to 85,000 ft with live instruments |
| [`design/declassified.html`](design/declassified.html) | The archive as a released case file, with a 3D folder and redactions that lift |
| [`design/blueprint.html`](design/blueprint.html) | Engineering drawings: a live line model with true dimensions and a J58 inlet explainer |

To view them locally: `cd design && python3 -m http.server 8121`, then open http://localhost:8121.

## Research

[`research/`](research/) holds the working fact pack: a sourced timeline (`timeline.json`), an airframe register (`airframes.json`), notes on disputed facts and myths (`fact_notes.md`), a source and rights survey (`sources.md`) and the stack check (`stack.md`).

## Corrections

Found an error or a better source? Open an issue. Please include the source.

## Licences

- Code: MIT, see [LICENSE](LICENSE).
- Original writing: CC BY-SA 4.0 (proposed).
- Structured data (timeline, airframe register): CC0 1.0 (proposed).
- Third-party photographs and documents keep their own terms, which are recorded with each item. The photographs in `design/img/` are U.S. government works in the public domain; credits are in `design/img/credits.json`.
