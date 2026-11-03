# Music and maps banner

The Chinese and English product pages now include this banner between fishing
rewards and the closing invitation. Figma file `LnrqTwMwkOfDH3AfZRSSA4`, frames
`3931:4998` (Chinese) and `3931:4999` (English).

`tools/worlds-cn.html` and `tools/worlds-en.html` are native static source
fragments converted from the full design context, retaining layer IDs, copy,
image crops, slider illustrations, glass panels, and map labels. The project has
no matching Code Connect library for Activity/ChevronRight, so their exact white
vector exports are used at their design slots. Temporary Figma URLs are not used
at runtime. Shared assets are deduplicated under `assets/little-elsewhere/worlds/`.
The design screenshots are references only, not implementation assets.

The banner uses the existing fonts and page reveal behavior. Six foreground
groups reveal in sequence over the lake background. Wide layouts preserve the
4177 by 1514 composition; narrow layouts stack music and maps at readable sizes.
The new section also works without JavaScript and with reduced motion enabled.
The English source preserves the two Chinese noise labels present in its Figma
frame. The sliders and map arrows are illustrations of the app, not web controls.

Rebuild pages with `python tools/build-little-elsewhere.py`; after copy edits,
rebuild font subsets with `python tools/build-little-elsewhere-fonts.py`.

Verified both languages at 1440, 768, and 390px: all six foreground groups reveal,
all images load, headings render, no horizontal overflow or page errors, and the
section is between rewards and the invitation. Reduced motion and mobile with
JavaScript disabled were checked. Site checks pass: 11 pages, 477 references;
`git diff --check` passes. No deployment performed.
