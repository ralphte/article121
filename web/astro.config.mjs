// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://article121.com',
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
  image: { responsiveStyles: true },
});
