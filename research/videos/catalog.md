# Article 121 video catalogue

Compiled 4 October 2026. This catalogue tries to list every moving-image (and key audio) record of the Lockheed A-12, YF-12, M-21/D-21 and SR-71 that we could find. For each one it records the best copy that exists, its rights, and whether we hold a local master. The machine-readable version is `catalog.json`, one record per item; it holds every field, source URLs, citations, sha256 checksums and duplicate copies. The downloaded masters are in `raw/`.

How to read the tiers (from `PLAN.md` section 6):

- **A** can be mirrored: US government work, CC0, public domain mark or "no known restrictions".
- **B** can be mirrored with the credit and licence.
- **C** is copyrighted: link only.
- **D** needs written permission before we host it.

Where an agency site carries contractor or third-party material, or NARA flags an item "Restricted - Possibly", the record says so in `rights_statement`, `caption_issues` or `notes`. Check those caveats before posting.

Every downloaded file keeps the URL it came from (`download_status`), its source page (`source_page_url`), the date we read it (`retrieved`) and, where we saved one, a Wayback snapshot of the page (`page_snapshot`). Lesser copies of the same footage are listed under `duplicates`, and where we also downloaded one, the duplicate entry carries its own `local_file` and `sha256`.

## At a glance

| Tier | Meaning | Items |
|---|---|---|
| A | US government work, CC0, PD mark or no known restrictions: can be mirrored | 129 |
| B | CC BY or CC BY-SA: mirror with credit and licence | 1 |
| C | Copyrighted: link only, never host | 208 |
| D | Permission needed before hosting | 75 |
| **All** | | **413** |

| Section | Items |
|---|---|
| Johnson announcement (24 July 1964) and the A-11 disclosure (29 February 1964) | 7 |
| Flight and test footage (USAF, DoD, newsreels, operations) | 63 |
| NASA research (YF-12, SR-71, LASRE) | 40 |
| CIA and A-12 OXCART | 13 |
| Museum and preservation | 67 |
| Interviews and oral histories | 155 |
| Documentaries, TV and other productions | 68 |

Local masters: **55 catalogued items** have a downloaded master; `raw/` holds **78 files, 16.2 GB** in all (the extra files are downloaded duplicate copies and multi-part programmes, each with its own sha256 in `catalog.json`). Tier A/B items still pending: **75** (47 exist only as undigitised NARA or LBJ Library originals, 28 are YouTube-only and were blocked, 0 other).

## 1. The Johnson announcement, 24 July 1964

### What happened

