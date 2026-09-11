# Adem Ferrah — Portfolio (Onyx)

Personal portfolio of **El Moattassam Billah Adem Ferrah** — Information Network
Administration & Security.

Zero frameworks, zero build step, zero runtime dependencies. Plain HTML, CSS and
vanilla JavaScript in a single document. English only.

Layout and section flow follow the classic developer-portfolio structure
(hero → about → skills → experience → projects → services → contact), dressed in
the Onyx identity: deep-green dark theme, pixel-art clover & wordmark, neon
gradient accents.

---

## Repository layout

| Path | What it is |
|---|---|
| `index.html` | **The source.** Inline CSS + JS, references `assets/`. Edit this. |
| `assets/` | Background, avatar, clover and koi images (full + downscaled `_s` variants). |
| `build.py` | Inlines every asset as Base64 and emits the standalone single file. |
| `Onyx-website.html` | **Deploy-ready single file.** ~0.45 MB, zero external references. |
| `_headers` | Netlify cache rules (immutable 1-year caching for `/assets/*`). |

---

## Page structure

| Section | Content |
|---|---|
| Nav | Sticky blurred bar, pixel wordmark brand, pill links with sliding glider + scrollspy, "Hire me" CTA, burger menu on mobile. |
| Hero | "Hi, my name is" → pixel wordmark, typed rotating role, chips, CTAs, socials; avatar stage with breathing halo, rotating light ring and floating clover. |
| Marquee | Infinite scrolling strip of discipline keywords. |
| 01 About | Bio, stats grid (24/7, 7+, 16/20, 100%), ID card with location / degree / focus. |
| 02 Skills | Tabbed categories (Networking · Security · Systems & Tools · Web & AI), icon cards. |
| 03 Experience | Tabbed timelines: Work (freelance web, CTE field engineer, inventory manager) and Education (degree, graduation project, continuous learning). |
| 04 Projects | Featured graduation project with animated 16/20 grade dial and full GNS3 topology diagram, plus three project cards. |
| 05 Services | Seven service cards + "AI in the workflow" innovation band (six cards). |
| 07 Contact | Gmail-style compose form (opens the mail app pre-filled), copy-address button, info cards, socials. |

---

## Editing

Everything lives in `index.html`:

- **Text & sections** — plain markup, edit in place.
- **Skill / service icons** — the `IC` map (stroke icons) at the top of the
  `<script>`; cards reference them with `data-ic="name"`.
- **Social links** — the `LINKS` array (+ `SI` icon map). `copy:"handle"` makes a
  card copy the handle instead of navigating.
- **Marquee terms / typed roles** — the `MARQ` and `TYPE` arrays.

No translation layer, no gate, no admin panel — the page is intentionally a
single static document.

### Rebuilding the standalone file

```bash
python3 build.py
```

Writes `index_standalone.html` (gitignored) and `Onyx-website.html`.
Then hard-refresh the browser: **Ctrl+Shift+R**.

---

## Deploy

**GitHub Pages** — Settings → Pages → Source: `main`, folder `/ (root)`.
Uses `index.html` + `assets/` automatically.

**Netlify** — drag the folder in, or connect the repo. No build command,
publish directory `.`. `_headers` gives repeat visitors a year of asset caching.

**Single file** — upload `Onyx-website.html` on its own and rename it to
`index.html`. Every image is embedded as Base64, so nothing can break from a
missing file.

---

## Features

- Sticky pill navigation with sliding indicator, driven by scroll position
- Scrollspy + IntersectionObserver reveal animations (staggered, GPU-friendly)
- Tabbed skills and experience panels (ARIA tablist semantics)
- Typing effect for the hero role line
- Animated grade dial on the featured project (SVG stroke-dashoffset)
- Gmail-style compose form (opens the mail app pre-filled, inline validation)
- Clipboard helpers with execCommand fallback
- Full-screen ambient background (blurred image + vignette + grain)
- Respects `prefers-reduced-motion`

---

## Performance notes

No frameworks, no fonts fetched over the network, no analytics, no third-party
requests. The page is fully static and CDN-cacheable, so concurrent traffic
costs essentially nothing.

Animations are restricted to `transform` and `opacity` (GPU-composited), the
scrollspy is throttled to one `requestAnimationFrame` per frame, and the nav
uses `contain: layout paint` to limit reflow scope.

---

## License

MIT — see [LICENSE](LICENSE).
