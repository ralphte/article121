# SR-71 systems: cockpits, J58 and inlet, and what made it work

Research pack for The Machine section of Article 121. Compiled 4 October 2026. Scope: Lockheed SR-71A (and SR-71B), with A-12 and YF-12 data where it applies or differs.

**How to read this file.** Every number carries a source key and a page. Page means the printed page of the document unless "PDF p" is given. Where good sources disagree, all values are given and the disagreement is stated; nothing has been averaged. Companion files: `specs.json` (the spec sheet as data, 77 rows, one source per row), `media/` (120 images: 62 flight manual figures, 14 NASA paper figures and 44 photographs) and `media/manifest.json` (rights per file). Rights tiers: **A** US government work, CC0 or no known restrictions (mirrored); **B** CC BY or BY-SA (mirrored with credit); **C** copyrighted, link only; **D** permission needed (sr-71.org, sr71.us, habu.org), link only. Nothing of tier C or D is in `media/`.

**Headline findings**

1. The declassified SR-71A-1 flight manual (Change 2, 1989) has fully keyed drawings of every panel in both cockpits, and the Internet Archive holds it as 4167 x 5834 px page masters. These are the backbone for recreating the cockpits: 50 keyed items on the pilot's centre panel alone (section 1).
2. The best real cockpit photographs are the National Museum of the USAF's Cockpit360 panorama faces of SR-71A 61-7976, rebuilt from Wayback Machine tiles. NASA has no public cockpit interior photograph of its SR-71s, and the Smithsonian has no CC0 one of 61-7972. No free photograph of an A-12 cockpit was found; the A-12 flight manual drawings are the only free source.
3. The J58 thrust disagreement is resolved: 32,500 lb was the early "J-engine" with fixed inlet guide vanes (YF-12A, early SR-71); 34,000 lb is the later "K-engine" with two-position vanes, which is the figure the 1989 SR-71A-1 manual gives (SP-4525 p.20 footnote 25; FM p.1-7). The Smithsonian and Pratt and Whitney's 30,000 lb is the odd one out.
4. The 54 / 17 / 29 percent thrust split (inlet / engine / ejector at Mach 3) has a single traceable chain: Merlin (NASA historian, AIAA 2009) citing a 1990 Lockheed course handout. NASA's fact sheet supports the shape of it ("less than 20 percent" from the engine). The flight manual gives an independent hint: derichment at cruise cuts an engine's own thrust about 45 percent but the overall engine-plus-inlet loss is only about 10 percent (FM p.1-13).
5. Corrections to received wisdom: the S1031 was a U-2R suit, not an SR-71 suit (the SR-71 wore the S901J, then the S1030, then the common S1031C, then the S1034); "NAS-14V2" and "R2-D2" for the astro-inertial navigation system were not found in any source examined; the "AG330" name for the start cart was not found in any primary source; the ASARS-1 pages of the flight manual (4-150 to 4-160) are deleted, so ASARS performance is undocumented in this pack.

## 0. Source keys

Flight manuals (both read in full for this pass, OCR plus page images):

- **[FM]** SR-71A-1 Flight Manual, USAF technical order, Issue E 31 Oct 1986, Change 2 31 Jul 1989. Internet Archive item `0003756-lockheed-sr-71-03`, https://archive.org/details/0003756-lockheed-sr-71-03 (three PDFs; part 01 is the local `model/plans/raw/fm-1SR71A-1_IssueE-Ch2_IA-part01.pdf`). Cited by printed page; "leaf N" is the IA page image `0003756-lockheed_sr71__0P_00NN.jp2` of part P. Covers Sections I to VII; the performance appendix is not in the item. Missing or deleted: pages 1-170 to 1-179 (canopies, windshield, map projectors, G-band beacon) are absent from the scan; pages 4-150 to 4-160 (ASARS-1) "DELETED IAW SR-71 Security Classification Guide 23 September 1996"; several DEF pages stamped "UNCONTROLLED COPY" with 1996 deletions; TEOC fields of view and OBC aperture blacked out. Rights tier A (USAF work; IA Public Domain Mark), scan uploaded anonymously.
- **[A12FM]** A-12 Utility Flight Manual, Lockheed for the CIA, 15 Sep 1965, changed 15 Mar and 15 Jun 1968, CIA document C01316457, https://www.cia.gov/readingroom/document/0001316457 (local `model/plans/raw/cia_C01316457_A-12-flight-manual_1968.pdf`). Cited by printed page and PDF page. Tier A with a note (Lockheed-prepared, released by CIA, no copyright notice).

Papers, museum records and other text sources (from the papers pass):

- **[M09]** Peter W. Merlin, "Design and Development of the Blackbird: Challenges and Lessons Learned", AIAA 2009-1522 (NASA Dryden historian, contractor). NTRS 20090007797. https://ntrs.nasa.gov/api/citations/20090007797/downloads/20090007797.pdf . PDF page = printed page. NTRS: PUBLIC_USE_PERMITTED. Figures credited Lockheed Martin = tier C; NASA-credited figures = A but AIAA paper, so link only.
- **[M12]** Merlin, "Mach 3 Legend: Design and Development of the Lockheed Blackbird", slides, 2012. NTRS 20120013451. https://ntrs.nasa.gov/api/citations/20120013451/downloads/20120013451.pdf . Slide numbers = PDF pages.
- **[SP4525]** Merlin, "Mach 3+: NASA/USAF YF-12 Flight Research, 1969-1979", NASA SP-2001-4525 (2002). https://www.nasa.gov/wp-content/uploads/2021/04/88796main_yf-12.pdf . Printed page = PDF page minus 7.
- **[FS030]** NASA Dryden Fact Sheet FS-2008-6-030-DFRC "SR-71 Blackbird". https://www.nasa.gov/wp-content/uploads/2021/09/495839main_fs-030_sr-71.pdf . PDF pages 3 and 4.
- **[TM104330]** Timothy R. Conners, "Predicted Performance of a Thrust-Enhanced SR-71 Aircraft with an External Payload", NASA TM-104330 (June 1997). https://ntrs.nasa.gov/api/citations/19970019923/downloads/19970019923.pdf . Printed page = PDF page minus 2. NTRS: GOV_PUBLIC_USE_PERMITTED, tier A.
- **[TP2000]** Corda, Moes, Mizukami et al., "The SR-71 Test Bed Aircraft: A Facility for High-Speed Flight Research", NASA/TP-2000-209023 (June 2000). https://ntrs.nasa.gov/api/citations/20000064011/downloads/20000064011.pdf . Printed page = PDF page minus 4. Tier A.
- **[LASRE]** Corda, Neal, Moes et al., "Flight Testing the Linear Aerospike SR-71 Experiment (LASRE)", NASA/TM-1998-206567. https://ntrs.nasa.gov/api/citations/19980223961/downloads/19980223961.pdf . Tier A.
- **[TMX56039]** James A. Albers, "Status of the NASA YF-12 Propulsion Research Program", NASA TM X-56039 (March 1976). https://ntrs.nasa.gov/api/citations/19760012064/downloads/19760012064.pdf . Printed page = PDF page minus 5. Tier A.
- **[SCAR]** James A. Albers and Frank V. Olinger, "YF-12 Propulsion Research Program and Results", Proceedings of the SCAR Conference Part 1, NASA CP-001 (1976). NTRS 19770011073. https://ntrs.nasa.gov/api/citations/19770011073/downloads/19770011073.pdf . Printed page = PDF page plus 416 (PDF p4 = p.420). Tier A.
- **[CP2054]** "YF-12 Experiments Symposium, Volume 1", NASA CP-2054 (1978). https://ntrs.nasa.gov/api/citations/19780024112/downloads/19780024112.pdf (127 MB). Kock overview p.3 to 24 (PDF p31 = printed p24); Cole, Neiner and Dustin p.157 ff. Most propulsion papers are "summary only, complete text in volume 3 (Secret)". Tier A.
- **[TM104317]** Jerald M. Jenkins and Robert D. Quinn, "A Historical Perspective of the YF-12A Thermal Loads and Structures Program", NASA TM-104317 (May 1996). Local copy model/plans/raw/ntrs-19960027893_*. https://ntrs.nasa.gov/api/citations/19960027893/downloads/19960027893.pdf . Printed page = PDF page minus 4. Tier A.
- **[TMX2880]** Wilson, Cazier and Larson, "Results of Ground Vibration Tests on a YF-12 Airplane", NASA TM X-2880 (1973). Local copy model/plans/raw/ntrs-19730021212_*. Printed page = PDF page minus 2. Tier A.
- **[TMX3144]** Dustin, Cole and Neiner, NASA TM X-3144 (1974). Local excerpt model/plans/raw/ntrs-19750003899_*. Tier A.
- **[BUR98]** Burcham, Ray and Conners, "Propulsion Flight Research at NASA Dryden From 1967 to 1997", NASA/TP-1998-206554. https://ntrs.nasa.gov/api/citations/19980218800/downloads/19980218800.pdf . Tier A.
- **[KLO11]** Kloesel, Ratnayake and Clark (NASA Dryden), "A Technology Pathway for Airbreathing, Combined-Cycle, Horizontal Space Launch Through SR-71 Based Trajectory Modeling", AIAA paper 2011. NTRS 20110013567. https://ntrs.nasa.gov/api/citations/20110013567/downloads/20110013567.pdf . p.9 of 19. AIAA paper: cite, link only for figures.
- **[EMIS]** J. D. Holdeman, "Gaseous Exhaust Emissions from a J-58 Engine at Simulated Supersonic Flight Conditions", NASA TM X-71532 (1974). NTRS 19740015227. https://ntrs.nasa.gov/api/citations/19740015227/downloads/19740015227.pdf . Tier A.
- **[ARCH]** David Robarge, "Archangel: CIA's Supersonic A-12 Reconnaissance Aircraft", 2nd ed., CIA. https://www.cia.gov/resources/csi/static/b45f5f8f5e4937963d9e9931313d84a4/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf . Printed page = PDF page minus 10. US government work.
- **[OXC]** Thomas P. McIninch, "The Oxcart Story", CIA. https://www.cia.gov/resources/csi/static/The-Oxcart-Story.pdf . Cited by PDF page.
- **[KJ81]** Clarence L. Johnson, "Development of the Lockheed SR-71 Blackbird" (typescript, 29 July 1981), with attached paper by William R. Brown (Pratt & Whitney), "J58/SR-71 Propulsion Integration, or the Great Adventure into the Technical Unknown" (AIAA, 13 May 1981). CIA release CIA-RDP90B00170R000100080001-5, Internet Archive https://archive.org/details/cia-readingroom-document-cia-rdp90b00170r000100080001-5 . Cited by Johnson's typed page and PDF page; Brown cited as **[BROWN]** with his own page number (Brown p.1 = PDF p22, so PDF page = Brown page plus 21). Lockheed and Pratt & Whitney authorship: facts citable, figures tier C.
- **[CIA67]** CIA memorandum, "Comparison of the Capabilities, Performance, Countermeasures Systems and Operational Status of the A-12 and SR-71", May 1967, CIA-RDP69B00369R000200240001-7. https://archive.org/details/cia-readingroom-document-cia-rdp69b00369r000200240001-7 . Pages 1 to 3.
- **[NRO67]** NRO memorandum (DNRO to Nitze, Helms, Hornig), "SR-71/A-12 Comparison", 23 September 1967, CIA-RDP74B00283R000100090012-2. https://archive.org/details/cia-readingroom-document-cia-rdp74b00283r000100090012-2 .
- **[NASM-J58]** Smithsonian NASM object A19920006000, "Pratt & Whitney J58 (JT11D-20) Turbojet Engine". https://airandspace.si.edu/collection-objects/pratt-whitney-j58-jt11d-20-turbojet-engine/nasm_A19920006000 (fetched 4 Oct 2026). Text: "Usage conditions apply".
- **[NASM-SR71]** Smithsonian NASM object A19920072000, SR-71A 61-7972. https://airandspace.si.edu/collection-objects/lockheed-sr-71-blackbird/nasm_A19920072000 .
- **[NMUSAF-SR71]** NMUSAF fact sheet "Lockheed SR-71A" (61-7976), Wayback http://web.archive.org/web/20241130031508/https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/198054/lockheed-sr-71a/ (live site blocks scripts).
- **[NMUSAF-J58]** NMUSAF fact sheet "Pratt & Whitney J58 Turbojet", Wayback http://web.archive.org/web/20230827143917/https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/195665/pratt-whitney-j58-turbojet/ .
- **[PW]** Pratt & Whitney "Classic Engines: J58 Engine" web page, Wayback http://web.archive.org/web/20160304123032/http://www.pw.utc.com/J58_Engine . Copyrighted page, facts only.
- **[DFA]** Dennis R. Jenkins, "Dressing for Altitude: U.S. Aviation Pressure Suits, Wiley Post to Space Shuttle", NASA/SP-2011-595. https://ntrs.nasa.gov/api/citations/20120014266/downloads/20120014266.pdf . Printed page = PDF page minus 3. Text NASA (PUBLIC_USE_PERMITTED); most suit images "Courtesy of the David Clark Company" = tier C.
- **[CRC560]** Coordinating Research Council, "Aviation Fuel Lubricity Evaluation", CRC Report 560 (July 1988), DTIC ADA198197, https://archive.org/details/DTIC_ADA198197 , Appendix A sec. 1.2.
- **[FDS74]** "A Fuel Data Standardization Study for JP-4, JP-5, JP-7, and RJ-5 Combusted in Air" (1974), DTIC AD0783308, https://archive.org/details/DTIC_AD0783308 , Table II.
- **[EIS90]** "Deactivation of the SR-71 Program at Beale Air Force Base, California" (USAF environmental assessment, Oct 1990), DTIC ADA270896, https://archive.org/details/DTIC_ADA270896 .

