> Legal editorial integration: see legal-review/REVIEW.md for the September-clause comparison, unresolved facts and approval/publication checklist. Bilingual approval sources are legal-review/privacy.md and legal-review/terms.md, rendered to the separate App privacy and supplementary terms pages. Owner confirms Apple Standard EULA as the licence; supplementary rules do not replace it. Both pages stay draft/noindex and no dates are finalized. App text/functionality unchanged.

# Little Elsewhere iOS 1.0 — submission readiness

Updated 2026-10-31. Supersedes all earlier claims that Plus is unimplemented. Owner confirms Plus implemented, Paywall UI being finalized, latest developer work on main. No production deployment, pricing change, final privacy publication or Released activation is authorized or performed.

## Evidence scope

- Earlier local checkout: d106141 (stale). Latest remote main inspected read-only: **7137ae8946733b1c17c2b1e58933ac00ccef4618**. update-ui 53be647 is UI work, not the Plus evidence source.
- Used an isolated bare source snapshot under ignored `.preview/readiness-source.git`; did not switch, merge, reset or edit the developer's working tree. Model exception for the read-only audit remains owner-authorized.
- No identified final TestFlight release candidate or physical iOS device session supplied. App Store Connect has no final configuration (owner confirmed). Source implementation is not proof of completed build testing.

## 1. Confirmed complete in the latest build

**None independently confirmed in a release build.** No final build supplied; do not relabel source findings as device results. Website edits/checks are complete locally: bilingual Free/Plus plan, purchase-type guidance, source-backed restore navigation, Apple subscription link and Apple standard EULA link. Design/CSS unchanged in this pass. Beta/default, empty store URL, privacy draft/noindex remain.

## 2. Implemented but requires testing

Latest main confirms `expo-iap` **6.3.0**, StoreKit 2 purchase adapter, current-entitlement queries, transaction completion/update handling, restore, system subscription management, cached status, expiry and lapsed fallbacks. Lifetime takes precedence over subscriptions, has no expiry and is removed when revoked; offline lifetime is retained from cache. Subscriptions expire at their known end while offline; unknown expiry requires store verification. Verify refunds/revocation after reconnect, pending purchases, grace periods, relaunch, foreground refresh and second-device restoration.

Source-backed product IDs (not invented; **not confirmed in App Store Connect**):

| Plan | ID in subscription/products.ts | Intended type |
| --- | --- | --- |
| Monthly | com.jevaiworks.littleelsewhere.plus.monthly | Auto-renewable, 1 month |
| Annual | com.jevaiworks.littleelsewhere.plus.annual | Auto-renewable, 1 year |
| Lifetime | com.jevaiworks.littleelsewhere.plus.lifetime | Non-consumable |

`PlusScreen.tsx` links Restore purchases, Apple's standard EULA (`https://www.apple.com/legal/internet-services/itunes/dev/stdeula/`) and in-app Privacy Policy in the Free purchase view. Restore is also present for Plus users. Settings → Membership & subscription opens Plus. Prices use store `displayPrice`; trial eligibility uses Apple's subscription-group eligibility query. Renewal/lifetime notes exist. Test final Paywall layout, accessibility, both languages, actual URLs and complete price/renewal/cancellation disclosures. Confirm selected EULA in App Store Connect; local app policy/user agreement still require owner/legal approval and reconciliation.

## 3. Missing or blocked — submission priorities

1. **Reconcile latest product decisions with source, then test the RC.** Plus exists; the blocker is evidence/mismatch, not absence of Plus. Per-feature status follows below.
2. **App Store Connect purchase configuration unfinished.** Create/confirm actual IDs/types, shared monthly/annual group, levels, regions, localized storefront prices, offer mode/duration/eligibility. Local StoreKit group `21000001` is a test fixture, not a verified production group. Fixture prices ¥12/¥68/¥168 and annual free-week offer are superseded by the new owner decisions. Update the app/fixture configuration in the developer's work, not this website task. Do not show ineligible introductory pricing. Current adapter primarily models eligible annual free trials, not the new paid monthly/annual introductory discounts; add/verify offer price, periods and subsequent renewal price. Do not silently retain a 7-day free trial as an approved new decision.
3. **Umeng withdrawal remains unresolved in latest main.** `modules/umeng/ios/UmengBridge.m` still enables `crashAndBlockMonitorEnable`; `setCrashReportingEnabled` changes only a bridge Boolean. No evidence of a new native-capture shutdown. Native capture/cached upload behavior needs real-device consent-off/on, termination/relaunch, offline/reconnect and proxy testing. Reconcile implementation, in-app promise, website policy and App Store disclosures; do not promise all capture/transmission immediately stops.
4. **Privacy/account/cloud/UGC facts unresolved.** New Plus cloud backup/sync and bottle sharing mean earlier device-only/no-account conclusions do not establish 1.0 behavior. Need actual provider/region/schema/authentication, synced fields, security, retention, access/export/delete flows, analytics deletion by ID, response periods and SDK partner disclosures. If accounts exist, demonstrate in-app deletion initiation and backend/backup deletion. No physical-device/account-flow proof supplied.
5. **Public sharing and rating:** owner targets 4+, Productivity, not Kids Category/not specifically children. Current Apple questionnaire separately asks about UGC and messaging/chat; answer from real sharing behavior. Receiving bundled local bottle texts is different from sending user text to others. For real UGC verify filtering, reporting, blocking, timely moderation and published contact under guideline 1.2. Evaluate random/anonymous bottle interactions against Apple's anonymous-chat restriction. Analytics is not automatically advertising; disclose real device IDs/diagnostics and consent. 4+ is a content rating, not an approved privacy minimum age. No rating/submission answers changed here.
6. **Release controls:** real App Store listing not yet available; remains blank. This is a release-day download prerequisite, not proof support/privacy cannot be prepared for review. Sandbox tests, final build number, policy/terms approval and privacy disclosures are needed before submission.