President Johnson announced the SR-71 at the start of his twenty-third news conference, held "in the State Department Auditorium at 3:30 p.m. on Friday, July 24, 1964" ([American Presidency Project transcript, from the Public Papers](https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-1053); [Wayback copy 2026-10-04](https://web.archive.org/web/20261004221017/https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-1053)).

### What he said (official transcript)

> I would like to announce the successful development of a major new strategic manned aircraft system, which will be employed by the Strategic Air Command. This system employs the new SR-71 aircraft, and provides a long-range, advanced strategic reconnaissance plane for military use, capable of worldwide reconnaissance for military operations.
>
> The Joint Chiefs of Staff, when reviewing the RS-70, emphasized the importance of the strategic reconnaissance mission. The SR-71 aircraft reconnaissance system is the most advanced in the world. The aircraft will fly at more than three times the speed of sound. It will operate at altitudes in excess of 80,000 feet. It will use the most advanced observation equipment of all kinds in the world.
>
> [...] The SR-7I [sic: OCR slip for SR-71 in the online text] uses the same J-58 engine as the experimental interceptor previously announced, but it is substantially heavier and it has a longer range. [...]
>
> This billion dollar program was initiated in February of 1963. The first operational aircraft will begin flight testing in early 1965. Deployment of production units to the Strategic Air Command will begin shortly thereafter.

Source: [American Presidency Project](https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-1053), item [1.] of the conference. The designation appears three times as "SR-71" (once mis-OCRed as "SR-7I") and once, separately, as "RS-70".

### RS-71 or SR-71: what the evidence says

| Evidence | What it says | Source |
|---|---|---|
| Official transcript (Public Papers text) | "SR-71" at every mention; "RS-70" once, in a separate sentence about the Joint Chiefs' review | [APP](https://www.presidency.ucsb.edu/documents/the-presidents-news-conference-1053) |
| The recording itself | A machine transcription of the conference audio (whisper.cpp small.en) hears "SR-71" at all three mentions and "RS-70" for the B-70. It still hears "SR-71" when it is deliberately prompted to expect "RS-71". **A person still needs to listen and confirm before we publish this.** | Audio of the [Miller Center film](https://millercenter.org/the-presidency/presidential-speeches/july-24-1964-press-conference-state-department), 0:34, 0:58, 1:39 |
| CIA, *Archangel* (2nd ed.), p. 53 | "After an initial contract for six RS-71s, the Air Force ordered 25 more in August 1963. When President Johnson disclosed the aircraft's existence in July 1964, he mistakenly transposed the designator letters. Air Force officials let the error stand and came up with the Strategic Reconnaissance (SR) category instead." | [CIA PDF](https://www.cia.gov/resources/csi/static/b45f5f8f5e4937963d9e9931313d84a4/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf) |
| Beale AFB, "This week in Beale History: SR-71 revealed" (24 Jul 2014) | "Then Air Force Chief of Staff General Curtiss Lemay preferred the SR (Strategic Reconnaissance) designation and wanted the RS-71 to be named the SR-71. After some debate, the designation was changed prior to the President's speech. Unfortunately, the information was not relayed in time for the media transcripts, which still had the RS-71 designation, thus creating the rumor that the president misread the aircraft's designation." The same article misdates the announcement to 25 July 1964. | [Wayback copy, 30 Nov 2024](https://web.archive.org/web/20241130160348/https://www.beale.af.mil/News/Article-Display/Article/667175/this-week-in-beale-history-sr-71-revealed/) |
| LBJ Library National Security File (digitised, NARA OCR) | We searched the OCR text of 52 digitised LBJ NSF folders for "RS-71". None contains it. No draft statement or press handout for 24 July 1964 was found online. The 29 Feb 1964 A-11 statement file is online (NAID 74258081). | [NARA catalog open data](https://nara-national-archives-catalog.s3.amazonaws.com/) |

**Conclusion.** Every primary source we can check has Johnson saying "SR-71": the official transcript says it, and the audio appears to agree (human check pending). The "RS-71" story rests on two things. First, "RS-71" was the designation before the announcement: the CIA says the contracts were for "RS-71s". Second, the Air Force says the press handouts still carried RS-71. The claim that Johnson "garbled" the name contradicts the recording and the transcript, and the CIA monograph repeats it without giving a source. Safe wording, matching `fact_notes.md`: "Johnson announced it as the SR-71; the old story that he garbled 'RS-71' is contradicted by the transcript and the recording."

### Recordings of the announcement: what exists, best copy first

1. **Film (moving image).** Our only find is a 32-minute black-and-white kinescope-style film of the whole conference. The Miller Center hosts it (Vimeo 1136213740, 480x360 at most, Miller Center logo burned in) and credits the LBJ Library as its source. **Tier D.** Ask the LBJ Library's audiovisual archives which film element it is, whether it is network pool coverage, and whether we can have a clean, higher-resolution transfer. The library says its CBS films are copyrighted except "footage of President Johnson's speeches", which is "pool coverage of live Presidential addresses". It says NBC and ABC films carry "copyright restrictions on all items" ([DiscoverLBJ film holdings, Wayback 2026-10-04](https://web.archive.org/web/20261004215404/https://discoverlbj.org/loh/av/av-film)).
2. **Audio master.** This is White House Communications Agency recording WHCA 107-1 at the LBJ Library, series NAID 34425227. The library describes that series as "Public domain", "100% digitized" and "Not yet available on DiscoverLBJ" ([DiscoverLBJ audio holdings, Wayback 2026-10-04](https://web.archive.org/web/20261004215428/https://discoverlbj.org/loh/av/audio)). **Tier A.** The best online copy is the LBJ Library's own YouTube slideshow, which sets the WHCA audio over photo 8736-J with Public Papers captions ([_GLxcw_hObY](https://www.youtube.com/watch?v=_GLxcw_hObY), uploaded 1 Jul 2014, 31:08). Its description reads "All public domain" and YouTube lists it as CC BY. **Pending download:** on 4 Oct 2026 YouTube refused every player request from this network. Fetch it by hand, or better, ask the LBJ Library for a WAV of WHCA 107-1. No permission is needed.
3. **Miller Center MP3** of the same conference: `https://d4q9blt8qjhv3.cloudfront.net/audio/spe_1964_0724_johnson.mp3`. It returns 403 to scripted clients.
4. **Not found** (each one checked):
   - **Universal Newsreel:** no SR-71 story. Release 60 (27 Jul 1964) and Release 61 (30 Jul 1964) have none (NARA NAIDs 234274839 and 234274840).
   - **USIA:** no film or audio for 24 July in NARA RG 306, although USIA filmed the 29 February conference.
   - **White House Naval Photographic Center:** no project for this date (NAID 595313 series list).
   - **Internet Archive:** no copy.
   - **Searches blocked by Cloudflare:** C-SPAN, CriticalPast, British Pathe/Reuters and AP Archive all refused scripted requests. A Wayback CDX search of CriticalPast found no clip of the announcement.

### Related: the A-11 disclosure, 29 February 1964

Johnson first revealed the family on 29 February 1964, as the "A-11" (the aircraft shown were YF-12As). Three recordings are catalogued below:

- **Universal Newsreel's story, "2,000-MPH Jet. Johnson Reveals U.S. Super Plane" (2 Mar 1964).** Downloaded, tier A. Universal donated the newsreel library to the public domain ([Commons PD-Universal Newsreel](https://commons.wikimedia.org/wiki/Template:PD-Universal_Newsreel)), but NARA's catalog still flags the releases "Restricted - Possibly".
- **USIA films of the conference** (NARA 306.3292 and 306.8249, not digitised).
- **The Miller Center film** (tier D).

Several YouTube uploads present the A-11 newsreel as the SR-71 announcement. They are miscaptioned.

### Catalogued items for this section

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| President Johnson's 6th Press Conference - February 29, 1964 (USIA film) | 1964-02-29 |  | U.S. Information Agency | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/49639) |
| PRESIDENT LYNDON JOHNSON PRESS CONFERENCE ON VIETNAM, PANAMA, CIVIL RIGHTS, SUPERSONIC... | 1964-02-29 |  | Voice of America (USIA) | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/123752) |
| 2,000-MPH Jet. Johnson Reveals U.S. Super Plane, 1964/03/02 (Universal Newsreel, Vol. 3... | 1964-02-29 | 0:01:54 | Universal Newsreel (Universal Pictures) | 720x480 | A | yes, `ia_1964-03-02_2000-MPH_Jet.mpeg` (52 MB) | [source](https://archive.org/details/1964-03-02_2000-MPH_Jet) |
| The President's News Conference, July 24, 1964 | 1964-07-24 | 0:31:08 | LBJ Presidential Library (slideshow); audio by... | not verified (YouTube player blocked for s... | A | pending | [source](https://www.youtube.com/watch?v=_GLxcw_hObY) |
| President Lyndon Johnson's Press Conference at the State Department, July 24, 1964 (Mil... | 1964-07-24 | 0:32:01 | UVA Miller Center (presentation); source credit... | 480x360 (Vimeo HLS top rendition, about 64... | D | no (tier D) | [source](https://millercenter.org/the-presidency/presidential-speeches/july-24-1964-press-conference-state-department) |
| WHCA audio recording 107 (WHCA107-1): President's News Conference, 24 July 1964 (origin... | 1964-07-24 |  | White House Communications Agency | audio only; original open-reel tape, digit... | A | pending | [source](https://catalog.archives.gov/id/34425227) |
| How the SR-71 Got it's Name |  | 0:01:06 | Spartan College of Aeronautics and Technology | 720x1280 (vertical short) | C | no (tier C) | [source](https://archive.org/details/youtube-RS6FwvnCLBw) |

## 2. Flight and test footage (USAF, DoD, newsreels, operations)

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| Footage Farm SR-71 reels: 'SR-71A Take Offs, Landings & Close Views 250212-07' and related | 1960s to 1980s (not dated) | 0:06:05 | Footage Farm Ltd (UK stock library; public-doma... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=LYWL4pT5YRk) |
| The SR-71 (USAF "Air & Space Power" short, Hill AFB, 1997) | footage 1960s to 1990s; programme 1997 | 0:01:20 | US Air Force, Media Production Flight, 367th Tr... | 640x480 | A | yes, `ia-ntis-ava20323-the-sr-71__ava20323-vnb1.mpeg` (48 MB) | [source](https://archive.org/details/gov.ntis.ava20323-vnb1) |
| Development of the A11 Interceptor (Now called the YF12A), Edwards Air Force Base, Cali... | 1964 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102044162) |
| New Missile Interceptor For U.S. Air Force (1964) | 1964 | 0:01:03 | British Pathe (FILM ID 3109.1) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=8HGI-5zQEvo) |
| YF-12A rollout and flight, Edwards AFB, California | 1964-09-27 to 1964-09-30 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/69131) |
| YF-12A, Edwards AFB, California | 1964-09-28 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/72055) |
| YF-12A preview, Edwards AFB, California | 1964-09-30 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/69122) |
| YF-12A landings, Edwards AFB, California | 1964-09-30 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/72517) |
| Universal Newsreel Volume 37, Release 79: "World's Fastest Plane" (first public flight... | 1964-09-30 |  | Universal Newsreel (story footage credited to H... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/234274858) |
| SR-71 first and second flights, Edwards AFB, California | 1964-12 (catalog coverage date 1964-12-21) |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/72516) |
| SR-71A First Flight | 1964-12-22 | 0:01:58 | Lockheed Martin (YouTube) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=QjCNBFS5CwE) |
| Distinguished Flying Cross to Five Air Force Officers For YF12A Record Flights, Washing... | 1965 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102044206) |
| YF12A Sets New Records, Edwards Air Force Base, California (DoD filmed news release) | 1965 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102048328) |
| 1965 AERIAL SR71 aircraft flies through the air | 1965 (per caption) | 0:00:14 | Archive Films (Getty Images Editorial) | 720x576 SD (master offered) | C | no (tier C) | [source](https://www.gettyimages.com/detail/video/news-footage/mr_00023840) |
| #TBT YF-12A Speed Run & Missile Launch | 1965 (spring) | 0:01:35 | Edwards Air Force Base (@EdwardsAirForceBase, U... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=ajwCX4PRkko) |
| YF-12A, Edwards AFB, California | 1965-02 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/70711) |
| YF-12A documentary, Edwards AFB, California | 1965-02-10 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/69379) |
| YF-12-A, Edwards AFB, California (record speed trial) | 1965-05-01 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/69415) |
| YF-12A (Edwards AFB, California): world record speed runs | 1965-05-01 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/69544) |
| YF-12A briefing, Edwards AFB, California (XAIM-47A launch) | 1965-12-17 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/69934) |
| United States Air Force Receives First Model of SR71B, Beale Air Force Base, California... | 1966 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102047666) |
| Strategic Air Command Semiannual Film Report (Feb-Jul 1966) | 1966-02/1966-07 | 0:29:51 | U.S. Air Force, Strategic Air Command; obtained... | 1920x1080 (16mm transfer) | A | yes, `ia-342-fr-375-sac-semiannual-film-report-1966__Strategic_20Air_20Command_20semiannual_20film_20report_20_28Feb_20-_20Jul_201966_29.mp4` (438 MB) | [source](https://archive.org/details/342-FR-375) |
| MD-21 Accident | 1966-07-30 (fatal D-21 launch collision; date from project knowledge, not the page) | 0:01:19 | Roadrunners Internationale (host); producer not... | 320x240 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |
| SR71 to Conduct Flight Tests, Various Locations (DoD filmed news release) | 1967 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102046842) |
| SR-71A, Beale AFB, California | 1968-11-06 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/71867) |
| PSD, Beale AFB, California (pressure suit fitting) | 1968-11-07 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/71259) |
| Senator Barry Goldwater's first flight in SR-71B, Beale AFB, California | 1969-04-02 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/71927) |
| Gen John P. McConnell's retirement, Andrews AFB, Maryland (flyover includes SR-71) | 1969-07-31 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/71231) |
| United States Air Force YF12 Test Program, Edwards Air Force Base, California (DoD film... | 1970 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102047730) |
| SYND 31/12/1970 US AIR FORCE TESTS SUPERSONIC YF - 12 | 1970 or earlier (AP date 31 Dec 1970) | 0:01:06 | AP Archive (syndicated news film) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=12hNWMrtzaE) |
| 1970s STRATEGIC AIR COMMAND FOOTAGE B-52, SR-71, U-2, TITAN II, MINUTEMAN MISSILE XD26895 | 1970s | 0:04:08 | PeriscopeFilm (reel of USAF footage) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=xNG3fWU9HCA) |
| Aim High (KC-135 refuelling an SR-71) | undated (1970s to 1980s) | 0:07:56 | US Air Force / Department of Defense (NARA RG 3... | 1920x1080 (4:3 film scan pillarboxed), 24 fps | A | yes, `nara_330-dimoc-ftbel1289.mp4` (131 MB) | [source](https://catalog.archives.gov/id/182800864) |
| The Record Breakers | 1971-04-26 and 1974-09-01 to 1974-09-13 | 0:17:22 | US Air Force / Department of Defense (NARA RG 3... | 1920x1080 (4:3 film scan pillarboxed), 24 fps | A | yes, `nara_330-dimoc-740901fzz999001.mp4` (312 MB) | [source](https://catalog.archives.gov/id/174689117) |
| SR-71 crew preparation, Beale AFB, California | 1971-08-31 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/71989) |
| The development of SR-71, and the SR-71 in flight, United States (CriticalPast clip ser... | 1972 (CriticalPast date) | 0:03:49 | CriticalPast LLC (resale of a USAF film) | 1920x1080 (HD master offered for sale) | C | no (tier C) | [source](https://www.criticalpast.com/video/65675028483_SR-71_Colonel-R-E-Sprinkel_plane-taking-off_Skunk-Work) |
| The Blackbird Story | c. 1972 (film); 1964-1972 content | 0:11:55 | U.S. Air Force (uploaded to YouTube by AIRBOYD) | 1734x1080 | A | yes, `commons-the-blackbird-story-1972__The_Blackbird_Story.webm` (479 MB) | [source](https://commons.wikimedia.org/wiki/File:The_Blackbird_Story.webm) |
| Attempt of U.S. Air Force SR71 Aircraft at World Record Speed Run, Various Locations (D... | 1974 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102043690) |
| SYND 31 8 74 NEW JET PLANE SR-71 | 1974-08-31 (AP date) | 0:01:46 | AP Archive (syndicated news film) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=f-Q8V1eXo8I) |
| USAF SR-71 Blackbird New York-London record during Farnborough 1974 | 1974-09 | 0:01:17 | Aviation videos archives part4 1975-2015 (YouTu... | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=MMCneQB3BnQ) |
| Farnborough Air Show 1974 Highlights | 1974-09 | 0:08:06 | FAST Aviation Archive (Farnborough Air Sciences... | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=i0wHkhB5MuU) |
| FARNBOROUGH AIR SHOW - COLOUR | 1974-09 | 0:08:34 | British Movietone (AP Archive) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=H5YzBTkX6KQ) |
| SR-71 taxis at Farnborough after record transatlantic flight (NBC News Archives clips v... | 1974-09-01 | 0:00:23 | NBC News Archives (licensed through Getty Images) | 720x480 SD (master offered) | C | no (tier C) | [source](https://www.gettyimages.com/detail/video/news-footage/1270757043) |
| SR-71 speed run, Beale Air Force Base, California, 13 September 1974 | 1974-09-13 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/62559) |
| SR-71 speed run, Beale Air Force Base, California, 27 July 1976 | 1976-07-27 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/62577) |
| Global Shield '79 (SAC exercise, includes SR-71B) | 1979-07 |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/72414) |
| Compilation of "Aim High" Recruitment Spots (includes SR-71) | 1980 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/166073165) |
| Video, Aim High: Air Force - Inflight Refueling of the SR-71 Blackbird, circa 1980. | c. 1980 | 0:01:14 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ouiW72qzh8U) |
| U-2R / SR-71A | 1981 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/604505) |
| KC-10A Refueling SR-71A | 1981-05-06 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/578527) |
| SR-71 Inflight Refueling 1989 | 1989 | 0:09:43 | Bill Baker (crew/tanker home video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=dlSVWo7__-k) |
| Lockheed SR-71 Blackbird 61-7976 At EAA AirVenture Oshkosh 7/31/89 | 1989-07-31 | 0:07:00 | YouTube user MiTbus (spectator video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=qDTECZShylA) |
| SR-71 Last flight from Kadena AFB Okinawa, Japan | 1990-01 | 0:08:05 | YouTube user H (H) (home video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=nFO--wzFfUs) |
| Jan. 19, 1990 -- Final SR-71 functional check flight at Kadena | 1990-01-19 | 0:02:02 | Armed Forces Radio and Television Service, Far... | not verified (YouTube player blocked); VHS... | A | pending | [source](https://www.youtube.com/watch?v=psUk_8vUtUw) |
| SR-71 RETIRED, RAF MILDENHALL, UK | undated (Detachment 4 closed 1990) |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/149280916) |
| SR-71 LAST FLIGHT | undated (probably early 1990; see notes) | 0:28:26 | US Air Force / Department of Defense (NARA RG 3... | 720x480 (29.97i source shown as 60 fps pro... | A | yes, `nara_330-dimoc-dfdee980124.mp4` (466 MB) | [source](https://catalog.archives.gov/id/148016899) |
| SR-71A AF REACTIVATED 1996 | 1996 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/147970933) |
| Clark Air Base gets a visit from a SR-71 |  | 0:00:59 | Armed Forces Radio and Television Service, Far... | not verified (YouTube player blocked); VHS... | A | pending | [source](https://www.youtube.com/watch?v=8LcldOcXIlE) |
| SR-71 Blackbird's First Test Flight |  | 0:01:20 | YouTube channel DOCUMENTARY TUBE (source film n... | 960x720 | C | no (tier C) | [source](https://archive.org/details/youtube-5RNdcArBrSM) |
| Lockheed SR-71 Blackbird Must See Clips |  | 0:02:12 | YouTube user Lee Gibson (airshow footage) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=N31eEXjNAUU) |
| Strategic Reconnaissance (U-2 and SR-71, for local TV) |  |  | US Air Force (NARA RG 342, Records of U.S. Air... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/62960) |
| Clip of the Commander-in-Chief of the U.S. Air Forces Europe (CINCUSAFE) (stock aerials... | undated |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/597853) |
| SR-71 | unknown | 0:00:10 | Roadrunners Internationale (host); producer not... | 192x144 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |
| F-0270 SR-71 | unknown | 0:03:01 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=fb6pquHLVDc) |

## 3. NASA research (YF-12, SR-71, LASRE)

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| YF-12 Test Program | catalog says 1960 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/148015381) |
| First Flight of YF12A Under Joint NASA/United States Air Force Test Program Takes Place... | 1969 |  | Department of Defense filmed news release (NARA... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/102044489) |
| YF-12A | 1970-06 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/575169) |
| YF-12 Take-off | 1970s | 0:00:20 | Roadrunners Internationale (host); producer not... | 640x480 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |
| Aeronautics and Space Report_69_71-75_77-79 | 1970s (YF-12 segment about 1971 to 1975) | 0:26:21 | NASA Armstrong Flight Research Center | 1920x1080 | A | yes, `nasa-aeronautics-space-report-compilation-yf12-mallick__NDTV000111ab-Aeronautics_and_Space_Report_69_71-75_77-79_orig.mp4` (3817 MB) | [source](https://images.nasa.gov/details/NDTV000111ab-Aeronautics_and_Space_Report_69_71-75_77-79) |
| YF-12C taxi and takeoff from Edwards Air Force Base | Circa 1970s | 0:00:34 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-05-yf12c-taxi-takeoff__EM-0041-05.mov` (6 MB) | [source](https://web.archive.org/web/20040817104349/http://www.dfrc.nasa.gov:80/gallery/Movie/YF-12/HTML/EM-0041-05.html) |
| YF-12C mid-air refueling | Circa 1970s | 0:00:27 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-06-yf12c-refueling__EM-0041-06.mov` (5 MB) | [source](https://web.archive.org/web/20040817104353/http://www.dfrc.nasa.gov:80/gallery/Movie/YF-12/HTML/EM-0041-06.html) |
| YF-12C approach and landing at Edwards Air Force Base | Circa 1970s | 0:00:32 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-07-yf12c-approach-landing__EM-0041-07.mov` (6 MB) | [source](https://web.archive.org/web/20040825023143/http://www.dfrc.nasa.gov:80/gallery/movie/YF-12/HTML/EM-0041-07.html) |
| YF-12A landing at Edwards Air Force Base | Circa 1970s | 0:00:25 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-08-yf12a-landing__EM-0041-08.mov` (5 MB) | [source](https://web.archive.org/web/20040830181349/http://www.dfrc.nasa.gov:80/gallery/Movie/YF-12/HTML/EM-0041-08.html) |
| YF-12C takeoff from Edwards Air Force Base | Circa 1970s | 0:00:20 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-09-yf12c-takeoff__EM-0041-09.mov` (4 MB) | [source](https://web.archive.org/web/20041107184844/http://www.dfrc.nasa.gov/Gallery/Movie/YF-12/HTML/EM-0041-09.html) |
| YF-12A low level test flight | Early 1970s | 0:00:41 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-02-yf12a-low-level__EM-0041-02.mov` (8 MB) | [source](https://web.archive.org/web/20030804000022/http://www.dfrc.nasa.gov:80/gallery/movie/YF-12/HTML/EM-0041-02.html) |
| Lunar Science Data / Aeronautics (NASA Aeronautics and Space Report): YF-12 segment wit... | 1971-09 |  | NASA | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/4145517) |
| 1973 NASA AERONAUTICS AND SPACE REPORT YEAR IN REVIEW SKYLAB VIKING MISSION TO MARS 19184 | 1973 | 0:14:50 | NASA 1973 report film (US government work); sca... | 960x540 | C | no (tier C) | [source](https://archive.org/details/19184-nasa-aeronautics-and-space-1973-man-in-space-vwr) |
| 1973 close up AERIAL PAN from tail to nose of YF-12 flying over desert (prototype for S... | 1973 (per caption) | 0:00:06 | Archive Films (Getty Images Creative) | 720x576 SD (master offered) | C | no (tier C) | [source](https://www.gettyimages.com/detail/video/news-footage/2045-2) |
| SR-71A/YF-12A takeoff and flight | 1974 (Dryden bib record); Internet Archive copy says 1978 | 0:00:27 | NASA Dryden Flight Research Center (now NASA Ar... | 352x240 | A | yes, `nasa-dryden-em-0041-01-sr71a-yf12a-takeoff-flight__EM-0041-01.mpg` (4 MB) | [source](https://web.archive.org/web/19990508141502/http://www.dfrc.nasa.gov:80/gallery/movie/YF-12/HTML/EM-0041-01.html) |
| NASA YF-12 Overview (film 'The Lockheed YF-12') | 1974 (per Commons) | 0:26:38 | NASA and U.S. Air Force | 604x360 | A | yes, `commons-nasa-yf12-overview-film-1974__NASA_YF-12_Overview.ogv` (96 MB) | [source](https://commons.wikimedia.org/wiki/File:NASA_YF-12_Overview.ogv) |
| YF-12A Coldwall Ground Separation Test - side view | Circa 1974 | 0:00:34 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-03-yf12a-coldwall-separation-side__EM-0041-03.mov` (6 MB) | [source](https://web.archive.org/web/20040803192742/http://www.dfrc.nasa.gov:80/Gallery/Movie/YF-12/HTML/EM-0041-03.html) |
| YF-12A Coldwall Ground Separation Test - front view | Circa 1974 | 0:00:37 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-04-yf12a-coldwall-separation-front__EM-0041-04.mov` (7 MB) | [source](https://web.archive.org/web/20040803193541/http://www.dfrc.nasa.gov:80/Gallery/Movie/YF-12/HTML/EM-0041-04.html) |
| YF-12A Coldwall Aerodynamic Heating Experiment | Circa 1975 | 0:00:39 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0041-10-yf12a-coldwall-heating__EM-0041-10.mov` (7 MB) | [source](https://web.archive.org/web/20060719191533/http://www.dfrc.nasa.gov:80/Gallery/Movie/YF-12/HTML/EM-0041-10.html) |
| NASA and the SR-71: Back to the Future | 1990 to 1991 | 0:04:58 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950004304) |
| SR-71 Arrival at NASA Dryden FRC | 1990-02-15 | 0:01:54 | YouTube user F104G826 (Dryden employee's VHS ca... | not verified (YouTube player blocked); VHS... | D | no (tier D) | [source](https://www.youtube.com/watch?v=3dgAUEgGsak) |
| SR-71 flight | 1990s | 0:00:10 | NASA Dryden Flight Research Center (now NASA Ar... | 352x240 | A | yes, `nasa-dryden-em-0025-01-sr71-flight__EM-0025-01.mpg` (1 MB) | [source](https://web.archive.org/web/19991005191046/http://www.dfrc.nasa.gov:80/gallery/movie/SR-71/HTML/EM-0025-01.html) |
| SR-71 flyover | 1990s | 0:00:14 | NASA Dryden Flight Research Center (now NASA Ar... | 352x240 | A | yes, `nasa-dryden-em-0025-02-sr71-flyover-844__EM-0025-02.mpg` (2 MB) | [source](https://web.archive.org/web/19991005205801/http://www.dfrc.nasa.gov:80/gallery/movie/SR-71/HTML/EM-0025-02.html) |
| SR-71 takeoff at Edwards Air Force Base | about 1991 | 0:00:44 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0025-03-sr71-takeoff-edwards__EM-0025-03.mov` (20 MB) | [source](https://web.archive.org/web/20030408191858/http://www.dfrc.nasa.gov:80/gallery/movie/SR-71/HTML/EM-0025-03.html) |
| SR-71 Blackbird refueling in flight | about 1991 | 0:00:35 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0025-04-sr71-refueling__EM-0025-04.mov` (16 MB) | [source](https://web.archive.org/web/20030405084440/http://www.dfrc.nasa.gov:80/Gallery/Movie/SR-71/HTML/EM-0025-04.html) |
| NASA Family Day 1992 SR71 Flyovers | 1992 | 0:01:09 | YouTube user Stephen Landers (home video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=Eqc-qZaYcis) |
| SR-71B Blackbird Dryden's Pilot Trainer Aircraft | circa 1992 | 0:00:29 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0025-07-sr71b-trainer__EM-0025-07.mov` (5 MB) | [source](https://web.archive.org/web/20030926104017/http://www.dfrc.nasa.gov:80/Gallery/Movie/SR-71/HTML/EM-0025-07.html) |
| EPIC NASA Tour at Edwards AFB March 1995 YF-23, SR-71A, SR-71B, B-52B, B-2, F-18s, F-15... | 1995-03 | 0:06:15 | YouTube user At The Fence 111 (home video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=FY1NCxvCkWg) |
| LASRE ground hotfire #2 | 1997 | 0:00:19 | NASA Dryden Flight Research Center (now NASA Ar... | 312x236 | A | yes, `nasa-dryden-em-0018-02-lasre-ground-hotfire-2__EM-0018-02.mov` (4 MB) | [source](https://web.archive.org/web/20010416232838/http://www.dfrc.nasa.gov:80/gallery/movie/LASRE/HTML/EM-0018-02.html) |
| NASA/Lockheed Martin Linear Aerospike SR-71 Experiment (LASRE) X-33 Ground Fire Test | 1997 to 1998 | 0:04:10 | YouTube channel 'X-33 Archive' (source footage... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=UN9KJWkNfFQ) |
| SR-71 LASRE during in-flight cold flow test | May 1998 | 0:00:11 | NASA Dryden Flight Research Center (now NASA Ar... | 352x240 | A | yes, `nasa-dryden-em-0018-01-lasre-inflight-cold-flow__EM-0018-01.mpg` (2 MB) | [source](https://web.archive.org/web/20000902074735/http://www.dfrc.nasa.gov:80/gallery/movie/LASRE/HTML/EM-0018-01.html) |
| SR-71 LASRE refueling in flight from a KC-135 | circa 1998 | 0:00:41 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0025-05-lasre-refueling-kc135__EM-0025-05.mov` (18 MB) | [source](https://web.archive.org/web/20030427192514/http://www.dfrc.nasa.gov:80/gallery/movie/SR-71/HTML/EM-0025-05.html) |
| SR-71 LASRE in flight over Mojave Desert | circa 1998 | 0:00:39 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0025-06-lasre-in-flight-mojave__EM-0025-06.mov` (17 MB) | [source](https://web.archive.org/web/20030623052304/http://www.dfrc.nasa.gov:80/Gallery/Movie/SR-71/HTML/EM-0025-06.html) |
| NASA Connect - TOAT - Wind Tunnels | 1999 | 0:02:36 | NASA Langley Research Center Office of Educatio... | 640x480 | A | yes, `nasa-connect-toat-wind-tunnels-sr71__NASATOAT-WindTunnels.mpg` (117 MB) | [source](https://archive.org/details/NasaConnect-Toat-WindTunnels) |
| SR 71 Blackbird last flight ever.Edwards AFB open house 1999. | 1999-10-09 | 0:08:52 | YouTube user mooneyes21 (spectator video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=I5URVG8nFBg) |
| The Case Of The Missing Blackbird / Check 6 Podcast | 2026 | 0:30:47 | AviationWeek | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=w3CXhRotie0) |
| YF-12A (SR-71 Blackbird) Landing at Edwards Air Force Base (~1970) / AiirSource |  | 0:00:24 | AiirSource Military (re-upload of NASA Dryden c... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=3B4ijozxEFs) |
| Lockheed Martin YF-12 SR-71 Blackbird Montage |  | 0:03:38 | AIRBOYD (montage of NASA Dryden clips) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=afOF-YnHdUg) |
| NASA Released Rare Footage Of The SR-71, The Fastest Plane To Ever Exist |  | 0:01:41 | Business Insider (compilation of NASA clips) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=tO_dYEAXg7Q) |
| YF-12C approach and landing at Edwards Air Force Base |  | 0:00:33 | Space Content (re-upload of NASA Dryden clip) | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=lrlWtglxqjY) |

## 4. CIA and A-12 OXCART

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| "Archangel" | 1960s archival footage; compiled for CIA by 2011 (exact production date not stated) |  | Central Intelligence Agency | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=JXi7LkNipdc) |
| The Fastest Plane in the World | 1960s archival; produced by 2017 | 0:10:13 | National Reconnaissance Office | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=CeTQhTtrTts) |
| First Flight A-12 | 1962-04 (first flight of Article 121; inferred from title and 'shalk' = Lou Schalk) | 0:02:25 | Roadrunners Internationale (host); producer not... | 320x240 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |
| A-12 First Flight | 1962-04-30 | 0:01:35 | Lockheed Martin (YouTube) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=psdtKHyefwA) |
| The 50th Anniversary Commemoration of the End of the A-12 OXCART | 2018-06-22 | 0:53:05 | National Reconnaissance Office | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=0iyU79EK_9I) |
| Behind the Scenes - The A-12 Oxcart on Display at CIA Headquarters | filmed at CIA HQ, Langley, c. 2019-2020 | 0:02:45 | Smithsonian National Air and Space Museum | 1280x720 (Internet Archive original .HD.mov) | C | no (tier C) | [source](https://www.youtube.com/watch?v=rWuC0izeIn4) |
| The Debrief: Behind The Artifact - A-12 OXCART | c. 2020 (CIA Museum, Langley) with archival inserts | 0:01:55 | Central Intelligence Agency | 1920x1080 | A | yes, `cia-debrief-behind-the-artifact-a12-oxcart__LPZJfChJLNs.mkv` (28 MB) | [source](https://www.youtube.com/watch?v=LPZJfChJLNs) |
| Outrunning The Enemy: The CIA's A-12 | c. 2020 (STEM in 30 'Perseverance' episode) | 0:03:40 | Smithsonian National Air and Space Museum | 1280x720 (Internet Archive original .HD.mov) | C | no (tier C) | [source](https://www.youtube.com/watch?v=p2RmWP0yynI) |
| A Look At the CIA's A-12 Oxcart | filmed at CIA campus, c. 2020 | 0:05:38 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=tJHs2OzwIF8) |
| The Debrief: Behind the Museum - CIA in the Sky | c. 2022 | 0:03:22 | Central Intelligence Agency | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=wD0N_3IcVqs) |
| Drones and the SR-71, dare we say more? |  | 0:00:51 | Lockheed Martin (YouTube) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=c0LUstcSMg0) |
| SR-71 Blackbird Midair Crash |  | 0:01:20 | YouTube user agouti6 (re-upload of declassified... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Gy0QUwxY5mQ) |
| L'Oxcart, un avion top secret |  | 0:02:34 | National Geographic (French channel), excerpt o... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=KwIuHDPgfY4) |

## 5. Museum and preservation

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| SR-71 landing at AF Museum Dayton OH2.wmv | 1990 | 0:02:55 | YouTube user John Kovacs (spectator video) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=Ib1EXdIam44) |
| 13News Now Vault: The fastest coast-to-coast flight ever recorded | 1990-03 (WVEC archive) | 0:01:59 | 13News Now | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=8qksDHfqvqM) |
| XR71 Dulles | 1990-03-06 | 0:05:02 | Michael Young | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=DoV12Nw156I) |
| NewsChannel2 Broadcasts, March 2-7, 1990 | 1990-03-06 | 2:03:23 | WMAR-TV (Baltimore), held by University of Balt... | 648x486 | C | no (tier C) | [source](https://archive.org/details/WMAR_NEWSB_013_033_DIG) |
| SR-71 Final Flight @ Palmdale to Dulles | 1990-03-06 (implied by title) | 0:02:53 | Sky Watcher_75 | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=2ctumhrjq-g) |
| Dedication of Article 128 on display at CIA Headquarters, Langley, VA Sep 19, 2007 | 2007-09-19 | 0:02:17 | Roadrunners Internationale (host); producer not... | 576x336 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |
| SR-71 Eclipse at Flight Test Museum | 2008 | 0:01:06 | FlightTestMuseum (@FlightTestMuseum), Flight Te... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=-UQ8lBmPTso) |
| Lockheed SR-71 Blackbird: Afterburner | c. 2010 | 0:00:31 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=_G6iG-DWJeg) |
| Lockheed SR-71 Blackbird - Buz Carpenter's Longest Flight | c. 2010 | 0:00:53 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=tJdOiNLD-K4) |
| Lockheed SR-71 Blackbird: Inlets | c. 2010 | 0:01:03 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=QUoplD1WalA) |
| Lockheed SR-71 Blackbird: Pressure Suit | c. 2010 | 0:00:32 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Vznuy7x6OSg) |
| Lockheed SR-71 Blackbird: Tires | c. 2010 | 0:00:33 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=S3x19vr96tk) |
| Lockheed SR-71 Blackbird - Record Flight | c. 2010 (Udvar-Hazy Center) | 0:00:46 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=suWhYA5EeD0) |
| #6 SR71.m4v | 2012 | 0:01:34 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=WwIP6EZFMDo) |
| Operation Blackbird | 2012 | 0:01:20 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=KbcPH7Jx-jQ) |
| Tour Guide Talks: Blackbird | 2012 | 0:01:34 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=o-nJUqgFWME) |
| SR-71 Blackbird: Making of a Mystery | c. 2012 | 0:02:57 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=fozCSFueJRM) |
| SR-71 Blackbird: Men & the Missions | c. 2012 | 0:02:51 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=QZyYI2lLyuU) |
| Museum of Aviation SR-71 Blackbird Lift onto Pedestals | 2013-04-05/2013-04-06 | 0:01:12 | Museum of Aviation RAFB (@MuseumofAviationRAFB) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=uHxz7ut7VyE) |
| A-12 OXCART on NBC | 2014-09-08 | 0:03:05 | NBC News (posted by Central Intelligence Agency... | 1920x1080 | C | no (tier C) | [source](https://commons.wikimedia.org/wiki/File:A-12_OXCART_on_NBC.webm) |
| CIA Museum on The Today Show | 2014-09-08 (NBC Today broadcast) | 0:04:39 | Central Intelligence Agency | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ZSnGHQCf_R0) |
| SR-71 at the National Museum of the United States Air Force | 2015-03-25 | 0:14:46 | Tech. Sgt. Nicholas Kurtz, Defense Media Activi... | 1920x1080 | A | yes, `dvids-396020-sr-71-nmusaf-broll__DOD_102322577-1920x1080-6221k.mp4` (692 MB) | [source](https://www.dvidshub.net/video/396020) |
| 4th Building Aircraft Moves 13-15 Oct 2015 | 2015-10-13/2015-10-15 | 0:03:35 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=VTvDpF7AK7k) |
| The SR-71 Blackbird - STEM in 30 | 2016 | 0:27:54 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=aFj5a8G_iGk) |
| STEM in 30 Focus on the SR 71 Blackbird | 2016-03-16 | 0:28:54 | Smithsonian National Air and Space Museum (STEM... | 1280x720 (Internet Archive NASA TV copy) | C | no (tier C) | [source](https://www.youtube.com/watch?v=VN4yw_6RaUU) |
| Geek Moment with the SR-71 Blackbird and STEM in 30 | c. 2016 | 0:00:31 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=fxiUtidtdQs) |
| 171117-F-DF621-SR-71 WASH | 2017-11-17 | 0:01:26 | Tech. Sgt. Shawn Bryant, 9th Reconnaissance Wing | 1280x720 | A | yes, `dvids-640384-sr-71-wash-beale__DOD_106216519-1280x720-2765k.mp4` (32 MB) | [source](https://www.dvidshub.net/video/640384) |
| SR-71 Ceremony (Barksdale Global Power Museum ribbon cutting) | 2017-12-03 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/640883835) |
| Aircraft of the Month: Lockheed A-12 | 2018 | 0:02:56 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Zc5bzKNW1Bk) |
| Year of Innovation - Lockheed A-12 | 2019 | 0:01:38 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=q1fsNksx9J4) |
| The SR-71 Blackbird on display at the Cosmosphere | 2021 | 0:02:18 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=_3W0ve0DuRc) |
| SR-71 Blackbird / Cold War icon | 2021 | 0:12:06 | Imperial War Museums | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Tn9U6hAlf14) |
| M-21 Blackbird / Curator on the Loose! | 2021 | 0:35:02 | The Museum of Flight | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Z5N1NnOWnDw) |
| March 17 - Aircraft Restoration Live - A12 Starter Cart | 2021-03-17 | 0:29:49 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=8B8Ch_ojvDo) |
| Air Zoo SR-71B YouTube Shorts and sub-2-minute clips (34 items) | 2021-2025 |  | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/channel/UCxW0CwwGllCPBfrWYGxirKw/shorts) |
| Newly renovated Lockheed A12 Aircraft | 2022 | 0:01:49 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=G0YpOAF7Rbs) |
| LOCKHEED A-12 vs. SR-71 | 2023 | 0:01:35 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=bjj_H7-YmFo) |
| Aircraft of the month - A12 | 2024 | 0:01:09 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=pVtNkYZCYbM) |
| AFRL Tech: Museum Series - J58 Engine | 2024-08-17 | 0:02:07 | Air Force Research Laboratory (AFRL History, Je... | 1920x1080 | A | yes, `dvids-935251-afrl-museum-series-j58__DOD_110534634.mp4` (65 MB) | [source](https://www.dvidshub.net/video/935251) |
| BD 0544 Spotlight Video   Lockheed A 12 Oxcart by Gordon Permann | c. 2024 | 0:03:41 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=i_T7RsA3cns) |
| Lockheed SR-71 "Blackbird" - Castle Air Museum | 2025 | 0:07:54 | Castle Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=leSaro5AOJg) |
| Curator Michael Hankins gives a quick tour of the SR-71 Blackbird | 2025 |  | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=wRD1PMivFWk) |
| A-12 Oxcart: The CIA's secret weapon | 2026 |  | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=AZY_cGs-ugY) |
| A-12 Oxcart | 2026 | 0:00:50 | Intrepid Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=wndLDlhcIss) |
| The way you started up an SR-71 Blackbird was weird. | 2026 |  | The Museum of Flight | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=NBUqNA8MPLM) |
| Differences between the SR-71A and SR-71B |  | 0:01:23 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=4dEmpImilvs) |
| The Pratt & Whitney J58 - The Engine of the SR-71 Blackbird |  | 0:24:49 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=MJrXUh0eZjw) |
| The Pratt & Whitney J58 - The Engine of the SR-71 Blackbird / Part Two |  | 0:39:57 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ifYSIeyhikA) |
| Opening an SR-71 Blackbird Cockpit |  | 0:01:58 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ydQl5RuL3gM) |
| SR-71 ABC's |  | 0:03:09 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=tOzrZS-7tbI) |
| SR-71 Flight Control Stick |  | 0:01:28 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=TBbdXDJ0ffY) |
| The Lockheed SR-71 Blackbird's METAL tires! |  | 0:01:42 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=nYdqHXiTHtY) |
| SR-71 Quick Facts Compilation |  | 0:09:12 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=4JmtXfkCJEc) |
| 'We got every one and broke it' - The SR-71's Start Cart |  | 0:02:45 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=KoD6kFb85co) |
| SR-71C at Hill Aerospace Museum - Mission "Get Shaba" |  | 0:02:26 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=1gs8O6T9wxQ) |
| The YF-12: The Armed Blackbird |  | 0:01:17 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=of45AS8eW7o) |
| 360° Video:  U.S. Air Force Flight Test Museum |  | 0:03:47 | Edwards Air Force Base (@EdwardsAirForceBase) | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=_XB-L_DQVg0) |
| Do you remember the SR-71 Blackbird and the YA-7F Strikefighter? #shorts #airforce #his... |  | 0:00:35 | Edwards Air Force Base (@EdwardsAirForceBase) | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=olxPSppy4-8) |
| SR-71 Blackbird - The Fastest Jet Aircraft Ever Built |  | 0:01:00 | Flight Test Museum (@TheFlightTestMuseum), Flig... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=OguJYMx5-dE) |
| Dan & Draco discuss the SR-71! |  | 0:02:51 | Frontiers of Flight Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=jP4A6-G11Oo) |
| Lockheed SR-71 "Blackbird" Strategic Reconnaissance Aircraft / Hill Aerospace Museum |  | 0:01:46 | Hill Aerospace Museum (@HillAerospaceMuseum) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=buduZxV0sIE) |
| SR-71 "Blackbird" Fastest Airplane in the World |  | 0:00:57 | Museum of Aviation RAFB (@MuseumofAviationRAFB) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=xq_g8p2kgnc) |
| Pratt & Whitney J58 Turbojet (Drone View) |  | 0:03:34 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=6tFmNY94Aic) |
| Lockheed SR-71A |  | 0:03:19 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=xLmxyJSbimE) |
| Lockheed SR-71A at the National Museum of the USAF |  | 0:01:40 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=-NiomYlfOyw) |
| Friday Dec. 17 & Saturday, Dec. 18, 2021 - Look inside the cockpit of the Lockheed SR-71A. |  | 0:01:40 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=DoOkG3LHLOE) |
| SR-71 Blackbird Memorial (Barksdale Global Power Museum installation) | undated |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/564394098) |

