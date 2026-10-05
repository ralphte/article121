// Content collections. The schemas are the site's rules made executable:
// an event or airframe without a source, or a photo without a creator, licence
// and source page, fails the build.
import { defineCollection, reference } from 'astro:content';
import { file } from 'astro/loaders';
import { z } from 'astro/zod';

const citation = z.object({
  source: reference('sources'),
  detail: z.string().optional(), // page numbers or a more specific title
});

const sources = defineCollection({
  loader: file('src/data/sources.json'),
  schema: z.object({
    title: z.string().min(1),
    publisher: z.string(),
    url: z.url(),
    uses: z.number().int(),
    archive: z.url().optional(), // Wayback Machine copy
    archived: z.string().optional(), // capture date of that copy
    offline: z.string().optional(), // why the original is unreachable; the copy becomes the main link
  }),
});

const PROGRAMS = ['context', 'archangel', 'oxcart', 'kedlock', 'tagboard', 'senior-bowl', 'senior-crown', 'nasa', 'legacy'] as const;

const events = defineCollection({
  loader: file('src/data/events.json'),
  schema: z.object({
    date: z.string().regex(/^\d{4}(-\d{2}(-\d{2})?)?$/),
    precision: z.enum(['day', 'month', 'year', 'approx']),
    title: z.string().min(1),
    summary: z.string().min(1),
    program: z.enum(PROGRAMS),
    airframes: z.array(z.string()),
    people: z.array(z.string()),
    citations: z.array(citation).min(1, 'Every event needs at least one source'),
    notes: z.string().optional(),
  }),
});

const location = z.object({
  museum: z.string(),
  city: z.string(),
  state_or_country: z.string(),
  lat: z.number(),
  lon: z.number(),
});

const airframes = defineCollection({
  loader: file('src/data/airframes.json'),
  schema: z.object({
    serial: z.string(),
    type: z.string(),
    article: z.string().nullable(),
    nickname: z.string().nullable(),
    first_flight: z.string().nullable(),
    fate: z.enum(['preserved', 'lost', 'other']),
    fate_detail: z.string().min(1),
    location: location.nullable(),
    displays: z.array(location.extend({ drone: z.string() }).partial({ city: true })).default([]),
    total_hours: z.number().nullable(),
    notable: z.array(z.string()),
    notes: z.string().nullable(),
    citations: z.array(citation).min(1, 'Every airframe needs at least one source'),
  }),
});

const photos = defineCollection({
  loader: file('src/data/photos.json'),
  schema: ({ image }) => z.object({
    file: image(),
    master: z.url().nullable(),
    airframe: z.string().nullable(),
    kind: z.enum(['hero', 'in service', 'today', 'system']),
    caption: z.string().min(1),
    creator: z.string().min(1),
    date: z.string().nullable(),
    license: z.string().min(1),
    license_url: z.url().nullable(),
    tier: z.enum(['A', 'B']),
    source_page: z.url(),
    original_id: z.string().nullable(),
  }),
});

// Media on the Chronology: a photograph, a page of a document, a film or a recording for an
// event, each with its own credit and licence. Only tiers A and B are hosted.
const media = defineCollection({
  loader: file('src/data/media.json'),
  schema: ({ image }) => z.object({
    event: reference('events'),
    kind: z.enum(['image', 'document', 'video', 'audio']),
    file: image().nullable(),           // the still: photograph, document page or video poster
    src: z.url().nullable(),            // video or audio on the files bucket
    master: z.url().nullable(),         // the full original on the files bucket
    duration: z.string().nullable(),
    page: z.number().int().nullable(),
    title: z.string().min(1),
    description: z.string().min(1),
    relation: z.enum(['exact', 'same-aircraft', 'same-program', 'representative']),
    creator: z.string().min(1),
    credit: z.string().min(1),
    date: z.string().nullable(),
    license: z.string().min(1),
    license_url: z.url().nullable(),
    tier: z.enum(['A', 'B']),
    source_page: z.url(),
  }),   // stills for images, documents and videos, and a src for video and audio, are checked by the import
});

export const collections = { sources, events, airframes, photos, media };
export { PROGRAMS };
