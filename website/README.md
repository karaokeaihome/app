# karaokeaihome.com

Deployed automatically by Cloudflare Workers Builds (worker `karaokeaihome-web`, root directory `website`) on every push to `main`.

- Edit text: `src/content.py` (pages), `src/pages.py` (download/support/privacy/terms).
- Rebuild HTML: `python3 src/build.py` (writes `public/`), then commit `public/` too.
- Localized mockup images: `src/mockups/` (see README.txt there).
