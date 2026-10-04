# Blackbird family history site: source scouting report

Scope: A-12 OXCART, YF-12, M-21/D-21, SR-71 (plus J58 engine, LASRE, NASA SR-71A/B/YF-12 research).
Compiled 2026-10-04. Every API call marked "verified" was actually run with curl from a Mac on that date; counts are what the endpoint returned that day and will drift.

Legend for rights:
- **PD-USGov**: work of a US federal employee in the course of duty, no US copyright (17 U.S.C. 105). Mirror freely, credit anyway.
- **CC0**: dedicated to the public domain by the holder. Mirror freely, credit anyway.
- **CC BY / BY-SA / BY-NC**: mirror only with the attribution and terms of that licence.
- **(c)**: all rights reserved. Link only, or mirror after written permission.

---

## 1. Primary image archives

### 1.1 Smithsonian Open Access (NASM SR-71A 61-7972) [best single image source]

- Object record: https://airandspace.si.edu/collection-objects/lockheed-sr-71-blackbird/nasm_A19920072000 (ARK: http://n2t.net/ark:/65665/nv9afd733c1-f6b5-45f1-ab28-2d19c801b502), the Udvar-Hazy aircraft, 61-7972.
- Holdings (verified via API): 14 media items on the SR-71 record, all flagged `access: CC0`. 10 have downloadable masters as TIFF and JPEG, for example:
  - NASM-NASM-9A08307: **10950 x 3750** px TIFF (panoramic)
  - NASM-NASM2016-00595 / 00596 / 00597: **8688 x 5792** px TIFF
  - NASM-NASM2013-00888 to 00891: 3000 to 5664 px
  - NASM-SI-2006-2744: 3300 x 2550
  - 4 items (NASM-SI-2000-9346, NASM-SI-92-14116, NASM-A19920072000cp08, NASM-NASM2013-00149 partial) are screen-size only.
  - Download pattern: `https://ids.si.edu/ids/download?id=NASM-NASM2016-00596.tif`
