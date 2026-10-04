# SR-71A structure and systems stations for the exploded model

Compiled 4 October 2026 for the see-through, exploded SR-71A model. Every number below carries its source; the same data, with every source string in full, is in `structure.json` (one record per item, with x, y and z already converted). Rights: only US government documents were used as sources (NASA reports, the USAF SR-71A-1 flight manual, CIA-released A-12 manuals); one Lockheed contractor report (CR-163106, tier C) and one Smithsonian record are cited for numbers only. No fan-site material (sr-71.org, sr71.us, habu.org) was used.

## Summary

- **There is no public SR-71A frame or bulkhead list.** The only real structural station data are for the YF-12A, which shares the SR-71A wing, nacelles and tail: NASA TM X-2880 (structure description, a generalized structural plan and a table of test-point stations) and NASA TM-104317 (labelled wing beams and ribs). The fuselage station datum is common to the A-12, YF-12 and SR-71 from the wing aft (main gear well FS 914 to 954 in all three; cowl lip near FS 790 to 800; rudder leading edge FS 1077), so these YF-12 numbers can be placed directly on the SR-71A from about FS 715 aft (agreement within about 10 in, the accuracy of the drawings). The forebodies differ (radome tip FS 90 on the YF-12, FS 102 on the SR-71A, cockpits about 25 in further aft on the YF-12), so YF-12 forebody stations are listed for reference only.
- **Wing:** a multibeam box with spanwise beams normal to the centreline at a 16 in pitch: forward box FS 738 to 914, aft box FS 954 to 1226, both WS 35 to 127; outboard box WS 213 to 293.5; ribs at WS 72, 100, 127, 213, 241 and 267; nacelle WS 134 to 206 (centre 170). The main gear sits between the boxes, on the beams at FS 914 and 954.
- **SR-71A forebody and systems** come from five flight manual figures without station labels, scaled against the TM-4749 stations: fig 4-24 (forward fuselage plan and side), fig 4-37 (whole-aircraft plan), fig 1-21 (nacelle section), fig 1-40 (tank schematic) and fig 2-3 (turning dimensions). Each scaling was checked against an independent number (calibration table below).
- **Fuel tanks** (fig 1-32 capacities) were placed by scaling fig 1-40 between the main gear well and the tail cone; two independent checks landed within 1 in (tank 2 to 3 boundary at FS 739 against the forward wing box at FS 738; tank 1A front at FS 404 against the refuelling receptacle at FS 403). Treat them as plus or minus 25 in.
- **Proposed WL datum:** z = (WL - 82.0) x 0.0254 m. It puts the labelled upper fuselage line WL 131 on the existing model outline and matches the TM-4749 side view (radome tip WL 79.7, chine WL 87.8, belly WL 64.9) to within 2.3 in.

## Frame and units

- x (m) = (FS - 102) x 0.0254. FS 102 radome tip, FS 1355 tail cone tip (TM-4749 figs 4 and 5).
- y (m) = BL x 0.0254, positive to the right wing. The NASA YF-12 papers give spanwise positions as WS measured from the centreline; WS is used as BL (the YF-12 nacelle centreline is WS 170 in TM X-2880 table 3 and 14.17 ft in TN D-6987 fig 2).
- z (m) = (WL - 82.0) x 0.0254 (proposed). Evidence and checks:
  - TM-4749 fig 5 side view (scaled with its own FS 102 and FS 1355 leaders, 1.483 px/in, leaders agree to 5 in): radome tip WL 79.7, chine line at FS 500 WL 87.8, belly WL 64.9. The conversion gives model values WL 82.0 (radome tip, z = 0), WL 85.8 (chine, z = 0.098 m) and WL 65.1 (belly, z = -0.43 m). Agreement within 2.3 in.
  - SR-71A-1 fig 4-24 side view (scaled 0.1445 in/px, see calibration notes): radome tip about WL 77.5 and belly WL 63.7 if its top line is WL 131.
  - TM-4749 nomenclature: moment reference point FS 900, BL 0, WL 100 (z = 0.457 m), near the body mid-depth of the model (about z = 0.41 m). The symbol drawn in fig 5 sits at about WL 94.
  - YF-12 cross-check (TM X-2880 table 3, V points): the fuselage underside at the ventral fin root runs from WL 69.5 at FS 1127.6 to WL 80.6 at FS 1270.8, consistent with a common WL datum for the family.
  - Uncertainty: plus or minus 3 in (0.08 m). Alternative: anchor the radome tip (WL about 80 by TM-4749 fig 5) instead, which lowers every z by about 0.05 m relative to the model outline.
- Where an item has side "both", BL and y are given for the right side; mirror with negative y for the left. Items with side "left" or "right" carry the sign of that side only where a BL is given.
- Fuselage stations are common to the A-12, YF-12 and SR-71 in the wing, nacelle and tail region: main gear well FS 914 to 954 in the YF-12 text (TM X-2880 p.2 to 3) and the A-12 manual (cover 70, "W.S. 914 to W.S. 954"), and FS 920 to 948 measured on the SR-71A fig 4-37; cowl lip near FS 790 to 800 on the SR-71A (fig 4-37, model trace) and the YF-12 (TM X-2880 fig 5a); the YF-12 movable rudder root leading edge NS 1076.6 matches the SR-71 fin leading edge at FS 1077 in the model trace. The forebodies differ: radome tip FS 90 (YF-12, TM X-2880), FS 102 (SR-71A, TM-4749); the YF-12 canopies span about FS 265 to 404 (TM X-2880 fig 5a concluded, p.43, scaled between its FS 90 and FS 670 labels), about 25 in further aft than the SR-71A canopies (FS 243 to 374, FM fig 4-37). Do not carry forebody stations across types.
- Nacelle stations (N.S.) and body stations (B.S.) in the A-12 manual and the YF-12 rudder table are taken as equal to FS: the YF-12 rudder root chord from its N.S. corners (177.6 in) equals Kock table 1 (4.512 m), and its leading edge (N.S. 1076.6) falls on the SR-71A fin leading edge in the model trace (FS 1077).

Confidence codes: **labelled** = Station printed on a labelled drawing or in a table; **text** = Read from text; **measured** = Measured from a drawing by scaling between labelled stations on the same figure; **estimated** = Estimated from a drawing without station labels (method stated); **derived** = Derived by calculation from published dimensions (method stated).

### How each unlabelled figure was scaled

- **TMX2880_fig2a.** TM X-2880 fig 2a (YF-12 generalized structure, plan): calibrated to its five labelled section cuts A-A FS 254, B-B 365, C-C 580, D-D 738, E-E 1040 plus the nose (FS 90) and fuselage end (FS 1310) from the text: FS = 0.67092 * px - 543.89 on the 300 dpi page (pages/ntrs-19730021212_TM-X-2880_p37_fig2a_*.png), residuals under 3 in. The printed inch axis of the figure is offset about 5.5 in from the drawn aircraft; the section labels were preferred. WS from the figure axis, WS = (row - 987) / 1.506.
- **FM_fig4-24.** SR-71A-1 fig 4-24 (plan and side of the forward fuselage, no stations): radome tip at row 4958 of the 4167 x 5834 page; one scale 0.1445 in/px fitted to the chine planform of the model trace (FS 105 to 344, rms 0.6 in). Checks: side-view body depth 67 in (model 65.7 in); canopy hump FS 245 to 381 (TM-4749 fig 5: FS 244 to 389). FS = 102 + (4958 - row) * 0.1445. Beyond FS 460 the figure could not be checked independently.
- **FM_fig4-37.** SR-71A-1 fig 4-37 (whole-aircraft plan, no stations): radome tip x = 567 px, tail cone tip x = 3697 px on the 4167 x 5834 page, 2.498 px/in, FS = 102 + (x - 567) / 2.498. Checks: main gear wells FS 920 to 948 (YF-12 and A-12: 914 to 954), outboard elevon hinge FS 1176 to 1182 (YF-12 EO 1 to 6: 1181 to 1187), cowl lip FS 790 (YF-12 fig 5a about 799).
- **FM_fig1-21.** SR-71A-1 fig 1-21 (nacelle section schematic, Mach 0 panel): scaled between the cowl lip (FS 790, fig 4-37) and the engine face (cowl lip plus 5.4 Rc = 159 in, CR-163106 figs 4 and 7, Rc = 29.38 in from TM X-3144 fig 8): 0.3087 in/px on the 2142 x 3000 media file. Checks: spike tip FS 692 (fig 4-37: 689); nacelle exit FS 1227 (fig 4-37: 1234).
- **FM_fig1-40.** SR-71A-1 fig 1-40 (axonometric schematic of the tanks): positions of tank end ellipses projected on the fuselage axis of the drawing, scaled between the main gear well (tank 3 aft end FS 914, tank 4 forward end FS 954; the drawing closes the gap) and the tail cone tip (FS 1355); 0.552 in per display unit. Checks: tank 2 to 3 boundary falls at FS 739, matching the YF-12 forward wing box start FS 738 (tank 3 group = forward wing boxes plus a fuselage tank, FM p.1-50); tank 1A forward end falls at FS 404, matching the air refuelling receptacle door FS 403 to 442 measured on fig 4-37 (fig 1-40 puts the receptacle on top of tank 1A). Uncertainty about 25 in.
- **FM_fig2-3.** SR-71A-1 fig 2-3 dimensions with p.1-4: turn centre on the main axle line, (28.3 + 47.4)/2 = 37.85 ft from the aircraft centreline; nose gear sqrt(54.5^2 - 37.85^2) = 39.21 ft ahead of the main axle (steering angle 46 deg against the 45 deg limit); probe tip sqrt(81.7^2 - 37.85^2) = 72.40 ft ahead of the main axle. With overall length 107.4 ft (p.1-4) ending at the tail cone FS 1355 (TM-4749), the probe tip is FS 66.2, the main axle FS 935.0 and the nose gear axle FS 464.5.
- **TM4749_fig4.** TM-4749 fig 4 plan view, 300 dpi page: least-squares fit to its FS 102, 736.5, 1226.5, 1295 and 1355 leaders, FS = 0.69304 * px - 112.84, residuals up to 9 in.
- **TM4749_fig5.** TM-4749 fig 5 side view, 300 dpi page: FS 102 leader at x = 364 px, FS 1355 at x = 2222 px (1.4828 px/in); other leaders (1023, 1033, 1041.9, 1196.5, 1230.9, 1244.6, 1295) fall within 5 in. WL from the labelled WL 131 line at row 725.5 with the same scale.

