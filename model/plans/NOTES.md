# Plans and geometry: what exists, how good it is, what it says

Survey of 4 October 2026. Every file is in `manifest.json` with its source URL, rights and a usefulness score (1 to 5). Pages are in `pages/`, original downloads are in `raw/`. Total size is about 177 MB.

Station shorthand used below: FS is fuselage station, WL waterline, BL buttline, WS wing station, NS nacelle station. All are in inches unless noted.

## 1. The five best sources for modelling

| Rank | Source | What it gives | Rights |
|---|---|---|---|
| 1 | NASA TM-4749 (1996), LASRE wind-tunnel paper, figs 4 and 5 (`pages/ntrs-19960038443_*`) | SR-71A side and plan outlines labelled with real station coordinates: nose FS 102, tail cone FS 1355, wing trailing-edge tip FS 1295, wing tip BL 340.2, upper fuselage WL 131. Use it to put a true scale and datum on any traced outline. | NASA TM, public domain (also printed as an AIAA paper; NASA authors) |
| 2 | NASA Dryden graphics EG-0075-02 (SR-71A) and EG-0075-05 (SR-71 with LASRE), 1998, original vector EPS from the Wayback Machine (`raw/dfrc_*`, `pages/dfrc_*`) | The cleanest public-domain three-view outline, as vectors. EG-0075-05 is dimensioned (55.60 / 107.40 / 18.50 ft). | U.S. government work, public domain |
| 3 | NASA TM X-2880 (1973), YF-12 ground vibration tests, figs 2a and 5 (`pages/ntrs-19730021212_*`) | The only fuselage cross sections found (five, keyed to FS 254, 365, 580, 738, 1040), plus FS, WS, fin and ventral-fin station grids on a plan view. | Public domain |
| 4 | NASA CP-2054 (1978), YF-12 Experiments Symposium: Gilyard and Smith fig 2 and Kock table 1 (`pages/ntrs-19780024116_*`, `pages/ntrs-19780024113_*`) | Front view with the fin cant (15 deg) and fin-tip spacing (6.92 m) on an SR-71A airframe (YF-12C). Full specification table: wing reference delta, elevons, fins, ventral fins, fuselage diameter. | Public domain |
| 5 | NASA TN D-6987 (1973), fig 2 (`pages/ntrs-19730015310_*`) | Dimensioned YF-12A three-view: nacelle centreline 14.17 ft from aircraft centreline, spike toe-in 3.25 deg, spike cant 5.3 to 5.63 deg. | Public domain |

Next in line: the inlet pair TM X-3144 (absolute cowl-lip radius) and Lockheed CR-163106 (to-scale normalised inlet sections, spike travel); the A-12 ground handling manual (the only orthographic A-12 outlines, with stations); and the SR-71A-1 flight manual (authoritative overall dimensions, a dimensioned plan silhouette, a forward fuselage plan and side, inlet sections).

## 2. Best sources for each view

### Plan view
- **SR-71A.** Trace Dryden EG-0075-02, then scale and register it to TM-4749 fig 4/5 (FS 102 nose, FS 1295 trailing-edge tip, FS 1355 tail cone, BL 340.2 tip). Check against the LASRE three-view (TM-1998-206567 fig 5, feet) and Gilyard fig 2 (metres). Flight manual fig 2-3 (turning radius) and fig 4-37 are stylised silhouettes; fig 4-24 is a good plan of the forward fuselage and chine bays. NASA photo EC97-44295-84 (`raw/nasa_EC97-44295-84_*`), taken from almost directly above, is for checking chine curvature and nacelle position.
- **YF-12A.** TN D-6987 fig 2 (dimensioned), TM X-2880 figs 2a and 5a (station grids), TP-1107 fig 2 (clean, undimensioned).
- **A-12.** CIA A-12 ground handling manual fig 1-1 sheets 1 to 3 (top and bottom views with FS, NS, WS and BL callouts). Its fig 2-8 walkway plan is badly compressed; do not trace it.

### Side view
- **SR-71A.** TM-4749 fig 4/5 (stations, WL 131), Dryden EG-0075-02 side view, LASRE three-view; flight manual fig 4-24 for the nose, cockpits and nose bay.
- **YF-12A.** TN D-6987 fig 2 (drawn with the folding ventral fin down).
- **A-12.** Ground handling manual fig 1-1 sheet 4 (left and right sides, fin and nacelle stations).