## Feature-by-feature validation ledger

Every row is the newest owner-approved product decision. None is claimed verified in a final release candidate. Source findings below are based on main 7137ae8 and `docs/active/SUBSCRIPTIONS.md`, not the stale local checkout. Future-benefit promises require owner scope approval and truthful shipping availability.

| Feature | Free decision | Plus decision | Latest source / RC action |
| --- | --- | --- | --- |
| Focus | 3 sessions/day; 10/25/45 min | Unlimited; custom durations | Presets/custom gates implemented. Current daily counter counts catch-earning sessions, not every session; reconcile and device-test. |
| Maps | 1 free | All maps/future Plus worlds | Quiet Lake free; other bundled scene gates and future-map tile implemented. Verify bundled worlds/access and scope of future promise. |
| BGM | 1 track | All 4 current/future tracks | Code lists 2 free tracks, docs say 6 total. Reconcile to 1/4 and verify catalogue/gates. |
| Ambience | Weather-based, no manual adjustment | Full ambience/mixing | Weather/off vs manual gate implemented; verify UI and saved settings. |
| Noise | White | White/pink/brown | Gates/lapsed fallback implemented; audio/device test required. |
| Characters/outfits | Default | Exclusive options | Subscription doc lists customization as later work; verify actual implementation/assets on RC. |
| Boats/gear | Basic | Exclusive boats/rods/accessories | Same later-work discrepancy; verify RC before advertising availability. |
| Fish/collection | All standard | Additional Plus-map special fish | Source docs list special Plus fish as future; verify catalog and gates. |
| Treasures | Basic collectibles | Exclusive treasures/collectibles | Source docs list as later; RC evidence needed. |
| Pond | Up to 10 fish | Up to 20 fish | 10/20 limits implemented for animals; verify fish-specific count and downgrade preservation. |
| Decorations | No new Free promise specified | Exclusive collectible decorations | Source docs list exclusive decorations as later; RC evidence needed. |
| Achievements | Basic achievements/badges | No additional entitlement specified | Collection/badges described as free; validate basic achievements and avoid inventing a Plus benefit. |
| Inspiration | 3 notes and 3 to-do lists | 6 notes and 6 to-do lists | Code caps items in each Inspiration/To-do list at 3/6, not necessarily number of lists. Clarify list-vs-item model and test. |
| History | Last 7 days | Full history/detailed insights | 7-day/full gating implemented. Detailed insights listed as later; verify RC. |
| Drift bottles | Basic interactions | Extended sharing/customization | Receive/free confirmed in docs; sending/sharing listed as later. RC/network/moderation/rating evidence needed. |
| Storage | Local | Cloud backup/cross-device sync | Source doc step 6 (iCloud) not complete, cross-device sync listed later. Owner's new scope supersedes old plan; need actual RC implementation/provider evidence. |

## Confirmed pricing decisions — documentation only

These are owner decisions, not verified StoreKit prices or public offers. No pricing is hardcoded into the website. Intro duration/mode is not yet specified; obtain it before configuring offers. International values are USD targets; actual storefront currency/prices come from StoreKit.

| Plan | Mainland China intro / regular | International USD intro / regular | Type |
| --- | --- | --- | --- |
| Monthly | ¥8 / ¥10 | $2.99 / $3.99 | Auto-renewable |
| Annual | ¥58 / ¥78 | $19.99 / $24.99 | Auto-renewable |
| Lifetime | ¥148 | $37.99 | Non-consumable |

## 4. Requires owner approval

- Final privacy processing facts, retention/deletion procedures, privacy minimum age (distinct from 4+), effective date and bilingual text; then remove draft/noindex and add policy to sitemap only after explicit approval.
- Introductory-offer duration/mode, selected EULA/custom terms and any future-world benefits. Preserve the confirmed pricing amounts; do not add an unapproved free trial. Verify App Store Connect configuration rather than assuming IDs/group/offer data already exist.
- Drift-bottle distribution/moderation model and actual age-questionnaire answers. 4+ remains a target until assessed against the RC.
- Final public release switch and deployment remain separately unapproved. Phone remains omitted as requested; verified address/postcode and email stay visible.

## Evidence needed from developer

Final TestFlight RC build/commit; App Store Connect products/group/offer export/screenshots without credentials; two eligible/ineligible Apple sandbox accounts and purchase/restore/lifetime/expiry/refund results; updated feature ledger per row; cloud/auth/deletion architecture; consent-off/on crash/network traces and release binary manifests; final policy/terms and age-rating questionnaire review.

## Apple references checked

- [Age questionnaire definitions](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions): UGC and messaging/chat assessed independently; regional rating outcomes may differ.
- [Introductory offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions/): eligibility and offer terms must match the actual user/group/storefront.
- [Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): UGC 1.2, subscriptions 3.1.2, privacy/deletion 5.1.1.

Website verification: run `node tools/check.mjs`, `node tools/release.test.mjs`, `node tools/readiness.test.mjs` (local review server on 4174). Source review is read-only; no app build or device test was performed on this Windows website task.