## 1. Datum and outline stations

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Radome tip (nose datum) | 102 | 0 |  |  | 79.7 to 82 | -0.058 to 0 | SR-71A | labelled | TM4749 figs 4 and 5, pp. 6 to 7 |
| Pitot mast tip | 66.2 | -0.909 |  |  |  |  | SR-71A | derived | FM p.1-4 and fig 2-3, pp. 1-4, 2-30; TM4749 FS 1355 tail cone, p. 6 |
| Tail cone tip | 1355 | 31.826 |  |  |  |  | SR-71A | labelled | TM4749 figs 4 and 5, pp. 6 to 7 |
| Upper fuselage line WL 131 (aft of the canopy) | 440 to 700 | 8.585 to 15.189 |  |  | 131 | 1.245 | SR-71A | labelled | TM4749 figs 4 and 5, pp. 6 to 7 |
| Aerodynamic moment reference point | 900 | 20.269 | 0 | 0 | 100 | 0.457 | SR-71A | labelled | TM4749 nomenclature and fig 4 label F.S.900, pp. 2, 6 |
| Wing tip (outline) | 1188 to 1200 | 27.584 to 27.889 | 333.6 to 340.2 | 8.473 to 8.641 |  |  | SR-71A | measured | FM p.1-4 span 55.6 ft, p. 1-4; TM4749 fig 5 plan, p. 7; FM fig 4-37 plan, p. 4-125; MODEL planform_half maximum at FS 1200 |
| Chine to inboard wing leading edge junction | 708 to 730 | 15.392 to 15.951 |  |  |  |  | SR-71A | measured | TM4749 fig 4 plan, p. 6; FM fig 4-37 plan, p. 4-125; MODEL planform jump at FS 729.7 |

Notes:

- **Radome tip (nose datum).** WL range: 79.7 measured on TM-4749 fig 5; 82.0 by definition of the proposed z datum (model radome tip z = 0).
- **Pitot mast tip.** Method: FS 1355 minus 107.4 ft (1288.8 in) = FS 66.2; fig 2-3 geometry gives the same main axle to probe distance (72.40 ft) when the main axle is FS 935. Mast about 36 in ahead of the radome tip.
- **Tail cone tip.** Other value: YF-12 fuselage ends FS 1310 (TMX2880 p.2 to 3 text, the SR-71A tail cone is longer)
- **Upper fuselage line WL 131 (aft of the canopy).** The WL 131 leader points at the fuselage top behind the canopy (about FS 440 in fig 5); the line runs level to about FS 700 in both figures.
- **Wing tip (outline).** BL 333.6 is half the published 55.6 ft span (the real tip); BL 340.2 is the TM-4749 reference tip. Other value: FS 1193, BL 332 (TM4749 fig 4 plan, measured) Other value: YF-12 tip about FS 1191 (TMX2880 fig 5a, measured)
- **Chine to inboard wing leading edge junction.** The model trace places the junction about 20 in aft of both flight manual and TM-4749 plans.

## 2. Fuselage frames and bulkheads

No SR-71A source lists frames. The SR-71A bulkheads below are the ones the flight manual figures show (nose joint, crew compartment ends, cockpit divider); the regular frame pattern must be borrowed from the YF-12 (TM X-2880 fig 2a, "a general representation of the structure only") or, in the wing region, from the wing beams, which run straight through the fuselage ("These tanks are continuous across the fuselage, and they occupy the entire fuselage in the wing area", TM X-2880 p.3).

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Nose section joint and nose bulkhead (interchangeable nose) | 232.5 to 237.3 | 3.315 to 3.437 |  |  |  |  | SR-71A | estimated | FM fig 4-24 plan and side, p. 4-80; FM fig 4-37 plan, p. 4-125; FM text, p. 1-134; FM OBC, p. 4-93 |
| Windshield base and forward cockpit front (sealed crew compartment forward end) | 242 to 246 | 3.556 to 3.658 |  |  |  |  | SR-71A | estimated | FM fig 4-24 side, p. 4-80; FM fig 4-37, p. 4-125; TM4749 fig 5 side, p. 7; FM text, p. 1-187 |
| Bulkhead between cockpits (RSO instrument panel) | 310 to 321 | 5.283 to 5.563 |  |  |  |  | SR-71A | estimated | FM fig 4-24 side, p. 4-80; FM fig 4-37, p. 4-125 |
| Aft bulkhead of the crew compartment (behind the RSO) | 378 to 387 | 7.01 to 7.239 |  |  |  |  | SR-71A | estimated | FM fig 4-24 side, p. 4-80; FM fig 4-37, p. 4-125 |
| YF-12 generalized forebody frames (plan-view lines) | 253.5, 382.3, 440, 485, 555.1, 673.5, 710.4, 716.4, 738.2 | 3.848, 7.12, 8.585, 9.728, 11.509, 14.516, 15.453, 15.606, 16.159 |  |  |  |  | YF-12 (forebody differs from SR-71A; reference only) | measured | TMX2880 fig 2a, p. 37; TMX2880 text, p. 2 |
| YF-12 structural cross sections A-A to E-E | 254, 365, 580, 738, 1040 | 3.861, 6.68, 12.141, 16.154, 23.825 |  |  |  |  | YF-12 | labelled | TMX2880 fig 2a section labels, p. 37 |
| Mid and aft fuselage as cylindrical fuel tanks | 715 to 1310 | 15.57 to 30.683 |  |  |  |  | YF-12 (structure shared with SR-71A) | text | TMX2880 text, p. 2 to 3 |
| Wing beams carried through the fuselage (aft box) as frames | 954, 970, 986, 1002, 1018, 1034, 1050, 1066, 1082, 1098, 1114, 1130, 1146, 1162, 1178, 1194, 1210, 1226 | 21.641, 22.047, 22.454, 22.86, 23.266, 23.673, 24.079, 24.486, 24.892, 25.298, 25.705, 26.111, 26.518, 26.924, 27.33, 27.737, 28.143, 28.55 |  |  |  |  | YF-12 (applies to SR-71A wing) | measured | TMX2880 fig 2a, p. 37; TMX2880 text, p. 3 |
| Structural section at FS 1130 (fuselage frame, wing beams, nacelle frame, rudder support) | 1130 | 26.111 |  |  |  |  | YF-12 | labelled | TM104317 fig 31, p. 23 |

Notes:

- **Nose section joint and nose bulkhead (interchangeable nose).** Method: Calibration notes FM_fig4-24 and FM_fig4-37.
- **Windshield base and forward cockpit front (sealed crew compartment forward end).** No source gives the pressure bulkhead stations; the sealed compartment lies between the nose bulkhead (FS about 235) and the bulkhead aft of the rear cockpit (FS about 380).
- **YF-12 generalized forebody frames (plan-view lines).** Method: Calibration note TMX2880_fig2a; lines found by column projection of the drawing. FS 253.5 coincides with section A-A (FS 254) and the chine start of the YF-12; the double line at 710 and 716 is the forebody to mid-fuselage joint given in the text as FS 715.
- **YF-12 structural cross sections A-A to E-E.** Schematic sections: round core with chine flare (A, B), flat chine bay section (C), round core with wing attachment stubs (D, E).
- **Mid and aft fuselage as cylindrical fuel tanks.** YF-12 fuselage diameter 64.0 in (1.626 m), CP2054 table 1 p.20.
- **Wing beams carried through the fuselage (aft box) as frames.** Measured centreline lines: 1003.9, 1019.4, 1035.8, 1051.9, 1067.7, 1083.8, 1100.2, 1117.0, 1132.7, 1148.5, 1164.6, 1180.7, 1197.1, 1213.2, 1226 to 1229. Values listed are the 16 in pattern through the labelled beams of TM-104317 fig 26.

