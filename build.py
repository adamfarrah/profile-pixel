#!/usr/bin/env python3
"""Inline every asset as Base64 and emit the standalone single-file build.

Reads  : index.html            (source of truth, references assets/)
Writes : index_standalone.html (gitignored scratch copy)
         Onyx-website.html     (deploy-ready single file, zero external refs)
"""
import base64, os, pathlib

here = pathlib.Path(__file__).resolve().parent
s = (here / 'index.html').read_text(encoding='utf-8')

IMG = {
    'assets/bg.jpg':     ('assets/bg_s.jpg',     'image/jpeg'),
    'assets/pfp.png':    ('assets/pfp_s.png',    'image/png'),
    'assets/clover.png': ('assets/clover_s.png', 'image/png'),
}

for ref, (file, mime) in IMG.items():
    b64 = base64.b64encode((here / file).read_bytes()).decode()
    s = s.replace(ref, 'data:%s;base64,%s' % (mime, b64))

# og:image would bloat the single file for no benefit — drop it there.
s = s.replace('<meta property="og:image" content="assets/koi.jpg">\n', '')
# favicon as a data URI is fine, but keep it tiny: it already got pfp_s above.

left = s.count('assets/')
assert left == 0, 'un-inlined asset references: %d' % left

(here / 'index_standalone.html').write_text(s, encoding='utf-8')
(here / 'Onyx-website.html').write_text(s, encoding='utf-8')
print('MB', round(len(s) / 1048576, 2), '| refs', left)