### Front view
- Gilyard fig 2 (SR-71A airframe): fin cant 15 deg inboard, fin tips 6.92 m apart. TN D-6987 fig 2 front view (YF-12A). The Dryden front views are about 3 percent wider than their own plan views, so do not take span from them.

### Fuselage cross sections (weakest area)
- TM X-2880 fig 2a: five small schematic YF-12 sections at FS 254, 365, 580, 738 and 1040. They show the character (round core, chine flare, the flat chine bay section at FS 580) but are structural sketches, not loft lines.
- TM-104317 fig 31: a true structural section at FS 1130 through fuselage, inboard wing, nacelle and outboard wing (YF-12A).
- CP-2054 p.240 fig 4: aft fuselage (boattail) top, side and rear sections for the YF-12A and for the SR-71 shape (YF-12C).
- Flight manual fig 1-21: nacelle longitudinal sections, schematic.
- **"Figure 71" sheets a to h (sr71.us, `raw/sr71us/`, tier D, private reference):** Lockheed-style lines drawings of the SR-71 with numbered stations. Sheet g groups the sections looking forward: forebody stations 1 to 9 as tents with concave flanks over a shallow V belly (1 to 3 a narrower hump on a flat chine shelf), stations 10 to 16 as a round body with a broad upper fillet to the wing and a straight underside from keel to nacelle. It also notes outer wing incidence (minus 1 deg 30 min), inner wing incidence (minus 1 deg) and conical camber on the outer leading edge. Model v0.2 takes its section shapes from this sheet; only shapes are measured, no image is reused. sr71.us is a fan site and not the origin. A search of NTRS, DTIC, the CIA reading room, NARA, the Dryden gallery and the scanned Blackbird books found no government copy (`research/drawing-provenance.md`): the sheet is an undated Lockheed-style lines drawing with no title block, probably drawn 1976 to 1982, online since spring 2002. The leads still open are listed in that report.
- **Not found anywhere:** an offsets table, chine section coordinates in numbers, or any Lockheed loft data.

### Inlet and spike
- Absolute scale: TM X-3144 fig 8, cowl-lip radius 74.62 cm (29.38 in).
- Shape: CR-163106 figs 4 and 5 (half-sections with spike forward and aft, axial scale x/Rc from the cowl lip, engine face at about x/Rc 5.4) and fig 7 (area distribution). Multiply by 29.38 in to get real sizes.
- Travel and schedule: flight manual p.1-31 and fig 1-22 sheet 2; CR-163106 p.29.
- Layout: flight manual figs 1-20 and 1-21; CP-2054 p.24 cutaway (counts of doors, louvres, struts, shock trap tubes).
- Orientation: TN D-6987 text p.3 and figs 2 and 9 (cant and toe-in); spike cone included angle 26 deg (text p.4).
- **Not found:** spike or cowl contour coordinates.

### Fins and ventral fins
- Kock table 1 (fixed plus movable fin planform numbers, both ventral fins), Gilyard fig 2 (cant), TM X-2880 figs 5b and 5c (fin and ventral fin station points), Lockheed CR-144972 ventral fin geometry drawings (poor scan, reference only), A-12 ground handling sheet 4 (fin STA 56 to 62).

### Canopy
- Only drawings at small scale: flight manual fig 4-24 side view, Dryden side views, A-12 and YF-12 three-views. **No dimensioned canopy geometry found.** The A-12 flight manual has canopy and windshield pages (pp. 1-85 to 1-87 in `raw/cia_C01316457_*`) that were not rendered; they describe rather than dimension.

## 3. Published dimensions