## 6. Interviews and oral histories

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| Vault Visit / NC A&T professor shares his experience with the fastest plane in history | 1990-03 (WFMY archive) | 0:01:18 | WFMY News 2 | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=o6r6suAy4M0) |
| F-16XL Interview with Marta Bohn-Meyer | 1992 | 0:30:15 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950013580) |
| Frank Murray talking about A-12 pilot training and Kadena missions (2005) | 2005 | 0:11:44 | Roadrunners Internationale (host); producer not... | 960x540 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |
| Ivie Wesley Chandler, Jr. Collection | 2005-04-11 | 1:09:59 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.26323/) |
| Former NASA Research pilot Ed Schneider Aerospace Walk of Honor Induction Ceremony | 2005-09-24 | 0:00:49 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0086-03-ed-schneider-walk-of-honor__EM-0086-03.mov` (10 MB) | [source](https://web.archive.org/web/20060222190850/http://www.dfrc.nasa.gov:80/Gallery/Movie/People/HTML/EM-0086-03.html) |
| Former NASA Research pilot Ed Schneider Aerospace Walk of Honor Induction Ceremony Comm... | 2005-09-24 | 0:01:17 | NASA Dryden Flight Research Center (now NASA Ar... | 640x480 | A | yes, `nasa-dryden-em-0086-04-ed-schneider-comments__EM-0086-04.mov` (15 MB) | [source](https://web.archive.org/web/20060222190856/http://www.dfrc.nasa.gov:80/Gallery/Movie/People/HTML/EM-0086-04.html) |
| Roadrunners Internationale A-12 session (Nevada Test Site Oral History Project) | 2005-10-05 |  | UNLV Libraries Special Collections, Nevada Test... | unknown (catalog record only) | D | no (tier D) | [source](https://special.library.unlv.edu/node/296850) |
| Anthony Philip Bevacqua Collection | 2005-11-18 | 0:29:52 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.31405/) |
| Retired NASA Pilot Fitz Fulton Comments on 747/Columbia Crosswind Landing at KSC | 2006-04-10 | 0:01:08 | NASA Dryden (now Armstrong) Flight Research Center | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=vs3ZvmDmVq0) |
| BG Dennis Sullivan on gear down at Mach 3 | Roadrunners reunion (2007 per Roadrunners page) | 0:01:52 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=OW2XoBDXG9k) |
| Troy Wade introduction of Roadrunners of Groom Lake | 2009 | 0:03:19 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=5HMMyHusppg) |
| Buddy L. Brown Collection | 2009-08-04 | 0:58:37 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.66346/) |
| Michael L. Cherry Collection | 2009-08-28 | 0:30:41 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.66815/) |
| T D Barnes intro Oxcart panel | 2009-10 | 0:04:26 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=AT5J8a8iWOE) |
| Roadrunners 2009: Mission Planners (Harold Mills, Sam Pizzo, Al Rossetti) and P&W J58 i... | 2009-10 | 1:16:52 | Roadrunners Internationale (host); producer not... | audio only | D | no (tier D) | [source](https://roadrunnersinternationale.com/c-span_symposium.html) |
| TD Barnes Intro Project Oxcart | 2009-10 (Atomic Testing Museum symposium) | 0:09:58 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=m8KgZZBqVwo) |
| Roadrunners 2009 Symposium Panel 2 (Spy Planes of Groom Lake) | 2009-10 (Las Vegas) | 1:53:40 | Roadrunners Internationale (host); producer not... | 320x240 | D | no (tier D) | [source](https://roadrunnersinternationale.com/c-span_symposium.html) |
| Engineer Fred White intro to A-12 | 2009-10 (symposium) likely | 0:02:18 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=swpxb1J5gdw) |
| Engineer Wayne Pendleton about RCS of A-12 | 2009-10 (symposium) or reunion; not stated | 0:06:53 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=NbvA8TsI4ms) |
| T D Barnes and Lt Gen Dick Leavitt on Blackbird Replacement | 2009-10 likely | 0:02:08 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=5dnuWnCVyFs) |
| BGen CIA pilot Dennis Sullivan about Project Oxcart | 2009-10 likely | 0:09:31 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=9Fqv3pZkKzo) |
| Frank Murray A-12 abort landing | 2009-10 likely | 0:04:16 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=euYcCLknNk4) |
| CIA A-12 PIlot Frank Murray on Oxcart at Groom Lake | 2009-10 likely | 0:02:34 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=2O-jZDSVuhM) |
| Groom Lake House Six Stories | 2009-10 likely | 0:07:13 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=FZWan6GIyWc) |
| Robert Rodert of Project Oxcart | 2009-10 likely | 0:07:48 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=zt-iSIwRuHQ) |
| Major Ron Girard USAF 1129th SAS Groom Lake | 2009-10 likely | 0:04:04 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=JtBrU5Ctab8) |
| Col Sam Pizzo on CIA selection Project Oxcart | 2009-10 likely | 0:04:21 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=trWG9M0iiAk) |
| T D Barnes on Groom Lake wives | 2009-10 likely | 0:04:05 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=DmwqyCXqSZY) |
| Spy Planes of Groom Lake | 2009-10-07 | 2:02:17 | C-SPAN (American History TV) | not verified (HLS stream) | C | no (tier C) | [source](https://www.c-span.org/program/american-history-tv/spy-planes-of-groom-lake/213696) |
| George Knapp introduction of Groom Lake Panelists | 2009-10-07 | 0:03:57 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=JPeP3ILQLx8) |
| Peter W. Merlin Dreamland America's Black Shield - Atomic Testing Museum - Oct 7, 2009 | 2009-10-07 | 0:01:07 | Quintessential Studios | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=bK0ob0SGP-A) |
| CIA A-12 pilot Ken Collins comments on Lockheed test pilots | c. 2009-2010 | 0:01:17 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=oQefpXyCYwo) |
| T D  BARNES  PROJECT OXCART | c. 2009-2010 | 0:06:47 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=2be1Yc4SLRs) |
| Tribute to MSGT Leland Haynes, Crew Chief of the SR-71 | 2010 | 0:04:23 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=KJDM3EbSI6w) |
| Presentation on Project OXCART at Defense Intelligence Agency in September 2010 | 2010-09 | 2:10:24 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=Psf4Ywz7Aqo) |
| Innovations Toward Invisibility: The CIA's OXCART Project and A-12 Reconnaissance Aircraft | 2010-09-24 | 1:29:50 | Smithsonian National Air and Space Museum | audio archive (per description); picture n... | C | no (tier C) | [source](https://www.youtube.com/watch?v=wT4uwr_eJnY) |
| OXCART Legacy Tour at Smithsonian's National Air and Space Museum in September 2010 | 2010-09-24 | 1:29:47 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=IuJPyuLQWt8) |
| Letter to Kelly Johnson | compiled 2010 from archival footage | 0:05:41 | NevAerospaceHOF (Nevada Aerospace Hall of Fame) | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=q4ye--F7I6s) |
| Book TV : CSPAN2 : September 10, 2011 8:00am-9:00am EDT (Annie Jacobsen, 'Area 51') | 2011 | 1:00:01 | C-SPAN2 Book TV; IA TV News Archive capture | 640x480 | C | no (tier C) | [source](https://archive.org/details/CSPAN2_20110910_120000_Book_TV) |
| Donald Augustus Walbrecht Collection | 2011-07-11 | 1:13:59 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.78206/) |
| Arthur Edwin Roberts Collection | 2011-08-26 | 1:26:33 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.79394/) |
| Archangel CIA's Supersonic Seminar.mp4 | 2011-10-04 | 0:59:57 | UNLVEngineering | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=HsdhBTOuUKg) |
| Joseph Francis Godlewski Collection | 2011-12-22 | 0:59:25 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.81244/) |
| Kenneth Maurice Enright Collection | 2012-06-29 | 1:42:51 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.83494/) |
| Brian Shul Shares his Inspiring Story of Flying an SR-71 Blackbird - LeWeb Paris 2012 | 2012-12 (LeWeb Paris) | 0:58:08 | LeWeb | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=o_Gyd6EYuXI) |
| The YF 12A Story and The People Who Kept Them Flying | c. 2012-2018 | 0:35:05 | Atomic Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=McgiotcDI8w) |
| Blackbird: The Fastest Spy Plane (Extended Cut) - SR-71 | 2013 | 0:44:30 | Montgomery College Television (Access to History) | 1920x1080 | D | no (tier D) | [source](https://archive.org/details/mctvafmd-Blackbird_-_The_Fastest_Spy_Plane_Extended_Cut_-_SR-71) |
| BD-0017 Richard Kantner Oral History  A-12/SR-71 Blackbird  9 23, 2013 | 2013-09-23 | 1:27:20 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=crRooDs8XYU) |
| BD-0011 Flying the Lockheed SR-71 with Maury Rosenberg Oral History | c. 2013 (uploaded 2013-06-12) | 1:03:15 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=RSOaKaFIgAs) |
| BD-0012 Frank Murray Oral Interview, Lockheed A-12, 4/29/14 | 2014-04-28 or 2014-04-29 | 1:26:37 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=SSTRXGP0nWM) |
| Michael Hall Johnson Collection | 2014-12-02 | 2:01:48 | Library of Congress Veterans History Project (i... | audio only | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.96729/) |
| SR-71 Pilot Maury Rosenberg | c. 2014 | 0:52:56 | PeninsulaSrsVideos | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=-5nSKLyrM1s) |
| SR 71, A 12, and U 2 Spy Plane Pilot Interviews | c. 2014 (Blackbird Airpark) | 0:54:31 | PeninsulaSrsVideos | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=K6qmTjXWoA8) |
| SR-71 A-12 U-2 Spy Planes: 50-year Cold War Commemoration | c. 2014 (Blackbird Airpark, Palmdale) | 0:58:30 | PeninsulaSrsVideos | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=47DnjpCkelA) |
| yeilding final1 (with 'Yeilding rough' and 'Yeilding rough2') | 2015 | 0:00:28 | Montgomery CCC (community channel, as IA credit... | 1920x1080 | D | no (tier D) | [source](https://archive.org/details/mcccal-yeilding_final1) |
| Ed Yeilding Visits - TROY TrojanVision News | 2015 | 0:01:40 | Troy University TrojanVision | 1920x1080 | D | no (tier D) | [source](https://archive.org/details/ttval-Ed_Yeilding_Visits_-_TROY_TrojanVision_News) |
| Mike Relja and the Destruction of the SR-71 Spares | 2015 | 0:46:25 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=hWJMHO00s8Q) |
| Pete Law's presentation as part of Kelly Johnson Month | 2015 | 0:59:59 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=OVBCIQHpQ4k) |
| Ken O'Donoghue Collection | 2015-08-17 | 1:39:42 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.99988/) |
| Ed Yeilding, Fastest Trojan | 2015-11 | 0:41:22 | TROY TrojanVision | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=l3Z-M6urAUE) |
| Ed Yeilding: World's Fastest Trojan | 2015-11-06 | 0:04:03 | Troy University | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=BkfVaUYB1LQ) |
| Brian Shul - From Butterflies to Blackbirds | c. 2015 | 0:52:40 | TheIHMC | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=3kIMTJRgyn0) |
| Episode 15  Brian Shul talks about piloting the SR 71 Blackbird spy plane | 2016 | 0:58:49 | TheIHMC | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=lX5rJATrtHU) |
| James C. Baranowski Collection | 2016-05-11 | 0:53:58 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.102648/) |
| SR-71 Blackbird Pilot Presentation | 2016-06-08 | 0:57:51 | Chris Rand | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=KhPY_6rIjvk) |
| FLYING THE SR-71 BLACKBIRD | 2016-10-06 | 0:51:56 | U.S. Space & Rocket Center | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=4eV4SuUagFU) |
| Author Brian Shul on piloting the SR-71 | 2016-11-15 | 1:10:57 | Lawrence Livermore National Laboratory (@Liverm... | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=wigZsFypdyI) |
| John M. Pietz Collection | 2016-11-30 | 0:34:53 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.105064/) |
| A look at the SR-71 | c. 2016 | 0:14:23 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=F4KD5u-xkik) |
| Tales of the SR-71 Blackbird from Col Buz Carpenter | c. 2016 | 0:04:24 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=GJP1ZQjzPyE) |
| BD-0066 Oral History, Bill Weaver and Maury Rosenberg Lockheed SR-71 Pilots | c. 2016 | 1:52:40 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=vGA8Jej_JtI) |
| SR-71 Overview by Col. James H Shelton, Jr USAF (ret.) | c. 2016 (Western Museum of Flight) | 0:58:30 | PeninsulaSrsVideos | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ptPRi7R3Bfw) |
| The SR-71 by Harlan Hain & Charlie Daubs | c. 2016-2017 | 1:37:57 | Curtis E LeMay Flight (16th Flight) Daedalians | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Y8bxdSwx5oU) |
| Major Brian Shul, USAF (Ret.) SR-71 Blackbird 'Speed Check' | 2017 | 0:05:59 | audience recording by Jan Johnson; speaker Bria... | 1920x1080 | D | no (tier D) | [source](https://www.youtube.com/watch?v=8AyHH9G9et0) |
| First Panel of the 2017 SR-71 Weekend at MFAM | 2017-04 | 1:18:48 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=YhrYJKXrb1k) |
| SR-71 Weekend 2017, Fourth Panel | 2017-04 | 1:35:51 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=_qBJR4x6UBs) |
| SR-71 Weekend 2017, Panel 2 Discussion | 2017-04-01 | 1:02:47 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=DlJYxQai8Ls) |
| SR-71 Instrument Panel Discussion | 2017-04-02 | 0:58:06 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=-ABsri8HaeM) |
| SR-71 Weekend 2017, Third Panel | 2017-04-02 | 0:58:49 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ndfitO-QuZk) |
| The Oxcart Story - Frank Murray | 2017-04-22 | 1:23:59 | Chris Johnson | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=MGdxpqqsHl8) |
| Veterans in Blue 2017 - Tony Bevacqua | 2017-05-16 | 0:02:11 | 9th Reconnaissance Wing Public Affairs, Beale A... | 1920x1080 | A | yes, `dvids-562694-veterans-in-blue-bevacqua__DOD_105043310-1920x1080-6221k.mp4` (105 MB) | [source](https://www.dvidshub.net/video/562694) |
| SR-71 Returns | c. 2017 | 0:58:51 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=K5dxCTScVhI) |
| Swedish pilots presented with U.S. Air Medal Full Ceremony | 2018-11-28 | 1:07:05 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1280x720 | A | yes, `dvids-644209-swedish-pilots-air-medal-full-ceremony__DOD_106258000-1280x720-2765k.mp4` (1477 MB) | [source](https://www.dvidshub.net/video/644209) |
| Swedish pilots presented with U.S. Air Medal - Major Krister Sjoberg Interview | 2018-11-28 | 0:01:07 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644272-sjoberg-interview__DOD_106258411-1920x1080-6221k.mp4` (54 MB) | [source](https://www.dvidshub.net/video/644272) |
| Swedish pilots presented with U.S. Air Medal - Major Roger Moller Interview | 2018-11-28 | 0:01:58 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644280-moller-interview__DOD_106258461-1920x1080-6221k.mp4` (95 MB) | [source](https://www.dvidshub.net/video/644280) |
| Swedish pilots presented with U.S. Air Medal - Colonel Lars-Erik Blad Interview | 2018-11-28 | 0:02:30 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644283-blad-interview__DOD_106258467-1920x1080-6221k.mp4` (120 MB) | [source](https://www.dvidshub.net/video/644283) |
| Swedish pilots presented with U.S. Air Medal - Colonel Per-Olof Eldh Interview | 2018-11-28 | 0:02:55 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644289-eldh-interview__DOD_106258476-1920x1080-6221k.mp4` (141 MB) | [source](https://www.dvidshub.net/video/644289) |
| Swedish pilots presented with U.S. Air Medal - Lt. Col. (Ret.) Tom Vetri | 2018-11-28 | 0:04:43 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644294-veltri-interview__DOD_106258487-1920x1080-6221k.mp4` (226 MB) | [source](https://www.dvidshub.net/video/644294) |
| Swedish pilots presented with U.S. Air Medal | 2018-11-30 | 0:00:43 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644195-swedish-pilots-air-medal-package__DOD_106257818-1920x1080-6221k.mp4` (35 MB) | [source](https://www.dvidshub.net/video/644195) |
| Swedish pilots presented with U.S. Air Medal - AFN w/titles | 2018-11-30 | 0:01:00 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644234-swedish-pilots-air-medal-afn-titles__DOD_106258274-1920x1080-6221k.mp4` (47 MB) | [source](https://www.dvidshub.net/video/644234) |
| Swedish pilots presented with U.S. Air Medal - AFN no titles | 2018-11-30 | 0:01:00 | SSgt Kelly OConnor, 100th Air Refueling Wing (R... | 1920x1080 | A | yes, `dvids-644259-swedish-pilots-air-medal-afn-no-titles__DOD_106258341-1920x1080-6221k.mp4` (47 MB) | [source](https://www.dvidshub.net/video/644259) |
| Test Flying the World's Fastest Airplanes. Robert J. Gilliland | 2019 | 0:50:29 | Doctors for Disaster Preparedness (DDPmeetings)... | 640x480 | D | no (tier D) | [source](https://www.youtube.com/watch?v=amA8bG5E-uU) |
| Col Buz Carpenter and the SR-71 Blackbird- What's New in Aerospace | 2019 | 0:28:08 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=uk_xV6bb6MU) |
| Gathering of Eagles-Col. Walter Watson Jr. | 2019-04-04 | 0:02:05 | Billy Blankenship, Air University Public Affairs | 1280x720 | A | yes, `dvids-670098-gathering-of-eagles-walter-watson__DOD_106607475-1280x720-2765k.mp4` (46 MB) | [source](https://www.dvidshub.net/video/670098) |
| Final Panel from SR-71 Weekend 2019 | 2019-04-07 | 1:32:09 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=7btMhn7q0A4) |
| SPYCAST WITH TD BARNES | c. 2019 | 0:53:17 | Atomic Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=-bKb9lTny_E) |
| TD Barnes: Project Oxcart The CIA at Area 51 | c. 2019 | 1:49:35 | Atomic Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=hwvwLFa5ceo) |
| Flying the SR-71 Blackbird - BC Thomas (Part 2) | 2020 | 1:55:50 | 10 Percent True - Tales from the Cockpit | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=fPsyshPWTtY) |
| Flying the SR-71 Blackbird - BC Thomas (Part 3) | 2020 | 1:12:45 | 10 Percent True - Tales from the Cockpit | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=IJEeFC6mNt8) |
| Flying the SR-71 Blackbird - BC Thomas (Part 4) | 2020 | 1:01:34 | 10 Percent True - Tales from the Cockpit | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=bIkJJcxptO0) |
| Flying the Lockheed SR-71 Blackbird - BC Thomas (Part 5) | 2020 | 0:35:39 | 10 Percent True - Tales from the Cockpit | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=T33YUfUTg4U) |
| The SR-71 Blackbird: Student Edition - STEM in 30 Mission Debrief | 2020 | 0:33:20 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=t4znFoyuzfk) |
| SR-71 RSO Walter Watson: My Path | 2020 | 0:03:13 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=70X20f1sEWs) |
| The SR-71 Blackbird with Walter Watson: What's New in Aerospace | 2020 | 0:36:17 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=K0MQj2P1Mik) |
| Lockheed SR-71 Lecture (March 2020) at the National Museum of the U.S. Air Force | 2020-03-07/2020-03-08 | 1:22:55 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=QnYhq_OCRpQ) |
| Lockheed SR-71 Blackbird Lecture (March 2020) at the National Museum of the USAF | 2020-03-07/2020-03-08 | 1:33:54 | National Museum of the U.S. Air Force (@USAFmus... | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=YqTL-JYzU2E) |
| SocialFlight Live! - 5-12-20 - SR-71 Crew Phil Soucy & Ed Yeilding | 2020-05-12 | 1:02:07 | SocialFlight | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=jsgkZfEgUUQ) |
| Virtual Coffee at the Cosmo: Celebrating the SR71 | 2020-10 | 1:07:35 | Cosmosphere | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=qnMLDXV9kcQ) |
| Pilots: Frank Murray & Rich Graham Remember: A-12 SR-71 | c. 2020 | 0:04:45 | Aerotech News | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=DwykjfnzTL8) |
| BD 0390 A Tribute to Bob Gilliland First to Fly the SR-71 | c. 2020 | 0:01:36 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | D | no (tier D) | [source](https://www.youtube.com/watch?v=g1-CiWYgfNQ) |
| John L. Roberts Collection | 2021-03-30 |  | Library of Congress Veterans History Project (i... | audio only | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.118982/) |
| Walter Watson - Flying on SR 71 Blackbird: My Path | c. 2021 | 0:03:39 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=d4Y1nl4K6Y0) |
| Nov. 5, 2022 SR-71 Crew - Spy Pilot Chronicles - Brian Shul & Walter Watson, Harris Cen... | 2022 | 1:43:07 | Sled Driver (channel); speakers Brian Shul and... | 1920x1080 | D | no (tier D) | [source](https://www.youtube.com/watch?v=BY3nRtRsdKg) |
| SR 71 Blackbird pilot interview Col Pat Bledsoe | c. 2022 | 1:30:05 | The Backyard Astronomer | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=vGlaZ9p_6n0) |
| Jim Shelton describes the SR-71 | c. 2022 | 0:55:30 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=GF8ASVzj1DA) |
| SR71 Pilots Symposium 2023 Evergreen Air & Space Museum | 2023 | 0:56:58 | Aviation Explored With Norman | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=SHv_L0aZL9o) |
| Live Chat - Suit Up: From the SR-71 Blackbird to the Space Shuttle | 2023-05-13 | 0:38:01 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=cnpCbbSugoQ) |
| Orville Maxon Collection | 2023-08-01 | 0:43:07 | Library of Congress Veterans History Project (i... | 640x480 | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.124710/) |
| SR-71 Engine by Jerry Glasser | 2024-04 | 0:57:37 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=bsVz_iSpbzk) |
| SR-71 Instrument Panel Presentation 20 April 2024 | 2024-04-20 | 1:11:18 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=MB6ns2VbASM) |
| First Panel from SR-71 Weekend 2024 | 2024-04-20 | 1:28:48 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=S4E_aBpZoSU) |
| Second Panel from SR-71 Weekend 2024 | 2024-04-20 | 1:19:39 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Wj8yVZL2bJg) |
| SR-71 Instrument Panel Presentation 21 April 2024 | 2024-04-21 | 1:18:26 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=BTwZWxGc4d8) |
| Third Panel from SR-71 Weekend 2024 | 2024-04-21 | 1:25:16 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Nfb430TnbJk) |
| Fourth Panel from SR-71 Weekend 2024 | 2024-04-21 | 1:07:26 | March Field Air Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=h6ziDSrBmeE) |
| SR-71 Pilot Lt. Col. Ed Yeilding Visits AEDC | 2024-07-30 | 0:02:09 | David Wright, Arnold Engineering Development Co... | 1280x720 | A | yes, `dvids-938909-ed-yeilding-visits-aedc__DOD_110600096.mp4` (56 MB) | [source](https://www.dvidshub.net/video/938909) |
| Charlie Daubs: SR-71 Blackbird Pilot | c. 2024-2025 | 0:32:23 | Strategic Air Command & Aerospace Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=lkHoP-0CRSI) |
| Ret. Lt. Col. Ed Yeilding "The SR-71 Blackbird and my coast to coast speed record flight" | 2025-08-21 | 0:58:20 | Aviation Club at UAH | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=oVWJkT-q6Y8) |
| IWM SR-71 YouTube Shorts (4 items) | 2025-2026 |  | Imperial War Museums | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/channel/UC3uAjWoLZ4bSi6qI9SjALxA/shorts) |
| "INVINCIBLE" - SR-71 Pilot Buz Carpenter Recalls Life in the Cockpit | c. 2025 | 0:35:09 | Americans in Wartime Experience | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Shvw60KzIWg) |
| Blackbird Pilots Answer Spy Plane Questions | 2026 | 0:24:32 | Imperial War Museums | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=Lm9NbFzU0Qk) |
| Aviation Historian Peter Merlin talks about the A-12 Spy Planes at AREA 51 - Part 2 | 2026-02-20 | 1:37:50 | Dreamland Resort | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=NmAKYlKNv-E) |
| Thomas R. Parker Collection | 2026-03-20 |  | Library of Congress Veterans History Project (i... | not online | D | no (tier D) | [source](https://www.loc.gov/item/afc2001001.130788/) |
| The View at Mach 3 with Lt. Col. Ed Yeilding / The Adrenaline Zone, Ep. 34 |  | 0:36:53 | The Adrenaline Zone Podcast | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=zrz6cgGpci4) |
| 360° SR-71 Cockpit Tour & Discussion |  | 0:52:59 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=FPMYEEx3rI8) |
| Breaking World Records: The SR-71's Need for Speed |  | 1:28:15 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=R7D97pSL6Tk) |
| SR-71 Blackbird: Stealth Legends and Legacies |  | 1:28:55 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=PYV533ZDuvs) |
| The SR-71 Experience |  | 1:12:26 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=J5qrMTtSUV8) |
| SR-71B Blackbird Cockpit Tour with its Former Instructor |  | 0:14:27 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=4K7lO3Z7avI) |
| SR-71B Blackbird Walkaround with its former Crew Chief |  | 0:28:36 | Air Zoo | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=tSXckp6OP28) |
| 27 - Flying the SR71 Spyplane |  | 0:52:44 | Cold War Conversations | audio podcast (static image likely) | C | no (tier C) | [source](https://www.youtube.com/watch?v=zKEEy6dt3hk) |
| EAA S71 Richard Graham Pilot |  | 1:27:12 | Kenneth Walker | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=vsEwSeION3c) |
| NASA Test Pilot flew the SR-71 Blackbird |  | 0:18:20 | Fighter Pilot Podcast | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=tVaEXy7CG0Q) |
| The Hermeus Podcast 09 - Flying the SR-71 "Blackbird" |  | 1:18:40 | Hermeus (company podcast) | 1920x1080 | C | no (tier C) | [source](https://archive.org/details/youtube-iY6nsTGqFSQ) |
| More from Col Buz Carpenter and the SR-71 Blackbird |  | 0:04:24 | Smithsonian National Air and Space Museum, STEM... | 1280x720 | C | no (tier C) | [source](https://archive.org/details/More_from_Col_Buz_Carpenter_and_the_SR-71_Blackbird) |
| Tour of the SR-71 |  | 0:14:23 | Smithsonian National Air and Space Museum, STEM... | 1280x720 | C | no (tier C) | [source](https://archive.org/details/Tour_of_the_SR-71) |
| Ask a Skunk: All About the SR-71 |  | 0:01:15 | Lockheed Martin (YouTube) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=m306YxtYds0) |
| Dare to Dream: A SR-71 Pilot's Tale |  | 0:04:10 | Lockheed Martin (YouTube) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=2xZIE_YSXnk) |
| Pilot Recounts Tales of SR-71 Blackbird |  | 0:05:23 | Lockheed Martin | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=vpVT5Lr0BbI) |
| OUR ISSUES BIRMINGHAM - EP 131 - LT. COL. ED YEILDING |  | 0:21:21 | Our Issues Birmingham | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=C43E1msKEpI) |
| SR-71 Eyes in the Night |  | 0:54:37 | PeninsulaSrsVideos | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=U6ABvIHohG0) |
| SR-71 Mystiques |  | 1:25:30 | PeninsulaSrsVideos | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=iexlShI9eFc) |
| March Museum SR-71 Weekend Panel |  | 1:09:17 | Stan Fry | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=3qlIJ9x7Xi8) |
| Trojan Talk w/ Ed Yielding - TROY TrojanVision News |  | 0:05:59 | TROY TrojanVision | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ZtN70rtsljM) |
| SR-71 Pilot Interview Richard Graham Veteran Tales |  | 1:18:35 | Erik Johnston | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=CeBu6mRDaro) |