- Other Smithsonian hits are library catalogue records (Crickmore, Graham, Merlin, Jenkins books) and two Smithsonian Research Online entries (unit SLA_SRO, e.g. "Setting Records with the SR-71 Blackbird"). No NASM object records for A-12, YF-12, D-21 or J58 came back from the API.
- Rights: CC0 on the media, but every item carries "Third party or legal restrictions may apply to your use of these images." Credit is not legally required for CC0 but is courteous and fits the site rule.
- Credit line to use: `Smithsonian National Air and Space Museum (NASM2016-00596), CC0`.
- API (verified): `https://api.si.edu/openaccess/api/v1.0/search?q=SR-71&api_key=DEMO_KEY&rows=50` returned rowCount 67; `q=SR-71+AND+unit_code:NASM` returned exactly the one SR-71 object. Needs an api.data.gov key (free, instant at https://api.data.gov/signup/). DEMO_KEY hit HTTP 429 after about 10 calls, so register a real key before bulk work.

### 1.2 NASA Image and Video Library (images.nasa.gov)

- URL: https://images.nasa.gov/
- Holdings (verified): `q=SR-71` = **50** images (mostly Armstrong/Dryden EC-numbered: LASRE 1997 to 1998, NASA 831 SR-71B, crew portraits, J58 afterburner run EC97-44007-01, KSC 1997/1999 visits); `q=YF-12` = 4 (including GRC-1977-C-04657, YF-12 model in the Lewis 10x10 tunnel, and ARC-1971-AC71-1988); `q=LASRE` = 11; `q=Blackbird` = 11. **Zero** video or audio for SR-71, YF-12, LASRE or J58. This library holds only a fraction of the Armstrong Blackbird photography; see 1.3.
- Max resolution: `~orig.jpg` masters. Example EC97-44295-29 (LASRE first flight) is 3039 x 2444, 7.5 MB, creator "NASA/Tony Landis".
- Rights: PD-USGov (NASA). NASA media guidelines: https://www.nasa.gov/nasa-brand-center/images-and-media/ . NASA asks that it be "acknowledged as the source", forbids implied endorsement, protects the meatball/worm insignia, and says third-party copyrighted items are marked in the caption. Check every caption for a non-NASA credit.
- Credit line to use: `NASA / Tony Landis (EC97-44295-29)`.
- API (verified, no key):
  - Search: `https://images-api.nasa.gov/search?q=SR-71&media_type=image&page_size=100`
  - Asset list (all renditions): `https://images-api.nasa.gov/asset/EC97-44295-29`
  - Full EXIF/XMP metadata: `https://images-assets.nasa.gov/image/EC97-44295-29/metadata.json`
  - Note: free-text `q=SR71` (no hyphen) returns 0, and `q=A-12` returns 14,735 irrelevant hits. Use `SR-71`, `YF-12`, `LASRE`, `Blackbird` plus `center=AFRC`.

### 1.3 Legacy NASA Dryden gallery (dfrc.nasa.gov), now dead, preserved in the Wayback Machine

- Live host does not resolve (curl 000, 2026-10-04).
- Wayback (verified via availability API):
  - SR-71 photos: http://web.archive.org/web/20250306052842/https://www.dfrc.nasa.gov/Gallery/Photo/SR-71/index.html (48 photo pages)
  - YF-12 photos: http://web.archive.org/web/20250306065111/https://www.dfrc.nasa.gov/Gallery/Photo/YF-12/index.html (11 photo pages)
  - YF-12 movies: http://web.archive.org/web/20161220041317/http://www.dfrc.nasa.gov/Gallery/Movie/YF-12/index.html (10 clips)
- CDX inventory (verified, `https://web.archive.org/cdx/search/cdx?url=dfrc.nasa.gov/Gallery/Photo/SR-71*&fl=original,mimetype&collapse=urlkey`): 418 unique captured URLs under the SR-71 galleries (sub-galleries SR-71, SR-71-LASRE, SR-71-UVE), 197 JPEGs of which 71 are "Large" renditions; YF-12 photo gallery 69 URLs, 33 JPEGs, 11 Large.
- **Video, not available anywhere else found so far**: the Dryden movie gallery clips survive in the Wayback Machine. SR-71 clips EM-0025-01 to EM-0025-07 and YF-12 clips EM-0041-01 to EM-0041-10 (27 and 42 captured movie files across sizes). Verified download: `https://web.archive.org/web/2010id_/http://www.dfrc.nasa.gov/Gallery/Movie/SR-71/480x/EM-0025-03.mov` returned a 6.5 MB QuickTime file. (EM-0041-01 also exists as Internet Archive item NIX-EM-0041-01.)
- Value: the original captions, the EC/ECN numbering and the clips. Most photo IDs now resolve in images.nasa.gov; use the Wayback pages to recover the longer historical captions and anything not migrated.
- Rights: PD-USGov (NASA). Credit: `NASA Dryden Flight Research Center, <EC or EM number>`.

### 1.4 Wikimedia Commons

- Category tree: https://commons.wikimedia.org/wiki/Category:Lockheed_SR-71_Blackbird (also Category:Lockheed_A-12, Category:Lockheed_YF-12, Category:Lockheed_M-21, Category:Lockheed_D-21, Category:Pratt_%26_Whitney_J58). Commons has per-airframe sub-categories (for example 61-7972) which are a ready-made airframe index.
- Holdings (verified with CirrusSearch `deepcat:` against namespace 6, approximate because deepcat is capped):

  | Tree | Files |
  |---|---|
  | Lockheed SR-71 Blackbird | ~690 |
  | Lockheed A-12 | ~218 |
  | Lockheed D-21 | ~97 |
  | Pratt & Whitney J58 | ~94 |
  | Lockheed YF-12 | ~83 |
  | Lockheed M-21 | ~62 |

  Licence breakdown inside the SR-71 tree: PD-USGov-NASA 110, PD-USGov-Military-Air Force 37, PD-USGov-CIA 6, other PD-USGov 24, CC BY 2.0 223 (mostly Flickr imports of museum photos), CC BY-SA 4.0 60, CC BY-SA 3.0 43. Files wider than 3000 px: 413.
- Max resolution: original upload; e.g. File:Lockheed_SR-71_Blackbird.jpg (NASA 831 over the Sierra Nevada, "USAF / Judson Brohmer") is 5100 x 3996.
- Rights: per file. Commons is a host, not a rights holder; treat its licence tag as a lead and confirm against the upstream source (NASA ID, NARA ID, Flickr page).
- Credit line: `"<title>" by <Artist>, <licence> (link), via Wikimedia Commons`. For PD-USGov files credit the original agency and photographer, not Commons.
- API (verified):
  - Category size: `https://commons.wikimedia.org/w/api.php?action=query&prop=categoryinfo&titles=Category:Lockheed%20SR-71%20Blackbird&format=json` (68 direct files, 15 subcats)
  - Tree search: `https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=deepcat:%22Lockheed%20SR-71%20Blackbird%22&srnamespace=6&srinfo=totalhits&format=json`
  - Licence/author/size for one file: `https://commons.wikimedia.org/w/api.php?action=query&titles=File:Lockheed_SR-71_Blackbird.jpg&prop=imageinfo&iiprop=url|size|extmetadata&format=json`
  - Rate limits are strict for anonymous clients: a recursive crawl at ~3 req/s got HTTP 429 within a minute. Use a descriptive User-Agent with a contact URL (Wikimedia policy), 1 request every 1 to 2 s, and prefer `deepcat:` search or `generator=categorymembers` with `prop=imageinfo` to batch.

### 1.5 Library of Congress

- Holdings (verified): `photos/?q=SR-71` = **303** results, `search/?q="SR-71"` = 929 (all formats).
- Mixed rights, decided per item. Two examples checked:
  - "Pres. Ford with crew of SAC-SR-71 after record breaking flight" (1974, Marion S. Trikosko, U.S. News & World Report collection): "No known restrictions on publication", master TIFF at `https://tile.loc.gov/storage-services/master/pnp/ppmsca/55500/55590u.tif`.
  - Joe McNally 2003 series of Col. Ken Collins with an SR-71 at China Lake (about 10 frames): "Publication may be restricted", so link only.
- Credit line (LoC's own format): `Library of Congress, Prints & Photographs Division, <collection>, <reproduction number>`.
- API (verified, no key): `https://www.loc.gov/photos/?q=SR-71&fo=json&c=25` and per item `https://www.loc.gov/item/2019631415/?fo=json` (gives `rights_advisory` and the master file URLs). Note: in zsh do not name a loop variable `path`; it clobbers `$PATH`.

### 1.6 National Archives (NARA) Catalog

- URL: https://catalog.archives.gov/search?q=SR-71
- Holdings: DoD still photos (RG 330 Defense Visual Information, RG 342 USAF), USAF and NASA motion pictures, CIA and NRO records. Many of the Commons PD-USGov-Military files trace back to RG 330 DVIC images.
- Rights: federal records, mostly PD-USGov; some donated materials restricted. NARA asks for `National Archives, NAID <number>` (or "Courtesy of the National Archives").
- API: Catalog API v2, `https://catalog.archives.gov/api/v2/records/search?q=SR-71` with header `x-api-key`. **Not verified**: without a key the endpoint (and the front end's `/proxy/records/search`) returns the SPA HTML, not JSON. The swagger spec is public at `https://catalog.archives.gov/api/v2/swagger.json`. Keys are free: email Catalog_API@nara.gov with your name and the email address for the key (read-only key is enough). v1 was retired in September 2023.

### 1.7 DVIDS (Defense Visual Information Distribution Service)

- URL: https://www.dvidshub.net/ (successor to the DoD imagery sites, hosts Beale AFB / 9th RW heritage and museum material).
- Rights: DoD works PD-USGov. DVIDS requires this line on non-commercial use: "The appearance of U.S. Department of War (DoW) visual information does not imply or constitute DoW endorsement." (https://www.dvidshub.net/about/copyright). Credit the photographer: `U.S. Air Force photo by <name>`.
- API: `https://api.dvidshub.net/search?q=SR-71&type=image&api_key=key-XXXX`. **Not verified**: returns `{"errors":["Bad Request - No API key was provided"]}` without a key. Key comes from signing up at https://api.dvidshub.net/ (documented as open access). The DVIDS website returns HTTP 202 bot challenges to curl, so plan on the API.

### 1.8 National Museum of the USAF and af.mil sites

- SR-71A fact sheet: https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/198054/ (32 linked photos on that page alone; tag pages /Upcoming/Photos/igtag/SR71 and /igtag/Blackbird). The museum's other Blackbird family exhibits (YF-12A 60-6935, a D-21B) have their own fact sheets.
- Max resolution: original via `https://media.defense.gov/<yyyy>/<Mon>/<dd>/<id>/-1/-1/0/<file>.JPG` (the `-1/-1` path segment is the full-size rendition).
- Rights: "U.S. Air Force photo" = PD-USGov; check captions for "courtesy" images from Lockheed or private donors, which are not.
- Credit line: `U.S. Air Force photo [by <name>], National Museum of the U.S. Air Force` plus the DoW non-endorsement line above.
- API: none. **Scripted access blocked**: nationalmuseum.af.mil, af.mil and media.defense.gov all returned HTTP 403 to curl (even with browser headers) and to WebFetch. The fact sheet is in the Wayback Machine (snapshot 2024-12-03). Collect by hand in a browser, or find the same images on DVIDS/Commons.

### 1.9 Flickr Commons: San Diego Air & Space Museum Archives (SDASM) and NASA on The Commons

- https://www.flickr.com/photos/sdasmarchives/ ; tag pages on https://commons.flickr.org/tags/sr71/
- Holdings (verified from commons.flickr.org tag pages): `sr71` 30 photos + 4 illustrations (SDASM and nasacommons), `sr71a` 20, `habu` 14, `yf12` 33 + 1 (all SDASM), `a12` 154 (SDASM; not all will be OXCART, check), `blackbird` 138 + 4 (mostly NASA on The Commons). SDASM includes a donated set from William Blondet (42nd TEWS, KC-135 pilot) with SR-71 photos.
- Rights: "No known copyright restrictions" (the Flickr Commons statement). For donated personal collections this is the museum's judgement, so credit both SDASM and the donor.
- Credit line: `San Diego Air & Space Museum Archives, <catalog number>`.
- API: Flickr API needs a key (not tested).

### 1.10 Internet Archive (images, film, texts)

- Holdings (verified with advancedsearch): `"SR-71"` 1,256 items (122 movies, 793 texts, many false positives); `"YF-12"` 139. Useful items found: NASA film `NIX-EM-0041-01` "SR-71A/YF-12A takeoff and flight"; NTIS films `gov.ntis.ava20323-vnb1` "The SR-71" (public domain mark); the declassified SR-71 flight manual `0003756-lockheed-sr-71-03` (public domain mark); `CIAA-12Files` (CC0 bundle of the CIA OXCART release); a full mirror of the CIA reading room as `cia-readingroom-document-*` items (very useful for bulk text access because cia.gov has no API).
- Rights: the uploader sets the licence field; verify upstream. Copyrighted books (Graham, Crickmore, Johnson's "Kelly") are lending-library scans only, do not mirror.
- API (verified, no key): `https://archive.org/advancedsearch.php?q=%22YF-12%22&fl[]=identifier&fl[]=title&fl[]=mediatype&fl[]=licenseurl&rows=50&output=json`

### 1.11 Other image holders (rights-restricted, permission or link only)

- Museum of Flight, Seattle (M-21 60-6940 with D-21 on top): https://digitalcollections.museumofflight.org/ . Rights shown as "Copyright undetermined"; publication needs permission and fee from the Museum of Flight Archives.
- Lockheed Martin / Skunk Works image galleries: (c) Lockheed Martin. Link only or request permission.
- airliners.net, JetPhotos, ABPic, Aerial Visuals: (c) individual photographers. Link only; ask photographers directly for key shots.
- Getty/Alamy/AP: (c) commercial. Do not use.

---

## 2. Documents

Access note: cia.gov reading-room inner pages, nro.gov, nationalmuseum.af.mil, afhra.af.mil and the DVIDS website all block scripted clients (302 loops, 403, or bot challenges). Where that happened the item was verified through a Wayback snapshot, a search-index record or an Internet Archive mirror, and is marked so. The PDFs marked "(verified)" returned `%PDF` on a ranged GET on 2026-10-04.

### 2.1 CIA (A-12 OXCART, BLACK SHIELD)

Rights: CIA site policy (https://www.cia.gov/site-policies/): "Unless a copyright is indicated, information on our website is in the public domain"; cite the Agency as source and keep photo credits and bylines. Watch for Lockheed-authored material inside CIA releases.

- **A-12 OXCART Reconnaissance Aircraft Documentation** collection: https://www.cia.gov/readingroom/collection/12-oxcart-reconnaissance-aircraft-documentation . About 350 documents, roughly 1,500 pages (memos, maps, diagrams, photos), released September 2007 with Archangel and the display of Article 128 (60-6931) at CIA HQ. Scripted clients are redirected; browse by hand.
  - Indexed Black Shield items (not curl-verified): "OXCART/BLACK SHIELD" memo 5 Apr 1966 (CIA-RDP68B00724R000100040079-0) https://www.cia.gov/readingroom/node/938941 ; "OXCART BLACK SHIELD ROUTE ONE" https://www.cia.gov/readingroom/document/0001465322 ; "Project OXCART and Operation Black Shield Briefing Notes" 3 Sep 1965, doc 0001472024.
- **Archangel: CIA's Supersonic A-12 Reconnaissance Aircraft**, David Robarge, 2nd ed. January 2012, 66 pp born-digital PDF (verified): https://www.cia.gov/resources/csi/static/b45f5f8f5e4937963d9e9931313d84a4/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf . Landing page: https://www.cia.gov/resources/csi/books-monographs/archangel-cias-supersonic-a-12-reconnaissance-aircraft . Also on GovInfo (GOVPUB-PREX3-PURL-gpo91936). PD-USGov; the best single narrative source for the A-12.
- **"The Oxcart Story"**, Thomas P. McIninch, Studies in Intelligence, Winter 1970-71, 38 pp (verified): https://www.cia.gov/resources/csi/static/The-Oxcart-Story.pdf . NARA scan NAID 7283819 https://catalog.archives.gov/id/7283819 .
- **Kelly Johnson, "Development of the Lockheed SR-71 Blackbird"**, Studies in Intelligence, Summer 1982. NARA NAID 7283113 (use "Unrestricted"): https://catalog.archives.gov/medialive/13/2831/7283113/content/arcmedia/dc-metro/rg-263/6922330/Box-8-94-1/263-a1-27-box-8-94-1.pdf . Rights caution: Johnson was a Lockheed employee, not a federal one, so this is not automatically PD-USGov even though NARA marks use unrestricted. Quote and link; mirror only after deciding the risk is acceptable. Johnson's own A-12 log has not been released publicly.
- **The CIA and Overhead Reconnaissance: The U-2 and OXCART Programs, 1954-1974** (Pedlow and Welzenbach), chapter 6 "The U-2's Intended Successor: Project OXCART, 1956-1968". CIA copy (image-only scan, 272 pp): https://www.cia.gov/resources/csi/static/CIA-and-U2-Program.pdf . Less-redacted 2013 FOIA release at the National Security Archive: https://nsarchive2.gwu.edu/NSAEBB/NSAEBB434/ . Internet Archive mirror: https://archive.org/details/CentralIntelligenceAgencyAndOverheadReconnaissanceU2AndOXCARTPrograms19541974
- Mission documents mirrored on the Internet Archive (verified): BSX001 mission critique 6 Jun 1967 https://archive.org/details/CIA-RDP69B00404R000100010001-3 ; Black Shield operational status 13 Jul 1967 https://archive.org/details/CIA-RDP70B00501R000100150001-8 ; OXCART/SR-71 information for ExCom Dec 1967 https://archive.org/details/cia-readingroom-document-cia-rdp89b00980r000600060013-9
- CIA web pages: https://www.cia.gov/legacy/museum/exhibit/a-12-oxcart/ and https://www.cia.gov/legacy/headquarters/a-12-oxcart
- **API**: the CIA reading room has none (HTML only, behind bot protection; search URL pattern `https://www.cia.gov/readingroom/search/site/OXCART`). **Bulk route (verified)**: the Internet Archive mirrors of CREST and the reading room, collections `cia-collection` and `ciareadingroom`:
  `https://archive.org/advancedsearch.php?q=collection:(cia-collection OR ciareadingroom) AND (title:OXCART OR title:"BLACK SHIELD" OR title:"SR-71" OR title:TAGBOARD)&fl[]=identifier&fl[]=title&rows=100&output=json` (2,704 hits, some noise).

### 2.2 NRO (D-21 TAGBOARD / SENIOR BOWL)

- nro.gov returns 403 to scripts; verified through the Wayback snapshot of 19 Apr 2026.
- **Declassified D-21 Drones Program Records**: https://www.nro.gov/foia-home/foia-declassified-nro-programs-and-projects/Declassified-D-21-Drones-Program-Records/ . 97 records, 659 pages, released 2018 (stamped "Approved for Release: 2018/11/16"). PDF pattern `https://www.nro.gov/Portals/135/documents/foia/declass/D-21/SC-2018-00037_C05114xxx.pdf`. Selected: Tagboard Study 18 Oct 1963 (C05114716); Reorientation of the Tagboard Program Nov 1966 (C05114715); Successful Tagboard Test Flight Jun 1968 (C05114717); Tagboard Operational Missions Sep 1969 (C05114714); Tagboard Mission over South China Mar 1971 (C05114709); SR-71 Aircraft Attrition Nov 1967 (C05114702); Q-12 Ramjet Drone Feb 1963 (C05114703); Tagboard Status Aug 1974 (C05114804).
- Seen in the index only: NRO staff records index with OXCART/SR-71 overflight items https://www.nro.gov/Portals/65/documents/foia/docs/declass/staff-records.pdf ; D-21 history presentation https://www.nro.gov/Portals/65/documents/history/csnr/D-21/Allman%20Presentation.pdf
- Video: "The 50th Anniversary Commemoration of the End of the A-12 OXCART" https://www.youtube.com/watch?v=0iyU79EK_9I
- Rights: PD-USGov (NRO statement not readable by script). No API. Because the site blocks scripts, download the D-21 set by hand once and keep it locally; it is exactly the kind of release that moves URL (Portals/65 vs Portals/135 already differ).

### 2.3 SR-71 Flight Manual (SR-71A-1, Issue E, Change 2)

- **Internet Archive scan**: https://archive.org/details/0003756-lockheed-sr-71-03 . Three image PDFs (about 35 MB each), OCR and JP2. Tagged Public Domain Mark, creator "US Department of Defense". The item date (1989-10-31) is wrong; the cover OCR reads "ISSUE E: 31 OCTOBER 1986, Change 2: 31 July 1989". Caution: the scan shows the original SENIOR CROWN classification notices and no visible declassification stamp, and the uploader is anonymous, so provenance is unclear. Prefer the sr-71.org edition for text and cite the Internet Archive scan as a second copy.
- **sr-71.org web edition**: https://sr-71.org/blackbird/manual/ (503 when tested; verified via Wayback 9 Jun 2025). Issue E Change 2, 1,052 pages; pages 1-28A, 1-28B, 1-174, 1-175 missing; 4-150 to 4-160 still classified. The site claims no copyright on the manual text, asks to be cited as "SR-71 Online", and asks for permission before mirroring its edition. The manual itself is a USAF technical order (PD-USGov once released); sr-71.org's transcription, formatting and page images are its own work, so ask.
- Commercial reprints of the manual exist (lending-library copy on the Internet Archive: `sr71flightmanual0000unse`). Their added material and layout are copyrighted; do not use them.
- No public SR-71 maintenance technical orders were found.

### 2.4 NASA Technical Reports Server (NTRS)

- **API (verified, no key)**: `https://ntrs.nasa.gov/api/citations/search?q=YF-12&page.size=100`. Totals 2026-10-04: YF-12 86, SR-71 71, LASRE 13, Blackbird 10. Each record has `copyright.determinationType` (GOV_PUBLIC_USE_PERMITTED, GOV_PERMITTED, PUBLIC_USE_PERMITTED, OTHER), a center code and `downloads[].links.pdf`. PDF pattern `https://ntrs.nasa.gov/api/citations/<id>/downloads/<id>.pdf` (read `downloads[]` when the file name differs, e.g. 19980223961). Treat `OTHER` (often AIAA or journal papers) as copyrighted.
- Key items (all PDFs returned HTTP 200):

  | NTRS ID | Title | Year |
  |---|---|---|
  | 19780024112 | YF-12 Experiments Symposium, Vol. 1 (NASA CP-2054), 127 MB | 1978 |
  | 19780024113 | Overview of the NASA YF-12 Program (Kock) | 1978 |
  | 19960027893 | A Historical Perspective of the YF-12A Thermal Loads and Structures Program (NASA TM-104317) | 1996 |
  | 19720023371 | Sonic-boom measurements for SR-71 aircraft at Mach numbers to 3.0 | 1972 |
  | 20000064011 | The SR-71 Test Bed Aircraft: A Facility for High-Speed Flight Research (NASA TP-2000-209023) | 2000 |
  | 19970026105 | Supersonic Flying Qualities Experience Using the SR-71 | 1997 |
  | 20020057965 | Stability and Control Estimation Flight Test Results for the SR-71 with Externally Mounted Experiment | 2002 |
  | 19980223961 | Flight Testing the Linear Aerospike SR-71 Experiment (LASRE) (NASA TM-1998-206567) | 1998 |
  | 20110008312 | Systems Engineering Processes at NASA/SR-71 Pratt and Whitney J58 Engine | 2010 |
  | 20090007797 | Design and Development of the Blackbird: Challenges and Lessons Learned (Merlin, AIAA-2009-1522) | 2009 |
  | 20120013451 | Mach 3 Legend: Design and Development of the Lockheed Blackbird (Merlin, presentation) | 2012 |

- **Peter W. Merlin, "Mach 3+: NASA/USAF YF-12 Flight Research, 1969-1979"**, NASA SP-2001-4525, Monographs in Aerospace History 25, 162 pp (verified): https://www.nasa.gov/wp-content/uploads/2021/04/88796main_yf-12.pdf . Not in NTRS.
- Merlin's AIAA book "From Archangel to Senior Crown" (2008) is copyrighted and commercial: cite only. His NTRS papers are marked "public use permitted"; he wrote them as a contractor historian, and AIAA may hold the 2009 conference paper, so treat them as link-and-cite rather than certain PD.
- Don Mallick, "The Smell of Kerosene" (NASA SP-4108), first-person NASA test pilot memoir including YF-12 flying: https://www.nasa.gov/wp-content/uploads/2023/04/sp-4108.pdf (PD-USGov).
- Rights summary: NASA TM/TP/TN/CP by civil servants are PD-USGov; contractor reports (CR) and journal papers may not be.

### 2.5 NASA Armstrong fact sheets

- SR-71 (FS-030, verified): https://www.nasa.gov/wp-content/uploads/2021/09/495839main_fs-030_sr-71.pdf
- YF-12 (FS-2002-09-047): https://www.nasa.gov/wp-content/uploads/2021/09/fs-047-dfrc-04-20-20.pdf
- LASRE (FS-043): https://www.nasa.gov/wp-content/uploads/2021/09/120298main_FS-043-DFRC.pdf
- Index: https://www.nasa.gov/armstrong/meda-resources/fact-sheets/
- "Where Are They Now" airframe pages: SR-71A 844 https://www.nasa.gov/image-article/where-are-they-now-sr-71a-844/ ; SR-71B 831 https://www.nasa.gov/image-article/where-are-they-now-sr-71b-831/ ; YF-12 06935 https://www.nasa.gov/image-article/where-are-they-now-yf-12-06935/
- Legacy Dryden image pages now redirect to nasa.gov/image-article (e.g. ECN-4767 to https://www.nasa.gov/image-article/yf-12a-yf-12c-flight-formation-dawn/).

### 2.6 Oral histories

- **Library of Congress Veterans History Project** (API verified, no key): `https://www.loc.gov/collections/veterans-history-project-collection/?q=%22SR-71%22&fo=json` returns 4 collections with digitised video: Donald A. Walbrecht https://www.loc.gov/item/afc2001001.78206/ ; Buddy L. Brown https://www.loc.gov/item/afc2001001.66346/ ; Anthony P. Bevacqua (Area 51 and Beale) https://www.loc.gov/item/afc2001001.31405/ ; Kenneth M. Enright https://www.loc.gov/item/afc2001001.83494/ . Rights: the interviewees keep copyright; LOC says permission is needed to publish or exhibit. Link and summarise; ask families for clips.
- **San Diego Air & Space Museum oral histories** (via Calisphere, video; "contact the contributing institution"): BD-0011 Maury Rosenberg https://calisphere.org/item/710bd4416b712d795f3375ae2df61ce2/ ; BD-0066 Bill Weaver and Maury Rosenberg https://calisphere.org/item/9fd799963f587ee175730f487117a290/ (Weaver survived the 1966 SR-71 break-up) ; BD-0017 Richard Kantner, A-12/SR-71, 2013 https://calisphere.org/item/1a9cc1f25a5fc34cfe5b1667f9ad93c0/
- **Huntington Library**: Robert Gilliland (first SR-71 flight) transcript, 2010 https://calisphere.org/item/635fcc6e07a51a5a8f746e27bce7ea04/ (Huntington permissions policy).
- **UNLV Nevada Test Site Oral History Project**: "Roadrunners Internationale A-12 session", 5 Oct 2005, MS-00818 (nts_000095) https://special.library.unlv.edu/node/296850 (not verified, Cloudflare challenge).
- **Roadrunners Internationale** stories and videos (private, authors hold copyright): https://roadrunnersinternationale.com/stories.html , https://roadrunnersinternationale.com/videos.html . See section 5.
- NASA: no online oral-history transcripts were found for Fitz Fulton, Don Mallick, Rogers Smith or Ed Schneider on the SR-71/YF-12; Merlin's "Mach 3+" draws on unpublished Dryden interviews (a FOIA/archive request to the Armstrong history office is the route). NASA oral history index: https://www.nasa.gov/history/history-publications-and-resources/oral-histories/

### 2.7 Lockheed Martin / Skunk Works

- Pages (verified): https://www.lockheedmartin.com/en-us/news/features/history/blackbird.html ; Ben Rich https://www.lockheedmartin.com/en-us/news/features/history/rich.html ; https://www.lockheedmartin.com/en-us/who-we-are/business-areas/aeronautics/skunkworks/skunk-works-origin-story.html . (`.../history/sr-71.html` is a 404.)
- Rights: (c) Lockheed Martin. Terms (https://www.lockheedmartin.com/en-us/contact/disclaimer.html) forbid copying or republishing beyond one personal copy without written permission. SKUNK WORKS and the skunk logo are registered marks. Link only.

### 2.8 Air Force histories, DTIC, Congress

- AFHRA 9th Reconnaissance Wing lineage: https://www.afhra.af.mil/About-Us/Fact-Sheets/Display/Article/1181001/9-reconnaissance-wing-acc/ (403 to scripts; Wayback). NMUSAF D-21B fact sheet: https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/195778/lockheed-d-21b/ . No declassified 9th SRW unit histories found online: FOIA to AFHRA is the route.
- **DTIC**: no public API (discover.dtic.mil uses a Google custom search; apps.dtic.mil/sti showed a maintenance page). Use the Internet Archive `dticarchive` mirror: High Altitude Radiation Exposure in the SR-71 (1974) https://archive.org/details/DTIC_ADA131229 ; Deactivation of the SR-71 Program at Beale (1989/1990) https://archive.org/details/DTIC_ADA270753 and https://archive.org/details/DTIC_ADA270896 ; Sonic Boom Experiments at Edwards (1967) https://archive.org/details/DTIC_AD0655310
- **GovInfo** (API verified with DEMO_KEY): `POST https://api.govinfo.gov/search?api_key=DEMO_KEY` body `{"query":"\"SR-71\" collection:CRECB publishdate:range(1989-01-01,1990-12-31)","pageSize":20,"offsetMark":"*"}`. "SR-71" 1,251 hits; bound Congressional Record 1989-90: 66; 1994-98: 121. Best item: Sen. Byrd, "SR-71 Blackbird Summary Statement", 29 Jul 1994 (reactivation) https://www.govinfo.gov/content/pkg/CREC-1994-07-29/html/CREC-1994-07-29-pt1-PgS13.htm ; H.R. 4424 (1998) on spending FY1998 SR-71 funds https://www.govinfo.gov/content/pkg/BILLS-105hr4424ih/pdf/BILLS-105hr4424ih.pdf . PD-USGov.
- National Archives: LBJ's 29 Feb 1964 A-11 announcement material, NSC file, NAID 74258081 https://catalog.archives.gov/medialz/presidential-libraries/johnson/7624433/7624433-nsf-nscm-b1-f04.pdf

---

## 3. Video

### 3.1 NASA (PD-USGov)

- **NASA Armstrong YouTube** (https://www.youtube.com/@NASAArmstrong), all confirmed live via oEmbed: SR-71 Takeoff at Edwards AFB `bJ3kJbv3oVI`; SR-71 Blackbird Refueling in Flight `iKNS4DTj3io`; SR-71B Pilot Trainer Aircraft `w61qCsDg7II`; SR-71 LASRE in Flight `KrhJ3vFD3fE`; SR-71 LASRE Refueling from KC-135 `cxGbmAtfaX8`; YF-12A Coldwall Aerodynamic Heating Experiment `vJ-XDNl8u_4`; YF-12A Low-Level Test Flight `A5otH-MrEPQ`; YF-12A Landing `USsKznwIQxI`; YF-12C Mid-air Refueling `Ol7Tcza6wi0`; YF-12C Taxi and Takeoff `pIPOVuJrOF0`. Embed from YouTube; the footage is PD, so higher-quality source files can also be requested from NASA Armstrong or recovered from the Wayback copies below where they overlap.
- **Legacy Dryden movie gallery in the Wayback Machine** (verified, see 1.3): SR-71 clips EM-0025-01 to -07, YF-12 clips EM-0041-01 to -10, downloadable as .mov/.mpg via `https://web.archive.org/web/2010id_/http://www.dfrc.nasa.gov/Gallery/Movie/SR-71/480x/EM-0025-03.mov`.
- **Internet Archive**: "SR-71A/YF-12A takeoff and flight", Dryden 1978, EM-0041-01 https://archive.org/details/NIX-EM-0041-01 ; NTIS film "The SR-71" https://archive.org/details/gov.ntis.ava20323-vnb1 (public domain mark).
- images.nasa.gov has **no** Blackbird video (verified: 0 hits for SR-71, YF-12, LASRE, J58, Blackbird).
- "NASA and the SR-71: Back to the Future" (1991), NTRS 19950004304, is catalogued but has no download.

### 3.2 National Archives

- Digitised MP4s (catalogue flags "Restricted - Possibly"; confirm before mirroring, they are DoD productions but may contain licensed music or third-party footage):
  - NAID 148016899 "SR-71 LAST FLIGHT" (330-DIMOC-DFDEE980124, 466 MB): https://catalog.archives.gov/medialz/mopix/330/DIMOC/330-dimoc-dfdee980124.mp4
  - NAID 174689117 "The Record Breakers" (1974 New York to London record), 312 MB: https://catalog.archives.gov/medialz/mopix/330/DIMOC/330-dimoc-740901fzz999001.mp4
- Not yet digitised, use "Unrestricted" (RG 342 Air Force films): THE BLACKBIRD STORY (71778); SR-71 first and second flights at Edwards (72516); SR-71 crew preparation at Beale (71989); The Record Breakers (72098); Goldwater's SR-71B flight (71927). These are candidates for a NARA reproduction order or a research visit to the College Park motion picture research room.
- 111-DD DoD filmed news releases: "Development of the A11 Interceptor" (102044162), YF-12 test programme (102047730). Only shot lists are digitised.

### 3.3 CIA, NRO, DVIDS, Smithsonian

- CIA: "Archangel" https://www.youtube.com/watch?v=JXi7LkNipdc ; "The Debrief: Behind The Artifact: A-12 OXCART" https://www.youtube.com/watch?v=LPZJfChJLNs ; on the Internet Archive "Outrunning The Enemy: The CIA's A-12" and "Behind the Scenes: The A-12 Oxcart on Display at CIA Headquarters" (PD-USGov).
- NRO: A-12 end-of-programme 50th anniversary https://www.youtube.com/watch?v=0iyU79EK_9I
- DVIDS: images such as https://www.dvidshub.net/image/712841/sr-71-ship-1-ramp are marked "PUBLIC DOMAIN, Courtesy Photo NASA"; DVIDS video search is bot-blocked, use the API with a key.
- Smithsonian NASM YouTube (copyrighted, embed only): `wT4uwr_eJnY` (OXCART lecture), `suWhYA5EeD0` (record flight).
- Avoid: PeriscopeFilm "The Blackbirds Are Flying" uploads (Lockheed promotional film, unclear rights, resold commercially).


---

## 4. 3D models

### Verdict

There is **no CC0 or public-domain 3D scan of any Blackbird airframe** from an official source. Checked and confirmed absent:

- Smithsonian 3D (3d.si.edu / Voyager): the 3D API (`https://3d-api.si.edu/api/v1.0/content/file/search?q=Blackbird`) returned 0 for Blackbird, Lockheed and J58; it does return the 1903 Wright Flyer, Bell X-1 and Apollo 11 CM, so the search works and the SR-71 simply has not been published as 3D. The Smithsonian Open Access API with `online_media_type:"3D Images"` also returned 0 for SR-71 and Blackbird. The only "3D" NASM ever offered for 61-7972 was an early-2000s QuickTime VR cockpit panorama (nasm.si.edu/interact/qtvr/uhc), not a model.
- NASA 3D Resources (github.com/nasa/NASA-3D-Resources, 1,583 files checked; science.nasa.gov/3d-resources): no SR-71, YF-12, A-12, D-21, J58 or LASRE model. The aircraft present are things like the X-57.
- Sketchfab with `license=cc0`: 0 results for sr-71, sr71, blackbird, j58, lockheed.

### Best openly licensed candidates

| Model | Licence | Notes |
|---|---|---|
| "Lockheed SR-71 Blackbird" by Emmanuel Baranger (helijah), FlightGear `Aircraft/Lockheed-SR71` https://sourceforge.net/p/flightgear/fgaddon/HEAD/tree/trunk/Aircraft/Lockheed-SR71/ | **GPL v2** (COPYING in the repo), authors Baranger (3D), F-GTUX, BITW, Paolo Amoroso; v1.7, still updated 2026 | Best documented provenance. Same mesh as Baranger's Sketchfab upload https://sketchfab.com/3d-models/lockheed-sr-71-blackbird-1850c7bb7ac54902bd9868381ff8b652 (69,135 faces, marked "Free Standard" there). GPL obliges you to ship the licence and the editable source with any copy you serve; fine for a non-commercial open site, but the site's viewer code does not become GPL. |
| "SR71-BlackBird" (A and B variants), FlightGear `Aircraft/SR71-BlackBird` | GPL v2, by Gerard Robin, updated by the grtux hangar team | Older (2014). Includes the SR-71B trainer. |
| "SR-71 Blackbird" by Tyler Nichols (nicholtt) https://sketchfab.com/3d-models/sr-71-blackbird-40794825d2f64a6ca945990c8ff1e90f | CC BY 4.0, downloadable | 185,850 faces, untextured, "created from blueprints", 2014. Cleanest CC BY geometry candidate. |
| "Sr71" by manilov.ap https://sketchfab.com/3d-models/sr71-908985d8ec544638bcd661bc315597ad | CC BY 4.0, downloadable | 31,421 faces, the most-liked SR-71 on Sketchfab (129 likes). Good lightweight web viewer model. |
| "Lockheed SR-71 'Blackbird'" by KOG_THORNS (ioai25312) https://sketchfab.com/3d-models/lockheed-sr-71-blackbird-e2400e6119f5414c89e075654a82d30a | CC BY 4.0, downloadable | 49,063 faces, 2024. |
| "Lockheed SR-71 Blackbird" by Spark_Customs https://sketchfab.com/3d-models/lockheed-sr-71-blackbird-9076a8fb5a4340a9b6e543a2e4728a9c | CC BY 4.0 | 37,018 faces, 2025, has a cockpit. |
| Starlight Designs family set on Printables: SR-71 https://www.printables.com/model/199944-sr-71-blackbird , A-12 https://www.printables.com/model/200313-a12-oxcart , YF-12 https://www.printables.com/model/287914-yf-12 | CC BY | The only consistent A-12 / YF-12 / SR-71 trio found under an open licence. Print-oriented, so simplified; good for side-by-side "spot the difference" comparisons. |
| "J58 jet engine" by amadeussvx https://sketchfab.com/3d-models/j58-jet-engine-bca3015516304cfabe249cfad5363939 | CC BY-NC-SA 4.0 | Phone (Scaniverse) scan of a real J58, 262,638 faces. Usable on a non-commercial site, but NC and SA both bind any derivative. Only real-object J58 scan with an open licence. |

### Real scans that are NOT openly licensed (ask permission)

- "Lockheed SR-71A Blackbird" by Zoilo (iliedom) https://sketchfab.com/3d-models/lockheed-sr-71a-blackbird-e8888c4342bd40b3b95af3c6fcb0f963 : photogrammetry, 300,116 faces, description cites the Smithsonian aircraft. Sketchfab Standard licence, not downloadable. Strongest real-aircraft scan; worth a permission request.
- "GRADD SR-71 Blackbird / A12 J58 Engine" https://sketchfab.com/3d-models/gradd-sr-71-blackbird-a12-j58-engine-3d-model-9fe852b2c84b442bb112aec9c8c8b29e : 199-photo RealityCapture scan of the J58 at the Museum of Flight, 2.5M faces, Editorial licence, not downloadable.
- Cesar Ferrolho's SR-71 cockpit instruments (attitude indicator, altimeter, triple display indicator, flight stick) on Sketchfab: no licence, view only.

### Cautions

- "Lockheed SR-71 Blackbird" by klopikc (CC BY, 69,131 faces) is almost certainly a re-upload of Baranger's 69,135-face FlightGear mesh relabelled CC BY. Do not use it; use the GPL original.
- Several pairs have identical face counts (pkaran6254 and Qpup1 at 77,824) which suggests re-uploads. Check before trusting a CC BY label; fan models are sometimes ripped from games (DCS, MSFS, Ace Combat).
- Printables' most popular SR-71 models are CC BY-NC or BY-NC-ND (Faran Gillbanks, occupied_brain). NC is legally usable on a non-commercial site but ND forbids even re-texturing.
- Recommendation: ship the manilov.ap or nicholtt CC BY mesh for the web viewer now; send permission requests to Zoilo (scan) and to Baranger (to ask whether he will also release under CC BY); and ask NASM's Digitization Program Office whether 61-7972 is on their 3D list.

### Sketchfab and Printables APIs (verified)

- `https://api.sketchfab.com/v3/search?type=models&q=sr-71&downloadable=true&count=24&sort_by=-likeCount` (no key for search; add `&license=cc0` to filter; downloading requires an OAuth token).
- `https://api.sketchfab.com/v3/models/<uid>` gives licence URL, face count, author, publish date.
- Printables: undocumented GraphQL at `https://api.printables.com/graphql/` (POST `searchPrints2(query:"sr-71")` returns licence abbreviations). Works today but is not a public contract.

---

## 5. Legacy fan and veteran sites

(see section filled from legacy site research below)

---

## 6. Recommended licensing policy

The site's rule (show the history, cite every source, never take credit, never charge, never show ads) is a good ethic but it is **not a copyright licence**. Being free and ad-free does not make copying lawful; it only lowers the stakes. Build the policy on rights, not on goodwill.

### 6.1 Four tiers

| Tier | What | Action |
|---|---|---|
| **A. Mirror** | PD-USGov works (NASA, USAF/DoD, CIA, NRO, NARA federal records, NASA technical reports by civil servants); Smithsonian Open Access CC0; items explicitly CC0 or Public Domain Mark; LoC items marked "No known restrictions"; Flickr Commons "No known copyright restrictions" | Download the master, store it, display it, crop it. Credit the agency and photographer anyway (site rule), keep the source ID. |
| **B. Mirror under licence** | CC BY, CC BY-SA (Commons, Sketchfab, Printables, Flickr), GPL (FlightGear models) | Mirror with the full TASL credit (Title, Author, Source link, Licence link). Edits to a BY-SA file must be released BY-SA. Avoid NC and ND material unless nothing else exists; NC is legally fine for this site today but blocks any future change (a sponsor, a printed book sold at cost, a museum partnership), and ND forbids even colour correction. |
| **C. Link only** | Anything (c) without permission: fan-site photos, crew personal photos posted online, Lockheed Martin pages, commercial photo agencies, airliners.net, copyrighted books and magazine scans, YouTube uploads of TV documentaries | Link to the source and, for preservation, to a Wayback Machine snapshot. Write your own summary in your own words. Use the platform's official embed only where its terms allow (YouTube embed). |
| **D. Permission-gated** | Legacy fan and veteran sites, crew photo collections, museum archives that sell licences, the non-downloadable scans | Ask in writing (template below). Mirror only after a yes, and only within the scope granted. |

### 6.2 Traps to watch

- **Government site is not the same as government work.** CIA, NASA and USAF pages carry Lockheed company photos, contractor drawings, Pratt & Whitney imagery and "courtesy" images. Check the caption credit; "Lockheed photo" or "courtesy of" means Tier C/D unless it was published without notice before 1989 and you have done that analysis.
- **Contractor reports.** NASA Contractor Reports (CR) and Lockheed-authored reports on NTRS can be copyrighted even though NASA distributes them. NASA TM/TN/TP by civil servants are PD.
- **Declassified is not the same as public domain.** Declassification removes the secrecy marking only. A declassified CIA memo is PD because CIA employees wrote it; a declassified Lockheed proposal in the same release may not be.
- **Insignia and endorsement.** Do not use the NASA meatball, USAF symbol, CIA seal or Lockheed Martin "Skunk" logo as site decoration; they are protected marks. Carry the DVIDS/DoW non-endorsement line next to DoD imagery.
- **People in photos.** PD status covers the photo, not the publicity rights of an identifiable person; for a non-commercial history site this is low risk, but do not use crew portraits in anything that looks like advertising.
- **AI-generated or "colourised" images** found online have no reliable provenance. Do not use them; if the site ever makes its own colourisation, label it as such.
- **Fair use.** Do not build on it. It is a defence decided case by case after a dispute, not a permission, and "non-commercial" and "for preservation" are only two of the factors. A site whose purpose is to mirror other people's photos in full fails the "amount used" and "market effect" factors. The one place it is reasonable is short quotations of text with citation (a sentence or two from a book or interview to support your own writing). For images: link, ask, or leave out.
- **Wayback links are fine; Wayback copies are not a licence.** Linking to an archived page is safe. Re-hosting files you pulled from the Wayback Machine is the same as re-hosting them from the original site.

### 6.3 Recording provenance and permissions

Keep a machine-readable register in the site repository, one record per asset (YAML or JSON), for example:

```yaml
- id: nasm-2016-00596
  file: images/sr71/nasm2016-00596.tif
  sha256: <hash of the master as downloaded>
  title: "Lockheed SR-71 Blackbird, Udvar-Hazy Center"
  creator: "Smithsonian National Air and Space Museum"
  source_url: https://ids.si.edu/ids/download?id=NASM-NASM2016-00596.tif
  source_record: https://airandspace.si.edu/collection-objects/lockheed-sr-71-blackbird/nasm_A19920072000
  rights_as_found: "CC0. Third party or legal restrictions may apply to your use of these images."
  rights_snapshot: https://web.archive.org/web/<timestamp>/<record url>
  tier: A
  licence: CC0-1.0
  credit_line: "Smithsonian National Air and Space Museum (NASM2016-00596), CC0"
  retrieved: 2026-10-04
  permission: null
```

For Tier D add a `permission` block: who granted it (name, role, how you verified they own the rights), date, exact scope ("display and archive on <site>, credit as X, may be passed to the Internet Archive"), and a pointer to the stored evidence (the email saved as .eml or PDF in a private folder, not in the public repo). Save a Wayback snapshot of each rights statement at retrieval time (Save Page Now: `https://web.archive.org/save/<url>`) because rights pages change.

Show the credit line under every image, and generate a per-page "Sources" list from the register so nothing is ever uncredited. Publish a takedown and corrections contact and honour requests promptly.

### 6.4 Permission request template (short)

> I run <site>, a free, non-commercial, ad-free history of the Lockheed A-12, YF-12, M-21/D-21 and SR-71. Your <site/collection> holds <specific items>. May I display and archive copies of these on <site>, credited as you choose (proposed: "<credit>"), with a link back to you? Nothing is sold and there is no advertising. If you are willing, a Creative Commons Attribution 4.0 licence would let the material survive even if my site changes hands; a simple written yes for <site> alone is also welcome. You can withdraw permission for future use at any time.

Asking for CC BY 4.0 rather than a site-only permission is worth the extra sentence: it survives a change of owner or domain, and it lets Wikimedia Commons and the Internet Archive preserve the material too, which is the point of the preservation goal.

### 6.5 Licence for the site's own work

- **Original text**: CC BY-SA 4.0. It matches Wikipedia, so content can flow both ways, and the share-alike term stops anyone repackaging the site's writing into a paid product without giving it back. If the owner prefers maximum reuse, CC BY 4.0 is the alternative.
- **Structured data** (airframe database, timelines, serial histories, the provenance register metadata): CC0 1.0. Facts are not copyrightable anyway; CC0 removes any doubt and invites reuse by Wikidata and researchers.
- **Code**: MIT (or Apache-2.0 if patent language is wanted).
- State clearly in the footer that third-party material keeps its own licence, shown under each item, and that the site licence covers only the site's own work.
