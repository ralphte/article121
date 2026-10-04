# Holding page

What article121.com shows until the Astro site is ready. A Cloudflare Worker with static assets: `public/` is served as-is, `src/worker.js` only redirects `www` to the bare domain.

Deploy (token read from 1Password, never pasted):

```bash
export CLOUDFLARE_API_TOKEN=$(op read "op://DarkClouds-Secrets/Cloudflare article121/credential")
npx wrangler@4 deploy
```

Fonts are self-hosted (Archivo and B612 Mono, SIL Open Font License) so visitors' browsers never contact a third party. The photo is NASA's, public domain.