## 3. Longerons and chine structure

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Side longerons (sides of the 64 in core cylinder) | 381 to 791 | 7.087 to 17.501 | -31.5 to 31.5 | -0.8 to 0.8 |  |  | YF-12 | measured | TMX2880 fig 2a plan lines at WS 31.2 and 31.9, p. 37; TMX2880 text, p. 2 to 3 |
| Top and bottom centreline longerons | 90 to 1310 | -0.305 to 30.683 | 0 | 0 |  |  | YF-12 (applies to SR-71A) | text | TMX2880 text, p. 2 to 3 |
| Inner forebody lines at WS 17 to 19 (purpose not stated) | 252 to 499 | 3.81 to 10.084 | -17.3 to 18.6 | -0.439 to 0.472 |  |  | YF-12 | measured | TMX2880 fig 2a, p. 37 |
| Chine edge line | 102 to 712 | 0 to 15.494 |  |  | 79.7 to 87.8 | -0.058 to 0.147 | SR-71A | measured | TM4749 fig 5 side, p. 7; FM p.1-4, p. 1-4; MODEL chine_z 0.03 to 0.10 m forward of FS 750 |

Notes:

- **Top and bottom centreline longerons.** No WL given; place on the upper and lower moldline of the core cylinder.
- **Inner forebody lines at WS 17 to 19 (purpose not stated).** Could be compartment walls; not identified by the text.
- **Chine edge line.** Chine and fillet structure: "Fairings between the fuselage shell and the wing enclose areas used for electrical and plumbing lines. These fairings carry local airloads only." (TM X-2880 p.3, YF-12). The SR-71A forebody chines hold the mission bays (FM fig 1-1, fig 4-24).

## 4. Wing: beams (spars), ribs, boxes, elevons, nacelle attachment

Outer wing panel break: the outer panel (outboard box WS 213 to 293.5, its leading edge and the tip) joins outboard of the nacelle (WS 206); the A-12 manual lists nacelle pin joints at FS 873 to 914 and FS 1130 to 1200 on the inboard side of the nacelle (WS 131 to 150). The beams carry spanwise bending, shear and part of the torsion; nacelle frames pass the outer wing bending into the inner wing; the forward and aft boxes are joined only at the root and the outboard end because of the open gear bay (TM X-2880 p.3). TM-104317 fig 2 shows the skeleton in perspective (main gear wheel well, outboard box, W.S. 72); fig 31 is a true section at FS 1130.

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Inboard forward wing box (tank 3 wing section) | 738 to 914 | 16.154 to 20.625 | 35 to 127 | 0.889 to 3.226 |  |  | YF-12 (applies to SR-71A) | text | TMX2880 text, p. 3 |
| Inboard aft wing box (tanks 6A and 6B wing sections) | 954 to 1226 | 21.641 to 28.55 | 35 to 127 | 0.889 to 3.226 |  |  | YF-12 (applies to SR-71A) | text | TMX2880 text, p. 3 |
| Outboard wing box (outer wing panel) | 1050 to 1190 | 24.079 to 27.635 | 213 to 293.5 | 5.41 to 7.455 |  |  | YF-12 (applies to SR-71A) | text | TMX2880 text, p. 3 |
| Spanwise wing beams (labelled) | 818, 850, 882, 914, 954, 986, 1018, 1050, 1082, 1114, 1146, 1178, 1210 | 18.186, 18.999, 19.812, 20.625, 21.641, 22.454, 23.266, 24.079, 24.892, 25.705, 26.518, 27.33, 28.143 |  |  |  |  | YF-12 (applies to SR-71A) | labelled | TM104317 fig 26, p. 19; TMX2880 text, p. 3 |
| All inboard wing beams (16 in pitch) | 754, 770, 786, 802, 818, 834, 850, 866, 882, 898, 914, 954, 970, 986, 1002, 1018, 1034, 1050, 1066, 1082, 1098, 1114, 1130, 1146, 1162, 1178, 1194, 1210, 1226 | 16.561, 16.967, 17.374, 17.78, 18.186, 18.593, 18.999, 19.406, 19.812, 20.218, 20.625, 21.641, 22.047, 22.454, 22.86, 23.266, 23.673, 24.079, 24.486, 24.892, 25.298, 25.705, 26.111, 26.518, 26.924, 27.33, 27.737, 28.143, 28.55 |  |  |  |  | YF-12 (applies to SR-71A) | measured | TMX2880 fig 2a, p. 37; TM104317 fig 26, p. 19 |
| Wing ribs (chordwise, constant WS) |  |  | 35, 72, 100, 127, 213, 241, 267, 293.5 | 0.889, 1.829, 2.54, 3.226, 5.41, 6.121, 6.782, 7.455 |  |  | YF-12 (applies to SR-71A) | labelled | TM104317 fig 31, p. 23; TM104317 fig 2, p. 4; TMX2880 text, p. 3; TMX2880 fig 2a, p. 37 |
| Nacelle (structural cylinder between inner and outer wing) |  |  | 134 to 206 | 3.404 to 5.232 |  |  | YF-12 (applies to SR-71A) | text | TMX2880 text, p. 3 |
| Nacelle and outer wing pin joints (outer panel attachment) | 873 to 914; 1130 to 1200 | 19.583 to 20.625; 26.111 to 27.889 | 131 to 150 | 3.327 to 3.81 |  |  | A-12 (shared structure, inference) | text | A12GH sheet 3 cover 21, p. 1-5 |
| Corrugated and beaded wing skins (thermal expansion relief) |  |  | 35 to 293.5 | 0.889 to 7.455 |  |  | YF-12 and SR-71A | text | TM104317 fig 5 and text, pp. 5 to 6 |
| Inboard elevon | 1226 to 1300 | 28.55 to 30.429 | 40 to 127 | 1.016 to 3.226 |  |  | YF-12 and A-12 (applies to SR-71A) | labelled | TMX2880 table 3, p. 10; A12GH sheet 3 cover 2A, p. 1-5; CP2054 Kock table 1, p. 19 |
| Outboard elevon | 1176 to 1257 | 27.28 to 29.337 | 210 to 327 | 5.334 to 8.306 |  |  | YF-12 and A-12 (applies to SR-71A) | labelled | TMX2880 table 3, p. 10; A12GH sheet 1 cover 64, p. 1-3; FM fig 4-37, p. 4-125 |

Notes:

- **Outboard wing box (outer wing panel).** FS range of the outboard beams measured on fig 2a (lines at FS 1067 to 1189 in the WS 215 to 235 band; WS 280 to 300 band only 1086 and 1184). TM-104317 fig 26 puts the outboard gauge rows at FS 1050 to 1178.
- **Spanwise wing beams (labelled).** Beams run straight across the span at constant FS. Main gear is supported by the aft beam of the forward box (FS 914) and the forward beam of the aft box (FS 954).
- **All inboard wing beams (16 in pitch).** Method: Calibration note TMX2880_fig2a; values rounded to the 16 in pattern defined by the labelled beams. FS 754 and 738 (box front) are only near the root because the inboard leading edge is swept.
- **Nacelle (structural cylinder between inner and outer wing).** Nacelle centreline BL 170 (YF-12 N test points, TM X-2880 table 3; 14.17 ft in TN D-6987 fig 2). The model trace puts the nacelle centre at BL 166.3.
- **Nacelle and outer wing pin joints (outer panel attachment).** Assumes nacelle (N.S.) and body (B.S.) stations equal FS; see datum_across_types.
- **Corrugated and beaded wing skins (thermal expansion relief).** No source gives stations for the corrugated panels. The corrugations run chordwise (fore and aft), across the spanwise beams, over the inboard and outboard boxes (Johnson 1981 typed p.10 and Merlin AIAA 2009-1522 p.19 as quoted in research/systems/systems.md 3.1; both tier C, facts only). Model them on the box skins between WS 35 to 127 and WS 213 to 293.5: estimate.
- **Inboard elevon.** Aft box ends FS 1226 (TM X-2880 p.3); the elevon hinge line lies just aft and is swept forward outboard.

## 5. Nacelle, inlet and engine

