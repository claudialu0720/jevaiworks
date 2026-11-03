# Fishing rewards scene

Implemented in the Chinese and English landing pages. The source Figma file is
`LnrqTwMwkOfDH3AfZRSSA4`: Chinese frame `3927:4996`, English frame `3927:4997`.

The Figma design context was converted to static HTML with native inline styles;
no React or Tailwind runtime is required. `tools/rewards-cn.html` and
`tools/rewards-en.html` preserve the original layer IDs, composition, card text,
glass effects, image crops, and phone UI. The landing generator embeds these
fragments. Images and SVGs are local under `assets/little-elsewhere/rewards/`;
identical files were deduplicated and PNGs encoded as WebP. The original design
screenshots are visual references only, not implementation assets.

`landing-v4.css` scales the 4177 × 1514 artboard on desktop and rearranges the
cards, notes, copy, phone, and decorations on narrow screens. `product.js` loads
the scene images ahead of the viewport, reveals layers once with staggered
transitions, and pauses gentle floating outside the viewport or in hidden tabs.
Reduced-motion preferences show the complete composition without animation.
The static composition also works with JavaScript disabled in modern browsers.

Validation: both languages at 1440, 768, and 390px; all scene images loaded;
no horizontal overflow or page errors; every layer revealed after scrolling;
live reduced-motion changes disabled animation. The local link/asset checker
passes (11 pages, 417 references). Desktop rendering also checked with JavaScript
disabled. Existing unrelated workspace changes were retained. No deployment.

Rebuild with `python tools/build-little-elsewhere.py`. After editing text, update
font subsets with `python tools/build-little-elsewhere-fonts.py`.