## 1. Cockpits

### 1.0 Sources used in this section

- **SR-71A-1 flight manual** (USAF T.O. SR-71A-1, Issue E 31 Oct 1986, Change 2 31 Jul 1989), Internet Archive item `0003756-lockheed-sr-71-03` (https://archive.org/details/0003756-lockheed-sr-71-03). Cited below as "FM" with the printed page number. The IA item is three PDFs; "IA part 01 leaf 39" means JP2 `0003756-lockheed_sr71__01_0039.jp2` (4167 x 5834 px). Pages 1-170 to 1-179 (canopies, windshield, map projector, G-band beacon) are missing from the scan; the SR-71B subsection (p.1A-20) briefly covers canopies and periscopes. Pages 4-150 to 4-160 (ASARS-1) were removed "IAW SR-71 Security Classification Guide 23 September 1996".
- **A-12 Utility Flight Manual** (Lockheed for the CIA, 15 Sep 1965, changed to 15 Jun 1968), CIA FOIA document C01316457 (https://www.cia.gov/readingroom/document/0001316457; local copy `model/plans/raw/cia_C01316457_A-12-flight-manual_1968.pdf`). Cited as "A-12 FM" with manual page and PDF page.

### 1.1 Front (pilot) cockpit, SR-71A

**Best diagrams (tier A):** FM Figure 1-12 Center Instrument Panel (p.1-23), Figure 1-13 Instrument Side Panels (p.1-24), Figure 1-14 Left Console (p.1-25), Figure 1-15 Right Console (p.1-26), Figure 1-16 Annunciator Panel (p.1-27), Figure 1-6 Throttle Quadrant (p.1-10), Figure 1-49 Control Stick Grip (p.1-95). Files: `media/diagram_SR-71A-1_fig1-12_*` to `fig1-16_*`, `fig1-6_*`, `fig1-49_*`. All are keyed line drawings; positions below are read from the drawings (left/right as the pilot sees them).

**Center instrument panel, FM Figure 1-12, p.1-23 (keyed 1 to 50).**

| Zone | Items (key number: name) |
|---|---|
| Glareshield and top row | 16 angle of attack indicator (top, left of centre); 17 standby attitude indicator (3-inch, top centre; inset shows the 2-inch unit used without S/B R-2466); 18 shaker indicator light; 19 attitude director indicator (ADI, the large instrument at the centre of the panel); 20 marker beacon light; 21 master caution and warning lights (push to reset, top right of centre); 22 elapsed time clock (upper right); 23 standby compass (mounted in the canopy) |
| Upper left (slanted) | 12 nosewheel steering engaged light; 13 KEAS warning light; 14 air refuel switch; 15 air refuel ready / disconnect pushbutton and light |
| Left column | 6 temperature indicator (far left edge); 7 RSO ejected indicator light; 8 drag chute handle (T-handle, upper left: pull to deploy, rotate left and pull for emergency); 9 left inlet unstart light; 10 compressor inlet temperature (CIT) gauge; 11 airspeed-Mach meter (left of the ADI); 4 compressor inlet pressure (CIP) gauge; 5 RSO bailout switch; 2 pusher/shaker (APW) switch |
| Inlet group (lower left) | 1 spike position indicator (dual pointer, 0 to 26 in aft); 3 forward bypass position indicator (dual, percent open); 49 spike switches (L and R rotary knobs, AUTO, FWD and a manual Mach scale 1.4 to 3.2); 46 forward bypass switches (L and R rotary knobs, AUTO, OPEN and manual schedule); 50 inlet restart switches (L and R toggles, bottom left corner) |
| Trim row (bottom) | 48 pitch trim indicator; 47 roll trim indicator; 45 yaw trim indicator |
| Centre column | 43 triple display indicator (TDI, digital KEAS, altitude and Mach, left of the HSI); 44 accelerometer; 42 horizontal situation indicator (HSI, below the ADI); 41 nav map display (projector screen, bottom centre) |
| Right of centre | 24 altimeter (right of the ADI); 25 inertial-lead vertical speed indicator (right of the HSI); 32 display mode select switch (ANS, INS, TACAN/ADF, ILS, approach); 40 bearing select switch; 39 attitude reference select switch (ANS or INS); 36 TACAN control transfer switch; 37 L and R hydraulic systems pressure gauge (inlet "SPIKE" systems); 38 A and B hydraulic systems pressure gauge (flight control "SURF CONT" systems) |
| Engine column (right) | 26 right inlet unstart light; 27 tachometers (pair, top); 28 fire warning lights; 29 exhaust gas temperature indicators (pair, digital); 30 fuel derich lights; 31 exhaust nozzle position indicators (pair, 0 to 10); 33 IGV lights; 34 fuel flow indicators (pair); 35 oil pressure indicators (pair, bottom right) |

Instrument facts from the manual text:
- TDI: digital KEAS, pressure altitude and Mach computed by DAFICS; altitude 0 to 99,950 ft, dropping the first digit above 100,000 ft (maximum DAFICS signal 109,950 ft); Mach 0 to 3.99 (signal limit Mach 3.5); KEAS 0 to 599 (signal limit 560). One TDI in each cockpit. FM p.1-135 to 1-136 (IA part 01 leaf 157).
- Spike position indicator marked in one-inch increments from 0 (forward) to 26 (full aft). Spike knobs graduated in Mach from 1.4 to 3.2. FM p.1-43 (leaf 60).
- CIP gauge has L and R needles plus a striped "expected normal CIP" needle driven by DAFICS; L and R should not differ by more than 1 psi. FM p.1-17 (leaf 33).
- EGT gauges are digital, 0 to 1198 C, with a red jewel light at 860 C; HOT and COLD flags. FM p.1-14 (leaf 30).
- Tachometers: main dial to 10,000 rpm plus a 1000 rpm subdial; self-energised. FM p.1-9 (leaf 25).
- Fuel flow indicators: dial in 5000 pph steps to 95,000 pph with a five-digit window. FM p.1-11 (leaf 27).
- Exhaust nozzle position indicators: 0 (closed) to 10 (open). FM p.1-19 (leaf 35).
- Peripheral Vision Display (PVD): a laser-generated thin red line parallel to the horizon projected across the pilot's instrument panel (masked off the ADI), driven by ANS or INS attitude. FM p.1-138 (leaf 160).

**Instrument side panels, FM Figure 1-13, p.1-24 (keyed 1 to 40).** Left side panel (left of the main panel): 1 manifold temperature switch; 2 landing and taxi light switch; 3 suit heat rheostat; 4 wet-dry (antiskid) switch; 5 face heat rheostat; 6 cockpit temperature control; 7 cockpit temperature control and override; 8 temperature indicator selector; 9 L and R refrigeration switches; 10 defog switch; 31 brake switch; 32 indicators and light test switch; 33 fuel derichment switch; 34 gear signal release switch; 35 landing gear lever (wheel-shaped handle); 36 landing gear indicator lights; 37 liquid oxygen quantity indicator; 38 bay air switch; 39 cockpit pressure dump switch; 40 cabin altitude indicator. Right side panel: 11 fuel quantity indicator (pounds x 1000 with digital total); 12 centre of gravity indicator (percent MAC); 13 fuel crossfeed switch; 14 system 3 nitrogen quantity indicator; 15 liquid nitrogen quantity indicator (systems 1 and 2); 16 fuel forward transfer switch; 17 emergency fuel shutoff switches; 18 emergency AC bus switch; 19 battery switch; 20 fuel dump switch; 21 instrument inverter switch; 22 generator bus tie switch; 23 L and R generator switches; 24 fuel boost pump switches (a vertical column, one per tank); 25 pump release switch; 26 fuel boost pump light test switch; 27 fuel quantity indicator selector switch; 28 manual fuel aft transfer switch; 29 igniter purge switch; 30 fuel tank pressure indicator.

**Left console, FM Figure 1-14, p.1-25 (keyed 1 to 30).** Throttle quadrant (forward): 1 roll trim switch and 2 right-hand rudder synchronizer switch (on a panel above the quadrant); 3 throttle friction lever; 4 throttle inlet control restart switch; 5 microphone switch; 6 throttles; 7 TEB counters (one aft of each throttle). Outboard, forward of the quadrant: 30 map projector control panel; 27 inlet aft bypass position lights; 28 inlet aft bypass position switches (CLOSE, A 15 percent, B 50 percent, OPEN; FM p.1-44); 29 EGT trim switches. Outboard strip: lighting controls 18 to 26 (LOX quantity switch, floodlights, console lights, thunderstorm lights, instrument lights, ADI light, tail lights, fuselage-tail intensity, anticollision). Console stack (front to back): 8 oxygen systems control panel; 10 UHF-1 radio control panel; 11 standby oxygen system control panel; 12 circuit breaker panel; then 16 throttle restart cutout switch and 17 fuel derich test switch on a small aft panel; 9 canopy jettison handle on the inboard wall; 13 spotlight; 14 relief pack box; 15 storage.

**Right console, FM Figure 1-15, p.1-26 (keyed 1 to 16).** Front to back: 1 autopilot OFF light switch; 15 SAS and autopilot control panel (pitch, roll and yaw SAS channel switches with A, B and M sensor and servo lights; autopilot pitch, roll, Mach hold, KEAS hold, auto nav, heading hold); 14 TACAN control panel; 13 interphone control panel; 12 IGV lockout and cabin pressure select panel (10,000 ft or 26,000 ft schedule); 11 VHF; 10 circuit breaker panel. Outboard: 2 DAFICS preflight BIT panel; 4 PVD control panel; 6 ILS control panel; 7 safety pins; 3 canopy seal pressure valve and 5 canopy latch handle (both on the sill); 8 spotlight; 9 water and chart holder; 16 map storage.

**Throttles (FM p.1-9 and Figure 1-6).** Two levers on the left console: the right throttle drives the right engine main fuel control, the left throttle the left engine afterburner fuel control, the two linked by a closed-loop cable. Positions OFF, IDLE, an unlabeled Military stop, and AFTERBURNER to the forward stop. TEB counters are set to 16 before engine start and count down each time a throttle goes OFF to IDLE or Military to afterburner. (A-12: counters set to 12, A-12 FM p.1-17, PDF p.29.)

**Control stick and pedals (FM p.1-94 to 1-96).** Conventional stick, about 9 deg forward and 16 deg aft of neutral, about 8 to 9 deg laterally; full lateral throw needs about 10 lb. Stick shaker is a 30 cps vibration (FM p.1-127). Rudder pedals adjusted by a PEDAL ADJ T-handle at the bottom of the annunciator panel.

### 1.2 Rear (reconnaissance systems officer) cockpit, SR-71A

**Best diagrams (tier A):** FM Figure 1-17 Instrument Panel, Aft Cockpit (p.1-28); Figure 1-18 Left Console (p.1-29); Figure 1-19 Right Console (p.1-30); Figure 4-3 Navigation Control and Display Panel (p.4-7); Figure 4-25 Power and Sensor Control Panel (p.4-81); Figure 4-33 Optical Viewsight Control Panel (p.4-108); Figure 4-36 DEF Control Panel (p.4-120). The manual index also lists aft instrument panel figures on p.1-28A and 1-28B (other service-bulletin configurations); those pages are not in this scan.

**Aft instrument panel, FM Figure 1-17, p.1-28 (keyed 1 to 36).** The RSO has no flight controls (the SR-71B instructor cockpit does; see 1.3).

| Zone | Items |
|---|---|
| Centre column, top to bottom | 13 viewsight (9-inch optical display at the top of the panel); 14 radar display (RCD screen); 30 viewsight control panel (horizontal strip); 31 map / data projector (bottom centre); 32 RCD film remaining panel (left of the projector); 28 RCD control panel (right) |
| Left wing panel | 1 cabin pressure switch; 2 UHF control transfer button; 3 face heat rheostat; 4 camera exposure / sun angle selector; 5 attitude reference select switch; 6 UHF frequency indicator; 7 annunciator panel; 8 V/H indicator; 9 camera point angle indicator; 10 forward transfer light (with S/B R-2691); 11 liquid oxygen quantity indicator; 12 centre of gravity indicator; 33 egress lights (along the lower edge) |
| Right wing panel | 15 DEF warning light; 16 RSO master caution light; 17 UHF distance indicator; 18 bearing distance heading indicator (BDHI); 19 pilot's caution light; 20 IFF caution light; 21 triple display indicator; 22 attitude indicator; 23 fuel quantity indicator selector switch; 24 fuel quantity indicator; 25 BDHI heading select switch; 26 BDHI No. 1 needle select switch; 27 elapsed time clock |
| Lower panels | 29 map and pencil boxes (both sides); 34 G-band beacon control panel; 35 TACAN control panel and transfer switch; 36 IFF control panel (lower left) |

**Left console, aft, FM Figure 1-18, p.1-29 (keyed 1 to 14).** 1 oxygen system control panel; 2 UHF modem control panel; 3 DEF control panel (large panel with system select, mode switches and GO/FAIL projection displays); 4 inertial control panel (ICP, for the SKN-2417 INS); 5 canopy jettison handle; 6 UHF-2 radio control panel; 7 INS segment (display) lights control panel; 8 chart storage box; 9 relief pack box; 10 lighting control panel; 11 spotlight; 12 HF radio control panel; 13 interphone control panel; 14 cockpit air shut-off control (emergency, on the side wall).

**Right console, aft, FM Figure 1-19, p.1-30 (keyed 1 to 13).** 5 radar control panel (front); 7 astroinertial navigation control panel (the ANS navigation control and display panel, NCDP); 9 mission equipment power and sensor control panel; 12 circuit breaker panel; 1 water bottle box; 2 safety pins; 3 dinghy stabber; 4 and 13 chart storage boxes; 6 canopy seal pressure valve and 8 canopy latch handle (sill); 10 storage box; 11 spotlight.

### 1.3 SR-71B trainer cockpits

FM Section IA. Figure 1A-1 Instrument Panel, Forward Cockpit (p.1A-4); Figure 1A-3 Instrument Panel, Aft Cockpit (p.1A-6, keyed 1 to 74). The SR-71B's raised second cockpit is an instructor station with a full set of flight, engine, inlet and fuel instruments (ADI 26, HSI 24, TDI 63, spike position 5, forward bypass position 71, spike and forward bypass switches 67 and 70, restart switches 72, tachometers 39, EGT 41, nozzle position 44, fuel quantity and CG 57 and 58, fuel boost pump switches 45, a navigation map projector 60) in place of the RSO's sensor displays. Rights tier A. Files `diagram_SR-71A-1_fig1A-1_*` and `fig1A-3_*`.

### 1.4 Triple display indicator

See 1.1. One in each cockpit (forward Figure 1-12 item 43; aft Figure 1-17 item 21). Three digital windows: KEAS, ALTITUDE-FT, MACH. FM p.1-135 to 1-136. The A-12 also had one (A-12 FM Figure 1-2 item 22).

### 1.5 Astro-inertial navigation system (ANS)

- **What it is.** "The ANS is an inertial navigation system employing a star tracker to eliminate gyro drift and to limit position error." It steers the autopilot, feeds attitude, heading and position to both cockpits, and can command the CAPRE side-looking radar and the technical objective cameras. FM p.4-3 (IA part 02 leaf 225).
- **Star tracker.** A 61-star catalogue is stored in the ANS computer; sun, moon and planets are not used; at least two different stars must be tracked for best performance. FM p.4-3. Stars are normally tracked by day as well as night.
- **Location and field of view.** The guidance group (inertial platform, star-tracking telescope, digital computer) is mounted in the fuselage aft of the rear cockpit and has an upward 78-degree cone of vision for the star-tracking telescope, axis vertical when the aircraft pitch angle is 7.5 deg. Software corrects star sightings for refraction by the shock wave over the window and for thermal lens effects in the window. FM p.4-5 to 4-6 (part 02 leaves 227 to 228). The bay locator (FM Figure 1-1, item 15 "ANS platform and computer") shows its position.
- **Modes and accuracy.** Astro-inertial, inertial-only, airstart (airspeed-damped astro-inertial) and dead reckoning. Rapid and gyrocompass alignments take 18 and 36 minutes. FM p.4-3 and Figure 4-2 (p.4-6), which gives probable radial errors (CEP): astro-inertial 0.3 nmi for up to 10 hours after a rapid or gyrocompass alignment and 1.0 nmi after a ground hot start; inertial-only 2 nmi/hr (5.0 nmi/hr after a hot start); dead reckoning 55 nmi/hr. Fixpoint weighting: 0.05 nm for ASARS, 0.5 nm for viewsight, 1.0 nm for TACAN (FM p.4-177, Tape 13 section, part 03 leaf 141).
- **Display and control.** The Navigation Control and Display Panel (NCDP) on the aft right console: present latitude and longitude windows, time-to-turn, range to destination, six SELECTED DATA windows, sensor and temperature lights, a MAL (malfunction) light, a star ON light (steady when at least two different stars have been tracked in the last 5 minutes), a 7-position MODE switch (OFF, WARM UP, ALIGN, ASTRO INERTIAL, INERTIAL ONLY, DEAD RECKON, AIRSTART), an 8-position DATA switch and a numeric keyboard. FM p.4-7 to 4-12, Figure 4-3. File `diagram_SR-71A-1_fig4-3_ANS-navigation-control-and-display-panel_p4-7.jpg`; system diagram Figure 4-1 (p.4-4).
- **Mission tape.** Up to 256 destination points, 256 fix points and 1023 control points (1535 total) plus a 40-point modification list. FM Tape 13 section (part 03 leaf 141). A portable chronometer in the aft cockpit supplies GMT to 0.01 s. FM p.4-5.
- **"NAS-14V2" and "R2-D2".** The flight manual calls it only "ANS" or "astroinertial navigation system" and gives no model number or nickname. The designation and nickname must come from other sources; see section 3.10.

### 1.6 Viewsight and periscopes

- **SR-71A optical viewsight (RSO).** Without S/B R-2538 the aft cockpit has "a 9-inch diameter optical display at the top of the instrument panel", a downward-looking ground viewing instrument for visual fixes, V/H measurement and manual camera operation. Wide field 136 deg (6:1 demagnification, about 149 ft on-axis resolution at nadir at cruise altitude), narrow field 56 deg (2:1, about 46 ft); display centred about 14.5 deg forward of nadir; unstabilised. FM p.4-105 (part 03 leaf 79). A video viewsight replaced it with S/B R-2538 (FM p.4-111 onward). Figures 4-32 (displays, p.4-107) and 4-33 (control panel, p.4-108).
- **SR-71 rear view periscopes.** "A rear view periscope is installed on each canopy. The field of view of the front periscope is partially blocked by the aft cockpit." FM SR-71B subsection p.1A-20 (part 01 leaf 241); the main section page (1-175) is missing from the scan.
- **A-12 downward periscope.** The single-seat A-12 had a periscope viewing system with a presentation screen in the centre of the instrument panel (A-12 FM Figure 1-2 item 14): a downward-looking optical system with a wide field covering about 85 deg forward of nadir and a narrow field about 47 deg forward of nadir, used for INS fixes; it doubled as a sun/sky compass and a 35 mm map projector screen. A-12 FM Section IV, PDF p.245 to 248 (printed page numbers not legible), Figure 4-14 (PDF p.246) and Figure 4-15 forward look range (PDF p.248). File `diagram_A-12-FM_fig4-14_A-12-periscope-viewing-system_pdf-p246.png`.
- **A-12 rear view periscope.** Manually extended from the top of the canopy; instantaneous cone of view about 10 deg, about 30 deg with head movement, rotatable 10 deg either side of the aft centreline, demagnification 1 to 0.5. A-12 FM p.1-88 to 1-89 (PDF p.100 to 101).

### 1.7 Ejection seats

- **SR-71: Lockheed SR-1 stabilized ejection seat**, rocket-propelled, upward-ejecting, "usable from zero speed and altitude to the extremities of the flight envelope". FM p.1-199 (part 01 leaf 211). Diagram FM Figure 1-83 (p.1-202) and trajectories Figure 1-85 (p.1-205).
- Sequence (D-ring, primary): canopy jettison first, then catapult through a 0.3 s delay initiator; rocket motor ignites as the seat clears the sills; drogue gun fires 0.2 s after the catapult and deploys a 6.5 ft drogue from the headrest; lower bridle lines cut 10 s later so the seat descends upright; dual aneroids hold man-seat separation until 15,000 ft; a rotary actuator ("butt-snapper") slings the crewmember out; a 35 ft main parachute deploys automatically. The T-handle (secondary) fires the catapult immediately and does not jettison the canopy. FM p.1-201 to 1-203.
- Seat vertical travel 9 in (pilot) and 6.75 in (RSO). FM p.1-199.
- Survival kit (hard-shell seat pack) with two 45 cu in emergency oxygen bottles at 2000 psi each per crewmember, about 15 minutes duration. FM p.1-195 to 1-197, Figure 1-84 (p.1-204).
- **A-12 seat.** Upward catapult plus rocket, minimum-risk ground-level ejection when airspeed is at least 65 KIAS (so not zero-zero), speed sensor selects one of two separation delays, foot spurs and knee guards. A-12 FM p.1-89 to 1-92 (PDF p.101 to 104), Figure 1-37 (PDF p.102). Parachute 35 ft canopy with drogue above 17,000 ft (A-12 FM PDF p.97).

### 1.8 Canopies and windshield

- SR-71: "The canopy shall be opened or closed only when the aircraft is stationary. Maximum taxi speed with a canopy open is 40 knots." FM p.5-17. CANOPY UNSAFE light in both cockpits (FM p.1A-20). Canopy seals pressurized by regulated bleed air (FM p.1-186). Ground crash rescue: an external jettison handle with about 6 ft of cable; the pilot's canopy jettisons immediately and the RSO's after a one second delay (FM crash rescue procedures figure, p.3-139). Canopy description pages 1-175 onward are missing from this scan.
- Cockpit glass reached 420 F outside while crew air was fed at minus 40 F (Merlin, fact_notes.md alternates).
- A-12: canopy of "two high temperature resistant glass windows secured within a reinforced titanium frame" hinged at the aft end, opened manually with a nitrogen-boost counterbalance, four-hook latch, inflatable rubber seal; windshield two glass assemblies in a V-shaped titanium frame with magnesium fluoride anti-reflective coating. A-12 FM p.1-85 to 1-88 (PDF p.97 to 100), Figure 1-36 (PDF p.98).

### 1.9 A-12 cockpit

**A-12 FM Figure 1-2, Instrument Panel (p.1-3, PDF p.15), keyed 1 to 75 (tier A).** Single seat. The periscope viewing screen (14) dominates the top centre of the panel, ringed by flight instruments (10 attitude indicator, 13 altimeter, 12 master caution, 11 de-icing warning light, 15 a light whose name is redacted, 16 compressor inlet static pressure gauge, 18 vertical speed, 19 CIT gauge, 20 elapsed time clock, 21 fire warning lights, 22 triple display indicator). Left side: 1 air conditioning control panel, 2 airspeed-Mach meter, 3 BDHI, 4 AN/ARC-50 range indicator, 5 INS distance-to-go / ground speed indicator, 6 to 9 windshield de-icer, rain removal, drag chute handle, air refuel ready-disconnect; 71 left forward panel, 72 to 75 landing and taxi light, alternate steer and brake, gear warning cutout, pitch-roll-yaw trim indicators. Right side engine and fuel column: 24 tachometers, 25 EGT, 26 exhaust nozzle position, 27 fuel tank switches, 28 fuel forward transfer, 29 quad hydraulic quantity, 30 air refuel switch, 31 liquid nitrogen quantity, 32 fuel tank pressure, 33 right forward panel, 34 fuel dump, 35 pump release, 36 fuel quantity, 37 ILS panel, 38 test N2 and tank light switch, 39 fuel flow, 41 oil pressure, 43 and 44 hydraulic pressure gauges. Lower centre: inlet group 40 forward bypass position indicator, 42 spike position indicator, 62 emergency spike switch, 64 spike and bypass control panel, 66 restart switches, 67 fuel derichment arming switch, 68 periscope control panel, 69 EGT trim switches; 49 annunciator panels, 52 landing gear release handle, 53 lower circuit breaker panel, 54 rudder pedal adjust handle, 55 nose air off handle, 56 to 61 trim power, hydraulic reserve oil, pitot heat, surface limiter handle, INS destination and select panel, course indicator, 63 turn and slip, 65 standby attitude indicator. Changed 15 March 1968.
- **A-12 FM Figure 1-3, Cockpit Left Side (PDF p.16)** and **Figure 1-4, Cockpit Right Side (PDF p.17)**: callout-labelled (not numbered). Left: throttle quadrant, aft bypass switches and indicator lights, rudder synchronizer and roll trim switches, oxygen panel, canopy jettison handle, UHF command radio and translator panels, Q-bay equipment panel (not shown), suit ventilation boost lever, HF, IFF/SIF, lighting. Right: SAS control panel, autopilot panel and selector, INS control panel, TACAN, ADF, FRS (flight reference system) panel, pitot pressure selector, nose hatch and canopy seal levers, flight recorder switch, face plate heat switch.
- **A-12 annunciator panels**, Figure 1-28 (p.1-65, PDF p.77).
- No free photograph of the A-12 cockpit was found (see 1.10).

### 1.10 Cockpit photographs

No NASA cockpit interior photograph of NASA 831 or 844 was found in images.nasa.gov or in any of the 67 SR-71 and 10 YF-12 caption pages of the old Dryden gallery (Wayback). The Smithsonian's 11 CC0 images of 61-7972 are all exteriors; its cockpit panorama (https://airandspace.si.edu/multimedia-gallery/panorama/10117pjpg) has no stated rights (tier C, link only). No free A-12 cockpit photograph was found (Commons, CIA, Library of Congress).

| Subject | Best image | Tier | Notes |
|---|---|---|---|
| Front cockpit, whole panel | `photo_front-cockpit-panel_NMUSAF-Cockpit360_61-7976.jpg` | A (caveat) | NMUSAF Cockpit360 forward cube face of SR-71A 61-7976, 2304 px, rebuilt from 24 of 25 Wayback tiles (one dark roof tile filled black). Rectilinear, so it can be keyed directly against FM Figures 1-12 and 1-13: every zone in the table in 1.1 is visible, including the drag chute handle, RSO EJECTED light, TDI, spike and bypass knobs, engine column, fuel quantity and CG gauges. |
| Front cockpit consoles | `photo_front-cockpit-left-console_NMUSAF-Cockpit360_61-7976.jpg`, `..._right-console_...` | A (caveat) | Commons stills from the same tour, some perspective stretch. |
| Front cockpit, other | `photo_front-cockpit_61-7975_March-Field_Alan-Wilson.jpg`; `photo_front-cockpit-stick-seat_Bill-Abbott.jpg` (61-7960, Castle) | B | CC BY-SA 2.0. |
| Rear cockpit panel | `photo_rear-cockpit-RSO-panel_NMUSAF-Cockpit360_61-7976.jpg` | A (caveat) | Central 1536 px crop (only the central 3 x 3 tiles survive). Shows the large display (FM Figure 1-17 item 14) with the viewsight controls above, TDI (21), fuel quantity (24), LOX (11), camera point angle (9), camera exposure selector (4), UHF frequency (6), PILOT EJECTED and BAILOUT lights, RCD film remaining (32), and the SLR and present latitude/longitude panels on the right console. |
| Rear cockpit, other | `photo_rear-cockpit-RSO_Bill-Abbott.jpg`; `photo_rear-cockpit_61-7975_March-Field_Alan-Wilson.jpg` | B | |
| ANS unit | `photo_ANS-astro-inertial-navigation-unit_Evergreen_Daderot.jpg` | A (CC0) | Display unit at Evergreen with star-tracker window on top; label transcribed in 3.10. No photo of it installed behind the RSO. |
| Ejection seat and canopy | `photo_ejection-seat-open-canopy_Bill-Abbott.jpg` | B | Castle Air Museum 61-7960. |
| Both canopies from a tanker | `photo_cockpits-from-tanker_NASA-831_EC94-42883-1.jpg` | A | SR-71B NASA 831, raised instructor cockpit visible. |
| Crew in cockpits, suited | `photo_crew-in-cockpit-pressure-suits_Beale_DVIC.jpg` | B (probably A upstream) | |
| Periscope, viewsight close-up | none found | | Gap. |

Tier C, link only: Brian Shul's in-cockpit self-portraits (tagged PD on Commons, but from his own book *The Untouchables*); Joe McNally's Library of Congress set ("Publication may be restricted"); sr-71.org, habu.org and sr71.us galleries (tier D).

## 2. Engine and inlet

### 2.1 Pratt and Whitney J58 (JT11D-20): numbers

| Item | Value | Applies to | Source, page | Disagreements and notes |
|---|---|---|---|---|
| Designation | JT11D-20 (company) = J58 (military) | SR-71 | [FM] p.1-4 | A-12: JT11D-20A ([A12FM] p.1-7, PDF p.19). Smithsonian label for 61-7972's engines: "JT11D-20B" ([NASM-SR71]). Late engines "K-engine" ([SP4525] p.20 fn 25); an Evergreen display engine is labelled JT11D-20K (photo manifest). Merlin's "JTD-11B-20" is a typo. |
| Max afterburning thrust, uninstalled, sea level static, standard day | **34,000 lbf** | SR-71A (K-engine) | [FM] p.1-7 | Also [TM104330] p.4, [TP2000] p.8, [M09] p.24, NASA Dryden caption EC97-43933-1 ("rated at 34,000 pounds of thrust each"). |
| Same, early engine | 32,500 lbf | YF-12A and early SR-71 (J-engine, fixed IGVs) | [SP4525] p.20 footnote 25 | Quote: "The early type (referred to as the J-engine), also used in the YF-12A, incorporated fixed compressor inlet guide vanes and had a maximum afterburner thrust rating of 32,500 pounds at sea-level standard-day conditions." NASA [FS030] PDF p.3 and NMUSAF use 32,500. The K-engine was fitted to YF-12A 60-6935 on 18 Oct 1974 (fn 27). |
| Same, A-12 | 31,500 lbf ("interim maximum afterburning static thrust rating") | A-12 (JT11D-20A) | [A12FM] p.1-7 (PDF p.19) | |
| Thrust (other figures) | 30,000 lb; 32,000 lbf | J58 | [NASM-J58], [PW]; [KLO11] p.9 | 30,000 is the outlier against the manuals. |
| Military (max dry) thrust | about 70 percent of max at sea level static; about 28 percent of max at high altitude | SR-71A | [FM] p.1-8 | About 23,800 lb by arithmetic (not printed). FM Figure 1-4 charts it against airspeed and temperature. |
| Minimum afterburning thrust | about 85 percent of max (sea level), about 55 percent (high altitude) | SR-71A | [FM] p.1-7 to 1-8 | |
| Idle | 3975 rpm up to 60 C ambient | SR-71A | [FM] p.1-8 | Overspeed reporting above 7450 rpm (below 300 C CIT) or 7300 rpm (above) [FM] p.5-5. |
| Weight | about 6,000 lb | J58 | [NMUSAF-J58]; [KLO11] p.9 | [NASM-J58]: 6,500 lb (2,948 kg); its "Overall: 8690 lb" line probably includes the display stand. |
| Length x diameter | 180 x 50 in (457.2 x 127 cm) | J58 | [NASM-J58] | THIN: only source. Its "6 ft 8 in x 20 ft" overall line is probably the stand. The often-quoted 17 ft 10 in x 4 ft 9 in was not found in a primary source. |
| Airflow | not found | J58 | | THIN. No primary figure for lb/s in any source examined. Brown: above Mach 2 corrected airflow held constant regardless of throttle ([BROWN] p.2). |
| Compressor | single rotor, 9-stage axial, pressure ratio 8.8:1 | SR-71A | [FM] p.1-4 | 9 stages also [NMUSAF-J58], [M09] p.21, [SCAR] p.421, [TM104330] p.4; [NASM-J58] says 8-stage (outlier). FM Figure 1-2 labels a "forward compressor section (4 stages)". A-12 JT11D-20A: 8:1 ([A12FM] p.1-7). Kock: a modest ratio was chosen because the inlet does most of the compression at cruise ([CP2054] p.4). |
| Inlet guide vanes | two-position: axial for takeoff and acceleration; cambered at CIT 85 to 115 C (about Mach 1.9); cambered mandatory above CIT 125 C | SR-71A K-engine | [FM] p.1-19 to 1-21 | J-engine had fixed IGVs ([SP4525] fn 25). |
| Combustor | 8 cans, 48 dual-orifice fuel nozzles (6 per can) | SR-71A | [FM] p.1-11 | [SCAR] p.421; [TM104330] p.4. |
| Turbine | 2-stage | SR-71A | [FM] p.1-7 | |
| Bleed bypass | 4th-stage bleed through six bypass tubes into the afterburner inlet; transition scheduled on CIT and rpm, normally CIT 85 to 115 C, Mach 1.8 to 2.0 | SR-71A | [FM] p.1-4 to 1-7 | Disagreement: [TM104330] p.4 and [TP2000] p.8 say "above Mach 2.2"; the A-12's JT11D-20A switched at CIT 150 to 190 C, Mach 2.2 to 2.3 ([A12FM] p.1-7). The 1989 SR-71 manual's schedule (Mach 1.8 to 2.0) is used here; the reason for NASA's later figure is not established. FM Figure 1-2 counts 24 internal bleeds, 12 external bleeds and 6 bleed bypass tubes. Brown: the cycle gave "more than 20 percent additional thrust" at high Mach ([BROWN] p.2). |
| Afterburner | 4 spray bar rings, 4 flame holders, fully modulating, variable area nozzle with 4 actuators; pump driven by an air turbine on compressor discharge air | SR-71A | [FM] Figure 1-2 (p.1-6), p.1-12 to 1-19 | Afterburner lights in up to 3 s at sea level and 7 s at altitude [FM] p.1-8. |
| Design conditions | Mach 3.2 continuous, 100,000 ft, CIT 800 F, turbine inlet 2,000 F, military and afterburner both continuous | JT11D-20 | [BROWN] Fig. 1, p.2 | Afterburner gas 3,200 F ([BROWN] Fig. 2) or 3,400 F ([ARCH] p.14). |
| Max CIT | 427 C with both IGVs cambered | SR-71A | [FM] p.5-5 | Mach 3.3 allowed when authorised if 427 C is not exceeded [FM] p.5-8. |
| EGT | derich at 860 C; gauges read 0 to 1198 C | SR-71A | [FM] p.1-13 to 1-14 | Cruise EGT 775 to 805 C [FM] p.2-50. |
| Fuel hydraulics | engine fuel used as hydraulic fluid at up to 1800 psi, 50 gpm, for nozzle, IGVs, bleeds and TEB dump | SR-71A | [FM] p.1-21 | Johnson: fuel "used as hydraulic fluid at 600 F" ([KJ81] typed p.3). |
| Oil | 6.7 US gal tank, serviced to 5.15 gal, MIL-L-87100 (PWA 524) | SR-71A | [FM] p.1-21 | |
| TEB ignition | triethylborane, 600 cc (1-1/4 pint) nitrogen-pressurised tank per engine, at least 16 metered shots, cockpit counters start at 16 | SR-71A | [FM] p.1-9, 1-22 | A-12 counters set to 12 ([A12FM] p.1-17, PDF p.29). TEB "will burn spontaneously with exposure to air above -5 C" [FM] p.1-22. Brown wrote "tetraethyl borane" in error. |
| Fuel burn | 36,000 to 38,000 lb/h total at Mach 3.0 to 3.15, 100,000 lb, standard day | SR-71A | [M09] p.26 | YF-12: "over 11,000 pounds of fuel per hour" per engine ([SP4525] p.16); A-12: 22,000 lb/h at cruise ([ARCH] p.8). Conditions differ. |
| Thrust-to-weight | 5.2 (design objective) | JT11D-20 | [BROWN] Fig. 1 | [KLO11] 5.3. |
| Materials | Ti front compressor; Waspaloy, Inconel 718, Hastelloy X, Astroloy, IN-100 hot section | J58 | [M09] p.21 | |

**Starting: the "AG330" cart.** The flight manual: "An external starting unit is required for ground starts. This may be a compressed air supply, a self-contained gas engine cart, or a multiple air-turbine cart. The output drive gear of either cart connects to a starter gear on the main gearbox at the bottom of the engine. There are no aircraft controls for this system." [FM] p.1-22; same wording for the A-12 ([A12FM] PDF p.29). Kelly Johnson: over 600 hp was needed, so "we took two Buick racing car engines and developed a gear box to connect them both to the J-58 starter drive", used "for several years" until air start systems were built into hangars ([KJ81] typed p.9, PDF p.12). CIA: "two Buick (later, Chevrolet) racecar engines on a special cart... put out over 600 horsepower" ([ARCH] p.13). The Hill Aerospace Museum label (secondary, quoted on Commons) gives "two 425 cubic inch Buick Wildcat engines" bringing the J58 to 4500 rpm. **The designation "AG330" was not found in any primary source**; use it only as the museum and enthusiast name.

### 2.2 The inlet

The inlet is the same on the A-12, YF-12 and SR-71 apart from spike material and the later SR-71's RCS cone, so NASA's YF-12 inlet research applies directly.

| Item | Value | Source, page | Notes |
|---|---|---|---|
| Type | axisymmetric mixed-compression inlet with translating spike, forward and aft bypass, spike porous centerbody bleed and cowl shock trap | [FM] p.1-31; [SCAR] p.420 to 421 | Inlets canted inboard and downward to match the flow off the chines ([FM] p.1-31; [KJ81] typed p.7); angles in model/plans/NOTES.md. |
| Spike travel | about 26 in aft, starting at Mach 1.6, about 1-5/8 in per 0.1 Mach | [FM] p.1-31; indicator 0 to 26 in, p.1-43 | 25.3 in in CR-163106 (model/plans NOTES.md); "as much as 26 inches" for the A-12 ([ARCH] p.14 to 15); "almost three feet" ([KJ81] typed p.7, an overstatement). |
| Spike lock | locked forward on the ground and below 30,000 ft | [FM] p.1-31 | |
| Capture and throat | captured stream tube 8.7 sq ft at Mach 1.6 rising 112 percent to 18.5 sq ft; throat closes to 4.16 sq ft, 54 percent of its Mach 1.6 area | [FM] p.1-31 | Cowl lip radius 29.38 in ([TMX3144]). |
| Spike bias | forward with load factor (3.12 in per negative g, 4.4 in per positive g), with angle of attack away from 5 deg, and with sideslip; tolerance plus or minus 0.2 in | [FM] p.1-39 to 1-40, Figures 1-23 to 1-27 | |
| Spike actuator | hydraulic, forces up to 31,000 lb | [KJ81] typed p.7 | |
| Forward bypass | rotating band of ports just aft of the throat; closed below Mach 1.4; DAFICS holds a duct pressure ratio schedule to keep the normal shock at the throat; fully open with gear down | [FM] p.1-31 to 1-35 | 16 forward bypass doors, 3 louvre exits ([CP2054] Kock Fig. 2, p.24). |
| Aft bypass | rotating band just forward of the engine face; pilot selects CLOSE, A (15 percent), B (50 percent) or OPEN (100 percent), about 5 s full travel; air passes round the engine to the ejector | [FM] p.1-35, 1-44 | 24 aft bypass doors ([CP2054] p.24). Added as an unstart fix, then used in normal flight ([BROWN] p.6). |
| Shock trap and centerbody bleed | shock trap supplies engine cooling air; 32 shock trap tubes; about 5 percent (shock trap) and 3 percent (centerbody) of captured flow at Mach 2.8 | [FM] Figure 1-21; [CP2054] p.24; [SCAR] p.423 | 4 spike support struts ([FM] Figure 1-20; [CP2054] p.24). |
| Inlet start | the inlet normally "starts" between Mach 1.6 and 1.8 | [FM] p.1-31 | |
| Pressure recovery | 97 percent at high subsonic Mach falling to about 76 percent supersonic | [SCAR] p.423, Fig. 11 p.443 | |
| Compression at cruise | about 40:1; each inlet swallowed about 100,000 cu ft of air per second | [M09] p.25 (citing Urie 1990, Lockheed) | [BROWN] p.5 also "approximately 40:1". |
| Inlet air temperature | over 800 F | [BUR98] p.7; [KJ81] typed p.15 | |
| Unstart detection | shock expulsion sensor trips on a momentary CIP drop of more than 23 percent; restart opens the forward bypass fully and drives the spike forward up to 15 in, retracting 3.75 s later; above Mach 2.3 the "cross tie" cycles both inlets | [FM] p.1-42A | |
| Unstart transient | shock to the spike tip in about 0.01 s; restart 0.5 s after unstart (YF-12, Mach 2.5) | [SCAR] p.425, Fig. 16 p.448 | Violent at Mach 2.3 to 2.6, "can snap the pilots head and helmet against the inside of the canopy" ([SP4525] p.105). A-12 unstarts clustered at Mach 2.4 to 2.9 ([ARCH] p.14; [OXC] PDF p.15). |
| Control | DAFICS digital control (A computer left inlet, B right, M for manual); "virtually eliminated inlet unstart"; range +7 percent | [FM] p.1-47; [TM104330] p.4; [BUR98] p.7; [M09] p.34 | The A-12 used an earlier air inlet computer ([A12FM] Figure 1-11, PDF p.36). |
| Spike material | titanium on the early aircraft; later SR-71 cones of asbestos-fiberglass "plastic" on a titanium substructure for RCS | [SP4525] p.20 fn 26; [M09] p.20 | |

**Inlet states by Mach number** (FM Figure 1-21, p.1-33; the storyboard for the inlet explainer):

| Mach | Spike | Forward bypass | Aft bypass | Centerbody bleed | Suck-in doors | Tertiary doors | Ejector flaps |
|---|---|---|---|---|---|---|---|
| 0.0 | forward | open | closed | inward | open | open | closed |
| 0.5 | forward | closed | closed | overboard | closed | open | closed |
| 1.5 | forward | open as required to position the inlet shock | closed | overboard | closed | closed | opening |
| 2.5 | retracting | open as required | scheduled open | overboard | closed | closed | opening |
| 3.2 | retracted | closed, opening as required | (not labelled) | overboard | closed | closed | open |

### 2.3 Ejector nozzle

- Airframe-mounted convergent-divergent blow-in-door ejector: tertiary (blow-in) doors open at low speed to entrain air; at high speed they close and free-floating flaps form a C-D nozzle; both moved by aerodynamic forces; shock trap and aft bypass air joins the exhaust ahead of it. [TM104330] p.4; [KLO11] p.9; door states in [FM] Figure 1-21.
- Flaps of Hastelloy X hinged on a Rene 41 ring; 1,400 F inside and 1,600 F outside in afterburner. [M09] p.20 to 21.
- Originally part of the engine, moved to the airframe; Pratt and Whitney kept performance responsibility. The ejector "went supersonic long before the airplane did", which drove the transonic "climb-dive" technique. [BROWN] p.3 to 4; [TM104330] p.8.
- THIN: number of tertiary doors and flaps not found (SAE 740832 Herrick, "J58/YF-12 Ejector Nozzle Performance", not obtained).

### 2.4 Thrust split at Mach 3

| Condition | Inlet | Engine | Ejector | Source |
|---|---|---|---|---|
| Mach 3+ cruise | 54 percent | 17 percent | 29 percent | [M09] p.25, citing D. Urie, Caltech course Ae107 (1990), a Lockheed source. Quote: "At Mach 3 cruising speeds the inlet provided 54 percent of the thrust and the exhaust ejector 29 percent. At this point the turbojet continued to operate but provided only 17 percent of the total motive force." |
| Mach 2.2 | 13 percent | 73 percent | 14 percent | [M09] p.25, same source |
| Mach 3 summary | "Less than 20 percent of the total thrust used to fly at Mach 3 was produced by the engine itself" | | | [FS030] PDF p.3 |
| YF-12 | inlet "70 to 80 percent of the total motive force" | | | [SP4525] p.18 (citing Matranga and Fox 1976) |
| Manual hint | derichment at supersonic cruise cuts that engine's thrust about 45 percent in max afterburner, but "overall engine/inlet thrust loss is about 10%" | | | [FM] p.1-13 |

Caution: [TM104330] p.4 attributes most of the cruise force to pressure "on the forward facing surfaces of the spike"; physically the internal compression surfaces of the inlet carry it. Do not quote that sentence. Archangel's "only about 20 percent of the power" ([ARCH] p.14) is a counterfactual, not a split.

### 2.5 Engine and inlet diagrams (tier A unless noted)

- J58 keyed cutaway: `diagram_SR-71A-1_fig1-2_JT11D-20-engine-cutaway-keyed_p1-6.jpg` ([FM] Figure 1-2, 26 callouts; artwork probably Pratt and Whitney in origin, published in the USAF technical order). A-12 version `diagram_A-12-FM_fig1-5_*`. Augmentor and bypass tubes: `diagram_J58-augmentor-cutaway-bypass-tubes_TM-104330-p7-fig8.png`.
- Inlet section: `diagram_SR-71A-1_fig1-20_*` ([FM] Figure 1-20); door counts `diagram_YF-12-inlet-cutaway-door-counts_CP-2054-p24-fig2.png` (the best labelled cutaway; NASA reproduction of a Lockheed-style drawing, tier A with a note); `diagram_SR-71-inlet-cutaway_TM-104330-p5-fig4.png`; airflow states `diagram_SR-71A-1_fig1-21_*`; spike schedule `fig1-22-sh2`; forward bypass at Mach 2.9 to 3.2 `fig1-22-sh5`; inlet controls `fig1-29`; DAFICS `fig1-31`; recovery and distortion vs Mach `diagram_YF-12-inlet-recovery-distortion-vs-Mach_NASA-CP-001-p443-fig11.png`; unstart time history `diagram_YF-12-inlet-unstart-pressure-time-history_*`.
- Schedules and limits: thrust `fig1-3`, bleed and IGV schedule `fig1-11`, engine fuel system `fig1-7`, operating limits `fig5-2`, TEB system (A-12) `diagram_A-12-FM_fig1-8_*`.
- Tier C, link only: Brown's J58 station-temperature figure and Johnson's airflow sketches in CIA-RDP90B00170R000100080001-5 (https://archive.org/details/cia-readingroom-document-cia-rdp90b00170r000100080001-5); Merlin's Lockheed Martin figures in AIAA 2009-1522.

### 2.6 Engine and inlet photographs

- Best engine run: `photo_J58-full-afterburner-run_NASA-EC97-44007-01.jpg` (A, NASA / Tony Landis, 4 Apr 1997). Both engines at max afterburner on the ramp: `photo_SR-71A-both-engines-max-afterburner-on-ramp_NASA-EC98-44817-2.jpg` (A).
- Test cell: `photo_J58-in-altitude-chamber_NASA-Lewis_NARA-17419331.jpg` and `photo_J58-bypass-ducts-closeup_NASA-Lewis_NARA-17417985.jpg` (A, NASA Lewis 1974 via NARA; Commons has 34 more from the same series).
- Engines on display: `photo_J58-engine_NMUSAF_Aaron-Headly.jpg` (B, CC BY 2.0, full side view with bypass tubes), `photo_J58-engine_Museum-of-Aviation_Dsdugan.jpg` (A, CC0), `photo_J58-JT11D-20K_Evergreen_Daderot.jpg` (A, CC0).
- Inlet and spike: `photo_head-on-inlets-chines_NASM-61-7972_NASM2016-00596.jpg` (A, CC0, Smithsonian), `photo_inlet-spike-head-on_Clemens-Vasters.jpg` (B), `photo_inlet-spike-side_A-12-60-6925_Intrepid_Jorge-Lascar.jpg` (B; its Flickr caption has the spike moving the wrong way, do not reuse).
- Ejector: `photo_J58-ejector-afterburner-rear_greyloch.jpg` (B, 61-7972).
- Start cart: `photo_AG330-start-cart_Hill-Aerospace-Museum_Jaydec.jpg` (B, CC BY-SA 3.0) and `photo_A-12-60-6924-with-start-cart_Blackbird-Airpark_Thomas-Ormston.jpg` (B; Article 121 itself with a start cart).
- Gaps: no photograph of the TEB system; the Smithsonian's J58 photographs (NASM2020-05108 to 05117) are "usage conditions apply", tier C.

## 3. Other systems that made it special

### 3.1 Titanium structure and thermal design

Key numbers:
- 93 percent of structural weight titanium alloys ([M09] p.16; [SP4525] p.3); "over 90 percent of the A-12's airframe" ([ARCH] p.11). Over 13 million titanium parts ([M09] p.15).
- Alloys: A-110AT (about 5 Al, 2.5 Sn), B-120VCA (about 13 V, 11 Cr, 3 Al) for most skin at 0.020 to 0.040 in, C-120AV (about 6 Al, 4 V) ([M09] p.16 to 17). Aged B-120 is half the weight of stainless steel per cubic inch with nearly its strength ([KJ81] typed p.9). Hot parts in A-126 steel (to 1,200 F), Rene 41 (to 1,600 F) and Hastelloy X ([M09] p.17).
- Non-metallic parts: silicone-asbestos and phenyl silane glass laminates in the chines, wing edges, spike cone, tail cone and fins, honeycomb over 1 in thick in areas at 400 to 750 F ([M09] p.17). Not on the A-12 prototype, A-12T, M-21 or YF-12A.
- Titanium rejection rates early on: 95 percent ([ARCH] p.11) or "some 80 percent" ([OXC] PDF p.6). Disagreement.
- Corrugated wing skins: a test panel warped under heat, so chordwise corrugations were added; at design heating "the corrugations merely deepened by a few thousandths of an inch" ([KJ81] typed p.10, PDF p.13). Inner surfaces corrugated, outer beaded chordwise, spot welded ([M09] p.19).
- Skin temperatures, all at cruise: YF-12A upper surface contours 250 to 600 F ([TM104317] p.3, Fig. 1); average 462 to 622 F, up to 1,050 F on the nacelle ([M12] slide 33); 500 to 600 F, over 1,000 F near the engines (A-12, [ARCH] p.11); average 550 K, about 530 F ([CP2054] Kock p.4); heat soak over 600 F and lab heating to 800 F ([FS030] PDF p.3); 316 C (600 F) ([NASM-SR71]). Ram air temperatures "may exceed 400 C at design airspeed" ([FM] p.1-185); ram air over 800 F ([KJ81] typed p.3).
- Cockpit: outer glass 420 F, adjacent titanium 450 F, boundary layer 632 F, cockpit inner surface about 80 F; air fed at minus 40 F to hold about 60 F ([M09] p.18). Cooling was "seven times as difficult as on the X-15" ([KJ81] typed p.3).
- Black paint: high-emissivity black to radiate heat ([M09] p.16; [FM] p.1-4 "painted black to reduce internal temperatures when at high speed"). THIN: no emissivity value found.
- Thermal growth "up to four inches in length" ([SP4525] p.5). Fuel on the tank bottoms keeps the lower fuselage cool while the top heats, so the chines deflect down ([KJ81] typed p.7 to 8; [M09] p.23).
- Structure: monocoque fuselage and nacelles, multispar multirib wing; the chines carried almost 20 percent of the lift ([M09] p.17; [SP4525] p.3).

Best diagrams (A): `diagram_YF-12A-upper-surface-temperature-contours_TM-104317-p3-fig1.png` (skin temperature map), `diagram_YF-12A-structural-skeleton_TM-104317-p4-fig2.png`, `diagram_YF-12A-wing-thermal-expansion-relief-corrugations_TM-104317-p6-fig5.png`. Tier C, link only: Merlin's skin temperature drawing (AIAA 2009-1522 Fig. 13, Lockheed Martin) and the sr-71.org panel temperature diagram (tier D, held in `model/plans/raw/` for private reference only). Best photo: none of corrugated skin found (gap); `photo_head-on-inlets-chines_NASM-61-7972_NASM2016-00596.jpg` (A) for chines.

### 3.2 JP-7 and the fuel system

- **Tanks.** Five fuselage tanks (1A, 1, 2, 4, 5) and two wing-fuselage tank groups (3 and 6, with 6 split into 6A and 6B). FM p.1-47. Capacities (FM Figure 1-32, p.1-48, normal flight attitude, JP-7 at 6.57 lb/gal, 46.2 API, 78 F):

| Tank | US gal | lb |
|---|---|---|
| 1A | 251.1 | 1,650 |
| 1 | 2,095.9 | 13,770 |
| 2 | 1,974.1 | 12,970 |
| 3 | 2,459.7 | 16,160 |
| 4 | 1,453.6 | 9,550 |
| 5 | 1,758.0 | 11,550 |
| 6A (forward) | 1,158.3 | 7,610 |
| 6B (aft) | 1,068.5 | 7,020 |
| **Total** | **12,219.2** | **80,280** |

- A-12 for comparison: six tanks numbered 1 to 6 front to back, total 10,590 gal and 68,300 lb at 6.45 lb/gal (A-12 FM Figure 1-12, p.1-26, PDF p.38).
- **Feed and CG management.** Sixteen AC boost pumps (four each in tanks 1 and 4, two in each of the others). The CG is moved by automatic tank sequencing, early depletion of tank 1 to a preset float-switch level (eight settings between 3,300 and 10,500 lb), automatic and manual aft transfer into tank 5 (about 65 lb/min with both afterburners lit, 23 lb/min otherwise, 233 lb/min manual) and manual forward transfer into tank 1 at about 950 lb/min. FM p.1-47, 1-54 to 1-55. Supersonic aft CG limit 25 percent (moving forward 0.7 percent per 0.1 Mach above Mach 3.2). FM p.5-16. CG warning lights at an indicated forward CG of 16.7 percent or aft CG of 25.3 percent (FM Figure 1-40A, p.1-64). Diagrams: Figure 1-33 CG vs gross weight (p.1-49), Figure 1-37 fuel feed system (p.1-53).
- **Nitrogen inerting and pressurization.** Three Dewar flasks: two of 106 liters of liquid nitrogen in the nosewheel well and one of 50 liters in the left forward chine (B bay); heaters boil it, and the gas pressurizes each tank to 1.5 (plus or minus 0.25) psi above ambient and "inerts the ullage space above the heated fuel to prevent autogenous ignition". Relief at 3.25 psi; secondary relief 4.15 psi. Most nitrogen is used on descent. FM p.1-58, Figure 1-38 (p.1-56). "Mach 2.6 is the maximum speed without an inert atmosphere in the fuel tanks" (FM p.5-8).
- **Fuel as heat sink.** Fuel cools the air-conditioning, hydraulic fluid, engine oil and accessory drive oil, the TEB tank and nozzle actuator lines. If the mixed loop and engine fuel exceeds 290 F the temperature control valve starts to close and hot loop fuel is routed to tank 4 instead of the engines; at 300 F the valve is fully closed and all loop fuel returns to tank 4. Loop flow 4,600 to 6,300 pph at idle, about 7,600 pph at military. FM p.1-58 to 1-60, Figure 1-39 (p.1-57).
- **Fuel dumping** nominally 2,500 lb/min. FM p.1-62A.
- **The heat sink running out.** Late in a long maximum-speed cruise, as tank 3 empties, the remaining fuel is heated by "high skin temperatures", so the fuel-air heat exchangers cool the bleed air less and suit vent air gets warmer; comfort returns when tank 2 is scheduled on. FM p.2-50 (Crew Comfort) and p.3-120 (Suit Overtemperature).

From the papers:
- JP-7: PWA 523 fuel "now designated MIL-T-38219 grade JP-7", with PWA 536 lubricity additive developed for pump wear ([CRC560] App. A sec. 1.2); heat of combustion 18,871 Btu/lb ([FDS74] Table II); "can autoignite at temperatures slightly over 400 F" ([TM104317] p.6). A lighted match would not ignite it ([ARCH] p.12; [M09] p.22). THIN: no numeric flash point found in a primary source.
- Fuel temperatures: stable from minus 90 F at refuelling to over 350 F at cruise, then used as hydraulic fluid at 600 F ([KJ81] typed p.3).
- Sealant: 10,000 linear ft of fluorosilicone, leaking because of expansion provisions over minus 60 to more than 600 F ([M09] p.22; [SP4525] p.5); A-12 acceptable leak rate 5 to 60 drops per minute ([ARCH] p.12). The take-off-then-refuel pattern is not simply because of leaks (see `research/fact_notes.md` myth 6).
- Range economics: 54.1 nmi per 1,000 lb at Mach 3.2, standard day ([M09] p.27, citing Graham); acceleration to Mach 3 burns 16,000 to 28,000 lb depending on temperature ([M09] p.26).
- Wing tanks: [SP4525] p.5 says the A-12 and YF-12A had no wing tanks; [TMX2880] p.3 describes three YF-12 wing tanks and [M09] p.11 says the A-12 wing was an integral fuel cell. Use TM X-2880.

Best diagram (A): `diagram_SR-71A-1_fig1-32_fuel-tank-arrangement-and-capacities_p1-48.jpg` (tank cutaway plus capacity table); also `fig1-37` feed, `fig1-38` nitrogen pressurization, `fig1-39` heat sink, `fig1-33` CG schedule, and the YF-12 `diagram_YF-12-fuel-compartments_TM-X-2880-p38-fig2b.png`. Best photo: `photo_CG-indicator-recovered-61-7974_Mlpearc.jpg` (B; the Commons loss date is wrong, 61-7974 was lost in April 1989).

### 3.3 Air refuelling and the KC-135Q

- "The air-refueling system can receive fuel at approximately 6000 pounds per minute from KC-10 or KC-135 boom-equipped tanker aircraft." All tanks fill simultaneously in 12 to 15 minutes at 65 to 70 psi; the boom disconnects automatically above 70 psi (normal end-of-refuel with a KC-135). The receptacle doors are held closed by L hydraulic pressure and spring open if it is lost. FM p.1-60. Receptacle is item 19 on the bay locator (Figure 1-1); diagram FM Figure 1-40 (p.1-59). Separate single-point ground refuelling receptacle feeding the same manifold (FM p.1-4).
- Tanker procedures and envelopes: FM Figure 2-12 KC-135 boom limits (p.2-55), Figure 2-13 KC-135 receiver director lights (p.2-56), Figure 2-14 and 2-15 for the KC-10 (p.2-57, 2-58). The procedures name the KC-135Q and KC-10 (for example the TACAN air-to-air note on p.2-59).

From the papers: the KC-135Q "provides exclusive air refueling for the SR-71" ([EIS90] p.1-4 approx.); typical refuelling at Mach 0.75 and 25,000 ft, then a constant Mach 0.9 climb to 33,000 ft, a push-over to 30,000 ft and acceleration to 450 KEAS ([TM104330] p.8); more than 18,000 refuellings by all Blackbirds by 1981 ([KJ81] typed p.16). THIN: how the KC-135Q kept JP-7 separate from its own fuel was not documented in any source read in this pass.

Best diagram (A): `diagram_SR-71A-1_fig1-40_air-refueling-system_p1-59.jpg` and `fig2-12` (KC-135 boom limits). Best photos (A): `photo_KC-135Q-refuelling-SR-71_DF-ST-83-07614.jpg` (USAF, Ken Hackman, 1983), `photo_SR-71-approaching-KC-135Q-boom_DF-ST-89-06276.jpg` (USAF 1989; Commons wrongly says "drogue"), `photo_refuelling-receptacle-view-from-tanker_Tubridy_1988.jpg`.

### 3.4 Pressure suits and life support

- "The model 1030 full-pressure suit" (David Clark S1030): six layers (internal comfort liner, vent duct, bladder, exposure garment, link net restraint, exterior cover), vertical back-entry zipper; suit controller valves hold 3.5 psi in the suit if the cockpit depressurizes; helmet with face seal, Baylor bar visor lock, two built-in oxygen regulators and electrically heated visor; boots and gloves pressure-retaining. FM p.1-197 to 1-198.
- Vent air comes straight from the cold air manifold, as low as minus 30 F at cruise, warmed by the suit heat rheostat. FM p.1-197.
- Cockpits pressurized to a 26,000 ft (usual) or 10,000 ft schedule; safety valve at 5.4 psi differential. FM p.1-186 to 1-187, Figure 1-81 (p.1-189).
- Flight without pressure suits is restricted to below 50,000 ft. FM p.5-23.
- Oxygen: dual liquid oxygen systems (0 to 10 liter gauges), average consumption for two crew 1 liquid liter per hour on the 26,000 ft schedule. FM p.1-195. A-12: "suit pressure at 3.5 psi (equivalent to pressure at 35,000 ft)", white leather boots "for heat reflection". A-12 FM p.1-84 (PDF p.96).

Suit history, from [DFA] (NASA SP-2011-595): A-12 pilots wore the David Clark S901 series ([DFA] p.302 to 314; $30,000 each, [ARCH] p.15). The SR-71 began with the S901J, purchase specification finalised 29 Nov 1966, total about 31 lb ([DFA] p.324, 329). The **S1030** replaced it from late 1978 and served until 1996: six layers, "old gold" Fypro cover, 12 sizes, 115 made, about $30,000 each ([DFA] p.339 to 341). The **S1031 was the U-2R suit** (1981, 231 made) and not an SR-71 suit; the **S1031C** of 1989 was a common SR-71 and U-2R suit that began replacing both from 1991 (60 made); the S1034 replaced the S1030 in 1996 ([DFA] p.348 to 350). Escape design requirement: zero speed at sea level to Mach 4 above 100,000 ft ([KJ81] typed p.3).

Best diagrams (A): `fig1-80` environmental control system, `fig1-81` cockpit pressurization schedule, `fig1-82` oxygen system. Best photos: `photo_NASA-SR-71-crew-in-pressure-suits_Jim-Ross_1991.jpg` (A, NASA), `photo_David-Clark-S1030-pressure-suit_Omer-Wazir.jpg` (B, Pima), `photo_crew-in-cockpit-pressure-suits_Beale_DVIC.jpg` (B as tagged, probably a USAF photo), `photo_Don-Mallick-pressure-suit-YF-12A_NASA-ECN-2978.jpg` (A). Tier C: most suit images in [DFA] are "Courtesy of the David Clark Company". Smithsonian suit object records were not reached (API rate limit, site blocks scripts).

### 3.5 Sensors and mission equipment

- **Sensors listed in the Change 2 manual** (FM p.4-79, Figure 4-23): two high-resolution, narrow-field technical objective cameras (TECH, also called TEOC), the Advanced Synthetic Aperture Radar System (ASARS), the CAPRE high-resolution side-looking radar (SLR), the ELINT Improvement Program / Electromagnetic Reconnaissance (EIP), and the optical bar camera (OBC); plus V/H system, viewsight, two map projectors, exposure control and the Mission Recorder System. The Terrain Objective Camera (TROC) and Operational Objective Camera (OOC) "are no longer available" (FM p.4-81).
- Sensor comparison chart (Figure 4-23): TECH film 9-1/2 x 9-1/2 in, warm-up 20 to 40 s, not stabilised, mirror rotation image motion compensation, V/H 21 to 45 mrad/s; ASARS tape 9200 ft (2), 6 min warm-up, stabilised in pitch, roll, yaw and tilt; CAPRE film 1300 ft, 6 min; EIP tape (2), 2 min; OBC 5 in film, nodding FMC, V/H 35 to 45. Some cells redacted.
- **TEOC.** Two cameras in the left and right aft mission bays; models HR-308B (-11 and -21) and HR-308C; variable pointing angle, forward motion compensation by rocking the oblique mirror; field of view, pointing limits and coverage are blacked out in this copy. FM p.4-81 to 4-82.
- **OBC.** "A high resolution panoramic camera with a 'folded' lens system", mounted in an interchangeable OBC nose, 140 deg scan (70 deg each side of track), about 8 deg along track, FMC between 35 and 45 mrad/s; aperture and format redacted. FM p.4-93.
- **CAPRE SLR.** Side-looking synthetic aperture radar that replaces the OBC when fitted (nose antenna); 10 or 20 nm swath either side, near edge 10 to 70 nm out; recorded on film in two recorders in the right forward mission bay; in-flight display on the RSO's radar correlator display (RCD). FM p.4-86.
- **ASARS-1.** Pages 4-150 to 4-160 deleted from the manual (security review, 23 Sep 1996). Only the fixpoint accuracy (0.05 nm) and the sensor chart survive.
- **EIP (ELINT).** Passive equipment in the aft ends of the left and right aft mission bays, digital and analogue recorders in the left forward mission bay, automatic after turn-on. FM p.4-99.
- **DEF (defensive electronic) systems.** "Arbitrarily assigned letters designate and identify the systems. Systems A2, C2, H and M are currently operational." Controlled by the RSO from the DEF control panel on the left console, with a DEF warning panel to the right of the RCD; no DEF controls in the front cockpit. FM p.4-119. Locations: Figure 4-24 (p.4-80) and Figure 4-37 (p.4-125). Several DEF pages are stamped "UNCONTROLLED COPY" with deletions dated 23 Sep 1996.
- **Mission bays.** FM Figure 1-1 (p.1-5): right and left chine bays, forward and aft mission bays (compartments K to T), camera bay C, nose compartment A for radar or OBC.

From the papers and museum records:
- 1967 comparison: the A-12's best camera covered a 63 nmi continuous swath at 1 ft resolution; the SR-71's high-resolution cameras gave 1 ft resolution in two separate 5-mile strips positionable up to 19.5 miles either side ([CIA67] p.1 to 2). A-12 cameras: Type I (Perkin-Elmer, 5,000 ft film, 71-mile swath, 12 in resolution, flown on all 29 missions), Type II (Kodak), Type IV (Hycon) ([ARCH] p.16).
- Three interchangeable chined noses: CAPRE SLR, OBC and ASARS, the ASARS nose with a one-piece quartz/polyimide radome-chine ([M09] p.17).
- Coverage: 100,000 sq mi per hour from 80,000 ft ([NMUSAF-SR71]).
- TEOC museum label (Evergreen, secondary): built by Hycon, flown in pairs left and right in the chine bays, "a resolution of 6\" X 6\", flying at 80,000, Mach 3", 36 built, the only sensor used from start to finish of SENIOR CROWN. Transcribed from `photo_TEOC-technical-objective-camera_Evergreen_Daderot.jpg`; confirm before using as a hero number.
- THIN: focal lengths, resolutions and ranges for the OBC, ASARS-1 and CAPRE are not in any free primary source found; the manual's fields are blacked out or deleted.

Best diagrams (A): `fig1-1` bay locator, `fig4-23` sensor comparison chart, `fig4-24` sensor and DEF locations, `fig4-25` power and sensor panel, `fig4-36` DEF control panel. Best photos: `photo_TEOC-technical-objective-camera_Evergreen_Daderot.jpg` (A, CC0), `photo_TROC-F489-terrain-objective-camera_Evergreen_Daderot.jpg` (A), `photo_DEF-H-A2C-C-AR1700-recorder_Evergreen_Daderot.jpg` and `photo_AN-ALR-50XC-and-unit_Evergreen_Daderot.jpg` (A; identifications from the uploader and museum label), `photo_detachable-nose-section_NMUSAF_loganrickert.jpg` (B). Gap: no free photo of the OBC, SLR or ASARS hardware.

### 3.6 Flight controls and SAS

- Full-power irreversible controls: four elevons (inboard and outboard of each nacelle) and two all-moving rudders on fixed stub fins, each canted inward 15 deg; dual A and B hydraulic servos at every surface (outboard elevons 14 actuating cylinders each). FM p.1-94 to 1-100.
- Limits (FM Figure 1-50, p.1-97): manual pitch 10 down to 24 up, roll 24 deg differential, yaw 20 deg left and right (limited manual: roll 14, yaw 10); combined pitch and roll limited to 20 down and 35 up by actuator stroke; maximum rates pitch 32.5, roll 65, yaw 37 deg/s. SAS authority pitch 6.5 up to 2.5 down, roll 4, yaw 8; autopilot pitch 2.3 deg.
- SAS: three axes, DAFICS A, B and M channels (FM p.1-104 onward; pitch, yaw and roll block diagrams Figures 1-55 to 1-57, p.1-109 to 1-112). Autopilot with Mach hold, KEAS hold, auto nav (ANS steering) and heading hold (FM p.1-119 to 1-123). APW (angle of attack) stick shaker and pusher; pusher drives the elevons 1.7 deg down.
- Operational limit load factors (rule of thumb, symmetrical flight): Mach 2.0 or less, -0.2 to +2.5 g at 65,000 to 124,000 lb and -0.2 to +2.0 g at 124,000 to 143,000 lb; Mach 2.0 to 2.6, -0.1 to +2.0 g; Mach 2.6 to 3.2, -0.1 to +1.5 g (all weights). FM p.5-8, Figure 5-5.

From the papers: Elgiloy control cables; triple-redundant fail-operational SAS electronics with dual hydraulics; fly-by-wire was rejected ([M09] p.22 to 23; [SP4525] p.4). Stub fin about 21 in above the nacelle, rudder about 75 in above the stub, plastic rudders about 500 lb ([M09] p.19 to 20). Takeoff about 210 kt, landing about 155 kt ([M09] p.22).

Best diagrams (A): `fig1-50` deflection limits and rates, `fig1-51` flight control systems, `fig1-55` pitch SAS. Best photo: the NMUSAF front cockpit face shows the stick (section 1).

### 3.7 Landing gear and drag chute

- Tricycle gear: three-wheel main bogies retracting inboard into the fuselage, dual-wheel nose gear retracting forward; L hydraulic system; retraction or extension 12 to 16 s. FM p.1-89. "A drag chute is provided to augment the six-mainwheel brakes." FM p.1-4.
- Main tyres Goodrich 27.5 x 7.5 x 16 "silver tires", rated 239 knots (275 mph) maximum ground speed, 400 psi pressure. FM Figures 5-6 and 5-8 (p.5-19, 5-21). Touchdown sink rate limit 600 fpm at 68,000 lb falling to 360 fpm at 125,000 lb; landing above 125,000 lb not recommended. FM p.5-18.
- Nosewheel steerable 45 deg either side, minimum steering radius about 55 ft. FM p.1-91.
- Brakes: normal (L system) and alternate (R system) with antiskid working above 12 mph. FM p.1-91 to 1-93.
- **Drag chute**: stowed in the aft fuselage above tank 4; deployment bag holds a 42 in vane-type pilot chute, a 10 ft extraction chute and a 40 ft ribbon drag chute; electrical normal deploy and jettison, mechanical emergency deploy (T-handle upper left of the instrument panel). FM p.1-93 to 1-94. Maximum deployment speed 210 KIAS; minimum jettison speed 55 KIAS; maximum crosswind for jettison 12 kt. FM p.5-23.

From the papers: wheels and tyres are buried among the fuel tanks, which act as a heat sink ([KJ81] typed p.3); YF-12 ground vibration test tyre pressure 415 psi ([TMX2880] Table 2).

Best photos (A): `photo_drag-chute-landing_NASA_GPN-2000-001944.jpg` (NASA 1990, 5100 x 4000 master), `photo_landing-gear-down-NASA-844_EC96-43463-1.jpg`, `photo_tires_Evergreen_Daderot.jpg`; `photo_main-gear-bogie_Duxford_Chad-Kainz.jpg` (B). No dedicated gear diagram was rendered; the gear, brake and drag chute text is FM p.1-89 to 1-94.

### 3.8 Radar cross section features

- The biggest early returns were "vertical stabilizers, the engine inlet, and the forward side of the engine nacelles"; work on "ferrites, high-temperature absorbing materials and high-temperature plastic structures" followed, and the fins became laminated plastic, "the first time that such a material had been used for an important part of an aircraft's structure" ([OXC] PDF p.7 to 8).
- Shaping: continuously curving airframe, chines, mid-wing nacelles, canted rudders, non-metallic parts; a cesium fuel additive to reduce the radar return of the afterburner plume ([ARCH] p.4).
- Edges: triangular plastic panels interlocked with triangular titanium panels along the wing and elevon edges ([M09] p.19; titanium "pie slice" fillets with radar-absorbing inserts, [ARCH] p.16).
- Canted fins: 15 deg inward ([FM] p.1-94); the cant cut roll-yaw coupling and "further reduced radar cross section" ([SP4525] p.4).
- Paint: "formulated to absorb radar signals" ([NASM-SR71]); the flight manual gives only the thermal reason. THIN: the "iron ball" ferrite paint was not named in any source examined.
- 1967: RCS "relatively low" for both A-12 and SR-71, the SR-71 in full sensor fit "somewhat higher" ([NRO67] p.2).
- No usable RCS diagram found in free sources. Photo: `photo_head-on-inlets-chines_NASM-61-7972_NASM2016-00596.jpg` (A) shows chines, spikes and canted fins head-on.

### 3.9 Environmental control and electrics

- "Ram air temperatures may exceed 400 C at design airspeed, and ambient static air pressure can be less than 1/3 psi near the limit altitude. The external skin surfaces are painted black to radiate heat. Special insulating materials are used extensively." FM p.1-185.
- Two parallel air-cycle refrigeration systems fed by ninth-stage bleed air, cooled by air-to-air and air-to-fuel heat exchangers; cold air manifold regulated to minus 30 F at supersonic altitudes; cockpit exhaust then cools the nose and radar. FM p.1-186, 1-191; Figure 1-80 (p.1-188).
- Electrical: two 60 kVA AC generators driven through constant speed drives on the accessory drive system. FM p.1-67. Four independent hydraulic systems (A and B for flight controls, L and R for the inlets, gear, brakes, refuelling); fluid cooled by fuel. FM p.1-86.

### 3.10 A note on the navigation system name

The flight manual calls it the "astroinertial navigation system (ANS)" and never gives a model number or nickname (section 1.5). The Evergreen museum label (secondary) credits Nortronics (a Northrop division), dates the system to 1962 and says it was originally designed for the GAM-87 Skybolt missile, with 14 units acquired by Lockheed for the test programme; it also claims 300 ft error after a 4 to 6 hour flight, which the manual's own error table does not support ([FM] Figure 4-2 gives 0.3 nmi probable radial error for astro-inertial after a full alignment). **"NAS-14V2" and "R2-D2" were not found in the manual, the papers or the label.** Treat both as unverified until a primary source turns up.

## 4. Spec sheet (SR-71A)

The full sheet is `specs.json` (one source per row; rows for other sources and for the A-12 sit beside the primary value). Summary of the primary values and where good sources disagree:

| Item | Value used | Source | Other values and why they differ |
|---|---|---|---|
| Length (with pitot mast) | 107.4 ft | [FM] p.1-4 | Same in [FS030], [TP2000] Table 1; 107 ft 5 in ([NMUSAF-SR71], [NASM-SR71]). About 104 ft without the mast (model/plans NOTES.md). |
| Span | 55.6 ft | [FM] p.1-4 | 55 ft 7 in ([NASM-SR71]); 55.45 ft (Gilyard, CP-2054). |
| Height | 18.5 ft | [FM] p.1-4 | 18 ft 5 15/16 in ([NASM-SR71]). |
| Wing area | 1,605 sq ft (reference) | [FM] p.1-4 | 1,795 sq ft is a different reference delta (YF-12A). |
| Crew | 2 (pilot, RSO) | [FM] p.1-4 | A-12: 1. |
| Gross weight | 135,000 to over 140,000 lb | [FM] p.1-4 | About 140,000 lb ([FS030] PDF p.4, [NMUSAF-SR71]); 143,000 lb (NASA 844 test bed, [TP2000] Table 1); 136,700 lb fully fuelled (1967, [CIA67] p.1); 170,000 lb ([NASM-SR71], outlier, do not use). |
| Zero fuel weight | 56,500 to more than 60,000 lb | [FM] p.1-4 | 59,000 lb basic (NASA 844, [TP2000] Table 1). |
| Max takeoff weight | not limited by the manual; performance-limited | [FM] p.5-5 | |
| Fuel | 12,219.2 US gal, 80,280 lb (JP-7 at 6.57 lb/gal) | [FM] Figure 1-32, p.1-48 | 80,000 lb ([FS030]). A-12: 10,590 gal, 68,300 lb at 6.45 lb/gal ([A12FM] p.1-26); 69,800 lb ([M09] p.11). |
| Engines | 2 x P&W J58 (JT11D-20), 34,000 lbf max afterburning each | [FM] p.1-4, p.1-7 | 32,500 (J-engine, [SP4525] fn 25; [FS030]); 31,500 (A-12 interim, [A12FM] p.1-7); 30,000 ([NASM-J58], [PW]). |
| Design / max cruise Mach | design Mach 3.2; max scheduled cruise Mach 3.17; Mach 3.3 when authorised (CIT 427 C) | [FM] p.5-8 | Max safe Mach 3.3 ([NASM-SR71]); 1967 training limit Mach 3.0 ([NRO67]). A-12 normal cruise Mach 3.1 ([A12FM] Section V). |
| Fastest recorded | 2,193.167 mph (FAI absolute speed record, 1976) | fact_notes.md (FAI) | A-12 reached Mach 3.29 ([ARCH] p.21). |
| Altitude limit | 85,000 ft unless authorised | [FM] p.5-10 | Records and tests: 85,068.997 ft sustained horizontal flight (record, 1976); 86,700 ft at 80,000 lb and 89,650 ft at Mach 3.22 in Category II tests ([M09] p.26); A-12 90,000 ft ([ARCH] p.21). |
| Range | about 2,900 statute miles unrefuelled | [NMUSAF-SR71] | Model specification 3,800 nmi; 3,048 nmi on the max-altitude profile; operational average 2,800 nmi ([M09] p.27). Not in the flight manual scan (performance appendix absent). |
| Endurance | more than one hour of continuous Mach 3 at a time | [FS030] PDF p.3 | Longest operational sorties 11.2 h with refuelling (1987); 15,000 mi in 10.5 h (1971) ([M09] p.27). |
| Fuel burn at cruise | 36,000 to 38,000 lb/h | [M09] p.26 | Specific range 54.1 nmi per 1,000 lb at Mach 3.2 ([M09] p.27). |
| Load factor | -0.1 to +1.5 g at Mach 2.6 to 3.2 | [FM] p.5-8 | -0.1 to +2.0 g at Mach 2.0 to 2.6; up to +2.5 g (or +3.5 g at 80,000 to 90,000 lb below 50,000 ft) at Mach 2.0 or less. |
| Sensors | 2 TEOC, ASARS-1, CAPRE SLR, EIP, OBC; DEF A2, C2, H, M | [FM] p.4-79, 4-119 | 1967 fit: Technical, Operational and Terrain Objective Cameras ([NRO67]). |

## 5. How well each system is documented

| System | Coverage | Why |
|---|---|---|
| Front and rear cockpit layouts | Strong | Keyed manual drawings of every panel and console in both cockpits (SR-71A, SR-71B, A-12) plus rectilinear NMUSAF photographs. Weak spots: the manual's canopy pages (1-170 to 1-179) are missing; the aft panel variants on p.1-28A/B are missing; the RSO photo is only a central crop. |
| Inlet | Strong | Manual text and schedules, NASA YF-12 inlet papers with door counts, recovery, bleed fractions and unstart time histories. Missing: spike and cowl contour coordinates (see model/plans NOTES.md). |
| J58 cycle and limits | Good | Manual plus Smithsonian, NMUSAF, NASA papers and Brown 1981. Thin: airflow, overall dimensions (one source), weight (two values). |
| Thrust split | Adequate | One traceable chain (Merlin citing a Lockheed handout), corroborated in shape by NASA FS-030 and by the manual's derichment note. |
| Fuel, inerting, CG, heat sink | Strong | Manual Section I in detail. Thin: JP-7 flash point number. |
| Air refuelling | Good | Manual rates and envelopes, USAF photographs. Thin: KC-135Q tanker-side details. |
| Thermal and structure | Good | NASA thermal-structures papers, Merlin, Johnson. Thin: paint emissivity; no corrugated-skin photograph. |
| Pressure suits | Good | Manual (S1030 layers and pressures) and NASA SP-2011-595 for the suit sequence. Thin: free suit photographs (most are David Clark Company, tier C). |
| ANS | Good on operation, thin on hardware | Manual Section IV (modes, accuracy, star catalogue, panel). Model number, nickname and installed photos not found. |
| Ejection seats | Good | Manual sequence and timings for the SR-1 and the A-12 seat. |
| Flight controls and SAS | Good | Manual limits, rates and block diagrams. |
| Landing gear and drag chute | Good | Manual numbers, NASA photographs. |
| Sensors | Thin | List, carriage and some film capacities only. TEOC fields of view and OBC aperture are blacked out; ASARS-1 pages deleted; no free OBC, SLR or ASARS hardware photos. |
| Radar cross section | Thin | Qualitative CIA and Merlin statements; no numbers, no diagrams, "iron ball" paint unconfirmed. |
| AG330 start cart | Adequate for the story, thin on the name | Johnson and CIA describe the twin Buick cart; the designation itself is unconfirmed. |

## 6. Rights problems and cautions

1. **NMUSAF Cockpit360 images (the best cockpit photos).** Made by a contractor photographer (Lyle Jansma, Aerocapture Images) for the museum. The museum's site statement says its information "is considered public information and may be distributed or copied. Use of appropriate byline/photo/image credits is requested" (archived 2016-02-06, https://web.archive.org/web/20160206235220/http://www.nationalmuseum.af.mil/Visit/Questions.aspx). Recorded as tier A with that caveat; ask NMUSAF (or Aerocapture) to confirm before featuring them, and always credit "National Museum of the U.S. Air Force; imagery by Lyle Jansma, Aerocapture Images".
2. **Flight manual scan provenance.** The SR-71A-1 PDF and page masters were uploaded anonymously to the Internet Archive; they are a USAF work (tier A) but carry SENIOR CROWN markings and 1996 security-review deletions. Cite with care. Some figures (the J58 cutaway) are probably Pratt and Whitney or Lockheed artwork reproduced in the technical order; mirrored as part of the government publication.
3. **A-12 manual.** Lockheed-prepared, released by CIA with no copyright notice: tier A with a note.
4. **NASA reproductions of contractor drawings** (CP-2054 inlet cutaway, TM-104330 inlet cutaway, TM X-56039 figures) are treated as tier A with a note. Contractor reports (CR-163106 and similar) stay tier C.
5. **Tier C sources used for facts only:** Merlin AIAA 2009-1522 and Kloesel 2011 (AIAA papers; Lockheed Martin figures); Johnson 1981 and Brown 1981 (Lockheed and Pratt and Whitney works released by CIA); Dressing for Altitude suit images credited to the David Clark Company; the Smithsonian J58 photographs ("usage conditions apply"); the Smithsonian cockpit panorama (no rights stated); Pratt and Whitney's J58 web page.
6. **Mislabelled "public domain" on Commons:** Brian Shul's cockpit self-portraits (his own book): tier C.
7. **Tier D:** everything from sr-71.org, sr71.us and habu.org (permission mandatory). The sr-71.org and sr71.us files in `model/plans/raw/` stay private reference and are not in this pack.
8. **Wrong captions not to reuse:** spike moving "forward" (Lascar Flickr caption); "drogue" for the KC-135Q boom (DF-ST-89-06276 on Commons); the 61-7974 loss date on the c.g. indicator photo; "IBM division called Nortronics" (Evergreen ANS label); FS-030's kilogram conversions (52,253.83 kg for 140,000 lb uses the wrong factor; 140,000 lb is 63,503 kg).
9. **Beale aircrew photo** is a Flickr CC BY re-upload of what reads like a DoD photograph; held as tier B until its VIRIN is found.

## 7. Open items for the next pass

- Confirm "NAS-14V2", "R2-D2" and "AG330" in a primary source (Northrop/Nortronics documents, USAF technical orders for the start cart, museum labels read by hand).
- Get the SR-71A-1 pages 1-170 to 1-179 (canopies, windshield, map projectors) from another copy of the manual; and the performance appendix (range charts).
- Smithsonian suit records (S1030) by hand; NMUSAF fact sheet photos by hand (the site blocks scripts).
- SAE 740832 (ejector) and NASA TM X-3138/3139 (full-scale inlet) for ejector door counts and inlet contours.
- Ask NMUSAF about the Cockpit360 imagery; ask the Smithsonian whether a CC0 cockpit image of 61-7972 exists.
