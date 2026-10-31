> Current decisions and submission status: READINESS-REVIEW.md supersedes earlier missing-Plus/account/cloud assumptions below. Latest remote main 7137ae8 confirms implemented purchases/restore; release-candidate validation and updated product decisions remain pending. The new Free/Plus matrix, pricing, 4+ target and Productivity/non-Kids positioning are recorded there. No final App Store Connect configuration is available.

# Little Elsewhere 1.0 launch handoff

Prepared 2026-10-31. Local changes only: no production deploy, DNS, hosting or release-state change.

## Intended public URLs

The repository uses the canonical www domain; keep the existing domain/redirect setup.

- Marketing: https://www.jevaiworks.com/little-elsewhere/
- Support: https://www.jevaiworks.com/little-elsewhere/support/
- App privacy: https://www.jevaiworks.com/little-elsewhere/privacy/ (**draft, not submission-ready**)
- Website privacy: https://www.jevaiworks.com/privacy/
- Website terms: https://www.jevaiworks.com/terms/ (not app subscription terms)

## Completed

- Original visual storytelling, images and animations preserved; bilingual support and privacy layouts reuse existing site styles.
- Beta remains default, with original TestFlight invitation, installation instructions and FAQ.
- Static release renderer switches landing CTA, installation section, homepage status and website terms together; works without browser JavaScript.
- Release requires an HTTPS apps.apple.com app URL and explicit manual verification flag. No public placeholder URL.
- Support, app privacy and contact links added to product footer and lower page; support mailto uses owner-confirmed hello@jevaiworks.com.
- Support FAQ includes only operations supported by existing screenshots. No invented subscription, sync, account or rarity rules.
- App policy has 14 bilingual review sections, visible draft status and noindex; intentionally excluded from sitemap until approved.
- Website legal pages remain separate. Website privacy links to the app draft.
- Product metadata improved; new page titles, descriptions, canonicals and Open Graph metadata supplied; support added to sitemap.
- Contact renderer corrected to update existing anchors without nesting links.

## Requires owner / iOS developer confirmation

The supplied app source has now been audited read-only. See READINESS-REVIEW.md for current findings, including Umeng telemetry, no accounts, release-candidate Plus validation, and in-app draft legal documents. The historical questions below must be interpreted against that audit; do not request already-confirmed source/account/address facts again.

- Confirm advertised focus, ambience, fishing and collections against release candidate. Confirm message-in-a-bottle reading versus sharing, maps and Plus. Existing discovery screenshot retained; no sharing promise added.
- Confirm early-ending behavior, focus history UI, collection navigation, rarity and locked sound behavior before adding those FAQ answers.
- Registered address has now been checked against the local business licence and added to support/privacy. Confirm it remains current and suitable for correspondence. Owner has chosen not to publish a phone number; do not add one. Postal code 266500 is confirmed. Verify support mailbox can send and receive.
- Owner confirms Plus for 1.0; verify the subscription implementation. If so, provide benefits, restoration steps, renewal/cancellation terms, prices/durations as appropriate and app terms/EULA URL. No app terms invented.
- General Apple subscription-management guidance and the Apple management link have been added with conditional wording. App-specific Plus benefits, restoration and troubleshooting still require implementation evidence.

## Privacy verification questions / current blockers

The privacy page is a review scaffold, not a finalized statement of processing. Do not submit it or deploy this draft as a production policy. Obtain answers and product-owner approval before submission:

1. Can people use the app without registration? What account identifiers/authentication providers are used?
2. Where are focus history, fish/collections and settings stored? Which sync, backup and device-restoration mechanisms actually operate?
3. Are notes, to-dos, profile images or user-generated bottle messages stored/uploaded? What permissions apply?
4. Which analytics, crash, attribution and other SDKs are bundled? Supply dependency list, privacy manifests and server integrations.
5. Are device identifiers, IPs, usage events or diagnostics processed, by whom, for what purpose and under what basis?
6. Which purchase/subscription SDKs and receipt/transaction validation services are used? What transaction data reaches servers?
7. Who receives data, in which countries/server regions? What international-transfer safeguards apply?
8. Which security controls are implemented? What are retention periods for primary data, logs and backups?
9. How can users access, correct, export and delete data or withdraw consent? What is the actual response process?
10. If accounts can be created, is account deletion initiated inside the iOS app? Verify on a device. Missing functionality is a submission blocker; email support alone is not a substitute.
11. What ages are intended? What child-data rules and age controls apply?
12. Confirm legal controller/contact details, effective date and update notices; reconcile the final policy with App Store Connect privacy disclosures and app behavior.

After approval replace every draft section with verified policy content, set a real effective date, remove the draft notice and noindex, and add the app privacy URL to sitemap. Ensure the policy is also linked inside the iOS app. Verify public HTTPS access without login after an explicitly approved deployment.

Apple references: https://developer.apple.com/app-store/review/guidelines/ (1.5, 5.1.1) and https://developer.apple.com/app-store/marketing/guidelines/ . Release CTA currently uses plain bilingual text; add unmodified official Apple badge artwork once available, preserving required size and clear space.

## Release day instructions

1. Manually open the real public App Store listing and confirm app identity, seller, regions and availability. A syntactically valid URL is not verification.
2. After explicit release approval, edit `site.config.js`: set `APP_RELEASE_STATUS: 'released'`, fill `APP_STORE_URL` with that actual listing and set `APP_STORE_URL_VERIFIED: true`.
3. Run from repository root:

```powershell
node tools/release.mjs
node tools/check.mjs
node tools/release.test.mjs
```

4. Review generated `index.html`, `little-elsewhere/index.html`, `terms/index.html`. Edit their source templates under `tools/templates/` for future content changes, then regenerate. Other pages are edited directly. Commit configuration, templates and generated HTML together.
5. Preview using `node tools/preview.mjs`. Verify desktop/mobile, download destination and policy/support/contact. Publish through the existing GitHub Pages workflow only with explicit approval; check public HTTPS routes and redirects afterward.
6. To return to beta, set status to `beta`, clear URL and verification flag, regenerate and review before deployment.

## Verification commands

Verification performed: seven pages and 164 local references passed; beta/released renderer and URL guards passed; `script.js` and `product.js` syntax checks passed. Browser checks covered 390px and 1280px product/support layouts, native FAQ expansion, privacy draft labels, zero nested contact links after reload and no captured console errors. Public deployment/HTTPS, mailbox delivery and actual iOS behavior remain unverified. The empty image inside the closed screenshot-preview dialog is intentional, populated when opening a screenshot.

Files created: `little-elsewhere/support/index.html`, `little-elsewhere/privacy/index.html`, `little-elsewhere/help.css`, `tools/release.mjs`, `tools/release.test.mjs`, `tools/templates/home.html`, `tools/templates/product.html`, `tools/templates/terms.html`, `LAUNCH.md`.

Files modified: `little-elsewhere/index.html`, `little-elsewhere/product.css`, `site.config.js`, `script.js`, `terms/index.html`, `privacy/index.html`, `sitemap.xml`, `tools/check.mjs`, `README.md`. Homepage generated output stays unchanged in beta; its release variant is in the template.

`node tools/check.mjs` checks all seven pages for local links/assets/fragments, one h1 and company identity. `node tools/release.test.mjs` exercises both states and invalid/unverified URLs without changing public files or the release flag. This static project has no package build, lint or type-check pipeline. Browser QA and any remaining limits are reported in the delivery message.
