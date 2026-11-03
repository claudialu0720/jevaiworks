# Marketing webfonts

Self-hosted WOFF2 subsets of LXGW WenKai TC Regular (400)/Bold (700) and Fredoka Regular (400)/Medium (500).

Sources: https://github.com/google/fonts/tree/main/ofl/lxgwwenkaitc and https://github.com/google/fonts/tree/main/ofl/fredoka

Both families use SIL Open Font License 1.1. Full license/copyright notices are retained alongside the fonts. FontTools creates web subsets without changing glyph artwork. Fredoka is instantiated at standard width (100).

After marketing copy changes, run `python tools/build-little-elsewhere.py` then `python tools/build-little-elsewhere-fonts.py` to refresh Chinese character coverage. That optional maintenance script requires `fonttools` and `brotli`; the regular static page build has no new dependency. Downloaded original fonts and optional installed tooling are cached in ignored `.preview/`.

Typography is scoped to the bilingual landing pages; legal text and corporate pages retain their existing styles.