Inlet stations are given as distance aft of the cowl lip in cowl radii (Rc = 29.38 in) in the YF-12 inlet reports and turned into FS with the cowl lip at FS 790 to 800. The inlet is the same on the A-12, YF-12 and SR-71 (systems.md 2.2). Door counts are from CP-2054 p.24.

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Spike tip, spike forward (ground and below Mach 1.6) | 689 to 702 | 14.91 to 15.24 | 160 to 165 | 4.064 to 4.191 |  |  | SR-71A | measured | FM fig 4-37 plan, p. 4-125; FM fig 1-21 Mach 0 panel, p. 1-33; CR163106 fig 4, p. 12; TND6987 fig 2, p. 17 |
| Spike travel aft (forward to fully aft) |  |  |  |  |  |  | SR-71A | text | FM about 26 in, p. 1-31; CR163106 spike translation 0.862 Rc, p. 29 |
| Cowl lip (capture plane) | 785 to 801 | 17.348 to 17.755 | 170 | 4.318 |  |  | SR-71A | measured | FM fig 4-37 plan, p. 4-125; TM4749 fig 4 plan, p. 6; MODEL cowl_plan FS 797.6 to 801.5; TMX2880 fig 5a, p. 42; TMX3144 fig 8, p. 16 |
| Spike porous centerbody bleed band (spike forward) | 796 to 808 | 17.628 to 17.932 | 170 | 4.318 |  |  | SR-71A | estimated | FM fig 1-21 Mach 0 panel, p. 1-33; CR163106 fig 4, p. 12 |
| Cowl shock trap (cowl bleed), 32 tubes | 831 to 845 | 18.517 to 18.872 | 170 | 4.318 |  |  | SR-71A | estimated | CR163106 fig 4, p. 12; FM fig 1-21 Mach 0 panel, p. 1-33; CP2054 fig 2, p. 24 |
| Inlet throat region | 830 to 850 | 18.491 to 18.999 | 170 | 4.318 |  |  | SR-71A | estimated | CR163106 fig 7 area distribution, pp. 15, 29; FM throat closes to 4.16 sq ft, p. 1-31 |
| Forward bypass doors (rotating band), 16 doors and 3 louvre exits | 843 to 866 | 18.821 to 19.406 | 170 | 4.318 |  |  | SR-71A | estimated | CR163106 fig 4, p. 12; FM fig 1-21 Mach 0 panel, pp. 1-31, 1-33; CP2054 fig 2, p. 24 |
| Spike (centerbody) support struts, 4 | 875 to 950 | 19.634 to 21.539 | 170 | 4.318 |  |  | SR-71A | estimated | CR163106 fig 4, p. 12; FM fig 1-20, p. 1-32; CP2054 fig 2, p. 24 |
| Aft bypass doors (rotating band), 24 doors | 938 to 950 | 21.234 to 21.539 | 170 | 4.318 |  |  | SR-71A | estimated | FM text, pp. 1-35, 1-33; CP2054 fig 2, p. 24 |
| Engine face (compressor inlet, IGVs) | 949 to 961 | 21.514 to 21.819 | 170 | 4.318 |  |  | SR-71A | derived | CR163106 figs 4 and 7, pp. 12, 15; TMX3144 Rc 29.38 in, p. 16 |
| Suck-in (inlet auxiliary) doors on the nacelle | 970 to 988 | 22.047 to 22.504 | 170 | 4.318 |  |  | SR-71A | estimated | FM fig 1-21 Mach 0 panel, p. 1-33; A12GH sheet 3 covers 10 and 13, p. 1-5 |
| Forward engine mount access (top of nacelle) | 1010 | 23.063 | 170 | 4.318 |  |  | A-12 (shared nacelle, inference) | text | A12GH sheet 1 cover 60, p. 1-3 |
| J58 (JT11D-20) engine body | 952 to 1150 | 21.59 to 26.619 | 170 | 4.318 |  |  | SR-71A | estimated | FM fig 1-21 Mach 0 panel, p. 1-33; NASMJ58 length 180 in |
| Tertiary (blow-in) doors | 1150 to 1160 | 26.619 to 26.873 | 170 | 4.318 |  |  | SR-71A | estimated | FM fig 1-21 Mach 0 panel, p. 1-33 |
| Ejector nozzle and free-floating flaps | 1160 to 1234 | 26.873 to 28.753 | 170 | 4.318 |  |  | SR-71A | measured | FM fig 1-21, p. 1-33; FM fig 4-37 plan, p. 4-125; TM4749 fig 4 plan, p. 6 |
| Nacelle frame lines (generalized) | 792, 882, 898, 914, 930, 945, 955, 970, 986, 1002, 1019, 1034, 1051, 1067, 1083, 1100, 1116, 1132, 1180, 1206, 1239 | 17.526, 19.812, 20.218, 20.625, 21.031, 21.412, 21.666, 22.047, 22.454, 22.86, 23.292, 23.673, 24.105, 24.511, 24.917, 25.349, 25.756, 26.162, 27.381, 28.042, 28.88 | 140 to 180 | 3.556 to 4.572 |  |  | YF-12 | measured | TMX2880 fig 2a, p. 37; TM104317 text, p. 4 |
| Nacelle centreline test points N 1 to N 7 | 834, 882, 954, 1050, 1114, 1178, 1196 | 18.593, 19.812, 21.641, 24.079, 25.705, 27.33, 27.788 | 170 | 4.318 |  |  | YF-12 | labelled | TMX2880 table 3, p. 10 |

Notes:

- **Spike tip, spike forward (ground and below Mach 1.6).** Spike axis canted down 5.3 deg (fig) or 5.63 deg (text) and toed in 3.25 deg (TN D-6987 p.3, figs 2 and 9); cone 26 deg included (TN D-6987 p.4). BL: the toe-in puts the tip about 5.5 in inboard of the nacelle axis over 96 in (derived BL 164.5); TM-4749 fig 4 measures BL 164, fig 4-37 about 160 after correcting its 3.4 percent narrower lateral scale. Other value: FS 730.6 (MODEL (Dryden EG-0075-02 trace), about 67 in ahead of the cowl lip, consistent with a drawing made with the spike retracted) Other value: FS 711 (TM4749 fig 4 plan, measured, also about 71 in ahead of its cowl lip)
- **Spike travel aft (forward to fully aft).** Fully aft tip about FS 715 to 728 (forward position plus 26 in).
- **Cowl lip (capture plane).** Recommended FS 790 to 800. Capture diameter 58.76 in.
- **Spike porous centerbody bleed band (spike forward).** Method: Calibration FM_fig1-21; moves aft with the spike.
- **Inlet throat region.** No source gives a throat station for the SR-71A. Place the throat near the shock trap (x/Rc about 1.5); it moves with spike position.
- **Engine face (compressor inlet, IGVs).** Method: Cowl lip FS 790 to 800 plus 158 to 161 in.
- **Forward engine mount access (top of nacelle).** No aft mount station found in any source.
- **J58 (JT11D-20) engine body.** 180 in from the face gives FS about 1130 to 1140; the schematic shows about 200 in. Fig 1-2 (p.1-6) gives the internal layout.
- **Ejector nozzle and free-floating flaps.** Other value: nacelle exit about FS 1240 (TMX2880 fig 5a (YF-12), measured) Other value: FS 1261 (MODEL (nacelle rings to x = 29.45 m))

## 6. Fins and rudders

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| All-moving rudder (movable vertical tail), root at fin station 55.5, tip at 130 | 1076.6 to 1254.2 | 24.754 to 29.266 | 170 | 4.318 |  |  | YF-12 (applies to SR-71A) | labelled | TMX2880 table 3 R points, p. 12; CP2054 Kock table 1, p. 19 |
| Rudder post (pivot) and rudder actuator | 1142 to 1172 | 26.416 to 27.178 | 170 | 4.318 |  |  | YF-12 (applies to SR-71A) | labelled | TMX2880 fig 5b, p. 44; A12GH sheet 4 cover 74, p. 1-6; TM104317 fig 31, p. 23 |
| Fixed stub fin on the nacelle | 1060 to 1280 | 24.333 to 29.921 | 170 | 4.318 |  |  | YF-12 (applies to SR-71A) | measured | CP2054 Kock table 1, p. 19; MODEL fin_side FS 1077.4 to 1280.4; A12GH N.S. 1090 bottom of fin, p. 1-6 |

Notes:

- **All-moving rudder (movable vertical tail), root at fin station 55.5, tip at 130.** Fin stations are measured along the canted (15 deg inboard) fin span from the nacelle centreline (total span 130 in = 3.302 m). The root chord from the R points (177.6 in) and tip chord (94.0 in) equal Kock table 1.
- **Fixed stub fin on the nacelle.** Stub about 21 in above the nacelle (Merlin AIAA 2009-1522 p.19, tier C fact as quoted in systems.md 3.6).

## 7. Fuel tanks