### SR-71A
| Item | Value | Source |
|---|---|---|
| Length overall | 107.4 ft | SR-71A-1 flight manual p.1-4; also TP-2000-209023 table 1 and LASRE three-view (107.40 ft) |
| Fuselage, nose tip to tail cone (no probe) | FS 102 to FS 1355 = 1253 in = 104.4 ft | TM-4749 figs 4 and 5 (derived from labelled stations) |
| Fuselage length, nose to tail without probe | 31.66 m (103.9 ft) | CP-2054, Gilyard and Smith fig 2 (YF-12C, an SR-71A airframe) |
| Wing span | 55.6 ft | Flight manual p.1-4; TP-2000-209023; LASRE three-view (55.60) |
| Wing span | 16.90 m (55.45 ft) | Gilyard fig 2 |
| Reference span | 56.7 ft (wing tip BL 340.2) | TM-4749 p.2 nomenclature, fig 5 |
| Height (to top of rudders) | 18.5 ft | Flight manual p.1-4; LASRE three-view |
| Height | 5.60 m (18.37 ft) | Gilyard fig 2 |
| Wing area (reference) | 1605 sq ft | Flight manual p.1-4; TM-4749 |
| Reference chord (MAC) | 37.7 ft | TM-4749; TP-2000-209023 table 1 |
| Main gear tread (middle wheel centrelines) | 16.67 ft | Flight manual p.1-4 |
| Fin cant | 15 deg inboard from vertical | Gilyard fig 2 |
| Fin tip to fin tip | 6.92 m (22.70 ft) | Gilyard fig 2 |
| Turning: centre of turn to probe tip / nose gear / outer wingtip / inner main gear / outer main gear | 81.7 / 54.5 / 69.5 / 28.3 / 47.4 ft; nose steering 45 deg max; 101.9 ft runway for 180 deg turn | Flight manual fig 2-3, p.2-30 |
| Other labelled stations | FS 726.5, 736.5, 754.5, 900 (moment reference), 934.5, 1226.5; WL 154.9 (fin region); BL 16.5, 45, 58.8 | TM-4749 figs 4 and 5 |

### Inlet and spike (J58 installation)
| Item | Value | Source |
|---|---|---|
| Cowl-lip radius | 74.62 cm (29.38 in); lip diameter 58.76 in | TM X-3144 fig 8 |
| Capture area | 18.5 sq ft captured stream tube at design (8.7 sq ft at Mach 1.6) | Flight manual p.1-31 (pi r squared from the lip radius gives 18.8 sq ft, consistent) |
| Throat | closes to 4.16 sq ft, 54 percent of its Mach 1.6 area | Flight manual p.1-31 |
| Spike travel | about 26 in aft, starting at Mach 1.6, about 1-5/8 in per 0.1 Mach | Flight manual p.1-31 and fig 1-22 sheet 2; A-12 flight manual p.1-19 (same 26 in) |
| Spike travel | 0.862 Rc = 25.3 in; throat to capture area ratio 0.41 / 0.33 / 0.23 at forward / mid / aft | CR-163106 p.29 |
| Spike axis | canted down 5.63 deg (text) or 5.3 deg (figure) to the wing reference plane, toed in 3.25 deg | TN D-6987 p.3, figs 2 and 9 |
| Spike cone | 26 deg included angle | TN D-6987 p.4 |
| Nacelle centreline | 4.32 m (14.17 ft) from the aircraft centreline, so 28.3 ft between nacelles | TN D-6987 fig 2 (YF-12A; same wing and nacelles) |

