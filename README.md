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

| Page | What it is |
|---|---|
| [`design/casefile.html`](design/casefile.html) | Home, "black file" direction: a dark classified case file led by real photographs |
| [`design/register.html`](design/register.html) | Where they are now: pick any airframe built and open its file |
| [`design/declassified.html`](design/declassified.html) | Round 2: the same case file in light paper |
| [`design/altitude.html`](design/altitude.html), [`design/blueprint.html`](design/blueprint.html) | Round 1 explorations |

To view them locally: `cd design && python3 -m http.server 8121`, then open http://localhost:8121.

## Research

[`research/`](research/) holds the working fact pack: a sourced timeline (`timeline.json`), an airframe register (`airframes.json`), notes on disputed facts and myths (`fact_notes.md`), a source and rights survey (`sources.md`) and the stack check (`stack.md`).

## Corrections

Found an error or a better source? Open an issue. Please include the source.

## Secrets

This repository is public, so no credential is ever written into it. Keys and tokens live in 1Password and scripts read them at run time (`tools/r2` and `tools/deploy-preview` call `op read`). Three guards back that up:

- `tools/git-hooks/pre-commit` and `pre-push` scan every commit with [gitleaks](https://github.com/gitleaks/gitleaks) before it leaves your machine. Enable them once per clone: `brew install gitleaks && git config core.hooksPath tools/git-hooks`.
- The `Secrets` workflow scans the full history on every push and pull request.
- GitHub secret scanning with push protection is switched on for the repository.

If a secret is ever committed, rotate it first; removing it from history does not make it safe again.

## Licences

- Code: MIT, see [LICENSE](LICENSE).
- Original writing: CC BY-SA 4.0 (proposed).
- Structured data (timeline, airframe register): CC0 1.0 (proposed).
- Third-party photographs and documents keep their own terms, which are recorded with each item. The photographs in `design/img/` are U.S. government works in the public domain; credits are in `design/img/credits.json`.