FM p.1-50: "Tanks 1, 1A, 2, 4, and 5 are entirely contained in the fuselage. Tank 1A is a small tank located immediately forward of and feeding into tank 1. Tanks 3 and 6 consist of three and five tank groups ... The No. 3 tank group is comprised of the forward section of each wing and a fuselage tank. The No. 6 tank group is located in the wings on either side of tanks 4 and 5 and includes a small sump tank (approximately 12 gallons) at the extreme aft end of the fuselage." Total 12,219.2 gal, 80,280 lb (fig 1-32). Volume check: tank 2 over FS 595 to 739 needs a 63.5 in equivalent diameter, close to the 64 in core; tank 4 needs 53 in, consistent with the drag chute compartment above it.

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Tank 1A (fuselage; small tank under the air refuelling receptacle, feeds tank 1) | 404 to 474 | 7.671 to 9.449 |  |  |  |  | SR-71A | estimated | FM fig 1-32 capacities, p. 1-48; FM text, p. 1-50; FM fig 1-40, p. 1-59 |
| Tank 1 (fuselage) | 474 to 595 | 9.449 to 12.522 |  |  |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; FM fig 1-40, p. 1-59; FM text, pp. 1-47, 1-58 |
| Tank 2 (fuselage) | 595 to 739 | 12.522 to 16.18 |  |  |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; FM fig 1-40, p. 1-59; FM text, p. 1-107; TP2000 pitch rate measured at FS 683.0, p. 10 |
| Tank 3 group (fuselage tank plus the forward section of each wing) | 739 to 914 | 16.18 to 20.625 | 0 to 127 | 0 to 3.226 |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; FM text, p. 1-50; TMX2880 forward wing box FS 738 to 914, p. 3 |
| Main gear well between tanks 3 and 4 (not fuel) | 914 to 954 | 20.625 to 21.641 |  |  |  |  | SR-71A | text | TMX2880 text, p. 3 |
| Tank 4 (fuselage; drag chute compartment above it) | 954 to 1106 | 21.641 to 25.502 |  |  |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; FM fig 1-40, p. 1-59; FM text, pp. 1-93, 1-58 |
| Tank 5 (aft fuselage; aft transfer tank) | 1106 to 1300 | 25.502 to 30.429 |  |  |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; FM fig 1-40, p. 1-59 |
| Tank 6A (forward part of the aft wing box, each wing) | 954 to 1090 | 21.641 to 25.095 | 35 to 127 | 0.889 to 3.226 |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; FM text, p. 1-50; TMX2880 aft wing box FS 954 to 1226, p. 3 |
| Tank 6B (aft part of the aft wing box, each wing) | 1090 to 1226 | 25.095 to 28.55 | 35 to 127 | 0.889 to 3.226 |  |  | SR-71A | estimated | FM fig 1-32, p. 1-48; TMX2880 aft wing box ends FS 1226, p. 3 |
| Tank 6 group sump tank (about 12 gal, boost pumps), extreme aft fuselage | 1261 to 1314 | 29.439 to 30.785 |  |  |  |  | SR-71A | estimated | FM text, p. 1-50; FM fig 1-40 item 6, p. 1-59 |

Notes:

- **Tank 1A (fuselage; small tank under the air refuelling receptacle, feeds tank 1).** Method: Calibration FM_fig1-40. Drawn as a partial shell (saddle) round the upper fuselage, not a full cylinder.
- **Tank 1 (fuselage).** Method: Calibration FM_fig1-40.
- **Tank 2 (fuselage).** Method: Calibration FM_fig1-40. The rate gyro station FS 683 (TP-2000) falls inside this estimate, as the FM statement requires.
- **Tank 3 group (fuselage tank plus the forward section of each wing).** Method: Fuselage part from calibration FM_fig1-40; wing part = forward wing box.
- **Tank 4 (fuselage; drag chute compartment above it).** Method: Calibration FM_fig1-40.
- **Tank 5 (aft fuselage; aft transfer tank).** Method: Calibration FM_fig1-40; aft end at the tail cone, uncertain.
- **Tank 6A (forward part of the aft wing box, each wing).** Method: Aft box split at its mid station FS 1090 (6A and 6B capacities are similar); the 6A to 6B boundary in fig 1-40 lies near the tank 4 to 5 boundary (FS about 1100).
- **Tank 6B (aft part of the aft wing box, each wing).** Method: As tank 6A.
- **Tank 6 group sump tank (about 12 gal, boost pumps), extreme aft fuselage.** Method: Calibration FM_fig1-40.

## 8. Equipment bays (fig 1-1 bay locator and fig 4-24 sensor locations)

Fig 1-1 (bay locator) is a perspective cutaway with no scale, so the station ranges come from fig 4-24 and fig 4-37; fig 1-1 identifies the items. Compartment letters were read from the circled labels of fig 4-24 (T and Q right aft, S and P left aft, N and L right forward, M and K left forward, R, E, C, B, A). FM: "The terms MISSION EQUIPMENT BAY and CHINE BAY are synonomous and interchangeable" (fig 4-24 note). Mission bays sit in the chines, outboard of the 64 in core.

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Compartment A, radar or OBC equipment (interchangeable nose) | 146 to 236 | 1.118 to 3.404 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 12, p. 1-5; FM fig 4-24 plan, p. 4-80; FM OBC in an interchangeable nose, pp. 4-86, 4-93 |
| Compartment B, left forward chine bay (50 L liquid nitrogen Dewar; pressure transducer assembly aft of the nose bulkhead) | 236 to 361 | 3.404 to 6.579 |  |  |  |  | SR-71A | estimated | FM text, p. 1-58; FM text, p. 1-134; FM fig 4-24 plan, p. 4-80 |
| Compartment D, right chine bay (DEF A2, C2, M) | 287 to 368 | 4.699 to 6.756 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 1, p. 1-5; FM fig 4-24 plan, p. 4-80; FM fig 4-37, p. 4-125; FM text, p. 4-124 |
| Compartment C, camera bay (circuit breakers) | 360 to 380 | 6.553 to 7.061 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 8, p. 1-5; FM fig 4-24 plan, p. 4-80; FM text, p. 1-71 |
| Compartment E, electronics bay (electrical equipment, circuit breakers) | 361 to 400 | 6.579 to 7.569 | -27 to -15 | -0.686 to -0.381 |  |  | SR-71A | estimated | FM fig 1-1 item 6, p. 1-5; FM fig 4-24 plan, p. 4-80 |
| Compartment R, radio equipment bay (PVD processor, roll gyros) | 420 to 445 | 8.077 to 8.712 | 15 to 25 | 0.381 to 0.635 |  |  | SR-71A | estimated | FM fig 1-1 item 3, p. 1-5; FM fig 4-24 plan, p. 4-80; FM text, pp. 1-107, 1-139 |
| Right forward mission bay, compartments L (forward) and N (aft); radar recorders | 360 to 522 | 6.553 to 10.668 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 2, p. 1-5; FM fig 4-24 plan, p. 4-80; FM fig 4-37 right-side chine doors FS 371 to 455, p. 4-125; FM text, p. 4-86 |
| Left forward mission bay, compartments K (forward, DEF H) and M (aft, digital and AR1700 EIP recorders) | 360 to 522 | 6.553 to 10.668 |  |  |  |  | SR-71A | estimated | FM fig 1-1 items 7, p. 1-5; FM fig 4-24 plan, p. 4-80; FM fig 4-37 and left-side doors FS 371 to 395, p. 4-125; FM text, p. 4-99 |
| Right aft mission bay, compartments Q (forward, technical objective camera or radar recorder) and T (aft, EIP) | 529 to 686 | 10.846 to 14.834 |  |  |  |  | SR-71A | estimated | FM fig 1-1 items 4, p. 1-5; FM fig 4-24 plan, p. 4-80; FM text, pp. 4-81, 4-99 |
| Left aft mission bay, compartments P (forward, technical objective camera) and S (aft, EIP) | 531 to 684 | 10.897 to 14.783 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 5, p. 1-5; FM fig 4-24 plan, p. 4-80; FM text, pp. 4-81, 4-99 |
| ANS guidance group and air conditioning bay (behind the rear cockpit, upper fuselage) | 387 to 416 | 7.239 to 7.976 | -9 to 9 | -0.229 to 0.229 |  |  | SR-71A | estimated | FM fig 4-24 side, p. 4-80; FM fig 1-1 item 15, p. 1-5; FM text, p. 4-5 |
| Nosewheel well equipment (two 106 L liquid nitrogen Dewars, lateral accelerometers, marker beacon antenna in the right door) |  |  |  |  |  |  | SR-71A | text | FM text, pp. 1-58, 1-107, 1-166 |
| Liquid oxygen containers (item 37) | 315 to 345 | 5.41 to 6.172 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 37, p. 1-5 |
| DEF A2 antennas: receive (aft of cut-outs in the nose chines) and transmit (lower chines opposite the pilot); DEF H CW receive antenna at the tail | 151 to 165; 258 to 316; 1300 | 1.245 to 1.6; 3.962 to 5.436; 30.429 |  |  |  |  | SR-71A | estimated | FM fig 4-37 boxes at x = 690 to 725 px, p. 4-125; FM text, p. 4-124; FM fig 1-1 items 29 and 39, p. 1-5 |