### YF-12 (NASA specification table and manual)
| Item | Value | Source |
|---|---|---|
| Length overall | 101.7 ft | YF-12A-1 flight manual p.1-3 (sr-71.org via Wayback, reference only) |
| Fuselage length / diameter | 30.986 m (101.66 ft) / 1.626 m (64.0 in) | Kock table 1, CP-2054 p.20 |
| Span / height | 55.7 ft / 18.4 ft | YF-12A-1 p.1-3 |
| Wing (theoretical delta) | area 166.761 sq m (1795 sq ft, the manual's "nominal" area), span 17.983 m (59.0 ft), root chord 18.542 m (60.83 ft), LE sweep 52.629 deg, incidence 1.20 deg, dihedral 0, modified biconvex 2.5 percent, MAC 12.361 m at WS 118.0 | Kock table 1, CP-2054 p.19 |
| Elevons | inboard 3.63 sq m each, outboard 4.877 sq m each, 35 deg up / 20 deg down | Kock table 1 |
| Vertical tail, total (each) | 14.006 sq m, root chord 6.096 m, tip chord 2.387 m, span 3.302 m, sweep 32.207 deg, AR 0.778, taper 0.392 | Kock table 1 |
| Movable vertical tail (each) | 6.526 sq m, root chord 4.512 m, tip chord 2.387 m, span 1.892 m, travel +/-20 deg | Kock table 1 |
| Fuselage ventral fin (folding) | 6.735 sq m, root chord 4.178 m, tip chord 2.616 m | Kock table 1 |
| Nacelle ventral fins | 2.044 sq m each, root chord 4.248 m, tip chord 3.266 m | Kock table 1 |
| Length with NASA nose boom | 33.26 m (109.17 ft); boom tip to spike tip 17.78 m (58.33 ft); semispan 8.50 m (27.81 ft); height 5.61 m (18.38 ft) | TN D-6987 fig 2 |
| Fuselage cross sections | FS 254, 365, 580, 738, 1040 | TM X-2880 fig 2a |
| Forebody stations | nose tip FS 90; FS 178, 301.5, 432.75, 550, 670 | TM X-2880 fig 5a concluded |
| Fin stations | 55.5, 72.75, 83.9, 108.5, 130 in; rudder post NS 1142.01 | TM X-2880 fig 5b |

### A-12
| Item | Value | Source |
|---|---|---|
| Span / length / height / tread | 55.62 ft / 101.6 ft / 18.45 ft / 16.67 ft | A-12 flight manual p.1-1 (CIA C01316457, changed 15 March 1968) |
| Control travel | elevons pitch 24 up / 10 down, pitch plus roll 35 up / 20 down, roll 12 / 12; rudders 20 deg each way | A-12 flight manual p.1-47 |
| Stations | nose cone FS 164 to 173; Q-bay about FS 318 to 387; fuel tank access FS 350, 685, 767 to 799, 875 to 907, 1063, 1159; fuel dump mixer FS 1242 to 1263; NS 890 to 1090; spike STA 118, 133 to 149; outboard elevon WS 210 to 297 | A-12 ground handling manual fig 1-1 sheets 1 to 4 (CIA C06230171) |

## 4. Where sources disagree

1. **Overall length.** 107.4 ft (flight manual, NASA) includes the pitot mast. Without it the SR-71A is 104.4 ft by the TM-4749 stations or 103.9 ft by Gilyard. The probe is therefore about 3.0 to 3.5 ft. On the Dryden LASRE drawing the 107.40 ft extension line is drawn at the radome tip, but the drawing's own proportions only work if 107.4 ft runs from the probe tip.
2. **Span.** 55.6 ft (manual, NASA), 55.45 ft (Gilyard), 56.7 ft reference span to BL 340.2 (TM-4749, a theoretical tip), 59.0 ft for the YF-12 theoretical delta (Kock). Model the real tip to 55.6 ft and treat the larger numbers as reference planforms.
3. **Wing area.** 1605 sq ft "reference" (SR-71A manual) against 1795 sq ft "nominal" (YF-12A manual, Kock 166.761 sq m). These are two different reference deltas, not a change in the wing.
4. **Height.** 18.5 ft (SR-71A manual), 18.37 ft (Gilyard), 18.4 ft (YF-12A manual), 18.38 ft (TN D-6987, ventral fin down), 18.45 ft (A-12).
5. **Spike travel.** About 26 in (SR-71A and A-12 manuals), 25.3 in (CR-163106), "almost three feet" (Kelly Johnson's 1981 paper, CIA reading-room copy, not mirrored here). Use 26 in.
6. **Spike cant.** 5.63 deg in TN D-6987's text and 5.3 deg in its own fig 2.
7. **Main gear.** Fig 2-3 puts the inner and outer main gear 28.3 and 47.4 ft from the centre of turn, 19.1 ft apart, against a 16.67 ft tread between middle wheels. These agree if fig 2-3 measures to the inner and outer wheels of each three-wheel bogie (that implies about 1.2 ft wheel spacing; derived, not published).
8. **Dryden drawings.** Front views are about 3 percent wider than the plan views. The Dryden YF-12A plan view (EG-0106-01) has the SR-71A's length-to-span ratio (1.93) instead of the YF-12A's (1.83 from the manual), so it is about 5 percent too long; rescale it.
9. **Station datums differ by type.** SR-71A nose FS 102 (TM-4749); YF-12A nose tip FS 90 (TM X-2880); A-12 nose cone panel FS 164 to 173. Never overlay FS values across types without checking each document's nose station.
10. **Misprint.** TM X-2880 fig 5c prints the ventral fin root as 2364.1 cm next to 1127.59 in; 2864.1 cm is meant.

A useful self-check: with nacelle centrelines at 14.17 ft, a 15 deg cant and fin tips 11.35 ft from the centreline (6.92 m apart), the fins rise about 10.5 ft, close to Kock's 3.302 m (10.8 ft) fin span. The numbers above hang together.

## 5. Outline differences a modeller must respect

- **A-12.** Single seat, one canopy (A-12 flight manual p.1-1). Q-bay camera bay behind the cockpit, FS 318 to 387 (ground handling sheet 2). Chines run all the way to the nose ("from the nose to the leading edge of the wing", A-12 FM p.1-1). Length 101.6 ft. The ground handling side views show no ventral fins.
- **YF-12A.** Two seats in tandem. Chines cut back to begin near the cockpit so the nose is a round radome cone (TN D-6987 fig 2, TP-1107 fig 2, Dryden EG-0106-01). Two fixed nacelle ventral fins plus a large folding fuselage ventral fin (Kock table 1; drawn in TN D-6987, CP-2054 p.86). Length 101.7 ft; nominal wing area 1795 sq ft.
- **SR-71A.** Two tandem cockpits. Chines run to the nose. Longer: 107.4 ft with the probe, about 104 ft without. No ventral fins. Its aft fuselage closure (boattail) differs from the YF-12A's: compare configurations A and C in CP-2054 p.240 fig 4.
- **SR-71B.** As the SR-71A, plus a ventral fin under each nacelle and a raised second (instructor) cockpit (SR-71A-1 p.1A-3).
- **All types.** Inlets canted inboard and downward (flight manuals); wing and nacelle geometry shared, so YF-12 wing, fin, nacelle and inlet data apply to the SR-71A.

## 6. Rights summary

- **Mirror (tier A):** NASA TM, TN, TP and CP items; NASA Dryden graphics; NASA photo EC97-44295-84; the SR-71A-1 flight manual pages (USAF technical order, Internet Archive item tagged Public Domain Mark). The manual scan's provenance is unclear: anonymous uploader, original SENIOR CROWN markings, and fig 4-37's page is stamped "UNCONTROLLED COPY" and annotated "Deleted IAW SR71 SCG 23 Sept 96". Cite it with care.
- **Mirror, with a note:** the A-12 flight manual and ground handling manual, released by the CIA under FOIA (stamped "Approved for Release 2017/07/25"). They were prepared by Lockheed for the government and carry no copyright notice.
- **Cite only until confirmed (tier C):** the Lockheed contractor reports CR-163106 and CR-144972. NTRS permits public use, but they are Lockheed work.
- **Permission needed (tier D):** everything from sr-71.org (Paul Kucher, "permission is mandatory") and sr71.us, including the YF-12A-1 manual pages and the three diagram GIFs in `raw/sr71org-wayback_*`. Kept for private reference only.
- **Commons:** `raw/commons_*` and `pages/commons_*` are marked public domain on Commons. The SR-71A three-view SVG there is a 2007 redraw of the USAF/Dryden drawing, so use the Dryden EPS as the master.
- Merlin's AIAA 2009 paper (Lockheed Martin figures, AIAA copyright) was deliberately not kept.

## 7. Searched, nothing usable

- **NTRS:** no offsets tables and no CFD surface grids or geometry files. The 1994 sonic boom workshop shows only low-resolution grid pictures. The full-scale inlet reports TM X-3138 and TM X-3139 are not in NTRS. Nothing on the A-12.
- **NASA SP-2001-4525 (Mach 3+) and the Armstrong fact sheets:** no three-views.
- **CIA:** no three-view of the A-12 found. The CIAA-12Files bundle on the Internet Archive is text only.
- **YF-12A-1 manual:** text pages survive on sr-71.org via Wayback, but its Section I figures were never archived. No A-12 or YF-12 manual on the Internet Archive itself.
- **sr-71.org SR-71A-1 web edition:** its page images are 1000 x 1400 px, the same as the Internet Archive PDF. The Internet Archive JP2 masters (4167 x 5834 px) used here are four times sharper.
- **Library of Congress:** photographs only, no drawings.
- **DTIC (via the Internet Archive mirror):** no geometry reports.
- **Smithsonian (Open Access API, collections.si.edu, SOVA):** blocked or rate-limited scripted access. The NASM technical files remain unchecked and are worth a manual request.
- **USAF museum and af.mil:** block scripts; Wayback had nothing beyond copies of the Dryden three-view.
- **Lockheed engineering drawings:** none found posted publicly.
