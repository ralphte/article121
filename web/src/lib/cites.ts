// Numbered citation marks for a page: every source gets a number in order of first use, and each
// mark remembers the pages it cites, for the page's own source list. One instance per page render.
import { resolveCitations, type Citation } from './data';

type Raw = { source: { id: string } | string; detail?: string | null };

export function pageCitations() {
  const order = new Map<string, number>();
  const pages = new Map<string, Set<string>>();
  const entries = new Map<string, Awaited<ReturnType<typeof resolveCitations>>[number]['entry']>();
  async function marks(raw: Raw[]) {
    const cites: Citation[] = raw.map((c) => ({ source: { id: typeof c.source === 'string' ? c.source : c.source.id, collection: 'sources' }, detail: c.detail ?? undefined }));
    const list = await resolveCitations(cites);
    return list.map(({ entry, detail }) => {
      if (!order.has(entry.id)) order.set(entry.id, order.size + 1);
      entries.set(entry.id, entry);
      if (detail) pages.set(entry.id, (pages.get(entry.id) ?? new Set()).add(detail));
      return { n: order.get(entry.id)!, title: `${entry.data.publisher}: ${entry.data.title}${detail ? ', ' + detail : ''}` };
    });
  }
  const supHtml = (ms: { n: number; title: string }[]) =>
    `<sup class="cite">${[...new Map(ms.map((m) => [m.n, m])).values()].map((m) => `<a href="#src-${m.n}" title="${m.title.replace(/&/g, '&amp;').replace(/"/g, '&quot;')}">${m.n}</a>`).join(',')}</sup>`;
  /** The sources cited so far, numbered, with the pages each was cited at. */
  const list = () => [...order.entries()].map(([id, n]) => ({ n, entry: entries.get(id)!, pages: [...(pages.get(id) ?? [])] })).sort((a, b) => a.n - b.n);
  return { marks, supHtml, list };
}