Notes:

- **Compartment A, radar or OBC equipment (interchangeable nose).** Method: Calibration FM_fig4-24.
- **Compartment B, left forward chine bay (50 L liquid nitrogen Dewar; pressure transducer assembly aft of the nose bulkhead).** Method: Extent assumed from the nose joint to the forward mission bay; only the B label position is measured.
- **Compartment D, right chine bay (DEF A2, C2, M).** Method: Calibrations FM_fig4-24 and FM_fig4-37.
- **Compartment C, camera bay (circuit breakers).** Only the label position is measured; extent unknown. Probably in the lower fuselage under the rear cockpit (fig 1-1).
- **Right aft mission bay, compartments Q (forward, technical objective camera or radar recorder) and T (aft, EIP).** Other value: chine doors FS 538 to 630 and 630 to 712 (FM fig 4-37 right side, measured)
- **Left aft mission bay, compartments P (forward, technical objective camera) and S (aft, EIP).** Other value: chine doors FS 572 to 652 and 652 to 712 (FM fig 4-37 left side, measured)
- **Nosewheel well equipment (two 106 L liquid nitrogen Dewars, lateral accelerometers, marker beacon antenna in the right door).** Station range: see nose_gear.
- **Liquid oxygen containers (item 37).** Method: Scaled locally between the two ejection seats of fig 1-1 (FS 279 and 345 from fig 4-24); perspective drawing, low confidence.
- **DEF A2 antennas: receive (aft of cut-outs in the nose chines) and transmit (lower chines opposite the pilot); DEF H CW receive antenna at the tail.** Method: Transmit range set to the forward cockpit range (FS 258 to 316) from the text; receive and tail positions scaled on fig 4-37 (calibration FM_fig4-37). The DEF H centreline receive antenna (fig 1-1 item 39) is under the forward fuselage; its station was not measured.

## 9. Cockpits, canopies and seats

Both cockpits share one sealed, insulated compartment pressurized to a 10,000 or 26,000 ft schedule (FM p.1-187). The SR-71A canopy pages (1-170 to 1-179) are missing from the scan.

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Forward (pilot) canopy | 243 to 314 | 3.581 to 5.385 |  |  |  |  | SR-71A | estimated | FM fig 4-37 plan, p. 4-125; FM fig 4-24 side, p. 4-80 |
| Aft (RSO) canopy | 319 to 374 | 5.512 to 6.909 |  |  |  |  | SR-71A | estimated | FM fig 4-37 plan, p. 4-125; FM fig 4-24 side, p. 4-80 |
| Canopy hump on the side profile (both canopies) | 244 to 389 | 3.607 to 7.29 |  |  | 131 | 1.245 | SR-71A | measured | TM4749 fig 5 side, p. 7; TM4749 fig 4 side, p. 6 |
| Canopy hinges | 310 to 314; 370 to 374 | 5.283 to 5.385; 6.807 to 6.909 |  |  |  |  | SR-71A | estimated | A12FM A-12 canopy, p. 1-85 (PDF p.97); FM SR-71A canopy pages 1-170 to 1-179 are missing |
| Forward cockpit (pilot): instrument panel to bulkhead | 258 to 316 | 3.962 to 5.436 |  |  |  |  | SR-71A | estimated | FM fig 4-24 plan, p. 4-80 |
| Pilot SR-1 ejection seat | 265 to 292 | 4.14 to 4.826 |  |  | 121 | 0.991 | SR-71A | estimated | FM fig 4-24 side, p. 4-80; FM seat vertical travel 9 in, p. 1-199 |
| Aft cockpit (RSO): instrument panel to aft bulkhead | 316 to 382 | 5.436 to 7.112 |  |  |  |  | SR-71A | estimated | FM fig 4-24 side, p. 4-80 |
| RSO SR-1 ejection seat | 345 | 6.172 |  |  | 127 | 1.143 | SR-71A | estimated | FM fig 4-24 side, p. 4-80; FM seat vertical travel 6.75 in, p. 1-199 |
| Test bed accelerometer "near the cockpit" | 234.5 | 3.365 |  |  |  |  | SR-71A | text | TP2000 normal and longitudinal acceleration and pitch, p. 10 |

Notes:

- **Canopy hump on the side profile (both canopies).** The model canopy object spans x = 3.5 to 8.5 m (FS 240 to 437), longer aft than these drawings.
- **Canopy hinges.** Not documented for the SR-71A in any source on disk. Placed at the aft edge of each canopy by analogy with the A-12; unconfirmed.
- **Pilot SR-1 ejection seat.** WL from the side view with its top line taken as WL 131; rough.

## 10. Landing gear, drag chute and air refuelling receptacle

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| Main gear axle line | 935 | 21.158 | -100 to 100 | -2.54 to 2.54 |  |  | SR-71A | derived | FM fig 2-3 and p.1-4, pp. 2-30, 1-4 |
| Main gear wells (retract inboard into the fuselage) | 914 to 954 | 20.625 to 21.641 | 35 to 98 | 0.889 to 2.489 |  |  | SR-71A | text | TMX2880 text, p. 3; FM fig 4-37, p. 4-125; FM text, p. 1-89; A12GH covers 70 and 71, p. 1-3 |
| Nose gear axle (dual wheels, retracts forward into the fuselage) | 464.5 to 490 | 9.207 to 9.855 |  |  |  |  | SR-71A | derived | FM fig 2-3 and p.1-4, pp. 2-30, 1-4; FM fig 2-3 nose gear mark at FS 490, p. 2-30; FM text, p. 1-89 |
| Drag chute compartment door (upper aft fuselage, above tank 4) | 1004 to 1070 | 22.911 to 24.587 |  |  |  |  | SR-71A | estimated | FM fig 4-37, p. 4-125; FM text, p. 1-93; FM fig 1-1 item 27, p. 1-5; A12GH sheet 1 cover 69, p. 1-3 |
| Air refuelling receptacle door (spine, behind the rear canopy) | 403 to 442 | 7.645 to 8.636 |  |  | 131 | 1.245 | SR-71A | estimated | FM fig 4-37, p. 4-125; FM fig 1-40 item 1, p. 1-59; FM fig 1-1 item 19, p. 1-5 |

Notes:

- **Main gear axle line.** Three-wheel bogies; derived spacing between wheels about 1.2 ft (14 in). Other value: FS 939 (FM fig 2-3 gear marks, measured (radome FS 102 to tail FS 1355)) Other value: FS 934 (well centre) (FM fig 4-37 and TMX2880 text)
- **Main gear wells (retract inboard into the fuselage).** Main gear pivot near BL 84 (A-12). Well covered by gear doors below and wing skin above (TM X-2880 p.3).
- **Nose gear axle (dual wheels, retracts forward into the fuselage).** No source gives the nosewheel well extent; it lies forward of the strut (gear retracts forward) and holds the two 106 L nitrogen Dewars (FM p.1-58). Other value: FS 477 (TMX2880 fig 4 side (YF-12), scaled)
- **Drag chute compartment door (upper aft fuselage, above tank 4).** Deployment bag holds a 42 in pilot chute, 10 ft extraction chute and 40 ft ribbon drag chute (FM p.1-93).
- **Air refuelling receptacle door (spine, behind the rear canopy).** Identification of the fig 4-37 door as the receptacle is an inference (position on the spine aft of the canopies, order behind the ANS in fig 1-1, and the tanker view in research/systems/media/photo_refuelling-receptacle-view-from-tanker_Tubridy_1988.jpg, which shows the boom just aft of the rear canopy). A separate single-point ground refuelling receptacle (fig 1-40 item 9) is under the same area.

## 11. Astro-inertial navigation (ANS) and star tracker window

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| ANS star tracker window (upper fuselage centreline) | 395 | 7.442 | 0 | 0 | 131 | 1.245 | SR-71A | estimated | FM fig 4-24 plan, p. 4-80; FM text, pp. 4-5 to 4-6 |

Notes:

- **ANS star tracker window (upper fuselage centreline).** Derived: the cone axis is tilted 7.5 deg forward of the body normal (vertical when the nose is 7.5 deg up). WL 131 is the local upper fuselage line (TM-4749).

## 12. Other stations

| Item | FS (in) | x (m) | BL or WS (in) | y (m) | WL (in) | z (m) | Applies to | Conf. | Sources |
|---|---|---|---|---|---|---|---|---|---|
| NASA test bed canoe on the upper fuselage (NASA 844 only) | 749.6 to 1244.6 | 16.449 to 29.022 | -16.5 to 16.5 | -0.419 to 0.419 | 131 to 154.2 | 1.245 to 1.834 | SR-71A NASA 844 (LASRE and test bed) | labelled | TM4749 fig 5, pp. 6 to 7; TP2000 canoe attached at fuselage hard points by, pp. 17, 19 |
| Wind-tunnel sting cut at FS 1295 (not aircraft structure) | 1295 | 30.302 | 58.8 | 1.494 |  |  | SR-71A | labelled | TM4749 figs 4 and 5, pp. 6 to 7 |
| Roll and pitch mixer (item 28, aft fuselage) | 1240 to 1290 | 28.905 to 30.175 |  |  |  |  | SR-71A | estimated | FM fig 1-1 item 28, p. 1-5 |

