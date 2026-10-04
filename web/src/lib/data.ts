import { getCollection, getEntry, type CollectionEntry } from 'astro:content';

export type Airframe = CollectionEntry<'airframes'>;
export type Event = CollectionEntry<'events'>;
export type Photo = CollectionEntry<'photos'>;
export type Citation = { source: { id: string; collection: 'sources' }; detail?: string };

const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

/** Format a date at the precision the record actually supports. */
export function fmtDate(d: string | null | undefined, precision?: string, short = false): string {
  if (!d) return '';
  const [y, m, dd] = d.split('-');
  const mon = m ? MONTHS[Number(m) - 1] : '';
  const prefix = precision === 'approx' ? 'about ' : '';
  if (dd) return `${prefix}${Number(dd)} ${short ? mon.slice(0, 3) : mon} ${y}`;
  if (m) return `${prefix}${short ? mon.slice(0, 3) : mon} ${y}`;
  return `${prefix}${y}`;
}

export const family = (type: string) =>
  type.startsWith('SR-71') ? 'SR-71' : type.startsWith('A-12') ? 'A-12' : type.startsWith('D-21') ? 'D-21' : type;

export const GROUPS: [string, string][] = [
  ['A-12', 'A-12 · CIA OXCART'],
  ['YF-12A', 'YF-12A · Air Force interceptor'],
  ['M-21', 'M-21 · drone carrier'],
  ['D-21', 'D-21 · reconnaissance drone'],
  ['SR-71', 'SR-71 · Air Force reconnaissance'],
];

export const PROGRAM_LABEL: Record<string, string> = {
  context: 'Context', archangel: 'Archangel', oxcart: 'OXCART', kedlock: 'KEDLOCK', tagboard: 'TAGBOARD',
  'senior-bowl': 'SENIOR BOWL', 'senior-crown': 'SENIOR CROWN', nasa: 'NASA', legacy: 'Legacy',
};

/** First full date written in a fate description, used for "Lost 24 May 1963" on index cards. */
export function lossDate(text: string): string | null {
  const m = text.match(/(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})/);
  return m ? `${m[1]} ${m[2].slice(0, 3)} ${m[3]}` : null;
}

export const placeOf = (a: Airframe['data']) => (a.location ? [a.location.museum, a.location.city].filter(Boolean).join(', ') : null);
export const displayName = (a: Airframe) => (a.id === 'd-21' ? 'D-21 drones' : a.data.serial);

export async function airframesInOrder() {
  const all = await getCollection('airframes');
  const order = new Map((await import('../data/airframes.json')).default.map((a: { id: string }, i: number) => [a.id, i]));
  return all.sort((a, b) => (order.get(a.id) ?? 0) - (order.get(b.id) ?? 0));
}

export async function eventsInOrder() {
  return (await getCollection('events')).sort((a, b) => a.data.date.localeCompare(b.data.date));
}

export async function resolveCitations(cites: Citation[]) {
  return Promise.all(cites.map(async (c) => ({ entry: (await getEntry('sources', c.source.id))!, detail: c.detail })));
}

export async function photosFor(airframeId: string) {
  return (await getCollection('photos', (p) => p.data.airframe === airframeId && p.data.kind !== 'hero'))
    .sort((a, b) => a.id.localeCompare(b.id));
}

/** Where a source link should go: the archived copy when the original has gone offline. */
export const sourceHref = (d: { url: string; archive?: string; offline?: string }) => (d.offline && d.archive ? d.archive : d.url);

/** Short label for a source: the work's title without parenthetical detail. */
export const shortTitle = (t: string) => t.replace(/\s*\([^)]*\)\s*$/, '').replace(/\s*\([^)]*\)/g, '').trim();
