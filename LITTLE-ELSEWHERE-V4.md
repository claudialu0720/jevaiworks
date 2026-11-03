# Little Elsewhere — V4 compact editorial redesign

Implemented locally on 2026-11-03. No deployment or push performed.

## Composition

- Three main sections: a lake and real timer interface in the hero; one connected setup → focus → catch journey; one collection/pond, soundscape, and map composition.
- A short closing CTA and compact footer replace the repeated final lake banner.
- Supplied Chinese and English copy is maintained independently. English screenshots and original English App Store collection artwork are used on the English page.
- White, airy sky blue, and pale turquoise CTAs; no changes to the shared legal stylesheet.

## Source and assets

- `tools/little_elsewhere_landing.py`: bilingual V4 copy and markup.
- `little-elsewhere/landing-v4.css`: responsive marketing styles, scoped to `.landing-page`.
- `tools/build-little-elsewhere.py`: existing static generator, updated landing stylesheet, headline metadata, and image dimensions.
- New WebP exports come from the supplied asset folder: `ss/focus.png`, `frame2_cn.png`, `frame2_en.png`, and `map.png`. Entire original compositions are preserved without redrawing UI. Existing setup/catch/landscape/soundscape exports remain in use.
- V3 CSS is retained for reference but is no longer loaded by landing pages.

## Validation

Run from the repository root:

```powershell
python tools/build-little-elsewhere.py
node tools/preview.mjs
# In another terminal while preview is running:
node tools/check.mjs
python tools/check-little-elsewhere.py
git diff --check
```

The build is static Python generation; no package installation or bundler is required.

Browser checks covered Chinese and English at 1440, 1024, and 390px. No horizontal document overflow was observed. At 1440 × 900 the complete Chinese page measured approximately 2816px (3.1 viewports); English approximately 2753px (3.1 viewports). Mobile reflows into a single journey with paired image/copy and an uncropped full-width landscape step. Images were verified loaded, the language switch was exercised, and no browser console warnings/errors were recorded.

The existing checks pass: 11 site pages, local assets/links, one H1 per page, legal-source wording, all six product/legal routes with repeated direct navigation, and corporate home/privacy/terms preservation. The four generated product legal pages, their sources, corporate pages, and routing code have no changes. Existing TestFlight destination remains `https://testflight.apple.com/join/Uk9rZz5B`.

Local visual evidence is saved under ignored `.preview/`.
