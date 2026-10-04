// Turn the research pack into the site's content data.
//
//   research/timeline.json, research/airframes.json, design/img/airframes/manifest.json
//     -> web/src/data/{sources,events,airframes,photos}.json
//
// Every citation in the research pack is an inline {title, publisher, url}. Here they are
// collected into one source register keyed by URL, and each event and airframe keeps a list
// of {source, detail} citations, where detail preserves page numbers or a more specific title.
// Photos are copied into src/assets/photos so Astro can make responsive versions; the
// full-resolution hero masters go to public/masters for the loupe and full-screen viewer.
import { createHash } from 'node:crypto';
import { copyFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../..');
const web = resolve(here, '..');
const read = (p) => JSON.parse(readFileSync(join(root, p), 'utf8'));

const timeline = read('research/timeline.json');
const airframes = read('research/airframes.json');
const manifest = read('design/img/airframes/manifest.json');
const legacyCredits = read('design/img/credits.json');

// ---------- source register
const sources = new Map();
const norm = (u) => u.trim().replace(/#.*$/, '').replace(/\/+$/, '');
const slug = (s) => s.toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);
function cite(s) {
  if (!s?.url) throw new Error(`citation without a URL: ${JSON.stringify(s)}`);
  const key = norm(s.url);
  if (!sources.has(key)) {
    const id = `${slug(s.publisher || 'source')}-${createHash('sha1').update(key).digest('hex').slice(0, 6)}`;
    sources.set(key, { id, title: s.title, publisher: s.publisher || '', url: s.url, uses: 0 });
  }
  const rec = sources.get(key);
  rec.uses += 1;
  return rec.title === s.title ? { source: rec.id } : { source: rec.id, detail: s.title };
}

// ---------- events
const events = timeline.map((e) => ({
  id: e.id,
  date: e.date,
  precision: e.precision,
  title: e.title,
  summary: e.summary,
  program: e.program,
  airframes: e.airframes || [],
  people: e.people || [],
  citations: (e.sources || []).map(cite),
  ...(e.notes ? { notes: e.notes } : {}),
}));

// ---------- airframes
const airframeId = (serial) => (serial.startsWith('D-21') ? 'd-21' : serial);
const afOut = airframes.map((a) => ({
  id: airframeId(a.serial),
  serial: a.serial,
  type: a.type,
  article: a.article ?? null,
  nickname: a.nickname ?? null,
  first_flight: a.first_flight ?? null,
  fate: a.fate,
  fate_detail: a.fate_detail,
  location: a.location ?? null,
  displays: a.displays ?? [],
  total_hours: a.total_hours ?? null,
  notable: a.notable || [],
  notes: a.notes ?? null,
  citations: (a.sources || []).map(cite),
}));
const known = new Set(afOut.map((a) => a.id));

// ---------- photos
const photosDir = join(web, 'src/assets/photos');
const mastersDir = join(web, 'public/masters');
mkdirSync(photosDir, { recursive: true });
mkdirSync(mastersDir, { recursive: true });
const photos = [];
function addPhoto(p, airframe, kind) {
  const src = join(root, 'design', p.file);
  if (!existsSync(src)) throw new Error(`missing photo ${p.file}`);
  const name = basename(p.file);
  copyFileSync(src, join(photosDir, name));
  let master = null;
  if (kind === 'hero') {
    copyFileSync(src, join(mastersDir, name));
    master = `/masters/${name}`;
  }
  for (const f of ['creator', 'license', 'source_page']) if (!p[f]) throw new Error(`photo ${name} lacks ${f}`);
  photos.push({
    id: name.replace(/\.[^.]+$/, ''),
    file: `../assets/photos/${name}`,
    master,
    airframe: airframe && known.has(airframe) ? airframe : null,
    kind,
    caption: p.caption,
    creator: p.creator,
    date: p.date ?? null,
    license: p.license,
    license_url: p.license_url ?? null,
    tier: p.tier ?? 'A',
    source_page: p.source_page,
    original_id: p.original_id ?? null,
  });
}
for (const [key, list] of Object.entries(manifest)) {
  if (key === 'hero') { list.forEach((p) => addPhoto(p, serialFromCaption(p.caption), 'hero')); continue; }
  const af = key === 'd21' ? 'd-21' : key;
  list.forEach((p) => addPhoto(p, af, p.kind || 'in service'));
}
// Round 1 picks that are not already in the manifest
const legacy = {
  'a12-flying.jpg': ['60-6932', 'A-12 60-6932 in flight in the 1960s. It was lost over the South China Sea in June 1968.', 'DoD VIRIN DF-SC-82-10542'],
  'sr71-tanker.jpg': [null, 'An SR-71A closes on the boom of a KC-135Q tanker, 1989.', 'DoD VIRIN DF-ST-89-06276'],
  'j58-afterburner.jpg': [null, 'A J58 turbojet in full afterburner during a ground run at NASA Dryden, 4 April 1997.', 'NASA EC97-44007-01'],
  'sr71-takeoff.jpg': ['61-7956', "NASA's SR-71B, 831, leaves the runway at Edwards with shock diamonds in both exhaust plumes, 1992.", null],
  'a12-helmet.jpg': [null, 'A-12 OXCART pilot helmet, from the CIA Museum collection.', null],
};
for (const [name, [af, caption, oid]] of Object.entries(legacy)) {
  const c = legacyCredits[name];
  addPhoto({ file: `img/${name}`, caption, creator: c.artist || 'U.S. government', date: c.date || null,
    license: 'Public domain (US government work)', license_url: 'https://commons.wikimedia.org/wiki/Template:PD-USGov',
    tier: 'A', source_page: c.page, original_id: oid }, af, 'in service');
}
function serialFromCaption(c) {
  const m = c.match(/\b(6[01]-\d{4})\b/);
  return m ? m[1] : null;
}

// ---------- write
const out = join(web, 'src/data');
mkdirSync(out, { recursive: true });
const srcList = [...sources.values()].sort((a, b) => b.uses - a.uses);
writeFileSync(join(out, 'sources.json'), JSON.stringify(srcList, null, 1));
writeFileSync(join(out, 'events.json'), JSON.stringify(events, null, 1));
writeFileSync(join(out, 'airframes.json'), JSON.stringify(afOut, null, 1));
writeFileSync(join(out, 'photos.json'), JSON.stringify(photos, null, 1));
console.log(`imported ${events.length} events, ${afOut.length} airframes, ${photos.length} photos, ${srcList.length} sources`);
