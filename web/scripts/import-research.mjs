// Turn the research pack into the site's content data.
//
//   research/timeline.json, research/airframes.json, design/img/airframes/manifest.json,
//   research/machine.json (+ research/systems/media/manifest.json)
//     -> web/src/data/{sources,events,airframes,photos,machine}.json
//
// Every citation in the research pack is an inline {title, publisher, url}. Here they are
// collected into one source register keyed by URL, and each event and airframe keeps a list
// of {source, detail} citations, where detail preserves page numbers or a more specific title.
// Photos are copied into src/assets/photos so Astro can make responsive versions; the
// full-resolution hero masters are served from the public R2 bucket at files.article121.com.
import { createHash } from 'node:crypto';
import { copyFileSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../..');
const web = resolve(here, '..');
const FILES_BASE = process.env.FILES_BASE || 'https://files.article121.com';
const read = (p) => JSON.parse(readFileSync(join(root, p), 'utf8'));

const timeline = read('research/timeline.json');
const airframes = read('research/airframes.json');
const manifest = read('design/img/airframes/manifest.json');
const legacyCredits = read('design/img/credits.json');
// Wayback Machine copies of cited pages (tools/archive_sources.py); optional so a fresh clone builds
const archives = existsSync(join(root, 'research/archives.json')) ? read('research/archives.json') : {};

// ---------- source register
const sources = new Map();
const norm = (u) => u.trim().replace(/#.*$/, '').replace(/\/+$/, '');
const slug = (s) => s.toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);
function cite(s) {
  if (!s?.url) throw new Error(`citation without a URL: ${JSON.stringify(s)}`);
  const key = norm(s.url);
  if (!sources.has(key)) {
    const id = `${slug(s.publisher || 'source')}-${createHash('sha1').update(key).digest('hex').slice(0, 6)}`;
    const arc = archives[s.url.trim()] ?? Object.entries(archives).find(([u]) => norm(u) === key)?.[1];
    sources.set(key, {
      id, title: s.title, publisher: s.publisher || '', url: s.url, uses: 0,
      ...(arc?.wayback ? { archive: arc.wayback, archived: arc.captured } : {}),
      ...(arc?.offline ? { offline: arc.offline } : {}),
    });
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
mkdirSync(photosDir, { recursive: true });
const photos = [];
function addPhoto(p, airframe, kind, masterUrl = null) {
  const src = join(root, 'design', p.file);
  if (!existsSync(src)) throw new Error(`missing photo ${p.file}`);
  const name = basename(p.file);
  copyFileSync(src, join(photosDir, name));
  // Full-resolution masters live in R2 (tools/r2 copy design/img/hero r2:article121-files/masters)
  const master = kind === 'hero' ? `${FILES_BASE}/masters/${name}` : masterUrl;
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

// ---------- The Machine (research/machine.json, figures from research/systems)
// Paragraphs and data plate rows cite sources by key and page; a missing or unknown key fails the
// build. Figures are reduced copies in design/img/systems; the full-resolution files are in R2
// under systems/ (tools/r2 copy research/systems/media r2:article121-files/systems).
const machineIn = read('research/machine.json');
const media = Object.fromEntries(read('research/systems/media/manifest.json').map((m) => [m.file, m]));
const licenseUrl = (l) => (
  /^CC BY-SA 3\.0/.test(l) ? 'https://creativecommons.org/licenses/by-sa/3.0/'
  : /^CC BY-SA 2\.0/.test(l) ? 'https://creativecommons.org/licenses/by-sa/2.0/'
  : /^CC BY 2\.0/.test(l) ? 'https://creativecommons.org/licenses/by/2.0/'
  : /^CC0/.test(l) ? 'https://creativecommons.org/publicdomain/zero/1.0/'
  : null);
function machineCites(list, where) {
  if (!list?.length) throw new Error(`machine.json ${where}: needs at least one source`);
  return list.map(([key, at]) => {
    const src = machineIn.sources[key];
    if (!src) throw new Error(`machine.json ${where}: unknown source ${key}`);
    return { source: cite(src).source, detail: at };
  });
}
const machineAdded = new Set();
function machineFigure(f, where) {
  const m = media[f.file];
  if (!m) throw new Error(`machine.json ${where}: ${f.file} is not in the systems media manifest`);
  if (!['A', 'B'].includes(m.rights_tier)) throw new Error(`${f.file}: tier ${m.rights_tier} cannot be shown`);
  const stem = f.file.replace(/\.[^.]+$/, '');
  if (machineAdded.has(stem)) return stem;
  machineAdded.add(stem);
  addPhoto({
    file: `img/systems/${stem}.jpg`, caption: f.caption, creator: m.creator, date: m.date || null,
    license: m.license, license_url: licenseUrl(m.license), tier: m.rights_tier,
    source_page: m.source_url, original_id: f.original_id ?? null,
  }, null, 'system', `${FILES_BASE}/systems/${encodeURIComponent(f.file)}`);
  return stem;
}
const machine = {
  intro: { text: machineIn.intro.text, citations: machineCites(machineIn.intro.cite, 'intro') },
  plate: machineIn.plate.map((r, i) => ({ label: r.label, value: r.value, metric: r.metric ?? null, citations: machineCites(r.cite, `plate ${i}`) })),
  hero: machineFigure(machineIn.hero, 'hero'),
  sections: machineIn.sections.map((sec) => ({
    id: sec.id, kicker: sec.kicker, title: sec.title,
    paras: sec.paras.map((p, i) => ({ text: p.text, citations: machineCites(p.cite, `${sec.id} paragraph ${i + 1}`) })),
    figures: sec.figures.map((f) => machineFigure(f, sec.id)),
  })),
  inlet: { ...machineIn.inlet_explainer, citations: machineCites(machineIn.inlet_explainer.cite, 'inlet explainer') },
};
delete machine.inlet.cite;
if (machineIn.model) machine.model = { text: machineIn.model.text, citations: machineCites(machineIn.model.cite, 'model') };
// Parts of the 3D model: what each is, with sources. Ids match the a121_part extras in the glTF;
// an entry with "alias" shares another entry's text (left and right of a pair).
if (machineIn.parts) {
  const parts = {};
  for (const [id, p] of Object.entries(machineIn.parts)) {
    const base = p.alias ? machineIn.parts[p.alias] : p;
    if (!base || !base.text) throw new Error(`machine.json part ${id}: no text (alias ${p.alias})`);
    parts[id] = { title: p.title || base.title, text: base.text, citations: machineCites(base.cite, `part ${id}`) };
  }
  machine.parts = parts;
  machine.layers = machineIn.layers ?? [];
}
// Panel explorer: positions of the keyed items on the pilot's panel drawing (research/systems/panel_fig1-12.json)
const panelIn = machineIn.panel;
if (panelIn && existsSync(join(root, panelIn.positions))) {
  const pos = read(panelIn.positions);
  const zoneOf = new Map(panelIn.zones.flatMap((z) => z.keys.map((k) => [k, z.id])));
  machine.panel = {
    figure: machineFigure({ file: panelIn.figure, caption: 'Flight manual Figure 1-12: the pilot\'s centre instrument panel, keyed 1 to 50.', original_id: 'T.O. SR-71A-1 p.1-23' }, 'panel'),
    width: pos.width, height: pos.height,
    citations: machineCites(panelIn.cite, 'panel'),
    zones: panelIn.zones.map(({ id, name }) => ({ id, name })),
    items: pos.items.map((it) => {
      const note = panelIn.notes[String(it.key)];
      if (!zoneOf.has(it.key)) throw new Error(`panel item ${it.key} has no zone`);
      return {
        key: it.key, name: it.name, zone: zoneOf.get(it.key), inset: !!it.inset,
        // tap targets: each half of a left/right pair separately where the positions give them
        spots: (it.parts?.length ? it.parts : [it]).map((q) => ({
          x: +(q.x / pos.width * 100).toFixed(3), y: +(q.y / pos.height * 100).toFixed(3), r: +(q.r / pos.width * 100).toFixed(3),
        })),
        note: note ? { text: note.text, citations: machineCites(note.cite, `panel note ${it.key}`) } : null,
      };
    }),
  };
}

// ---------- Chronology and Stories media (research/timeline-media.json and research/stories-media.json,
// prepared by tools/timeline_media.py). A story item may reuse a Chronology item: { "story", "reuse": id }.
const mediaDir = join(web, 'src/assets/media');
mkdirSync(mediaDir, { recursive: true });
const eventIds = new Set(events.map((e) => e.id));
const RELATIONS = ['exact', 'same-aircraft', 'same-program', 'representative'];
const storiesIn = existsSync(join(root, 'research/stories.json')) ? read('research/stories.json').stories : [];
const storyIds = new Set(storiesIn.map((s) => s.id));
const tlItems = read('research/timeline-media.json').items;
const tlById = new Map(tlItems.map((m) => [m.id, m]));
const storyItems = existsSync(join(root, 'research/stories-media.json')) ? read('research/stories-media.json').items : [];
const tlMedia = [];
function addMedia(m, owner) {
  if (m.kind !== 'audio' && !m.file) return;                     // not fetched yet, or failed
  if (!['A', 'B'].includes(m.tier)) throw new Error(`media ${m.id}: tier ${m.tier} is not hosted`);
  for (const f of ['creator', 'credit', 'license', 'source_page', 'title']) if (!m[f]) throw new Error(`media ${m.id} lacks ${f}`);
  if (['video', 'audio'].includes(m.kind) && !m.src) throw new Error(`media ${m.id}: ${m.kind} without a src`);
  let file = null;
  if (m.file) {
    const name = basename(m.file);
    copyFileSync(join(root, 'design', m.file), join(mediaDir, name));
    file = `../assets/media/${name}`;
  }
  tlMedia.push({
    id: owner.id, event: owner.event ?? null, story: owner.story ?? null, kind: m.kind, file, src: m.src ?? null, master: m.master ?? null,
    duration: m.duration ?? null, page: m.kind === 'document' ? (Number.isInteger(m.page) ? m.page : parseInt(String(m.page ?? '').match(/\d+/)?.[0] ?? '1', 10)) : null,
    title: m.title, description: m.description || m.title, relation: RELATIONS.includes(owner.relation ?? m.relation) ? owner.relation ?? m.relation : 'representative',
    creator: m.creator, credit: m.credit, date: m.date ?? null, license: m.license, license_url: m.license_url ?? null,
    tier: m.tier, source_page: m.source_page,
  });
}
for (const m of tlItems) {
  if (!eventIds.has(m.event)) throw new Error(`timeline-media ${m.id}: unknown event ${m.event}`);
  addMedia(m, { id: m.id, event: m.event });
}
for (const m of storyItems) {
  if (!storyIds.has(m.story)) throw new Error(`stories-media ${m.id}: unknown story ${m.story}`);
  const base = m.reuse ? tlById.get(m.reuse) : m;
  if (!base) throw new Error(`stories-media ${m.id}: reuses unknown item ${m.reuse}`);
  addMedia(base, { id: m.id, story: m.story, relation: m.relation });
}

// ---------- Stories (research/stories.json): each paragraph cites keys from its story's own sources
function storyCites(st, list, where) {
  if (!list?.length) throw new Error(`stories.json ${st.id} ${where}: needs at least one source`);
  return list.map(([key, at]) => {
    const src = st.sources?.[key];
    if (!src) throw new Error(`stories.json ${st.id} ${where}: unknown source ${key}`);
    return { source: cite(src).source, detail: at || undefined };
  });
}
const storiesOut = storiesIn.map((st) => ({
  id: st.id, title: st.title, dek: st.dek, date: st.date, precision: st.precision || 'day',
  programs: st.programs || [], airframes: st.airframes || [], people: st.people || [], kind: st.kind === 'legend' ? 'legend' : 'story',
  verdict: st.verdict ? { text: st.verdict, citations: storyCites(st, st.verdict_cite, 'verdict') } : null,
  body: st.body.map((p, i) => ({ text: p.text, citations: storyCites(st, p.cite, `paragraph ${i + 1}`) })),
  differ: st.differ ? { text: st.differ.text, citations: storyCites(st, st.differ.cite, 'differ') } : null,
}));

// ---------- write
const out = join(web, 'src/data');
mkdirSync(out, { recursive: true });
const srcList = [...sources.values()].sort((a, b) => b.uses - a.uses);
writeFileSync(join(out, 'sources.json'), JSON.stringify(srcList, null, 1));
writeFileSync(join(out, 'events.json'), JSON.stringify(events, null, 1));
writeFileSync(join(out, 'airframes.json'), JSON.stringify(afOut, null, 1));
writeFileSync(join(out, 'photos.json'), JSON.stringify(photos, null, 1));
writeFileSync(join(out, 'machine.json'), JSON.stringify(machine, null, 1));
writeFileSync(join(out, 'media.json'), JSON.stringify(tlMedia, null, 1));
writeFileSync(join(out, 'stories.json'), JSON.stringify(storiesOut, null, 1));
// The data changed: drop Astro's cached content store so it re-reads every entry (the image cache
// in node_modules/.astro/assets is kept).
for (const f of ['node_modules/.astro/data-store.json', '.astro/data-store.json']) rmSync(join(web, f), { force: true });
console.log(`imported ${events.length} events, ${afOut.length} airframes, ${photos.length} photos, ${tlMedia.length} media, ${storiesOut.length} stories, ${srcList.length} sources`);
