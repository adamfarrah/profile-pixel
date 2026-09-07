# Adem Ferrah — Portfolio

Personal portfolio of **El Moattassam Billah Adem Ferrah** — Information Network
Administration & Security.

Zero frameworks, zero build step, zero runtime dependencies. Plain HTML, CSS and
vanilla JavaScript in a single document. Trilingual (EN / FR / AR) with full RTL
support.

---

## Repository layout

| Path | What it is |
|---|---|
| `index.html` | **The source.** Inline CSS + JS, references `assets/`. Edit this. |
| `assets/` | Background, profile picture, clover and koi images (full + downscaled `_s` variants). |
| `i18n/dict.py` | **Translation source of truth.** `{ english: (arabic, french) }`. |
| `i18n/dict.js` | Generated from `dict.py` — the dictionary embedded into the page. |
| `build.py` | Inlines every asset as Base64 and emits the standalone file. |
| `Onyx-website.html` | **Deploy-ready single file.** ~560 KB, zero external references. |
| `_headers` | Netlify cache rules (immutable 1-year caching for `/assets/*`). |
| `site.json` | *(optional, you create it)* Shared links + profile picture, manual publishing. |
| `supabase-setup.sql` | Run once in Supabase to enable automatic cloud sync. |

---

## Two ways to deploy

**A — single file (simplest).**
Upload `Onyx-website.html` on its own and rename it to `index.html`. Every image
is embedded as Base64, so nothing can break from a missing file.

**B — the folder (faster for repeat visitors).**
Deploy the repo root as-is. Images are cached separately for a year via
`_headers`, so returning visitors only re-download the HTML.

> Option B is measurably faster on repeat visits; option A is immune to broken
> asset paths. Both are fine.

### GitHub Pages
Settings → Pages → Source: `main`, folder `/ (root)`.
Uses `index.html` + `assets/` automatically (option B). `_headers` is ignored by
GitHub Pages — it only applies on Netlify.

### Netlify
Drag the folder into Netlify, or connect the repo. No build command, publish
directory `.`.

---

## Editing

### Content
All card content lives in JS arrays near the bottom of `index.html`:

| Array | Section |
|---|---|
| `LINKS` | Social links (defaults; users can override in-browser) |
| `FOCUS` | 02 — Technical Focus |
| `SERV`  | 04 — Services |
| `AI`    | 05 — Innovation |
| `MARQ`  | Scrolling marquee terms |

The Experience timeline (03) is plain markup — edit it directly in the HTML.

### Translations
1. Edit `i18n/dict.py` — add `"English string": ("عربي", "Français"),`
2. Run `python3 build.py` (it regenerates `dict.js` and re-embeds it).

Names, brands and technical tokens (pfSense, VLAN, Instagram, `Adem Ferrah`, …)
are deliberately **never** translated — they're protected by a `KEEP` regex in
the i18n engine.

### Rebuilding after any change

```bash
python3 build.py
```

Writes `index_standalone.html` (gitignored) and `Onyx-website.html`.
Then hard-refresh the browser: **Ctrl+Shift+R**.

---

## Admin panel

Add, edit, reorder and remove links, and change the profile picture, without
touching code.

- **Open:** the "Manage links" button in the footer, or `Ctrl+Shift+L`
- **Default password:** `onyx2026`

Change it from inside the panel. The password is stored as a SHA-256 hash and
gates **link editing only** — never access to the site itself.

### Publishing your changes

Edits in the panel are saved to `localStorage` by default, which is **private to
that one browser**. There are two ways to make them visible to everyone.

#### Option 1 — Cloud sync (automatic, recommended)

Set this up once and every future edit reaches all visitors by itself — no file
uploads, works from your phone.

1. Create a free project at [supabase.com](https://supabase.com).
2. Open **SQL Editor → New query**, paste all of
   [`supabase-setup.sql`](supabase-setup.sql), press **RUN**.
   (Change the password on the `insert into private_admin` line first.)
3. Go to **Settings → API** and copy the **Project URL** and the **anon public
   key**.
4. On your site: admin panel → **Cloud sync** → paste both plus your password →
   **Connect & sync**.
5. It hands you one line like
   `var CLOUD={url:'https://xxxx.supabase.co',key:'eyJ...'};`
   Paste it into `index.html` (replacing the empty `var CLOUD=...`) and upload
   the file **once**.

Done. From then on: open the panel anywhere, enter your password, edit — and
everyone sees it within seconds.

> **Is the anon key safe in public HTML?** Yes — it is designed to be public.
> The database policy only accepts a write when the request carries your admin
> password, which is stored in a table the anon key cannot read. A visitor
> sending a forged write gets `403`. This is verified by an automated test.

#### Option 2 — site.json (manual, no accounts)

1. Edit in the admin panel.
2. Click **Publish (site.json)** — a file downloads.
3. Upload it next to `index.html`.

**Priority order:**

```
Supabase cloud   (if configured — everyone, instantly)
   ↓
site.json        (if uploaded — everyone, after upload)
   ↓
localStorage     (your browser only — private preview)
   ↓
LINKS defaults   (built into index.html)
```

Nothing configured? The site quietly uses the defaults — no errors.

> Both options need **http/https**. Opening the file straight from disk
> (`file://`) skips the network fetch because browsers block it.

## Features

- Full-screen gate on every load (deliberately not persisted — refresh re-locks)
- Pixel-font `ADEM FERRAH` wordmark rendered as inline SVG in three places
- Sticky pill navigation with a sliding indicator, driven by scroll position
- Trilingual EN / FR / AR with automatic RTL layout flip
- Graduation project section with an inline SVG network topology diagram
- Gmail-style compose form (opens Gmail pre-filled, `mailto:` fallback)
- Password-gated admin panel for links and profile picture
- Respects `prefers-reduced-motion`

---

## Performance notes

Built to stay cheap under load: no frameworks, no fonts fetched over the
network, no analytics, no third-party requests. The page is fully static and
CDN-cacheable, so concurrent traffic costs essentially nothing.

Animations are restricted to `transform` and `opacity` (GPU-composited), the
scroll spy is throttled to one `requestAnimationFrame` per frame, and the nav
uses `contain: layout paint` to limit reflow scope.

---

## License

MIT — see [LICENSE](LICENSE).