Notes:

- **Wind-tunnel sting cut at FS 1295 (not aircraft structure).** model/plans/NOTES.md lists FS 1295 as the wing trailing-edge tip; the figures show it is the sting mount cut across the aft fuselage.
- **Roll and pitch mixer (item 28, aft fuselage).** Method: Position by eye on a perspective drawing; low confidence.

## Where sources disagree

- Spike tip. FS 689 (SR-71A fig 4-37), FS 692 (fig 1-21) and about 96 to 100 in ahead of the cowl lip in the YF-12 reports (CR-163106 fig 4; TN D-6987 fig 2) all describe the spike forward, as it is on the ground. The model trace (Dryden EG-0075-02) has FS 730.6 and TM-4749 fig 4 about FS 711, only 67 to 71 in ahead of their cowl lips: those drawings appear to show the spike retracted (26 in further aft). The model should use FS about 690 for a parked aircraft.
- Cowl lip. FS 790 (fig 4-37), 781 to 788 (TM-4749 fig 4, plus or minus 9), 797.6 to 801.5 (model trace), about 799 (YF-12, TM X-2880 fig 5a).
- Chine to wing junction. FS 708 (TM-4749 fig 4) and FS 712 (fig 4-37) against FS 729.7 in the model trace.
- Nacelle exit. FS 1227 (fig 1-21), 1234 (fig 4-37), 1235 (TM-4749 fig 4), about 1240 (YF-12 fig 5a) against FS 1261 in the model.
- Canopy aft end. FS 373 to 389 in every drawing against FS 437 (x = 8.5 m) for the model canopy object.
- Main gear. Axle FS 935.0 derived from fig 2-3 dimensions, FS 939 from its gear marks, well centre FS 934 (fig 4-37, YF-12 text).
- Nose gear. FS 464.5 derived from fig 2-3 dimensions, FS 490 from its gear mark, about FS 477 on the YF-12 (TM X-2880 fig 4).
- Aft mission bays, aft end. FS 683 to 686 (fig 4-24 bay arrows and equipment) against FS 712 (fig 4-37 chine doors, which run to the wing junction).
- Radome tip height. WL 77.5 (fig 4-24 side), 79.7 (TM-4749 fig 5), 82.0 (model with the proposed datum).
- Moment reference. Labelled WL 100 in TM-4749 text; its symbol is drawn at about WL 94 in fig 5.
- J58 length. 180 in (Smithsonian record); about 200 in from engine face to nozzle on the fig 1-21 schematic.
- Spike cant. 5.63 deg (TN D-6987 text) against 5.3 deg (its fig 2).
- FS 1295. model/plans/NOTES.md lists it as the wing trailing-edge tip; TM-4749 figs 4 and 5 show it is the wind-tunnel sting cut across the aft fuselage (B.L. 58.8 is the body half width there). The SR-71A wing tip is near FS 1188 to 1200.

## Coverage gaps

- No SR-71A frame, bulkhead or longeron stations exist in the documents on disk; frames must be taken from the YF-12 generalized plan (forebody) and the wing beam pattern (wing region).
- Fuel tank boundaries are estimates from a schematic (plus or minus 25 in). No tank end bulkhead stations were found for any Blackbird.
- No WL for the nacelle axis, the wing reference plane or the chine in any table; only the TM-4749 side view gives heights (WL 131 upper line, WL 100 reference, WL 154 canoe).
- Nosewheel well extent, main gear strut geometry and door hinge lines: not found.
- Canopy hinge positions and canopy frame geometry: the SR-71A canopy pages are missing; only the A-12 manual says "hinged at the aft end".
- Engine mounts: only the A-12 forward mount access (N.S. 1010); no aft mount station.
- Inlet throat station: not published for the SR-71A; the YF-12 area distribution shows several near-minimum regions.
- Corrugated skin panel extents: described, not dimensioned.
- Bay heights (WL) and depths: none published; fig 4-24 side view shows the mission bays at chine level and the ANS just under the upper skin.
- Fig 1-1 and fig 1-32 are perspective drawings; positions from them (LOX containers, roll and pitch mixer) are rough.
- Leads not on disk: Lockheed weight and balance manual (named in the flight manual p.1-4 note), SR-71 structural repair or maintenance technical orders, NASA reference 11 of TM-104317 (the YF-12A load calibration report, which should have full beam and rib drawings).

## Figures to show beside each part in the viewer

Paths are relative to the repository root. Media files are tier A or B per `research/systems/media/manifest.json`; `model/plans/pages/` files are NASA or USAF pages (tier A). Do not show CR-163106 figures (tier C).

- **Datum, outline and station frame:** `model/plans/pages/ntrs-19960038443_TM-4749_p6_fig4_SR-71-LASRE-fwd-model-FS-WL-BL.png`; `model/plans/pages/ntrs-19960038443_TM-4749_p7_fig5_SR-71-LASRE-aft-model-FS-WL-BL.png`; `model/plans/pages/dfrc_EG-0075-02_SR-71A_3view.png`
- **Fuselage frames, longerons, sections:** `research/systems/media/diagram_YF-12A-structural-skeleton_TM-104317-p4-fig2.png`; `model/plans/pages/ntrs-19730021212_TM-X-2880_p37_fig2a_YF-12-structure-fuselage-sections-A-E.png`; `model/plans/pages/ntrs-19960027893_TM-104317_p23_fig31_YF-12A-section-FS1130.png`
- **Chines:** `model/plans/pages/ntrs-19730021212_TM-X-2880_p37_fig2a_YF-12-structure-fuselage-sections-A-E.png` (sections A-A to C-C); `research/systems/media/photo_head-on-inlets-chines_NASM-61-7972_NASM2016-00596.jpg`
- **Wing beams, ribs, corrugated skin:** `model/plans/pages/ntrs-19960027893_TM-104317_p19_fig26_YF-12A-wing-FS-WS-grid.png`; `research/systems/media/diagram_YF-12A-wing-thermal-expansion-relief-corrugations_TM-104317-p6-fig5.png`; `model/plans/pages/ntrs-19960027893_TM-104317_p23_fig31_YF-12A-section-FS1130.png`; `research/systems/media/diagram_YF-12A-upper-surface-temperature-contours_TM-104317-p3-fig1.png`
- **Elevons and flight controls:** `research/systems/media/diagram_SR-71A-1_fig1-51_flight-control-systems_p1-98.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-50_surface-control-deflection-limits-and-rates_p1-97.jpg`
- **Inlet, spike, bypass doors:** `research/systems/media/diagram_SR-71A-1_fig1-20_air-inlet-system-spike-forward_p1-32.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-21_inlet-airflow-patterns-nacelle-sections_p1-33.jpg`; `research/systems/media/diagram_YF-12-inlet-cutaway-door-counts_CP-2054-p24-fig2.png`; `research/systems/media/diagram_SR-71-inlet-cutaway_TM-104330-p5-fig4.png`; `model/plans/pages/ntrs-19750003899_TM-X-3144_p16_fig8_YF-12-inlet-section-cowl-radius.png`; `research/systems/media/photo_inlet-spike-head-on_Clemens-Vasters.jpg`
- **J58 engine and ejector:** `research/systems/media/diagram_SR-71A-1_fig1-2_JT11D-20-engine-cutaway-keyed_p1-6.jpg`; `research/systems/media/diagram_J58-augmentor-cutaway-bypass-tubes_TM-104330-p7-fig8.png`; `research/systems/media/photo_J58-engine_Museum-of-Aviation_Dsdugan.jpg`; `research/systems/media/photo_J58-ejector-afterburner-rear_greyloch.jpg`
- **Fins and rudders:** `model/plans/pages/ntrs-19730021212_TM-X-2880_p44_fig5b_YF-12-rudder-stations.png`; `model/plans/pages/ntrs-19780024113_CP-2054_p19_table1_YF-12-specifications.png`
- **Fuel tanks:** `research/systems/media/diagram_SR-71A-1_fig1-32_fuel-tank-arrangement-and-capacities_p1-48.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-40_air-refueling-system_p1-59.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-37_fuel-feed-system_p1-53.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-38_fuel-system-pressurization-nitrogen_p1-56.jpg`; `research/systems/media/diagram_YF-12-fuel-compartments_TM-X-2880-p38-fig2b.png`
- **Equipment and chine bays, nose:** `research/systems/media/diagram_SR-71A-1_fig1-1_general-arrangement-bay-locator_p1-5.jpg`; `research/systems/media/diagram_SR-71A-1_fig4-24_sensor-component-and-DEF-equipment-locations_p4-80.jpg`; `model/plans/pages/fm-1SR71A-1_fig4-37_DEF-equipment-location-plan-view.png` (page carries "UNCONTROLLED COPY" stamps and a 1996 deletion note; crop to the plan view); `research/systems/media/photo_detachable-nose-section_NMUSAF_loganrickert.jpg`; `research/systems/media/photo_TEOC-technical-objective-camera_Evergreen_Daderot.jpg`; `research/systems/media/photo_DEF-H-A2C-C-AR1700-recorder_Evergreen_Daderot.jpg`
- **Cockpits and seats:** `research/systems/media/diagram_SR-71A-1_fig1-12_front-cockpit-center-instrument-panel_p1-23.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-17_rear-cockpit-RSO-instrument-panel_p1-28.jpg`; `research/systems/media/diagram_SR-71A-1_fig1-83_SR-1-ejection-seat_p1-202.jpg`; `research/systems/media/photo_front-cockpit-panel_NMUSAF-Cockpit360_61-7976.jpg`; `research/systems/media/photo_cockpits-from-tanker_NASA-831_EC94-42883-1.jpg`; `research/systems/media/photo_ejection-seat-open-canopy_Bill-Abbott.jpg`
- **Landing gear:** `model/plans/pages/fm-1SR71A-1_fig2-3_minimum-turning-radius-plan-view.png`; `research/systems/media/photo_landing-gear-down-NASA-844_EC96-43463-1.jpg`; `research/systems/media/photo_main-gear-bogie_Duxford_Chad-Kainz.jpg`; `research/systems/media/photo_tires_Evergreen_Daderot.jpg`
- **Drag chute:** `research/systems/media/diagram_SR-71A-1_fig1-1_general-arrangement-bay-locator_p1-5.jpg` (item 27); `research/systems/media/photo_drag-chute-landing_NASA_GPN-2000-001944.jpg`
- **Air refuelling receptacle:** `research/systems/media/diagram_SR-71A-1_fig1-40_air-refueling-system_p1-59.jpg`; `research/systems/media/photo_refuelling-receptacle-view-from-tanker_Tubridy_1988.jpg`; `research/systems/media/photo_KC-135Q-refuelling-SR-71_DF-ST-83-07614.jpg`; `research/systems/media/photo_boomer-view-NASA-844_EC97-43933-4.jpg`
- **ANS and star tracker:** `research/systems/media/diagram_SR-71A-1_fig4-24_sensor-component-and-DEF-equipment-locations_p4-80.jpg` (side view, "ANS"); `research/systems/media/diagram_SR-71A-1_fig4-1_navigation-and-sensor-control-system_p4-4.jpg`; `research/systems/media/diagram_SR-71A-1_fig4-3_ANS-navigation-control-and-display-panel_p4-7.jpg`; `research/systems/media/photo_ANS-astro-inertial-navigation-unit_Evergreen_Daderot.jpg`