## 7. Documentaries, TV and other productions

| Title | Footage date | Length | Creator | Best copy | Tier | Downloaded | Link |
|---|---|---|---|---|---|---|---|
| NACA-NASA: 75 Years of Flight | 1915 to 1990 archival | 0:03:25 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19940010849) |
| Dryden's 60 Years of Flight Research (Six Decades of Flight Research: Dryden Flight Res... | 1946 to 2006 archival | 1:12:21 | NASA Dryden Flight Research Center | 320x240 (Wayback combined era files); 640x... | A | yes, `nasa-dryden-60-years-of-flight-research-2006__EM-0093_LiftingBody_era.mov` (59 MB) | [source](https://web.archive.org/web/20080303233315/http://www.dfrc.nasa.gov/Gallery/Movie/60th_Anniversary/index.html) |
| AFRC 75th Anniversary Series- Episode 1 Speed | archival 1946 to 2021 | 0:07:03 | NASA Armstrong Flight Research Center | 1920x1080 | A | yes, `nasa-afrc75-ep1-speed__AFRC-2021-13626-1-AFRC75th_Episode1Speed_orig.mp4` (834 MB) | [source](https://images.nasa.gov/details/AFRC-2021-13626-1-AFRC75th_Episode1Speed) |
| AFRC 75th Anniversary Series Episode 7- Spaceflight | archival 1946 to 2022 | 0:16:08 | NASA Armstrong Flight Research Center | 1920x1080 | A | yes, `nasa-afrc75-ep7-spaceflight__AFRC-2021-13626-7-AFRC75th_Episode7Spaceflight_orig.mp4` (1960 MB) | [source](https://images.nasa.gov/details/AFRC-2021-13626-7-AFRC75th_Episode7Spaceflight) |
| AFRC 75th Anniversary Series Episode 9- Airborne Science | archival 1946 to 2022 | 0:22:31 | NASA Armstrong Flight Research Center | 1920x1080 | A | yes, `nasa-afrc75-ep9-airborne-science__AFRC-2021-13626-9-AFRC75th_Episode9AirSci_orig.mp4` (2738 MB) | [source](https://images.nasa.gov/details/AFRC-2021-13626-9-AFRC75th_Episode9AirSci) |
| NACA/NASA History at Dryden, Part 1 and 2 | 1950s to 1980s | 0:50:37 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950004301) |
| VT 311 Blackbirds Are Flying Lockheed SR-71 | 1960s to 1970s (Lockheed film) | 1:12:57 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=zeC_tKaWUbM) |
| Air Force Now 68 (Kelly Johnson, U-2, SR-71) | undated (Air Force Now series, 1960s to 1980s) |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/651099740) |
| Strategic Air Command Semiannual Film Report (Aug 1965-Jan 1966) | 1965-08/1966-01 | 0:31:12 | United States Department of the Air Force (Stra... | 1280x720 29.97 fps | A | yes, `ia-342-fr-646-sac-semiannual-film-report-1965-66__Strategic_20Air_20Command_20semiannual_20film_20report_20_28Aug_201965_20-_20Jan_201966_29_20_28720p_30fps_H264-192kbit_AAC_29.mp4` (372 MB) | [source](https://archive.org/details/342-FR-646) |
| "THE BLACKBIRDS ARE FLYING" LOCKHEED SR-71 BLACKBIRD PROMO FILM SR-71A / SR-71B X-PLANE... | 1970s (per Periscope) | 0:15:16 | Lockheed California Company, Advanced Developme... | 960x540 | C | no (tier C) | [source](https://archive.org/details/xd-12994-the-blackbirds-are-flying-xr-71-vwr) |
| HISTORY OF EDWARDS AIR FORCE BASE "REACH BEYOND THE HORIZON" X-PLANES MUROC 63354 | 1970s film (YF-12 at 35:54) | 0:40:29 | U.S. Air Force (Edwards AFB) film; copy uploade... | 960x540 | C | no (tier C) | [source](https://archive.org/details/63354-a-history-of-edward-air-force-base-vwr) |
| Space in the 70s: Aeronautics (NASA film, Periscope Film 45234) | about 1970 to 1971 | 0:27:44 | NASA (film); scan and upload by Periscope Film LLC | 950x540 | C | no (tier C) | [source](https://archive.org/details/45234NASASpaceInThe70sAeronautics) |
| NASA 1971 Aeronautics and Space Highlights (Periscope Film 19194) | 1971 | 0:14:52 | NASA (film); scan and upload by Periscope Film LLC | 960x540 | C | no (tier C) | [source](https://archive.org/details/19194nasa1971aeronauticsandspacehighlightsvwr) |
| "THE GIANT STEP" 25th ANNIVERSARY OF U.S. AIR FORCE 1972 DOCUMENTARY 63454 | 1972 film (SR-71 takeoff shot at 06:37) | 0:39:07 | U.S. Air Force film; copy digitised and uploade... | 960x540 | C | no (tier C) | [source](https://archive.org/details/63454-the-giant-step-museum-vwr) |
| Aeronautics and Space 1973 (NASA year-in-review film) | 1973 | 0:14:45 | NASA (film); scan and upload by Periscope Film LLC | 960x540 | C | no (tier C) | [source](https://archive.org/details/71922AeronauticsAndSpace1973) |
| Herdenking van de eerste Indievlucht van KLM in 1974 Weeknummer 74-41 - Open Beelden -... | 1974 (Polygoon weekly newsreel 74-41, about week 41 of 1974); Blackbird and Concorde landing shots in black and white | 0:02:36 | Polygoon-Profilti (producer) / Nederlands Insti... | 352x288 | B | yes, `commons-polygoon-1974-klm-blackbird-concorde__17654.WEEKNUMMER744-HRE0001C1F0.mpg` (27 MB) | [source](https://www.openbeelden.nl/media/17655) |
| NASA 1978 Highlights (Periscope Film 75372) | 1978 | 0:14:45 | NASA (film); scan and upload by Periscope Film LLC | 960x540 | C | no (tier C) | [source](https://archive.org/details/75372NASA1978Highlights) |
| Air Force Now 139 | 1981 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/4524386) |
| Air Force Now 190 | 1985-08-08 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/4524580) |
| Forty and Forward (SAC 40th anniversary) | 1986-06-26 |  | US Air Force / Department of Defense (NARA RG 3... | not digitised (original film or tape only)... | A | pending | [source](https://catalog.archives.gov/id/4524583) |
| FEN feature on Det 1 SR-71 mission, March 17, 1988 | 1988-03-17 | 0:04:46 | Russ Maheras | not verified (YouTube player blocked) | A | pending | [source](https://www.youtube.com/watch?v=INEUCT1Z6gA) |
| Dryden Overview for Schools | early 1990s | 0:06:28 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950004298) |
| Dryden Overview for Schools | early 1990s | 0:06:26 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950004335) |
| Dryden Tour Tape, 1994 | early 1990s | 0:19:46 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950004302) |
| Dryden Year in Review: 1992 | 1992 | 0:04:32 | NASA (Dryden/Ames-Dryden), catalogued by NASA S... | not verified (YouTube player blocked); sou... | A | pending | [source](https://ntrs.nasa.gov/citations/19950004300) |
| Lockheed SR-71 Blackbird - Jeremy Clarkson - "Speed" | 2001 | 0:04:26 | BBC (Speed, presented by Jeremy Clarkson; BBC B... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=ogJSRa5cukc) |
| History Channel Interview: T.D. Barnes and Frank Murray (excerpts) | 2003 (Roadrunners reunion) | 0:01:32 | Roadrunners Internationale (host); producer not... | 240x180 | C | no (tier C) | [source](https://roadrunnersinternationale.com/barnes_murray_history.html) |
| KLAS News Special: Project Oxcart | c. 2007-2010 | 0:06:05 | Roadrunners Internationale (host); producer not... | 720x540 | C | no (tier C) | [source](https://roadrunnersinternationale.com/videos.html) |
| ABC News Nightline and ABC News segments with T.D. Barnes (re-uploads by NevAerospaceHOF) | 2011 | 0:13:46 | ABC News (re-uploaded by NevAerospaceHOF) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=KVgnf5DiBlY) |
| National Geographic 'Area 51 Declassified' (2011): eight excerpts re-uploaded by NevAer... | 2011 | 0:16:43 | National Geographic Channel (re-uploaded by Nev... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=c3mKuDIsoLc) |
| Know Your Aircraft - SR-71 | archival (compiled 2013-07-31; source footage undated) | 0:00:45 | Keith Langsdorf, 934th Airlift Wing (USAF) | 1280x720 | A | yes, `dvids-297723-know-your-aircraft-sr-71__DOD_100875338-1280x720-3000k.mp4` (20 MB) | [source](https://www.dvidshub.net/video/297723) |
| Yesterday's Air Force: The World's Fastest Plane | archival plus 2015 museum footage | 0:02:59 | Tech. Sgt. Nicholas Kurtz, Defense Media Activi... | 1280x720 | A | yes, `dvids-402699-yesterdays-air-force-fastest-plane__DOD_102420483-1280x720-2765k.mp4` (66 MB) | [source](https://www.dvidshub.net/video/402699) |
| This SR-71 Pilot Free Fell from the Edge of Space | c. 2015 (from 'Planes That Changed the World: SR-71 Blackbird') | 0:03:04 | Smithsonian Channel | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=mnEgS3buPb8) |
| Why the Truth About Area 51 May Not Be ‘Out There’ | c. 2015 (from 'The Missing Evidence: The Nevada Triangle') | 0:04:03 | Smithsonian Channel | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=AOwrCfT3Ghs) |
| Spy Planes: Eyes in the Sky - STEM in 30 | 2020 | 0:28:03 | Smithsonian National Air and Space Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=bmDwjmGcocQ) |
| The Legacy of Kelly Johnson & Skunk Works | 2025 | 0:01:44 | Flight Test Museum | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=S5ZcviSkloo) |
| BD 0656  The Impossible Factory Skunk Works | 2026-06 (SDASM volunteer meeting) | 0:52:59 | San Diego Air and Space Museum Archives | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=un3P79kQUfY) |
| SR71-Blackbird: Faster than Missiles / Warplane |  | 0:01:28 | American Heroes Channel / Military Channel (War... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=JIcf82Hk4Nw) |
| SR-71Blackbird - U.S. Air Force - 1979 - 4K AI Upscaled |  | 0:11:32 | SW Upscaling (AI upscale of a 1979 USAF film) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=QR8dguEEXH0) |
| Battle Stations - SR-71 Blackbird Stealth Plane -Full Documentary |  | 1:04:01 | History Channel 'Battle Stations' (as titled by... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=YJ5FjVOvkB0) |
| Russian Su-27 fighter jets attempt to intimidate a USAF SR-71 Blackbird. |  | 0:01:12 | YouTube channel iceman_fox1 (Digital Combat Sim... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=8ZICiF7Y3rM) |
| Lockheed SR-71 Blackbird / New York to London in 1h 54 mins / The untouchable reconnais... |  | 0:43:05 | DroneScapes (compilation of archive films, upsc... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=xLoSLK7jmrc) |
| SR-71 Takeoff from Okinawa (FULL Afterburner) |  | 0:01:09 | YouTube user OsanBlackCat5RS | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=EnDRUru9KZU) |
| History Channel "Spy Planes" Documentary |  | 0:43:07 | History Channel (per uploader) | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=oMws46bKuNs) |
| DC Wings "Specials" : Command Vision - Reconnaissance Intelligence Aircraft |  | 1:00:28 | Wings (Discovery Channel) special | 624x480 | C | no (tier C) | [source](https://archive.org/details/dc-wings-specials-command-vision-reconnaissance-intelligence-aircraft-480-p) |
| 1987 VHS - Discovery TV Broadcast: Russian and American Military Aviation 60 FPS |  | 0:52:52 | Firepower (Bravo network series, per IA descrip... | 976x720 (60 fps VHS capture) | C | no (tier C) | [source](https://archive.org/details/TheVistaGroup-DiscoveryTVBroadcastRussianandAmericanMilitaryAviation) |
| First Flights with Neil Armstrong (24/39) : Faster than the Eye and Higher than the Sky |  | 0:22:13 | First Flights with Neil Armstrong (TV series; b... | 1280x720 (upscaled) | C | no (tier C) | [source](https://archive.org/details/faster-than-the-eye-and-higher-than-the-sky-515-mb) |
| Great Fighting Jets: SR-71 Blackbird (1991) |  | 0:49:32 | Time-Life Video; Network Projects Pty. Ltd. | 640x480 | C | no (tier C) | [source](https://archive.org/details/great-fighting-jets-sr71-1991) |
| Great Planes "2009" (16/17) : SR-71 Blackbird |  | 0:43:47 | Great Planes (2009 edition; producer not verified) | 1280x720 | C | no (tier C) | [source](https://archive.org/details/great-planes-2009-16-17-sr-71-blackbird-720-p-hd) |
| Great Planes : SR-71 Blackbird |  | 0:50:32 | Great Planes / Wings (Discovery Channel); produ... | 650x480 | C | no (tier C) | [source](https://archive.org/details/great-planes-sr-71-blackbird-480-p) |
| Lockheed SR-71 Blackbird |  | 0:07:15 | compilation by YouTube user jaglavaksoldier (so... | 600x480 | C | no (tier C) | [source](https://archive.org/details/youtube--1250fZuhUg) |
| Les Ailes De Legendes - SR71 Blackbird |  |  | AVI International / Canal Plus / TVCF (per IA) | 596x480 | C | no (tier C) | [source](https://archive.org/details/les-ailes-de-legendes-sr-71-blackbird-fr-divx-documentaire) |
| Blackbird |  | 0:43:12 | Lockheed (promotional film, 1989); uploaded by... | 640x480 | C | no (tier C) | [source](https://archive.org/details/youtube-ozuR-X7QVFE) |
| Pulling G's: An Immersion Video Experience (Pioneer, 1987, 80s Aircraft Stock Footage) |  | 0:57:17 | Pioneer / Optical Data Corporation | 640x480 | C | no (tier C) | [source](https://archive.org/details/pulling-gs-a-1-t-00) |
| SR-71 Blackbird: The Secret Vigil (1989) |  | 1:01:06 | Aviation Week Video, Vol. 4 No. 2 (McGraw-Hill,... | 640x480 | C | no (tier C) | [source](https://archive.org/details/sr-71-blackbird-the-secret-vigil) |
| Strange Planes (3/6) : Eyes in the Sky |  | 0:47:57 | Strange Planes (Discovery Channel Wings series) | 614x480 | C | no (tier C) | [source](https://archive.org/details/strange-planes-3-6-eyes-in-the-sky-480-p) |
| Strange Planes, Strange Shapes by Discovery Channel (1990) |  | 0:54:47 | Discovery Channel; Network Projects Ltd.; Atlas... | 1280x720 (upscaled VHS) | C | no (tier C) | [source](https://archive.org/details/strange-planes) |
| Top Gun Jets |  | 0:25:18 | Top Gun Jets VHS (publisher not stated) | 640x480 | C | no (tier C) | [source](https://archive.org/details/top-gun-jets-1988) |
| SR-71 Blackbird & National Anthem |  | 0:01:24 | unidentified TV station sign-off film (uploader... | 854x478 | C | no (tier C) | [source](https://archive.org/details/youtube-JYaH7H6xP38) |
| SR-71 - Unknown Documentary clip (and 'SR-71 Blackbird FOUND/Missing Documentary footage') |  | 0:00:55 | unidentified documentary; uploaded from deleted... | 360x270 | C | no (tier C) | [source](https://archive.org/details/SR_71_Blackbird_Documentarry_Clip) |
| SR-71 Blackbird |  | 0:46:06 | unidentified TV documentary | 1280x720 | C | no (tier C) | [source](https://archive.org/details/sr-71-blackbird_202601) |
| Wings (11/12) : Spy Planes |  | 0:55:06 | Wings (Discovery Channel) | 624x480 | C | no (tier C) | [source](https://archive.org/details/wings-11-12-spy-planes-480-p) |
| The last official flight of the SR-71 Blackbird |  | 0:06:00 | YouTube user jaylowblow | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=yqW5oOskPIM) |
| Air Crash Investigation First Stealth Blackbird SR 71 History Documentary (and variants) |  | 0:44:16 | unidentified documentary, uploaded under false... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=G--pwsXliXM) |
| Was This North Korean Missile Attack Real? |  | 0:03:02 | Smithsonian Channel | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=SHY1-A13FCk) |
| Lockheed SR-71 Blackbird Fastest Jet in the World Full Documentary |  | 0:47:23 | unidentified TV documentary (one copy titled 'B... | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=s3tvBRs8_qU) |
| A-12 at Groomlake | unknown | 0:45:29 | A-12 | not verified (YouTube player blocked) | C | no (tier C) | [source](https://www.youtube.com/watch?v=axdTCSR0LeI) |
| SR-71 Blackbird | unknown | 0:07:15 | Roadrunners Internationale (host); producer not... | 300x240 | D | no (tier D) | [source](https://roadrunnersinternationale.com/videos.html) |

## What can be posted now, and what needs approval

| | Tier A | Tier B | Tier C | Tier D |
|---|---|---|---|---|
| Johnson announcement | 5 | 0 | 1 | 1 |
| Flight and test footage | 42 | 0 | 12 | 9 |
| NASA research | 29 | 0 | 6 | 5 |
| CIA and A-12 OXCART | 5 | 0 | 7 | 1 |
| Museum and preservation | 12 | 0 | 51 | 4 |
| Interviews and oral histories | 18 | 0 | 83 | 54 |
| Documentaries, TV and other productions | 18 | 1 | 48 | 1 |

### Can be posted now (tier A and B, 130 items)

Credit the agency or author anyway; tier B needs the exact licence credit. Items marked *pending* are cleared for posting but we do not yet hold a copy.

| Title | Tier | Rights as stated (short) | Our copy |
|---|---|---|---|
| "Archangel" | A | CIA.gov Copyright Notice: "Unless a copyright is indicated, information on our website is in the public domain and ma... | pending |
| The 50th Anniversary Commemoration of the End of the A-12 OXCART | A | NRO Site Policies, Copyright Notice: "Unless a copyright is indicated, information on the NRO Web site is in the publ... | pending |
| The Debrief: Behind The Artifact - A-12 OXCART | A | CIA.gov Copyright Notice: "Unless a copyright is indicated, information on our website is in the public domain and ma... | yes, `cia-debrief-behind-the-artifact-a12-oxcart__LPZJfChJLNs.mkv` (28 MB) |
| The Debrief: Behind the Museum - CIA in the Sky | A | CIA.gov Copyright Notice: "Unless a copyright is indicated, information on our website is in the public domain and ma... | pending |
| The Fastest Plane in the World | A | NRO Site Policies, Copyright Notice: "Unless a copyright is indicated, information on the NRO Web site is in the publ... | pending |
| AFRC 75th Anniversary Series Episode 7- Spaceflight | A | NASA description: 'The majority of archival footage and sound used in this video are in the public domain [...]. Addi... | yes, `nasa-afrc75-ep7-spaceflight__AFRC-2021-13626-7-AFRC75th_Episode7Spaceflight_orig.mp4` (1960 MB) |
| AFRC 75th Anniversary Series Episode 9- Airborne Science | A | NASA description: 'The majority of archival footage and sound used in this video are in the public domain and can be... | yes, `nasa-afrc75-ep9-airborne-science__AFRC-2021-13626-9-AFRC75th_Episode9AirSci_orig.mp4` (2738 MB) |
| AFRC 75th Anniversary Series- Episode 1 Speed | A | NASA description: 'The majority of archival footage and sound used in this video are in the public domain and can be... | yes, `nasa-afrc75-ep1-speed__AFRC-2021-13626-1-AFRC75th_Episode1Speed_orig.mp4` (834 MB) |
| Air Force Now 139 | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Air Force Now 190 | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Air Force Now 68 (Kelly Johnson, U-2, SR-71) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Dryden Overview for Schools | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| Dryden Overview for Schools | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| Dryden Tour Tape, 1994 | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| Dryden Year in Review: 1992 | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| Dryden's 60 Years of Flight Research (Six Decades of Flight Research: Dryden... | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED' for the DVD (20070031215). Plus NASA media guidelines: NASA c... | yes, `nasa-dryden-60-years-of-flight-research-2006__EM-0093_LiftingBody_era.mov` (59 MB) |
| FEN feature on Det 1 SR-71 mission, March 17, 1988 | A | none stated on the YouTube page (standard YouTube licence); copyright presumed held by the channel owner or the produ... | pending |
| Forty and Forward (SAC 40th anniversary) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Know Your Aircraft - SR-71 | A | "PUBLIC DOMAIN This work, Know Your Aircraft - SR-71, by Keith Langsdorf, identified by DVIDS, must comply with the r... | yes, `dvids-297723-know-your-aircraft-sr-71__DOD_100875338-1280x720-3000k.mp4` (20 MB) |
| NACA-NASA: 75 Years of Flight | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| NACA/NASA History at Dryden, Part 1 and 2 | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| Strategic Air Command Semiannual Film Report (Aug 1965-Jan 1966) | A | none stated on the Internet Archive item; description: "Obtained by the National Security Archive via FOIA." Basis: U... | yes, `ia-342-fr-646-sac-semiannual-film-report-1965-66__Strategic_20Air_20Command_20semiannual_20film_20report_20_28Aug_201965_20-_20Jan_201966_29_20_28720p_30fps_H264-192kbit_AAC_29.mp4` (372 MB) |
| Yesterday's Air Force: The World's Fastest Plane | A | "PUBLIC DOMAIN This work, Yesterday's Air Force: The World's Fastest Plane, by Nicholas Kurtz, identified by DVIDS, m... | yes, `dvids-402699-yesterdays-air-force-fastest-plane__DOD_102420483-1280x720-2765k.mp4` (66 MB) |
| #TBT YF-12A Speed Run & Missile Launch | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Aim High (KC-135 refuelling an SR-71) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | yes, `nara_330-dimoc-ftbel1289.mp4` (131 MB) |
| Attempt of U.S. Air Force SR71 Aircraft at World Record Speed Run, Various Lo... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Clark Air Base gets a visit from a SR-71 | A | None stated on YouTube. Basis: AFRTS/FEN news is produced by US service members as official duty (17 U.S.C. 105). | pending |
| Clip of the Commander-in-Chief of the U.S. Air Forces Europe (CINCUSAFE) (sto... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Compilation of "Aim High" Recruitment Spots (includes SR-71) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Development of the A11 Interceptor (Now called the YF12A), Edwards Air Force... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Distinguished Flying Cross to Five Air Force Officers For YF12A Record Flight... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Gen John P. McConnell's retirement, Andrews AFB, Maryland (flyover includes S... | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| Global Shield '79 (SAC exercise, includes SR-71B) | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| Jan. 19, 1990 -- Final SR-71 functional check flight at Kadena | A | None stated on YouTube. Basis: AFRTS/FEN news is produced by US service members as official duty (17 U.S.C. 105). | pending |
| KC-10A Refueling SR-71A | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| PSD, Beale AFB, California (pressure suit fitting) | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| SR-71 LAST FLIGHT | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | yes, `nara_330-dimoc-dfdee980124.mp4` (466 MB) |
| SR-71 RETIRED, RAF MILDENHALL, UK | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| SR-71 crew preparation, Beale AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| SR-71 first and second flights, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| SR-71 speed run, Beale Air Force Base, California, 13 September 1974 | A | NARA catalog use restriction: "Undetermined". US Air Force record film (US government work). | pending |
| SR-71 speed run, Beale Air Force Base, California, 27 July 1976 | A | NARA catalog use restriction: "Undetermined". US Air Force record film (US government work). | pending |
| SR-71A AF REACTIVATED 1996 | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| SR-71A, Beale AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| SR71 to Conduct Flight Tests, Various Locations (DoD filmed news release) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Senator Barry Goldwater's first flight in SR-71B, Beale AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| Strategic Air Command Semiannual Film Report (Feb-Jul 1966) | A | None stated on the item; description: "This film highlights activities, achievements and developments within Strategi... | yes, `ia-342-fr-375-sac-semiannual-film-report-1966__Strategic_20Air_20Command_20semiannual_20film_20report_20_28Feb_20-_20Jul_201966_29.mp4` (438 MB) |
| Strategic Reconnaissance (U-2 and SR-71, for local TV) | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| The Blackbird Story | A | Commons: {{PD-USGov}} 'Public domain' (author USDoD) | yes, `commons-the-blackbird-story-1972__The_Blackbird_Story.webm` (479 MB) |
| The Record Breakers | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | yes, `nara_330-dimoc-740901fzz999001.mp4` (312 MB) |
| The SR-71 (USAF "Air & Space Power" short, Hill AFB, 1997) | A | IA licenseurl "http://creativecommons.org/licenses/publicdomain/" (set by uploader); description: "Department of the... | yes, `ia-ntis-ava20323-the-sr-71__ava20323-vnb1.mpeg` (48 MB) |
| U-2R / SR-71A | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| United States Air Force Receives First Model of SR71B, Beale Air Force Base,... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| United States Air Force YF12 Test Program, Edwards Air Force Base, California... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| Universal Newsreel Volume 37, Release 79: "World's Fastest Plane" (first publ... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| YF-12-A, Edwards AFB, California (record speed trial) | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A (Edwards AFB, California): world record speed runs | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A briefing, Edwards AFB, California (XAIM-47A launch) | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A documentary, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A landings, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A preview, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A rollout and flight, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF-12A, Edwards AFB, California | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| YF12A Sets New Records, Edwards Air Force Base, California (DoD filmed news r... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| F-16XL Interview with Marta Bohn-Meyer | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| Former NASA Research pilot Ed Schneider Aerospace Walk of Honor Induction Cer... | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0086-03-ed-schneider-walk-of-honor__EM-0086-03.mov` (10 MB) |
| Former NASA Research pilot Ed Schneider Aerospace Walk of Honor Induction Cer... | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0086-04-ed-schneider-comments__EM-0086-04.mov` (15 MB) |
| Gathering of Eagles-Col. Walter Watson Jr. | A | "PUBLIC DOMAIN This work, Gathering of Eagles-Col. Walter Watson Jr., by Billy Blankenship, identified by DVIDS, must... | yes, `dvids-670098-gathering-of-eagles-walter-watson__DOD_106607475-1280x720-2765k.mp4` (46 MB) |
| Lockheed SR-71 Blackbird Lecture (March 2020) at the National Museum of the USAF | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Lockheed SR-71 Lecture (March 2020) at the National Museum of the U.S. Air Force | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Retired NASA Pilot Fitz Fulton Comments on 747/Columbia Crosswind Landing at KSC | A | none stated on the upload; basis: NASA media guidelines. NASA content (images, audio, video, and media files used in... | pending |
| SR-71 Pilot Lt. Col. Ed Yeilding Visits AEDC | A | "PUBLIC DOMAIN This work, SR-71 Pilot Lt. Col. Ed Yeilding Visits AEDC, by David Wright, identified by DVIDS, must co... | yes, `dvids-938909-ed-yeilding-visits-aedc__DOD_110600096.mp4` (56 MB) |
| Swedish pilots presented with U.S. Air Medal | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal, by SSgt Kelly OConnor, identified by DVIDS, m... | yes, `dvids-644195-swedish-pilots-air-medal-package__DOD_106257818-1920x1080-6221k.mp4` (35 MB) |
| Swedish pilots presented with U.S. Air Medal - AFN no titles | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - AFN no titles, by SSgt Kelly OConnor, identi... | yes, `dvids-644259-swedish-pilots-air-medal-afn-no-titles__DOD_106258341-1920x1080-6221k.mp4` (47 MB) |
| Swedish pilots presented with U.S. Air Medal - AFN w/titles | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - AFN w/titles, by SSgt Kelly OConnor, identif... | yes, `dvids-644234-swedish-pilots-air-medal-afn-titles__DOD_106258274-1920x1080-6221k.mp4` (47 MB) |
| Swedish pilots presented with U.S. Air Medal - Colonel Lars-Erik Blad Interview | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - Colonel Lars-Erik Blad Interview, by SSgt Ke... | yes, `dvids-644283-blad-interview__DOD_106258467-1920x1080-6221k.mp4` (120 MB) |
| Swedish pilots presented with U.S. Air Medal - Colonel Per-Olof Eldh Interview | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - Colonel Per-Olof Eldh Interview, by SSgt Kel... | yes, `dvids-644289-eldh-interview__DOD_106258476-1920x1080-6221k.mp4` (141 MB) |
| Swedish pilots presented with U.S. Air Medal - Lt. Col. (Ret.) Tom Vetri | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - Lt. Col. (Ret.) Tom Vetri, by SSgt Kelly OCo... | yes, `dvids-644294-veltri-interview__DOD_106258487-1920x1080-6221k.mp4` (226 MB) |
| Swedish pilots presented with U.S. Air Medal - Major Krister Sjoberg Interview | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - Major Krister Sjoberg Interview, by SSgt Kel... | yes, `dvids-644272-sjoberg-interview__DOD_106258411-1920x1080-6221k.mp4` (54 MB) |
| Swedish pilots presented with U.S. Air Medal - Major Roger Moller Interview | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal - Major Roger Moller Interview, by SSgt Kelly... | yes, `dvids-644280-moller-interview__DOD_106258461-1920x1080-6221k.mp4` (95 MB) |
| Swedish pilots presented with U.S. Air Medal Full Ceremony | A | "PUBLIC DOMAIN This work, Swedish pilots presented with U.S. Air Medal Full Ceremony, by SSgt Kelly OConnor, identifi... | yes, `dvids-644209-swedish-pilots-air-medal-full-ceremony__DOD_106258000-1280x720-2765k.mp4` (1477 MB) |
| Veterans in Blue 2017 - Tony Bevacqua | A | "PUBLIC DOMAIN This work, Veterans in Blue 2017 - Tony Bevacqua, must comply with the restrictions shown on https://w... | yes, `dvids-562694-veterans-in-blue-bevacqua__DOD_105043310-1920x1080-6221k.mp4` (105 MB) |
| 2,000-MPH Jet. Johnson Reveals U.S. Super Plane, 1964/03/02 (Universal Newsre... | A | Internet Archive item licence: http://creativecommons.org/licenses/publicdomain/. Wikimedia Commons PD-Universal News... | yes, `ia_1964-03-02_2000-MPH_Jet.mpeg` (52 MB) |
| PRESIDENT LYNDON JOHNSON PRESS CONFERENCE ON VIETNAM, PANAMA, CIVIL RIGHTS, S... | A | NARA catalog use restriction: "Undetermined". Voice of America (US government) recording. | pending |
| President Johnson's 6th Press Conference - February 29, 1964 (USIA film) | A | NARA catalog use restriction "Restricted - Possibly" citing Public Law 101-246: "Issued February 6, 1990, this law pr... | pending |
| The President's News Conference, July 24, 1964 | A | YouTube description: "Slideshow created by staff at the LBJ Presidential Library, and composed of White House Communi... | pending |
| WHCA audio recording 107 (WHCA107-1): President's News Conference, 24 July 19... | A | DiscoverLBJ holdings guide for "[WHCA] Sound Recordings of President Lyndon B. Johnson, 11/22/1963 - 1/17/1969": "Pub... | pending |
| 171117-F-DF621-SR-71 WASH | A | "PUBLIC DOMAIN This work, 171117-F-DF621-SR-71 WASH, by MSgt Shawn Bryant, identified by DVIDS, must comply with the... | yes, `dvids-640384-sr-71-wash-beale__DOD_106216519-1280x720-2765k.mp4` (32 MB) |
| 360° Video:  U.S. Air Force Flight Test Museum | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| 4th Building Aircraft Moves 13-15 Oct 2015 | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| AFRL Tech: Museum Series - J58 Engine | A | "PUBLIC DOMAIN This work, AFRL Tech: Museum Series - J58 Engine, by Kenneth M McNulty, identified by DVIDS, must comp... | yes, `dvids-935251-afrl-museum-series-j58__DOD_110534634.mp4` (65 MB) |
| Do you remember the SR-71 Blackbird and the YA-7F Strikefighter? #shorts #air... | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Friday Dec. 17 & Saturday, Dec. 18, 2021 - Look inside the cockpit of the Loc... | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Lockheed SR-71A | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Lockheed SR-71A at the National Museum of the USAF | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| Pratt & Whitney J58 Turbojet (Drone View) | A | none stated on YouTube (standard YouTube licence shown by default); basis: U.S. Government work. DVIDS/DoW notice: "I... | pending |
| SR-71 Blackbird Memorial (Barksdale Global Power Museum installation) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| SR-71 Ceremony (Barksdale Global Power Museum ribbon cutting) | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| SR-71 at the National Museum of the United States Air Force | A | "PUBLIC DOMAIN This work, SR-71 at the National Museum of the United States Air Force, by Nicholas Kurtz, identified... | yes, `dvids-396020-sr-71-nmusaf-broll__DOD_102322577-1920x1080-6221k.mp4` (692 MB) |
| Aeronautics and Space Report_69_71-75_77-79 | A | none stated in the record (keywords 'filmstock', center AFRC); basis: NASA media guidelines, NASA-produced 1970s film... | yes, `nasa-aeronautics-space-report-compilation-yf12-mallick__NDTV000111ab-Aeronautics_and_Space_Report_69_71-75_77-79_orig.mp4` (3817 MB) |
| First Flight of YF12A Under Joint NASA/United States Air Force Test Program T... | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| LASRE ground hotfire #2 | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0018-02-lasre-ground-hotfire-2__EM-0018-02.mov` (4 MB) |
| Lunar Science Data / Aeronautics (NASA Aeronautics and Space Report): YF-12 s... | A | NARA catalog use restriction: "Unrestricted"; access restriction: "Unrestricted". Federal agency production (US gover... | pending |
| NASA Connect - TOAT - Wind Tunnels | A | Internet Archive item rights field: 'Public Domain'; creator 'NASA LaRC Office of Education'. Plus NASA media guideli... | yes, `nasa-connect-toat-wind-tunnels-sr71__NASATOAT-WindTunnels.mpg` (117 MB) |
| NASA YF-12 Overview (film 'The Lockheed YF-12') | A | Commons: {{PD-USGov-NASA}} and {{PD-USGov-Military-Air Force}} 'Public domain' | yes, `commons-nasa-yf12-overview-film-1974__NASA_YF-12_Overview.ogv` (96 MB) |
| NASA and the SR-71: Back to the Future | A | NTRS copyright determination 'GOV_PUBLIC_USE_PERMITTED', distribution 'PUBLIC'. Plus NASA media guidelines: NASA cont... | pending |
| SR-71 Blackbird refueling in flight | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-04-sr71-refueling__EM-0025-04.mov` (16 MB) |
| SR-71 LASRE during in-flight cold flow test | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0018-01-lasre-inflight-cold-flow__EM-0018-01.mpg` (2 MB) |
| SR-71 LASRE in flight over Mojave Desert | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-06-lasre-in-flight-mojave__EM-0025-06.mov` (17 MB) |
| SR-71 LASRE refueling in flight from a KC-135 | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-05-lasre-refueling-kc135__EM-0025-05.mov` (18 MB) |
| SR-71 flight | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-01-sr71-flight__EM-0025-01.mpg` (1 MB) |
| SR-71 flyover | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-02-sr71-flyover-844__EM-0025-02.mpg` (2 MB) |
| SR-71 takeoff at Edwards Air Force Base | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-03-sr71-takeoff-edwards__EM-0025-03.mov` (20 MB) |
| SR-71A/YF-12A takeoff and flight | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-01-sr71a-yf12a-takeoff-flight__EM-0041-01.mpg` (4 MB) |
| SR-71B Blackbird Dryden's Pilot Trainer Aircraft | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0025-07-sr71b-trainer__EM-0025-07.mov` (5 MB) |
| YF-12 Test Program | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| YF-12A | A | NARA catalog use restriction: "Restricted - Possibly" (specific restriction "Copyright"), note: "Some or all of this... | pending |
| YF-12A (SR-71 Blackbird) Landing at Edwards Air Force Base (~1970) / AiirSource | A | NASA footage (US government work) re-uploaded by a third party; NASA media guidelines. | pending |
| YF-12A Coldwall Aerodynamic Heating Experiment | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-10-yf12a-coldwall-heating__EM-0041-10.mov` (7 MB) |
| YF-12A Coldwall Ground Separation Test - front view | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-04-yf12a-coldwall-separation-front__EM-0041-04.mov` (7 MB) |
| YF-12A Coldwall Ground Separation Test - side view | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-03-yf12a-coldwall-separation-side__EM-0041-03.mov` (6 MB) |
| YF-12A landing at Edwards Air Force Base | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-08-yf12a-landing__EM-0041-08.mov` (5 MB) |
| YF-12A low level test flight | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-02-yf12a-low-level__EM-0041-02.mov` (8 MB) |
| YF-12C approach and landing at Edwards Air Force Base | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-07-yf12c-approach-landing__EM-0041-07.mov` (6 MB) |
| YF-12C approach and landing at Edwards Air Force Base | A | NASA footage re-uploaded; NASA media guidelines. | pending |
| YF-12C mid-air refueling | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-06-yf12c-refueling__EM-0041-06.mov` (5 MB) |
| YF-12C takeoff from Edwards Air Force Base | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-09-yf12c-takeoff__EM-0041-09.mov` (4 MB) |
| YF-12C taxi and takeoff from Edwards Air Force Base | A | none stated on the Dryden caption page (no credit or copyright line); basis: NASA media guidelines. NASA content (ima... | yes, `nasa-dryden-em-0041-05-yf12c-taxi-takeoff__EM-0041-05.mov` (6 MB) |
| Herdenking van de eerste Indievlucht van KLM in 1974 Weeknummer 74-41 - Open... | B | Open Beelden: 'is gelicenseerd onder Creative Commons - Naamsvermelding-Gelijk delen' (CC BY-SA 3.0 NL); Commons {{Cc... | yes, `commons-polygoon-1974-klm-blackbird-concorde__17654.WEEKNUMMER744-HRE0001C1F0.mpg` (27 MB) |

### Needs approval before hosting (tier D, 75 items)

| Title | Who to ask | Why |
|---|---|---|
| SR-71 Inflight Refueling 1989 | Bill Baker | Private or amateur recording; hosting needs the uploader's (camera operator's) written permission. |
| Test Flying the World's Fastest Airplanes. Robert J. Gilliland | Doctors for Disaster Preparedness (DDPmeetings); speaker Robert J. Gilliland | Talk by a private individual recorded by a third party. |
| Farnborough Air Show 1974 Highlights | Farnborough Air Sciences Trust | Commercial archive licence required. |
| President Lyndon Johnson's Press Conference at the State Department, July 24,... | LBJ Presidential Library audiovisual archives (identify the film element and its rights... | Only moving-image record of the SR-71 announcement found; underlying film is probably a network pool kinescope whose rights the LBJ Libra... |
| Author Brian Shul on piloting the SR-71 | Lawrence Livermore National Laboratory / LLESA, and Brian Shul (or the holder of his ph... | Contractor-operated lab recording of a private author using his own copyrighted photographs |
| XR71 Dulles | Mike Young (uploader 'Michael Young' on YouTube) | private home video; the only footage found of the 6 Mar 1990 Dulles arrival |
| Blackbird: The Fastest Spy Plane (Extended Cut) - SR-71 | Montgomery College Television (and Col. Joe Kinego) | College TV production with a veteran interview; no licence stated. |
| BG Dennis Sullivan on gear down at Mach 3 | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| BGen CIA pilot Dennis Sullivan about Project Oxcart | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| CIA A-12 PIlot Frank Murray on Oxcart at Groom Lake | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| CIA A-12 pilot Ken Collins comments on Lockheed test pilots | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Col Sam Pizzo on CIA selection Project Oxcart | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Engineer Fred White intro to A-12 | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Engineer Wayne Pendleton about RCS of A-12 | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Frank Murray A-12 abort landing | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| George Knapp introduction of Groom Lake Panelists | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Groom Lake House Six Stories | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Letter to Kelly Johnson | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Major Ron Girard USAF 1129th SAS Groom Lake | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Presentation on Project OXCART at Defense Intelligence Agency in September 2010 | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Robert Rodert of Project Oxcart | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| T D  BARNES  PROJECT OXCART | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| T D Barnes and Lt Gen Dick Leavitt on Blackbird Replacement | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| T D Barnes intro Oxcart panel | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| T D Barnes on Groom Lake wives | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| TD Barnes Intro Project Oxcart | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Tribute to MSGT Leland Haynes, Crew Chief of the SR-71 | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| Troy Wade introduction of Roadrunners of Groom Lake | Nevada Aerospace Hall of Fame (T.D. Barnes) / Roadrunners Internationale | event recording by a private organisation; speakers may also hold rights |
| OXCART Legacy Tour at Smithsonian's National Air and Space Museum in Septembe... | Nevada Aerospace Hall of Fame and Smithsonian NASM (event host) | event recording by a private organisation; speakers may also hold rights |
| Frank Murray talking about A-12 pilot training and Kadena missions (2005) | Roadrunners Internationale (webmaster, Dreamland Resort site) | private veterans' site; footage origin not stated |
| Roadrunners 2009: Mission Planners (Harold Mills, Sam Pizzo, Al Rossetti) and... | Roadrunners Internationale (webmaster, Dreamland Resort site) | private veterans' site; footage origin not stated |
| SR-71 | Roadrunners Internationale (webmaster, Dreamland Resort site) | private veterans' site; footage origin not stated |
| SR-71 Blackbird | Roadrunners Internationale (webmaster, Dreamland Resort site) | private veterans' site; footage origin not stated |
| YF-12 Take-off | Roadrunners Internationale (webmaster, Dreamland Resort site) | private veterans' site; footage origin not stated |
| Dedication of Article 128 on display at CIA Headquarters, Langley, VA Sep 19,... | Roadrunners Internationale; if CIA-produced, CIA Office of Public Affairs (would make i... | the only video found of the 2007 CIA HQ installation ceremony; producer unknown |
| Roadrunners 2009 Symposium Panel 2 (Spy Planes of Groom Lake) | Roadrunners Internationale; possibly C-SPAN if it is their recording | private veterans' site; footage origin not stated |
| MD-21 Accident | Roadrunners Internationale; underlying film Lockheed (chase camera) or CIA | private veterans' site; footage origin not stated |
| First Flight A-12 | Roadrunners Internationale; underlying film probably Lockheed or CIA | private veterans' site; footage origin not stated |
| BD 0390 A Tribute to Bob Gilliland First to Fly the SR-71 | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| BD-0011 Flying the Lockheed SR-71 with Maury Rosenberg Oral History | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| BD-0012 Frank Murray Oral Interview, Lockheed A-12, 4/29/14 | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| BD-0017 Richard Kantner Oral History  A-12/SR-71 Blackbird  9 23, 2013 | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| BD-0066 Oral History, Bill Weaver and Maury Rosenberg Lockheed SR-71 Pilots | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| F-0270 SR-71 | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| SR-71 Final Flight @ Palmdale to Dulles | Sky Watcher_75 | uploader footage of uncertain origin |
| Nov. 5, 2022 SR-71 Crew - Spy Pilot Chronicles - Brian Shul & Walter Watson,... | Sled Driver (channel); speakers Brian Shul and Walter Watson | Talk by a private individual recorded by a third party. |
| Ed Yeilding Visits - TROY TrojanVision News | Troy University (TrojanVision) and Ed Yeilding | University production of a talk/interview; no licence stated. |
| Archangel CIA's Supersonic Seminar.mp4 | UNLV Howard R. Hughes College of Engineering (and the speakers) | university event recording; high-value panel with CIA Chief Historian and A-12 veterans |
| Roadrunners Internationale A-12 session (Nevada Test Site Oral History Project) | UNLV University Libraries Special Collections and Archives | oral history; rights with UNLV and participants |
| EPIC NASA Tour at Edwards AFB March 1995 YF-23, SR-71A, SR-71B, B-52B, B-2, F... | YouTube user At The Fence 111 | Private home video of a public NASA tour. |
| SR-71 Arrival at NASA Dryden FRC | YouTube user F104G826 (the camera operator) | Personal footage shot by an individual; not a NASA production even if the camera was NASA-owned (status unclear). |
| NASA Family Day 1992 SR71 Flyovers | YouTube user Stephen Landers | Private home video. |
| Major Brian Shul, USAF (Ret.) SR-71 Blackbird 'Speed Check' | audience recording by Jan Johnson; speaker Brian Shul | Talk by a private individual recorded by a third party. |
| yeilding final1 (with 'Yeilding rough' and 'Yeilding rough2') | the producing community channel | No licence stated. |
| Anthony Philip Bevacqua Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Arthur Edwin Roberts Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Buddy L. Brown Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Donald Augustus Walbrecht Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Ivie Wesley Chandler, Jr. Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| James C. Baranowski Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| John L. Roberts Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| John M. Pietz Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Joseph Francis Godlewski Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Ken O'Donoghue Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Kenneth Maurice Enright Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Michael Hall Johnson Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Michael L. Cherry Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Orville Maxon Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Thomas R. Parker Collection | the veteran or next of kin, via the Veterans History Project (American Folklife Center,... | interviewee and interviewer retain copyright; LOC cannot grant permission |
| Lockheed SR-71 Blackbird 61-7976 At EAA AirVenture Oshkosh 7/31/89 | uploader | Private or amateur recording; hosting needs the uploader's (camera operator's) written permission. |
| Lockheed SR-71 Blackbird Must See Clips | uploader | Private or amateur recording; hosting needs the uploader's (camera operator's) written permission. |
| SR 71 Blackbird last flight ever.Edwards AFB open house 1999. | uploader | Private or amateur recording; hosting needs the uploader's (camera operator's) written permission. |
| SR-71 Last flight from Kadena AFB Okinawa, Japan | uploader | Private or amateur recording; hosting needs the uploader's (camera operator's) written permission. |
| SR-71 landing at AF Museum Dayton OH2.wmv | uploader | Private or amateur recording; hosting needs the uploader's (camera operator's) written permission. |
| USAF SR-71 Blackbird New York-London record during Farnborough 1974 | uploader (source unknown) | Commercial archive licence required. |

### Link only (tier C, 208 items)

These are copyrighted. They are listed in the section tables above for completeness; use them only as links or official embeds, never as hosted copies. Where a tier C item would be valuable on the site, the permission column below says whom to ask.

| Title | Who to ask if we want a copy | Why |
|---|---|---|
| Flying the SR-71 Blackbird - BC Thomas (Part 2) | 10 Percent True podcast | third-party recording; link or embed only |
| Flying the SR-71 Blackbird - BC Thomas (Part 3) | 10 Percent True podcast | third-party recording; link or embed only |
| Flying the SR-71 Blackbird - BC Thomas (Part 4) | 10 Percent True podcast | third-party recording; link or embed only |
| Flying the Lockheed SR-71 Blackbird - BC Thomas (Part 5) | 10 Percent True podcast | third-party recording; link or embed only |
| History Channel Interview: T.D. Barnes and Frank Murray (excerpts) | A&E Networks (History Channel) | TV documentary excerpts |
| History Channel "Spy Planes" Documentary | A+E Networks | Copyrighted production; link or embed only. |
| ABC News Nightline and ABC News segments with T.D. Barnes (re-uploads by NevA... | ABC News (Disney) | network news |
| SYND 31/12/1970 US AIR FORCE TESTS SUPERSONIC YF - 12 | AP Archive (syndicated news film) | Commercial archive licence required. |
| SYND 31 8 74 NEW JET PLANE SR-71 | AP Archive (syndicated news film) | Commercial archive licence required. |
| Les Ailes De Legendes - SR71 Blackbird | AVI International / Canal Plus / TVCF (per IA) | Commercial documentary; third-party upload. |
| Pilots: Frank Murray & Rich Graham Remember: A-12 SR-71 | Aerotech News | third-party recording; link or embed only |
| The Legacy of Kelly Johnson & Skunk Works | Air Force Flight Test Museum / Flight Test Museum Foundation | museum-produced video; link or embed, ask before hosting |
| Air Zoo SR-71B YouTube Shorts and sub-2-minute clips (34 items) | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced |
| Differences between the SR-71A and SR-71B | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| The Pratt & Whitney J58 - The Engine of the SR-71 Blackbird | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| The Pratt & Whitney J58 - The Engine of the SR-71 Blackbird / Part Two | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| Opening an SR-71 Blackbird Cockpit | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71 ABC's | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71 Flight Control Stick | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| The Lockheed SR-71 Blackbird's METAL tires! | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71 Quick Facts Compilation | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| 'We got every one and broke it' - The SR-71's Start Cart | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71C at Hill Aerospace Museum - Mission "Get Shaba" | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| The YF-12: The Armed Blackbird | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| 360° SR-71 Cockpit Tour & Discussion | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| Breaking World Records: The SR-71's Need for Speed | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71 Blackbird: Stealth Legends and Legacies | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| The SR-71 Experience | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71B Blackbird Cockpit Tour with its Former Instructor | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| SR-71B Blackbird Walkaround with its former Crew Chief | Air Zoo Aerospace & Science Center (Kalamazoo, MI) | museum-produced video; link or embed, ask before hosting |
| "INVINCIBLE" - SR-71 Pilot Buz Carpenter Recalls Life in the Cockpit | Americans in Wartime Museum / Experience | third-party recording; link or embed only |
| Ret. Lt. Col. Ed Yeilding "The SR-71 Blackbird and my coast to coast speed re... | Aviation Club at UAH (University of Alabama in Huntsville) | third-party recording; link or embed only |
| SR71 Pilots Symposium 2023 Evergreen Air & Space Museum | Aviation Explored With Norman (uploader); Evergreen Aviation & Space Museum (event) | third-party recording; link or embed only |
| The Case Of The Missing Blackbird / Check 6 Podcast | Aviation Week Network | third-party recording; link or embed only |
| SR-71 Blackbird: The Secret Vigil (1989) | Aviation Week Video, Vol. 4 No. 2 (McGraw-Hill, Inc.) | Commercial documentary; third-party upload. |
| Lockheed SR-71 Blackbird - Jeremy Clarkson - "Speed" | BBC | Copyrighted production; link or embed only. |
| FARNBOROUGH AIR SHOW - COLOUR | British Movietone (AP Archive) | Commercial archive licence required. |
| New Missile Interceptor For U.S. Air Force (1964) | British Pathe (FILM ID 3109.1) | Commercial archive licence required. |
| NASA Released Rare Footage Of The SR-71, The Fastest Plane To Ever Exist | Business Insider (compilation of NASA clips) | Copyrighted production; link or embed only. |
| Spy Planes of Groom Lake | C-SPAN (National Cable Satellite Corporation) | C-SPAN-produced event coverage |
| Book TV : CSPAN2 : September 10, 2011 8:00am-9:00am EDT (Annie Jacobsen, 'Are... | C-SPAN (licensing request form) | Non-federal C-SPAN programming. |
| SR-71 Blackbird Midair Crash | CIA/Lockheed original; uploader has no rights | Copyrighted production; link or embed only. |
| Lockheed SR-71 "Blackbird" - Castle Air Museum | Castle Air Museum (Atwater, CA) | museum-produced video; link or embed, ask before hosting |
| The Oxcart Story - Frank Murray | Chris Johnson (uploader); Frank Murray estate | third-party recording; link or embed only |
| SR-71 Blackbird Pilot Presentation | Chris Rand (uploader) and Science Museum of Virginia | third-party recording; link or embed only |
| 27 - Flying the SR71 Spyplane | Cold War Conversations podcast | third-party recording; link or embed only |
| #6 SR71.m4v | Cosmosphere (Hutchinson, KS) | museum-produced video; link or embed, ask before hosting |
| Operation Blackbird | Cosmosphere (Hutchinson, KS) | museum-produced video; link or embed, ask before hosting |
| SR-71 Blackbird: Making of a Mystery | Cosmosphere (Hutchinson, KS) | museum-produced video; link or embed, ask before hosting |
| SR-71 Blackbird: Men & the Missions | Cosmosphere (Hutchinson, KS) | museum-produced video; link or embed, ask before hosting |
| The SR-71 Blackbird on display at the Cosmosphere | Cosmosphere (Hutchinson, KS) | museum-produced video; link or embed, ask before hosting |
| Virtual Coffee at the Cosmo: Celebrating the SR71 | Cosmosphere (Hutchinson, KS) | museum-produced video; link or embed, ask before hosting |
| The development of SR-71, and the SR-71 in flight, United States (CriticalPas... | CriticalPast LLC (or use the NARA PD original) | Commercial archive licence required. |
| The SR-71 by Harlan Hain & Charlie Daubs | Daedalians, Curtis E. LeMay Flight 16 | third-party recording; link or embed only |
| SR71-Blackbird: Faster than Missiles / Warplane | Discovery (American Heroes Channel) | Copyrighted production; link or embed only. |
| Strange Planes, Strange Shapes by Discovery Channel (1990) | Discovery Channel | Commercial documentary; third-party upload. |
| Aviation Historian Peter Merlin talks about the A-12 Spy Planes at AREA 51 -... | Dreamland Resort (Joerg Arnu) | third-party recording; link or embed only |
| Lockheed SR-71 Blackbird / New York to London in 1h 54 mins / The untouchable... | DroneScapes (compilation of archive films, upscaled) | Copyrighted production; link or embed only. |
| NewsChannel2 Broadcasts, March 2-7, 1990 | E.W. Scripps Company via University of Baltimore Special Collections & Archives | Copyrighted local TV news; stream-only on IA. |
| EAA S71 Richard Graham Pilot | EAA (event) / Kenneth Walker (uploader) | third-party recording; link or embed only |
| SR-71 Pilot Interview Richard Graham Veteran Tales | Erik Johnston (uploader) | third-party recording; link or embed only |
| NASA Test Pilot flew the SR-71 Blackbird | Fighter Pilot Podcast | third-party recording; link or embed only |
| 1987 VHS - Discovery TV Broadcast: Russian and American Military Aviation 60 FPS | Firepower (Bravo network series, per IA description) | Commercial documentary; third-party upload. |
| First Flights with Neil Armstrong (24/39) : Faster than the Eye and Higher th... | First Flights with Neil Armstrong (TV series | Commercial documentary; third-party upload. |
| SR-71 Eclipse at Flight Test Museum | Flight Test Historical Foundation / Flight Test Museum Foundation | Private foundation channel |
| SR-71 Blackbird - The Fastest Jet Aircraft Ever Built | Flight Test Museum Foundation (Edwards AFB) | Private foundation channel |
| Brian Shul - From Butterflies to Blackbirds | Florida Institute for Human and Machine Cognition (IHMC) | third-party recording; link or embed only |
| Episode 15  Brian Shul talks about piloting the SR 71 Blackbird spy plane | Florida Institute for Human and Machine Cognition (IHMC) | third-party recording; link or embed only |
| Footage Farm SR-71 reels: 'SR-71A Take Offs, Landings & Close Views 250212-07... | Footage Farm Ltd | Commercial archive licence required. |
| Dan & Draco discuss the SR-71! | Frontiers of Flight Museum (Dallas) | third-party recording; link or embed only |
| 1965 AERIAL SR71 aircraft flies through the air | Getty Images | Commercial archive licence required. |
| 1973 close up AERIAL PAN from tail to nose of YF-12 flying over desert (proto... | Getty Images | Commercial archive licence required. |
| SR-71 taxis at Farnborough after record transatlantic flight (NBC News Archiv... | Getty Images / NBC News Archives | Commercial archive licence required. |
| Great Planes "2009" (16/17) : SR-71 Blackbird | Great Planes (2009 edition | Commercial documentary; third-party upload. |
| Great Planes : SR-71 Blackbird | Great Planes / Wings (Discovery Channel) | Commercial documentary; third-party upload. |
| The Hermeus Podcast 09 - Flying the SR-71 "Blackbird" | Hermeus (company podcast) | Commercial documentary; third-party upload. |
| Lockheed SR-71 "Blackbird" Strategic Reconnaissance Aircraft / Hill Aerospace... | Hill Aerospace Museum / Aerospace Heritage Foundation of Utah | Foundation channel, no public-domain statement |
| Battle Stations - SR-71 Blackbird Stealth Plane -Full Documentary | History Channel 'Battle Stations' (as titled by uploader | Copyrighted production; link or embed only. |
| SR-71 Blackbird / Cold War icon | Imperial War Museums (IWM Duxford) | museum-produced video; link or embed, ask before hosting |
| IWM SR-71 YouTube Shorts (4 items) | Imperial War Museums (IWM Duxford) | museum-produced |
| Blackbird Pilots Answer Spy Plane Questions | Imperial War Museums (IWM Duxford) | museum-produced video; link or embed, ask before hosting |
| Tour Guide Talks: Blackbird | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| Aircraft of the Month: Lockheed A-12 | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| Year of Innovation - Lockheed A-12 | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| March 17 - Aircraft Restoration Live - A12 Starter Cart | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| Newly renovated Lockheed A12 Aircraft | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| LOCKHEED A-12 vs. SR-71 | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| Aircraft of the month - A12 | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| A-12 Oxcart: The CIA's secret weapon | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| A-12 Oxcart | Intrepid Museum (New York) | museum-produced video; link or embed, ask before hosting |
| KLAS News Special: Project Oxcart | KLAS-TV (Las Vegas) | TV station news special |
| Brian Shul Shares his Inspiring Story of Flying an SR-71 Blackbird - LeWeb Pa... | LeWeb | third-party recording; link or embed only |
| Blackbird | Lockheed (promotional film, 1989) | Commercial documentary; third-party upload. |
| SR-71A First Flight | Lockheed Martin | Copyrighted production; link or embed only. |
| A-12 First Flight | Lockheed Martin | Copyrighted production; link or embed only. |
| Drones and the SR-71, dare we say more? | Lockheed Martin | Copyrighted production; link or embed only. |
| Ask a Skunk: All About the SR-71 | Lockheed Martin | Copyrighted production; link or embed only. |
| Dare to Dream: A SR-71 Pilot's Tale | Lockheed Martin | Copyrighted production; link or embed only. |
| Pilot Recounts Tales of SR-71 Blackbird | Lockheed Martin | third-party recording; link or embed only |
| VT 311 Blackbirds Are Flying Lockheed SR-71 | Lockheed Martin (film owner); SDASM holds the tape | Lockheed promotional film; SDASM copy carries a non-commercial request |
| Mike Relja and the Destruction of the SR-71 Spares | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| Pete Law's presentation as part of Kelly Johnson Month | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| First Panel of the 2017 SR-71 Weekend at MFAM | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Weekend 2017, Fourth Panel | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Weekend 2017, Panel 2 Discussion | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Instrument Panel Discussion | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Weekend 2017, Third Panel | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Returns | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| Final Panel from SR-71 Weekend 2019 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| Jim Shelton describes the SR-71 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Engine by Jerry Glasser | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Instrument Panel Presentation 20 April 2024 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| First Panel from SR-71 Weekend 2024 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| Second Panel from SR-71 Weekend 2024 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 Instrument Panel Presentation 21 April 2024 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| Third Panel from SR-71 Weekend 2024 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| Fourth Panel from SR-71 Weekend 2024 | March Field Air Museum (Riverside, CA) | museum-produced video; link or embed, ask before hosting |
| SR-71 "Blackbird" Fastest Airplane in the World | Museum of Aviation, Warner Robins GA | Museum/foundation channel, no public-domain statement |
| Museum of Aviation SR-71 Blackbird Lift onto Pedestals | Museum of Aviation, Warner Robins GA (Museum of Aviation Foundation) | Museum/foundation channel, no public-domain statement |
| A-12 OXCART on NBC | NBCUniversal (NBC News Archives) | NBC broadcast content; CIA upload does not make it a federal work |
| CIA Museum on The Today Show | NBCUniversal (NBC News Archives) | NBC broadcast footage; CIA's public-domain notice does not cover third-party copyright |
| The YF 12A Story and The People Who Kept Them Flying | National Atomic Testing Museum (Las Vegas) | museum lecture recording; ask to host |
| TD Barnes: Project Oxcart The CIA at Area 51 | National Atomic Testing Museum (Las Vegas) | museum lecture recording; ask to host |
| SPYCAST WITH TD BARNES | National Atomic Testing Museum; SpyCast (International Spy Museum) if it is their recor... | museum lecture recording; ask to host |
| L'Oxcart, un avion top secret | National Geographic | Copyrighted production; link or embed only. |
| National Geographic 'Area 51 Declassified' (2011): eight excerpts re-uploaded... | National Geographic (Disney) | commercial documentary |
| OUR ISSUES BIRMINGHAM - EP 131 - LT. COL. ED YEILDING | Our Issues Birmingham | third-party recording; link or embed only |
| SR-71 Pilot Maury Rosenberg | Peninsula Seniors (Jarel and Betty Wheaton) | third-party recording; link or embed only |
| SR 71, A 12, and U 2 Spy Plane Pilot Interviews | Peninsula Seniors (Jarel and Betty Wheaton) | third-party recording; link or embed only |
| SR-71 A-12 U-2 Spy Planes: 50-year Cold War Commemoration | Peninsula Seniors (Jarel and Betty Wheaton) | third-party recording; link or embed only |
| SR-71 Overview by Col. James H Shelton, Jr USAF (ret.) | Peninsula Seniors (Jarel and Betty Wheaton) | third-party recording; link or embed only |
| SR-71 Eyes in the Night | Peninsula Seniors (Jarel and Betty Wheaton) | third-party recording; link or embed only |
| SR-71 Mystiques | Peninsula Seniors (Jarel and Betty Wheaton) | third-party recording; link or embed only |
| 1970s STRATEGIC AIR COMMAND FOOTAGE B-52, SR-71, U-2, TITAN II, MINUTEMAN MIS... | Periscope Film | Commercial archive licence required. |
| 1973 NASA AERONAUTICS AND SPACE REPORT YEAR IN REVIEW SKYLAB VIKING MISSION T... | Periscope Film (for their scan); see notes for the underlying film | Stock-house copy, watermarked ('_vwr') or licence-restricted; obtain a clean PD copy from the agency instead where th... |
| "THE BLACKBIRDS ARE FLYING" LOCKHEED SR-71 BLACKBIRD PROMO FILM SR-71A / SR-7... | Periscope Film (for their scan); see notes for the underlying film | Stock-house copy, watermarked ('_vwr') or licence-restricted; obtain a clean PD copy from the agency instead where th... |
| Space in the 70s: Aeronautics (NASA film, Periscope Film 45234) | Periscope Film LLC (for this scan), or obtain a clean copy from NARA RG 255 (NASA films... | Stock-house scan, possibly watermarked; the NASA film itself is PD. |
| NASA 1971 Aeronautics and Space Highlights (Periscope Film 19194) | Periscope Film LLC (for this scan), or obtain a clean copy from NARA RG 255 (NASA films... | Stock-house scan, possibly watermarked; the NASA film itself is PD. |
| Aeronautics and Space 1973 (NASA year-in-review film) | Periscope Film LLC (for this scan), or obtain a clean copy from NARA RG 255 (NASA films... | Stock-house scan, possibly watermarked; the NASA film itself is PD. |
| NASA 1978 Highlights (Periscope Film 75372) | Periscope Film LLC (for this scan), or obtain a clean copy from NARA RG 255 (NASA films... | Stock-house scan, possibly watermarked; the NASA film itself is PD. |
| HISTORY OF EDWARDS AIR FORCE BASE "REACH BEYOND THE HORIZON" X-PLANES MUROC 6... | Periscope Film LLC (or obtain the USAF original from NARA) | Stock-house copy with NC-ND terms; underlying USAF film is likely public domain |
| "THE GIANT STEP" 25th ANNIVERSARY OF U.S. AIR FORCE 1972 DOCUMENTARY 63454 | Periscope Film LLC (or obtain the USAF original from NARA) | Stock-house copy with NC-ND terms; underlying 1972 USAF film is likely public domain |
| Pulling G's: An Immersion Video Experience (Pioneer, 1987, 80s Aircraft Stock... | Pioneer / Optical Data Corporation | Commercial documentary; third-party upload. |
| Peter W. Merlin Dreamland America's Black Shield - Atomic Testing Museum - Oc... | Quintessential Studios | independent production |
| SR-71Blackbird - U.S. Air Force - 1979 - 4K AI Upscaled | SW Upscaling (AI upscale of a 1979 USAF film) | Copyrighted production; link or embed only. |
| BD 0544 Spotlight Video   Lockheed A 12 Oxcart by Gordon Permann | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| BD 0656  The Impossible Factory Skunk Works | San Diego Air & Space Museum Library and Archives | SDASM holds the recording; 'do not use for commercial purposes without permission' |
| More from Col Buz Carpenter and the SR-71 Blackbird | Smithsonian National Air and Space Museum | Smithsonian production; link or embed the museum's YouTube copy instead of hosting. |
| Tour of the SR-71 | Smithsonian National Air and Space Museum | Smithsonian production; link or embed the museum's YouTube copy instead of hosting. |
| STEM in 30 Focus on the SR 71 Blackbird | Smithsonian National Air and Space Museum (STEM in 30 team) | Smithsonian-produced webcast; NASA only distributed it. |
| Behind the Scenes - The A-12 Oxcart on Display at CIA Headquarters | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Outrunning The Enemy: The CIA's A-12 | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| A Look At the CIA's A-12 Oxcart | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Lockheed SR-71 Blackbird: Afterburner | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Lockheed SR-71 Blackbird - Buz Carpenter's Longest Flight | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Lockheed SR-71 Blackbird: Inlets | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Lockheed SR-71 Blackbird: Pressure Suit | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Lockheed SR-71 Blackbird: Tires | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Lockheed SR-71 Blackbird - Record Flight | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| The SR-71 Blackbird - STEM in 30 | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Geek Moment with the SR-71 Blackbird and STEM in 30 | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Curator Michael Hankins gives a quick tour of the SR-71 Blackbird | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Innovations Toward Invisibility: The CIA's OXCART Project and A-12 Reconnaiss... | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| A look at the SR-71 | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Tales of the SR-71 Blackbird from Col Buz Carpenter | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Col Buz Carpenter and the SR-71 Blackbird- What's New in Aerospace | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| The SR-71 Blackbird: Student Edition - STEM in 30 Mission Debrief | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| SR-71 RSO Walter Watson: My Path | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| The SR-71 Blackbird with Walter Watson: What's New in Aerospace | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Walter Watson - Flying on SR 71 Blackbird: My Path | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Live Chat - Suit Up: From the SR-71 Blackbird to the Space Shuttle | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Spy Planes: Eyes in the Sky - STEM in 30 | Smithsonian National Air and Space Museum (rights and reproductions) | Smithsonian content with usage conditions; embed or link, ask before hosting |
| Was This North Korean Missile Attack Real? | Smithsonian Networks (Paramount) | Copyrighted production; link or embed only. |
| This SR-71 Pilot Free Fell from the Edge of Space | Smithsonian Networks (Smithsonian Channel) | commercial TV documentary excerpt; link only |
| Why the Truth About Area 51 May Not Be ‘Out There’ | Smithsonian Networks (Smithsonian Channel) | commercial TV documentary excerpt |
| SocialFlight Live! - 5-12-20 - SR-71 Crew Phil Soucy & Ed Yeilding | SocialFlight | third-party recording; link or embed only |
| How the SR-71 Got it's Name | Spartan College of Aeronautics and Technology | Commercial documentary; third-party upload. |
| March Museum SR-71 Weekend Panel | Stan Fry (uploader); March Field Air Museum (event) | third-party recording; link or embed only |
| Strange Planes (3/6) : Eyes in the Sky | Strange Planes (Discovery Channel Wings series) | Commercial documentary; third-party upload. |
| Charlie Daubs: SR-71 Blackbird Pilot | Strategic Air Command & Aerospace Museum (Ashland, NE) | museum-produced video; link or embed, ask before hosting |
| Ed Yeilding, Fastest Trojan | TROY TrojanVision (Troy University) | third-party recording; link or embed only |
| Trojan Talk w/ Ed Yielding - TROY TrojanVision News | TROY TrojanVision (Troy University) | third-party recording; link or embed only |
| The View at Mach 3 with Lt. Col. Ed Yeilding / The Adrenaline Zone, Ep. 34 | The Adrenaline Zone Podcast | third-party recording; link or embed only |
| SR 71 Blackbird pilot interview Col Pat Bledsoe | The Backyard Astronomer (uploader) | third-party recording; link or embed only |
| M-21 Blackbird / Curator on the Loose! | The Museum of Flight (Seattle) | museum-produced video; link or embed, ask before hosting |
| The way you started up an SR-71 Blackbird was weird. | The Museum of Flight (Seattle) | museum-produced video; link or embed, ask before hosting |
| Great Fighting Jets: SR-71 Blackbird (1991) | Time-Life Video | Commercial documentary; third-party upload. |
| Top Gun Jets | Top Gun Jets VHS (publisher not stated) | Commercial documentary; third-party upload. |
| Ed Yeilding: World's Fastest Trojan | Troy University | third-party recording; link or embed only |
| FLYING THE SR-71 BLACKBIRD | U.S. Space & Rocket Center (Huntsville, AL) and HAL5 | museum-produced video; link or embed, ask before hosting |
| Vault Visit / NC A&T professor shares his experience with the fastest plane i... | WFMY News 2 (TEGNA) | TV station archive |
| 13News Now Vault: The fastest coast-to-coast flight ever recorded | WVEC 13News Now (TEGNA) | TV station archive |
| Wings (11/12) : Spy Planes | Wings (Discovery Channel) | Commercial documentary; third-party upload. |
| DC Wings "Specials" : Command Vision - Reconnaissance Intelligence Aircraft | Wings (Discovery Channel) special | Commercial documentary; third-party upload. |
| SR-71 Blackbird's First Test Flight | YouTube channel DOCUMENTARY TUBE (source film not credited) | Commercial documentary; third-party upload. |
| The last official flight of the SR-71 Blackbird | YouTube user jaylowblow | Copyrighted production; link or embed only. |
| Lockheed SR-71 Blackbird | compilation by YouTube user jaglavaksoldier (sources not credited) | Commercial documentary; third-party upload. |
| Video, Aim High: Air Force - Inflight Refueling of the SR-71 Blackbird, circa... | none needed for the underlying footage if NARA confirms; Cosmosphere for its copy | museum-produced video; link or embed, ask before hosting |
| SR-71 Blackbird | unidentified TV documentary | Commercial documentary; third-party upload. |
| Lockheed SR-71 Blackbird Fastest Jet in the World Full Documentary | unidentified TV documentary (one copy titled 'Battle Stations: Blackbird Stealth') | Copyrighted production; link or embed only. |
| SR-71 Blackbird & National Anthem | unidentified TV station sign-off film (uploader MidNightRider2001) | Commercial documentary; third-party upload. |
| SR-71 - Unknown Documentary clip (and 'SR-71 Blackbird FOUND/Missing Document... | unidentified documentary | Commercial documentary; third-party upload. |
| Air Crash Investigation First Stealth Blackbird SR 71 History Documentary (an... | unidentified documentary, uploaded under false 'Air Crash Investigation' and 'BBC' titles | Copyrighted production; link or embed only. |
| A-12 at Groomlake | unknown (re-upload by channel 'A-12') | third-party recording; link or embed only |
| Lockheed Martin YF-12 SR-71 Blackbird Montage | uploader edit; use NASA originals | Copyrighted production; link or embed only. |
| NASA/Lockheed Martin Linear Aerospike SR-71 Experiment (LASRE) X-33 Ground Fi... | uploader, or obtain the NASA original from NASA Armstrong | Unknown provenance; LASRE was a joint NASA and Lockheed Martin project, so footage may be Lockheed Martin's. |

## Tier A/B masters not yet downloaded

| Title | Why pending | Master URL | Size |
|---|---|---|---|
| President Johnson's 6th Press Conference - February 29, 1964 (USIA film) | no digital copy online (original element only) | https://catalog.archives.gov/id/49639 |  |
| PRESIDENT LYNDON JOHNSON PRESS CONFERENCE ON VIETNAM, PANAMA, CIVIL RIGHTS, S... | no digital copy online (original element only) | https://catalog.archives.gov/id/123752 |  |
| The President's News Conference, July 24, 1964 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=_GLxcw_hObY |  |
| WHCA audio recording 107 (WHCA107-1): President's News Conference, 24 July 19... | no digital copy online (original element only) | https://catalog.archives.gov/id/34425227 |  |
| Development of the A11 Interceptor (Now called the YF12A), Edwards Air Force... | no digital copy online (original element only) | https://catalog.archives.gov/id/102044162 |  |
| YF-12A rollout and flight, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/69131 |  |
| YF-12A, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/72055 |  |
| YF-12A preview, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/69122 |  |
| YF-12A landings, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/72517 |  |
| Universal Newsreel Volume 37, Release 79: "World's Fastest Plane" (first publ... | no digital copy online (original element only) | https://catalog.archives.gov/id/234274858 |  |
| SR-71 first and second flights, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/72516 |  |
| Distinguished Flying Cross to Five Air Force Officers For YF12A Record Flight... | no digital copy online (original element only) | https://catalog.archives.gov/id/102044206 |  |
| YF12A Sets New Records, Edwards Air Force Base, California (DoD filmed news r... | no digital copy online (original element only) | https://catalog.archives.gov/id/102048328 |  |
| #TBT YF-12A Speed Run & Missile Launch | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=ajwCX4PRkko |  |
| YF-12A, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/70711 |  |
| YF-12A documentary, Edwards AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/69379 |  |
| YF-12-A, Edwards AFB, California (record speed trial) | no digital copy online (original element only) | https://catalog.archives.gov/id/69415 |  |
| YF-12A (Edwards AFB, California): world record speed runs | no digital copy online (original element only) | https://catalog.archives.gov/id/69544 |  |
| YF-12A briefing, Edwards AFB, California (XAIM-47A launch) | no digital copy online (original element only) | https://catalog.archives.gov/id/69934 |  |
| United States Air Force Receives First Model of SR71B, Beale Air Force Base,... | no digital copy online (original element only) | https://catalog.archives.gov/id/102047666 |  |
| SR71 to Conduct Flight Tests, Various Locations (DoD filmed news release) | no digital copy online (original element only) | https://catalog.archives.gov/id/102046842 |  |
| SR-71A, Beale AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/71867 |  |
| PSD, Beale AFB, California (pressure suit fitting) | no digital copy online (original element only) | https://catalog.archives.gov/id/71259 |  |
| Senator Barry Goldwater's first flight in SR-71B, Beale AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/71927 |  |
| Gen John P. McConnell's retirement, Andrews AFB, Maryland (flyover includes S... | no digital copy online (original element only) | https://catalog.archives.gov/id/71231 |  |
| United States Air Force YF12 Test Program, Edwards Air Force Base, California... | no digital copy online (original element only) | https://catalog.archives.gov/id/102047730 |  |
| SR-71 crew preparation, Beale AFB, California | no digital copy online (original element only) | https://catalog.archives.gov/id/71989 |  |
| Attempt of U.S. Air Force SR71 Aircraft at World Record Speed Run, Various Lo... | no digital copy online (original element only) | https://catalog.archives.gov/id/102043690 |  |
| SR-71 speed run, Beale Air Force Base, California, 13 September 1974 | no digital copy online (original element only) | https://catalog.archives.gov/id/62559 |  |
| SR-71 speed run, Beale Air Force Base, California, 27 July 1976 | no digital copy online (original element only) | https://catalog.archives.gov/id/62577 |  |
| Global Shield '79 (SAC exercise, includes SR-71B) | no digital copy online (original element only) | https://catalog.archives.gov/id/72414 |  |
| Compilation of "Aim High" Recruitment Spots (includes SR-71) | no digital copy online (original element only) | https://catalog.archives.gov/id/166073165 |  |
| U-2R / SR-71A | no digital copy online (original element only) | https://catalog.archives.gov/id/604505 |  |
| KC-10A Refueling SR-71A | no digital copy online (original element only) | https://catalog.archives.gov/id/578527 |  |
| Jan. 19, 1990 -- Final SR-71 functional check flight at Kadena | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=psUk_8vUtUw |  |
| SR-71 RETIRED, RAF MILDENHALL, UK | no digital copy online (original element only) | https://catalog.archives.gov/id/149280916 |  |
| SR-71A AF REACTIVATED 1996 | no digital copy online (original element only) | https://catalog.archives.gov/id/147970933 |  |
| Clark Air Base gets a visit from a SR-71 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=8LcldOcXIlE |  |
| Strategic Reconnaissance (U-2 and SR-71, for local TV) | no digital copy online (original element only) | https://catalog.archives.gov/id/62960 |  |
| Clip of the Commander-in-Chief of the U.S. Air Forces Europe (CINCUSAFE) (sto... | no digital copy online (original element only) | https://catalog.archives.gov/id/597853 |  |
| YF-12 Test Program | no digital copy online (original element only) | https://catalog.archives.gov/id/148015381 |  |
| First Flight of YF12A Under Joint NASA/United States Air Force Test Program T... | no digital copy online (original element only) | https://catalog.archives.gov/id/102044489 |  |
| YF-12A | no digital copy online (original element only) | https://catalog.archives.gov/id/575169 |  |
| Lunar Science Data / Aeronautics (NASA Aeronautics and Space Report): YF-12 s... | no digital copy online (original element only) | https://catalog.archives.gov/id/4145517 |  |
| NASA and the SR-71: Back to the Future | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=RsoxG1cQP0Y |  |
| YF-12A (SR-71 Blackbird) Landing at Edwards Air Force Base (~1970) / AiirSource | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=USsKznwIQxI |  |
| YF-12C approach and landing at Edwards Air Force Base | no digital copy online (original element only) | https://www.youtube.com/watch?v=lrlWtglxqjY |  |
| "Archangel" | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=JXi7LkNipdc |  |
| The Fastest Plane in the World | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=CeTQhTtrTts |  |
| The 50th Anniversary Commemoration of the End of the A-12 OXCART | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=0iyU79EK_9I |  |
| The Debrief: Behind the Museum - CIA in the Sky | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=wD0N_3IcVqs |  |
| 4th Building Aircraft Moves 13-15 Oct 2015 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=VTvDpF7AK7k |  |
| SR-71 Ceremony (Barksdale Global Power Museum ribbon cutting) | no digital copy online (original element only) | https://catalog.archives.gov/id/640883835 |  |
| 360° Video:  U.S. Air Force Flight Test Museum | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=_XB-L_DQVg0 |  |
| Do you remember the SR-71 Blackbird and the YA-7F Strikefighter? #shorts #air... | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=olxPSppy4-8 |  |
| Pratt & Whitney J58 Turbojet (Drone View) | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=6tFmNY94Aic |  |
| Lockheed SR-71A | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=xLmxyJSbimE |  |
| Lockheed SR-71A at the National Museum of the USAF | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=-NiomYlfOyw |  |
| Friday Dec. 17 & Saturday, Dec. 18, 2021 - Look inside the cockpit of the Loc... | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=DoOkG3LHLOE |  |
| SR-71 Blackbird Memorial (Barksdale Global Power Museum installation) | no digital copy online (original element only) | https://catalog.archives.gov/id/564394098 |  |
| F-16XL Interview with Marta Bohn-Meyer | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=O9-SQ0Ikk8k |  |
| Retired NASA Pilot Fitz Fulton Comments on 747/Columbia Crosswind Landing at KSC | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=vs3ZvmDmVq0 |  |
| Lockheed SR-71 Lecture (March 2020) at the National Museum of the U.S. Air Force | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=QnYhq_OCRpQ |  |
| Lockheed SR-71 Blackbird Lecture (March 2020) at the National Museum of the USAF | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=YqTL-JYzU2E |  |
| NACA-NASA: 75 Years of Flight | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=3kLoH431MDc |  |
| NACA/NASA History at Dryden, Part 1 and 2 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=P9os295TqGg |  |
| Air Force Now 68 (Kelly Johnson, U-2, SR-71) | no digital copy online (original element only) | https://catalog.archives.gov/id/651099740 |  |
| Air Force Now 139 | no digital copy online (original element only) | https://catalog.archives.gov/id/4524386 |  |
| Air Force Now 190 | no digital copy online (original element only) | https://catalog.archives.gov/id/4524580 |  |
| Forty and Forward (SAC 40th anniversary) | no digital copy online (original element only) | https://catalog.archives.gov/id/4524583 |  |
| FEN feature on Det 1 SR-71 mission, March 17, 1988 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=INEUCT1Z6gA |  |
| Dryden Overview for Schools | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=beGuNH55mh8 |  |
| Dryden Overview for Schools | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=UTQ05_1wG98 |  |
| Dryden Tour Tape, 1994 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=3xVJUbEM6Eg |  |
| Dryden Year in Review: 1992 | YouTube refused player requests from this network on 2026-10-04 (bot check); download m... | https://www.youtube.com/watch?v=rhgy58PN5gY |  |

## Misdated or miscaptioned items (89)

- **2,000-MPH Jet. Johnson Reveals U.S. Super Plane, 1964/03/02 (Universal Newsreel, Vol. 37 Release 18, partial)** (A): This is the 29 Feb 1964 A-11 disclosure, not the 24 Jul 1964 SR-71 announcement; uploads that call it the SR-71 announcement are miscaptioned. Universal Newsreel did not cover the 24 Jul 1964 conference: Releases 60 (27 Jul) and 61 (30 Jul 1964) have no aircraft story. AIRBOYD title says 'Lockheed Martin A-12 (A-11, SR-71)': the company name is anachronistic for 1964, and the 'A-11' that LBJ announced was the YF-12A interceptor, whose publicity served as cover for the A-12, not the SR-71. Check whether the stills show a YF-12A rather than an A-12. Title 'Lockheed Martin A-12 (A-11, SR-71)' is anachronistic ('Lockheed Martin') and conflates the 29 Feb 1964 'A-11' announcement with the SR-71. Description calls the YF-12 'a Mach 3+ modification of the CIA's A-12' (broadly right); the date in the title is unexplained. IA description says 'still pictures of the A-11'; the aircraft actually pictured in the 1964 disclosure were YF-12As (Merlin). The two YouTube copies are titled 'President Johnson Reveals Lockheed Martin A-12 (A-11, SR-71)': 'Lockheed Martin' did not exist until 1995, and the 29 Feb 1964 A-11 disclosure is conflated with the separate 24 Jul 1964 SR-71 announcement. AIRBOYD's description also changes 'still pictures of the A-11' to 'still pictures of the A-12'.
- **The President's News Conference, July 24, 1964** (A): None in the upload. Note that the American Presidency Project transcript the captions come from has an OCR slip, "SR-7I", in the fourth paragraph.
- **How the SR-71 Got it's Name** (C): Repeats the disputed RS-71 transposition story; the 24 Jul 1964 transcript has Johnson saying 'SR-71', and Beale history attributes the 'SR' choice to LeMay.
- **The SR-71 (USAF "Air & Space Power" short, Hill AFB, 1997)** (A): Metadata crossed with sibling item gov.ntis.ava20320-vnb1 ('The F-16 (was SR-71)'): this SR-71 item's description cites NTIS AVA20320-VNB1, date Jan 1979, and lists 'F-16 SR-71' shots; the F-16 item cites AVA20323-VNB1 and Oct 1997. Thumbnail stills checked: this item shows an SR-71 head-on at 20 s, the sibling shows an F-16, so the current titles are right but the NTIS numbers and dates in the descriptions are swapped. The 1979 date is not reliable. Lead check of the downloaded file (2026-10-04): opening card reads "Air & Space Power" and "SR-71" with the USAF 50th anniversary logo (1947 to 1997), closing card "Produced by Media Production Flight, 367th Training Support Sq, Hill AFB Utah 613537". So the programme dates from 1997, not Jan 1979. Identifiers are swapped: this SR-71 item sits at IA identifier gov.ntis.ava20323-vnb1 but its corrected description gives NTIS AVA20320-VNB1, and the companion item gov.ntis.ava20320-vnb1 is titled 'The F-16 (was SR-71)'. Cite the NTIS number AVA20320-VNB1 with this IA URL. Two Commons copies of one film with different durations (66.7 s vs 79.6 s) and different licence tags (CC0 vs PD-USGov-Military-Air Force).
- **New Missile Interceptor For U.S. Air Force (1964)** (C): Pathe calls the aircraft 'A-11'; it is a YF-12A (the A-11 name was Johnson's cover designation). Pilot's name is given as 'Stevens' in the description and 'Lt Col Robert Stephens' would be the usual spelling; not verified.
- **Universal Newsreel Volume 37, Release 79: "World's Fastest Plane" (first public flight of the A-11)** (A): Release sheet repeats 1964 press claims (2,500 mph, 100,000 ft) that exceed the YF-12A's real performance; card catalog OCR spells YF-12A as "YK12A" and the pilot as "Stevens" (Robert L. Stephens).
- **SR-71 first and second flights, Edwards AFB, California** (A): Catalog coverage date 21 Dec 1964 is one day before the first flight date given by NASA, Smithsonian, Lockheed Martin and CIA (22 Dec 1964); treat as approximate.
- **Strategic Air Command Semiannual Film Report (Feb-Jul 1966)** (A): The film's opening slate reads '342.FR.735, Source: 16mm INSK/DNT (I Copy)', but the IA identifier and title say 342-FR-375; one of the two numbers is transposed. The IA description has no SR-71 tag, but thumbnail stills near the end show SR-71 crew being suited, an SR-71 nose marked U.S. AIR FORCE, and an SR-71 under a KC-135 boom.
- **MD-21 Accident** (D): 'MD-21' is the informal name for the M-21/D-21 pair.
- **SYND 31/12/1970 US AIR FORCE TESTS SUPERSONIC YF - 12** (C): AP often files undated material under 31 Dec of a year; the YF-12 was a NASA/USAF joint programme from 1969, so 'US Air Force tests' may be loose (not verified).
- **The Record Breakers** (A): NARA scope note ends 'Command: United States Northern Command (USNORTHCOM)', impossible for 1974 (USNORTHCOM formed 2002). footagefarm dates the flight 31 Aug 1974; NARA says 1 Sept 1974. Cold War Core copy is AI/upscaled to '4K 48fps'. Producer disputed: Retrofootage says Lockheed, footagefarm says USAF film with a Lockheed focus chart. AIRBOYD retitled it 'SR-71 Blackbird & Farnborough Air Show 1974'; NARA title is 'THE RECORD BREAKERS, BEALE AFB AND LOS ANGELES...' (shares a name with the edited DIMOC film, but this is the USAF reel). Commons author 'USDoD / Lockheed' flags possible Lockheed footage. Airframe 61-7972 for the Sep 1974 records is project knowledge, not stated in the clip record. Description says the record was set 'On August 31, 1974'; it was 1 Sep 1974 (Guinness, Beale history).
- **The development of SR-71, and the SR-71 in flight, United States (CriticalPast clip series 65675028483 to 65675028489)** (C): Clip 65675028489 description says 'SA-71 takes off' (typo for SR-71). CriticalPast date 1972 may be its own estimate.
- **The Blackbird Story** (A): 1734x1080 is not a native film-transfer size: likely upscaled and cropped. Shot list includes Lockheed plant scenes, so Lockheed footage may be inside. CriticalPast resells cuts of this film (clips 65675028483 to 65675028489) dated "1972"; NARA dates the film ca. 1967. AIRBOYD dates it 'Ca. 1972'; the shot list (14th Strategic Aerospace Division sign at Beale, SR-71B crew welcome, Mach 3 pins) suggests 1966-1968 material; date unconfirmed. Shot list writes serials as 17976, 17950, 17956.
- **FARNBOROUGH AIR SHOW - COLOUR** (C): Rounded '1 hour, 55 minutes' versus the record 1 h 54 min 56.4 s; acceptable.
- **SR-71 speed run, Beale Air Force Base, California, 13 September 1974** (A): Use restriction Undetermined. 13 Sep 1974 is the date of the London to Los Angeles record flight.
- **SR-71 Inflight Refueling 1989** (D): StoryDocs re-upload labels VHS footage 'HD' (upscaled).
- **Lockheed SR-71 Blackbird 61-7976 At EAA AirVenture Oshkosh 7/31/89** (D): 'AirVenture' is an anachronism (the EAA convention adopted that name in 1998); serial as given by uploader, not verified.
- **SR-71 LAST FLIGHT** (A): Title "SR-71 LAST FLIGHT" gives no date; do not caption as the 1999 NASA last flight or the 1998 USAF last flight without identification. Catalogue gives no date or description. Which 'last flight' (6 Mar 1990 transfer flights, 1998 Det 2 end, or 9 Oct 1999 NASA) is unknown; the local ID suffix '980124' might encode a 1998 date but that is a guess.
- **SR-71 Blackbird's First Test Flight** (C): Description says the SR-71 was 'used as a spy plane for the CIA'; the CIA operated the A-12, not the SR-71 (CIA Archangel). Also claims 'Mach 3.5+'.
- **Lockheed SR-71 Blackbird Must See Clips** (D): The 'Royal International Air Tattoo' title dates from 1996, so the uploader's 'RIAT' label may be retrospective; the event year is not given.
- **YF-12 Test Program** (A): Catalog production date 1960 is impossible (the YF-12A first flew on 7 Aug 1963); misdated.
- **YF-12 Take-off** (D): Probably the NASA clip 'YF-12C Takeoff' (20.1 s), which shows SR-71A 61-7951 under the cover name YF-12C, not a YF-12A.
- **YF-12C taxi and takeoff from Edwards Air Force Base** (A): 'YF-12C' is the cover designation for SR-71A 61-7951 (tail 06937); label it as an SR-71A on the site. Captioned 'YF-12C': the aircraft is really SR-71A 61-7951, loaned to NASA under the false serial 60-6937 (research/fact_notes.md item 12; NASA FS-030).
- **YF-12C mid-air refueling** (A): 'YF-12C' is SR-71A 61-7951. Captioned 'YF-12C': the aircraft is really SR-71A 61-7951, loaned to NASA under the false serial 60-6937 (research/fact_notes.md item 12; NASA FS-030).
- **YF-12C approach and landing at Edwards Air Force Base** (A): 'YF-12C' is SR-71A 61-7951. Captioned 'YF-12C': the aircraft is really SR-71A 61-7951, loaned to NASA under the false serial 60-6937 (research/fact_notes.md item 12; NASA FS-030).
- **YF-12A landing at Edwards Air Force Base** (A): Which YF-12A is not stated.
- **YF-12C takeoff from Edwards Air Force Base** (A): 'YF-12C' is SR-71A 61-7951. Captioned 'YF-12C': the aircraft is really SR-71A 61-7951, loaned to NASA under the false serial 60-6937 (research/fact_notes.md item 12; NASA FS-030).
- **YF-12A low level test flight** (A): NASA Video 2013 upload carries a file-name title 'YF-12A_flight' that does not say it is the low-level clip. Which YF-12A (60-6935 or 60-6936) is not stated.
- **1973 close up AERIAL PAN from tail to nose of YF-12 flying over desert (prototype for SR-71 Blackbird)** (C): Caption calls the YF-12 the 'prototype for SR-71 Blackbird'; the YF-12 was an interceptor version of the A-12 and a precursor, not the SR-71 prototype (NASA description).
- **SR-71A/YF-12A takeoff and flight** (A): Date conflict: Dryden bib says 1974, Internet Archive (NASA Image Exchange) says 1/2/1978. Gallery index (2004) shortens the title to 'SR-71A/YF-12 takeoff and flight'. Page lists Medium .mov as 9,108 KB but the captured .mov is about 2.1 MB. Which airframes appear is not stated; 'SR-71A' here most likely means the YF-12C (61-7951). Title pairs 'SR-71A/YF-12A'; the description is about the YF-12. Which aircraft appears was not checked.
- **NASA YF-12 Overview (film 'The Lockheed YF-12')** (A): Commons title 'NASA YF-12 Overview' differs from the film title 'The Lockheed YF-12'. Airframes inferred: NASA flew YF-12A 60-6935 and 'YF-12C' 61-7951. Uploader's title is descriptive, not the film's real title; '1974' unverified. Description says 'three prototypes were built', correct for YF-12A (60-6934 to 60-6936).
- **YF-12A Coldwall Ground Separation Test - side view** (A): NASA Armstrong YouTube gives the side-view and front-view clips the identical title 'YF-12A Coldwall Ground Separation Test'; use the duration (34 s side, 37 s front) to tell them apart.
- **YF-12A Coldwall Ground Separation Test - front view** (A): Same YouTube title as the side-view clip (see EM-0041-03).
- **NASA and the SR-71: Back to the Future** (A): Prior research listed this as 'catalogued but no download'; it is in fact viewable on the NASA STI Program YouTube channel (RsoxG1cQP0Y).
- **SR-71 flight** (A): Gallery index calls it 'SR-71 takeoff and flight' but the clip page title is 'SR-71 flight' and describes flight and landing, not takeoff. Page says 'about 13 seconds'; the surviving MPEG probes at about 10 s. Page lists Medium .mov as 2,004 KB but the captured .mov is about 352 KB, so the larger version was replaced before capture. Specific airframe not identified.
- **SR-71 takeoff at Edwards Air Force Base** (A): Page header says 480x320 for the 480x file; aircraft (NASA 844 or 832) not identified. 2017 press coverage called this 'new' or 'rare' footage; it had been on the Dryden site since about 2003.
- **SR-71 Blackbird refueling in flight** (A): Dryden page gives the 640x size as '640x4800' (typo for 640x480). NASA Video channel copy (796WbgaF4TQ) is only 2 s, a defective upload. Aircraft not identified.
- **NASA Family Day 1992 SR71 Flyovers** (D): No description; location and aircraft not stated beyond the title.
- **LASRE ground hotfire #2** (A): Gallery index calls it 'LASRE engine ground hotfire #2'; the clip page has no clip-specific description, only LASRE background text. Whether the pod was on the SR-71 during this run is not stated. LASRE was a NASA and Lockheed Martin project: footage is NASA-filmed per the gallery, but confirm no Lockheed Martin credit.
- **SR-71 LASRE refueling in flight from a KC-135** (A): NASA Armstrong YouTube description expands LASRE as 'Linear Aerospike Rocket Engine'; NASA's own fact sheet and gallery use 'Linear Aerospike SR-71 Experiment'.
- **YF-12A (SR-71 Blackbird) Landing at Edwards Air Force Base (~1970) / AiirSource** (A): 'YF-12A (SR-71 Blackbird)' conflates two types; 'YF-12C ... (~1970)' is too early, since the YF-12C (SR-71A 61-7951 under a false serial) joined NASA in 1971.
- **Lockheed Martin YF-12 SR-71 Blackbird Montage** (C): 'Lockheed Martin YF-12' is anachronistic (the company was Lockheed until 1995).
- **NASA Released Rare Footage Of The SR-71, The Fastest Plane To Ever Exist** (C): 'Rare footage' / 'NASA released' framing: these are long-public Dryden gallery clips. Title contains an em dash in the source, replaced here.
- **YF-12C approach and landing at Edwards Air Force Base** (A): Caption is NASA's, but viewers should know the 'YF-12C' was SR-71A 61-7951 painted as 06937.
- **First Flight A-12** (D): Date and airframe inferred from title only; not verified.
- **A-12 First Flight** (C): 30 April 1962 is the official first flight; unannounced hops on 25 and 26 April preceded it (fact_notes section 1). Footage date not otherwise verified.
- **Behind the Scenes - The A-12 Oxcart on Display at CIA Headquarters** (C): Misattributed in research/sources.md section 3.3 as a CIA public-domain video; it is a Smithsonian NASM STEM in 30 production (tier C). This is NOT footage of the 2007 installation of 60-6931. sources.md section 3.3 lists this item as a PD-USGov CIA video; the IA record credits the Smithsonian Institution (STEM in 30), so treat it as Smithsonian (tier C), not CIA.
- **The Debrief: Behind The Artifact - A-12 OXCART** (A): Source title uses an en dash; replaced by a hyphen here.
- **Outrunning The Enemy: The CIA's A-12** (C): Misattributed in research/sources.md section 3.3 as a CIA public-domain video on the Internet Archive; it is a Smithsonian NASM STEM in 30 production (tier C). sources.md section 3.3 lists this as PD-USGov (CIA); the IA record credits the Smithsonian Institution (STEM in 30). Tier C, not A.
- **The Debrief: Behind the Museum - CIA in the Sky** (A): Source title uses an en dash; replaced by a hyphen here.
- **Drones and the SR-71, dare we say more?** (C): Miscaption by the manufacturer: the M-21 was a modified A-12 (Articles 134 and 135, 60-6940 and 60-6941), not a modified SR-71.
- **SR-71 Blackbird Midair Crash** (C): Titled 'SR-71 ... Crash' but shows the M-21 (modified A-12) and D-21; 'Mach2' in another title is wrong (separation at about Mach 3.2); 'MD21' is an informal name. Collision date 30 Jul 1966.
- **13News Now Vault: The fastest coast-to-coast flight ever recorded** (C): Description says 'an average speed of over 2,300 mph'; the record LA to DC average was about 2,124 to 2,145 mph (research/fact_notes.md item 3). 'Average speed of over 2,300 mph' is wrong: the Smithsonian gives 2,124 mph for LA to DC (sr-71.org 2,144.83 mph).
- **NewsChannel2 Broadcasts, March 2-7, 1990** (C): IA shot list is AI-generated ('This shot list was AI-generated and may not be fully accurate'); timing not checked.
- **SR-71 Final Flight @ Palmdale to Dulles** (D): Content not verified: description only names Yeilding and Vida; may show the Palmdale departure, the Dulles arrival, or news footage.
- **SR-71 Blackbird: Making of a Mystery** (C): Description says the SR-71 'served with the U.S. Air Force from 1964 to 1998'; 1964 is first flight, operational service began 1966.
- **A-12 OXCART on NBC** (C): Licence miscaption: Commons {{PD-USGov-CIA}} is wrong for NBC-produced footage.
- **STEM in 30 Focus on the SR 71 Blackbird** (C): Official title uses an en dash after 'STEM in 30'; rendered here with a space per house style.
- **SR-71 Blackbird / Cold War icon** (C): Says Duxford's SR-71 set the 1976 sustained altitude record at 85,000 ft; attribution of the 1976 records between 61-7958, 61-7962 and 61-7963 is disputed (research/fact_notes.md). 2.2M views.
- **The way you started up an SR-71 Blackbird was weird.** (C): Title says 'SR-71 Blackbird' but the description and aircraft are the Museum's M-21/D-21 (60-6940).
- **F-16XL Interview with Marta Bohn-Meyer** (A): Peripheral: the interview is about the F-16XL, not the SR-71.
- **Former NASA Research pilot Ed Schneider Aerospace Walk of Honor Induction Ceremony** (A): Peripheral: a ceremony clip about a NASA SR-71 pilot; the caption does not say whether the SR-71 is mentioned.
- **Former NASA Research pilot Ed Schneider Aerospace Walk of Honor Induction Ceremony Comments** (A): Peripheral: Schneider speaking about his career; SR-71 content not confirmed from the caption.
- **Retired NASA Pilot Fitz Fulton Comments on 747/Columbia Crosswind Landing at KSC** (A): Peripheral: Fulton was the lead NASA YF-12 pilot but this clip is about the 1981 shuttle ferry flight, not the Blackbird.
- **BG Dennis Sullivan on gear down at Mach 3** (D): The ATFSCrash copy calls gear-down at Mach 3.2 a 'World Record'; it is an anecdote, not a sanctioned record.
- **Tribute to MSGT Leland Haynes, Crew Chief of the SR-71** (D): Uses the serial form '64-17972'; project convention is 61-7972 (research/fact_notes.md item 11).
- **Joseph Francis Godlewski Collection** (D): Record conflates the U-2 with the 'Blackbird'; service 1953-1957 predates the A-12 and SR-71.
- **BD-0012 Frank Murray Oral Interview, Lockheed A-12, 4/29/14** (D): Title says 4/29/14; description says the interview was 'conducted 4-28-14'.
- **Swedish pilots presented with U.S. Air Medal - Lt. Col. (Ret.) Tom Vetri** (A): Title and rights line spell the RSO's name 'Tom Vetri' and a tag reads 'tom-veltir'; the DVIDS description itself spells it 'Tom Veltri'.
- **Nov. 5, 2022 SR-71 Crew - Spy Pilot Chronicles - Brian Shul & Walter Watson, Harris Center Folsom CA** (D): Description repeats '4,000 missiles'; Air & Space Forces Magazine and Beale/DVIDS give 'more than 1,000' (see fact_notes myth 4).
- **Trojan Talk w/ Ed Yielding - TROY TrojanVision News** (C): Title spells the name 'Yielding'; correct spelling is Yeilding (NASM). Title misspells 'Yeilding' as 'Yielding'.
- **Dryden's 60 Years of Flight Research (Six Decades of Flight Research: Dryden Flight Research Center, 1946 to 2006)** (A): Dryden index labels both the Shuttle era and the High Alpha era files 'clips 20-26 combined'; the High Alpha file is actually clips 27-34.
- **VT 311 Blackbirds Are Flying Lockheed SR-71** (C): Runs 1:12:57, much longer than the Lockheed film alone; tape VT 311 probably holds more than one item. Not verified.
- **Aeronautics and Space 1973 (NASA year-in-review film)** (C): Periscope 71922 caption says 'SR-71 Blackbird / YF-12'; the NASA research aircraft of 1973 were YF-12s (plus the YF-12C/SR-71A 61-7951). Not verified by viewing. Periscope's description says 'SR-71 Blackbird / YF-12'; in 1973 NASA flew YF-12s (the YF-12C was SR-71A 61-7951 under a false serial), so 'SR-71' here likely means the YF-12C.
- **Herdenking van de eerste Indievlucht van KLM in 1974 Weeknummer 74-41 - Open Beelden - 17655** (B): Commons dates it 1974-01-01 and files it under 'January 1974 in Europe', but the newsreel number 74-41 indicates about October 1974. The black and white Blackbird landing shots are probably not filmed in the Netherlands (possibly Farnborough, September 1974); not verified.
- **Know Your Aircraft - SR-71** (A): DVIDS location (Minneapolis-St. Paul) is the producing unit's home, not where the footage was shot. The AIRBOYD re-upload pastes the NMUSAF 61-7976 fact sheet into its description, which implies the footage shows 61-7976; not verified.
- **This SR-71 Pilot Free Fell from the Edge of Space** (C): 'Free Fell from the Edge of Space' is hyperbole: the description itself gives 79,000 ft. Airframe 61-7952 (25 Jan 1966 break-up) is project knowledge, not stated in the video page.
- **SR-71Blackbird - U.S. Air Force - 1979 - 4K AI Upscaled** (C): AI-upscaled to '4K'; not an original-resolution master.
- **Battle Stations - SR-71 Blackbird Stealth Plane -Full Documentary** (C): The same programme circulates as 'Battle Stations', 'BBC Documentary' and 'Blackbird Stealth'; running times of 47:23, 1:04:01, 1:14:21 and 1:21:29 all carry the Battle Stations name, so at least two different programmes share the title.
- **Russian Su-27 fighter jets attempt to intimidate a USAF SR-71 Blackbird.** (C): Simulator (DCS) renders captioned like real events; one claims '(1969 - UNCLASSIFIED)', another an SR-71 beside a Delta airliner. GoPro did not exist in the SR-71 era. Some descriptions disclose DCS only after truncation.
- **Lockheed SR-71 Blackbird / New York to London in 1h 54 mins / The untouchable reconnaissance plane** (C): DroneScapes labels its archive compilations 'Upscaled' (machine upscaling; not original resolution). gkuY-_7Gx10 calls the YF-12 the 'SR-71 Blackbird (interceptor Version)'; the YF-12 was an A-12 derivative.
- **SR-71 Takeoff from Okinawa (FULL Afterburner)** (C): Uploader admits the picture is not real; only the sound is claimed genuine.
- **1987 VHS - Discovery TV Broadcast: Russian and American Military Aviation 60 FPS** (C): IA title says 'Discovery TV Broadcast' while the description identifies the programme as Bravo's 'Firepower'.
- **First Flights with Neil Armstrong (24/39) : Faster than the Eye and Higher than the Sky** (C): Description implies the SR-71 was developed after the May 1960 U-2 shootdown; A-12 design work began before it (CIA Archangel), so the sequence is oversimplified.
- **Strange Planes (3/6) : Eyes in the Sky** (C): Description says LA to Dulles took 62 minutes; the 6 Mar 1990 flight took 1 h 4 min 20 s (Smithsonian).
- **The last official flight of the SR-71 Blackbird** (C): 'Last official flight' is ambiguous: USAF retired the SR-71 in 1990 (and again in 1998), NASA's last flight was 9 Oct 1999. Verify what is shown before citing.
- **Air Crash Investigation First Stealth Blackbird SR 71 History Documentary (and variants)** (C): Mislabelled: no Air Crash Investigation (Mayday) episode about the SR-71 appears in Wikipedia's episode list; 'BBC' attribution unverified.
- **Lockheed SR-71 Blackbird Fastest Jet in the World Full Documentary** (C): Identical 47:23 running time under four different titles, one of them claiming to be Battle Stations and one 'Wings & Discovery'; producer unconfirmed.
- **A-12 at Groomlake** (C): Uploader calls it 'This awesome documentary'; looks like a TV documentary re-upload with no credit. Calls the A-12 'US first stealth aircraft'.

## Method, gaps and blocked sources

**What we swept on 4 October 2026:**

- **National Archives.**
  - Full-text sweep of the NARA catalog's open-data export (`s3://nara-national-archives-catalog`, descriptions JSONL). It covered RG 342 (USAF films), RG 330 (DIMOC/DVIC), RG 111 (DoD filmed news releases), RG 306 (USIA), RG 255 (NASA), RG 263, RG 341 and RG 428, plus the Universal Newsreel collection and the LBJ Library collections (WHNPC films, WHCA audio, network films, NSF).
  - In the record groups swept, only three Blackbird films have digital copies attached in the NARA catalog: SR-71 LAST FLIGHT, The Record Breakers and Aim High. All three were downloaded. Every other NARA film listed here is held only as original film or tape.
- **NASA.**
  - images.nasa.gov API: no hits for "SR-71", "YF-12" or "LASRE" video. Four 1080p masters with Blackbird segments were found only by searching the caption files.
  - The legacy Dryden movie gallery in the Wayback Machine (EM-0025 SR-71, EM-0041 YF-12, EM-0018 LASRE, EM-0086, EM-0093).
  - The NTRS video records and the NASA YouTube channels.
- **DoD.** DVIDS (17 videos found; higher-resolution renditions on DVIDS's CloudFront store), NMUSAF, Edwards and USAF YouTube channels, and the AFRTS/FEN uploads.
- **CIA, NRO and Smithsonian.** CIA and NRO YouTube channels and sites, Smithsonian NASM and Channel, and Wikimedia Commons (category trees and API).
- **Oral histories.** Library of Congress Veterans History Project, SDASM/Calisphere, UNLV and Roadrunners Internationale.
- **Internet Archive.** Advanced search including NTIS, FedFlix, Universal Newsreels and C-SPAN mirrors.
- **Commercial archives.** CriticalPast, British Pathe/Reuters, AP, Getty and Footage Farm (record only), plus museum channels and notable documentaries.

**Blocked or incomplete:**

- **YouTube.** It refused every player request from this network (the "Sign in to confirm you're not a bot" check). As a result:
  - YouTube-only items have no verified resolution or file size.
  - Tier A items that exist only on YouTube are listed as *pending download*.
  - Their titles, dates, durations and licence rows come from the channel listings and page data.
- **Sites refusing scripted clients or showing bot challenges:**
  - **Reached only through Wayback snapshots:** discoverlbj.org, c-span.org and criticalpast.com.
  - **Not reached at all:** britishpathe.com, aparchive.com, nbcnewsarchives.com, af.mil, nationalmuseum.af.mil, collections.si.edu, calisphere.org, special.library.unlv.edu and the DVIDS search pages.
  - **Consequence:** the DVIDS list is surely incomplete. We could not search for DVIDS heritage pieces from Beale or for the July 2026 Mildenhall veterans' visit.
- **Search engine.** The WebSearch budget for this session was used up before this task started, so discovery relied on site-native APIs, channel listings, Wayback CDX and the NARA export.
- **Not found anywhere online:**
  - Government film of the 26 Jan 1990 USAF retirement ceremony.
  - Government film of the 6 Mar 1990 transcontinental flight. The only footage of its arrival at Dulles is an amateur video.
  - Any digitised copy of the 1976 record flights. The NARA 342-CAM reels are undigitised.
  - Government film of the D-21/M-21 launches. Only Lockheed and Roadrunners copies exist.
  - The 1995 to 1998 reactivation. NARA holds an undigitised tape.

**Next steps that would add the most:**

1. Order NARA digitisation of the RG 342 Blackbird reels. The best are:
   - SR-71 first and second flights, 342-USAF-60150.
   - YF-12A rollout and public debut, 342-USAF-37637 and -37579.
   - The 1965 YF-12A record runs, 342-USAF-39371.
   - SR-71 crew preparation, 342-USAF-49151.
   - The Goldwater SR-71B flight, 342-USAF-48867.
   - The 1974 and 1976 speed-run reels, 342-CAM-335 and -536.
2. Order the 111-DD filmed news releases from the same source.
3. Ask the LBJ Library for WHCA 107-1 (public domain) and for the status of the 24 July 1964 film.
4. Download the pending YouTube tier A items by hand from a normal browser session: the CIA "Archangel" video, the NRO A-12 50th-anniversary event, the NMUSAF lectures, and the LBJ Library slideshow.
5. Request a DVIDS API key and re-run the DVIDS search.