## Sources

- **FM.** SR-71A-1 Flight Manual, USAF T.O., Issue E 31 Oct 1986, Change 2 31 Jul 1989. Internet Archive item 0003756-lockheed-sr-71-03 (part 01 local: model/plans/raw/fm-1SR71A-1_IssueE-Ch2_IA-part01.pdf; OCR text from the item djvu.txt files). https://archive.org/details/0003756-lockheed-sr-71-03. Tier A (USAF work; anonymous scan, SENIOR CROWN markings, 1996 deletions).
- **TM4749.** Moes, Cobleigh, Conners, Cox, Smith and Shirakata, Wind-Tunnel Development of an SR-71 Aerospike Rocket Flight Test Configuration, NASA TM-4749, June 1996. model/plans/raw/ntrs-19960038443_TM-4749_SR-71-LASRE-wind-tunnel.pdf; printed page = PDF page minus 4. https://ntrs.nasa.gov/api/citations/19960038443/downloads/19960038443.pdf. Tier A.
- **TP2000.** Corda, Moes, Mizukami et al., The SR-71 Test Bed Aircraft: A Facility for High-Speed Flight Research, NASA/TP-2000-209023, June 2000. model/plans/raw/ntrs-20000064011_TP-2000-209023_SR-71-test-bed.pdf; printed page = PDF page minus 4. https://ntrs.nasa.gov/api/citations/20000064011/downloads/20000064011.pdf. Tier A.
- **TMX2880.** Wilson, Cazier and Larson, Results of Ground Vibration Tests on a YF-12 Airplane, NASA TM X-2880, 1973. model/plans/raw/ntrs-19730021212_TM-X-2880_YF-12-ground-vibration.pdf; printed page = PDF page minus 2. https://ntrs.nasa.gov/api/citations/19730021212/downloads/19730021212.pdf. Tier A.
- **TM104317.** Jenkins and Quinn, A Historical Perspective of the YF-12A Thermal Loads and Structures Program, NASA TM-104317, May 1996. model/plans/raw/ntrs-19960027893_TM-104317_YF-12A-thermal-loads-structures.pdf; printed page = PDF page minus 4. https://ntrs.nasa.gov/api/citations/19960027893/downloads/19960027893.pdf. Tier A.
- **TND6987.** Johnson and Montoya, Local Flow Measurements at the Inlet Spike Tip of a Mach 3 Supersonic Cruise Airplane, NASA TN D-6987, 1973. model/plans/raw/ntrs-19730015310_TN-D-6987_YF-12A-spike-tip-flow.pdf. https://ntrs.nasa.gov/api/citations/19730015310/downloads/19730015310.pdf. Tier A.
- **TMX3144.** Dustin, Cole and Neiner, Continuous-Output Terminal-Shock-Position Sensor for Mixed-Compression Inlets Evaluated in Wind-Tunnel Tests of YF-12 Aircraft Inlet, NASA TM X-3144, 1974. model/plans/raw/ntrs-19750003899_TM-X-3144_*.pdf (page subset). https://ntrs.nasa.gov/api/citations/19750003899/downloads/19750003899.pdf. Tier A.
- **CP2054.** YF-12 Experiments Symposium, Volume 1, NASA CP-2054, 1978 (Kock overview: table 1 p.19 to 20, inlet cutaway fig 2 p.24). model/plans/raw/ntrs-19780024112_* and ntrs-19780024113_*. https://ntrs.nasa.gov/api/citations/19780024112/downloads/19780024112.pdf. Tier A (inlet cutaway is a NASA reproduction of a Lockheed-style drawing).
- **CR163106.** Bangert, Feltz, Godby and Miller (Lockheed-California Co.), Aerodynamic and Acoustic Behavior of a YF-12 Inlet at Static Conditions, NASA CR-163106, 1981. model/plans/raw/ntrs-19810012550_CR-163106_*.pdf (page subset). https://ntrs.nasa.gov/api/citations/19810012550/downloads/19810012550.pdf. Tier C (Lockheed contractor report: cite numbers, do not republish figures).
- **A12GH.** A-12 Support Manual, Ground Handling, fig 1-1 Access Panels and Openings, sheets 1 to 4 (pp. 1-3 to 1-6), CIA document C06230171, released 2017-07-25. model/plans/raw/cia_C06230171_A-12-support-manual-ground-handling.pdf; pages model/plans/pages/cia-A-12-ground-handling_fig1-1-sh*.png. https://archive.org/download/cia-readingroom-document-06230171/06230171.pdf. Tier A with a note (Lockheed-prepared, CIA release, no copyright notice).
- **A12FM.** A-12 Utility Flight Manual, Lockheed for the CIA, changed 15 Mar 1968, CIA document C01316457. model/plans/raw/cia_C01316457_A-12-flight-manual_1968.pdf. https://www.cia.gov/readingroom/document/0001316457. Tier A with a note.
- **NASMJ58.** Smithsonian NASM object A19920006000, Pratt and Whitney J58 (JT11D-20) Turbojet Engine (as quoted in research/systems/systems.md section 2.1). quoted in research/systems/systems.md section 2.1. https://airandspace.si.edu/collection-objects/pratt-whitney-j58-jt11d-20-turbojet-engine/nasm_A19920006000. Tier C for images ("usage conditions apply"); the number is a fact, cite only.
- **MODEL.** Existing Article 121 model trace, model/trace/dfrc/components.json (NASA Dryden EG-0075-02 vector three-view traced and calibrated to TM-4749 FS 102 and FS 1355). model/trace/dfrc/components.json and report.json. Tier derived from tier A drawings; internal data, not a primary source.

Most useful, in order: TM X-2880 (structure text, fig 2a, table 3), TM-104317 (figs 26 and 31, labelled beams and ribs), the SR-71A-1 flight manual (figs 4-24, 4-37, 1-21, 1-40, 2-3 and the Section I and IV text), TM-4749 (the only SR-71A station and waterline labels).
