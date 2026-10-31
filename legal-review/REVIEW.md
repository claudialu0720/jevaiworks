# Legal integration review / 法律草稿整合说明

Review date: 2026-10-31. Both documents are **approval drafts**, not final published policies. The September documents are editorial references, not implementation evidence. No app functionality or in-app text was changed; no deployment or Released switch occurred.

## Deliverables and source

- [Privacy draft](privacy.md): eight original sections, expanded with source-backed detail and explicit unresolved facts; bilingual throughout.
- [Supplementary terms draft](terms.md): ten original sections, with Plus/Apple billing rules; not a replacement EULA.
- Website previews: `/little-elsewhere/privacy/` and `/little-elsewhere/terms/`, both visibly draft and noindex. Editable Markdown is the content source. Run `node tools/legal-drafts.mjs` after editing, then website checks. Do not manually finalize through this generator.
- Latest remote `main` checked again on 2026-10-31: **7137ae8946733b1c17c2b1e58933ac00ccef4618**, unchanged since the previous latest-source audit. Read through an isolated ignored bare snapshot, without modifying the developer checkout. Source/model audit permission remains applicable.
- Code evidence is commit-specific: `apps/mobile/src/subscription/{products,purchases,PlusProvider,plus-policy,plus-status}.ts[x]`, `screens/{PlusScreen,DataScreen,useBackupActions}.tsx/ts`, `platform/{backups,privacy-preferences}.ts`, `privacy/policy-text.ts`, `telemetry/*`, `modules/umeng/ios/{UmengBridge.m,LittleElsewhereUmeng.podspec}` and `docs/active/{SUBSCRIPTIONS,CHINA-TELEMETRY}.md`. Source is not device-test evidence.

## Clause comparison / 条款对照

| Original clause / 原条款 | Treatment / 处理 | Reason and basis / 原因与依据 |
| --- | --- | --- |
| Privacy introduction: simple, transparent, necessary information | Preserved / 保留 | Retained welcome/voice; added verified operator and draft/evidence scope. Avoided claiming every current SDK field has proven necessity. |
| “如果你创建或登录账号…” | Modified / 修改 | Current audited source has no customer accounts; online identity/cloud decisions remain pending. Analytics `signIn` is install-ID grouping, not customer login. |
| Focus, fish, Pond, collection/settings | Preserved + expanded / 扩展 | Local storage/runtime and DataScreen; added goals, notes/to-dos and distinction between Free storage and unverified Plus cloud plan. |
| Save/sync progress as existing use | Modified / 修改 | Latest SUBSCRIPTIONS.md still treats cloud/sync as later. Owner plan confirmed, not RC data flow verified. No blanket on-device-only statement. |
| User-created personal content not public by default | Preserved with scope / 限定保留 | Current local implementation does not publish typed notes. Public bottle text distribution must be separately verified. |
| “匿名的功能使用信息” | Removed/replaced / 替换 | Random ID, IDFV, UMID, IP/city and report grouping make “fully anonymous” misleading. Telemetry/native adapter and integration records support pseudonymous wording. |
| Device/crash information | Expanded / 扩展 | Listed events/attributes, device IDs, network/IP and sanitized errors; SDK podspec and app privacy manifest. Final binary/SDK fields still pending. |
| Uses: restoring account/purchases, preventing fraud | Modified / 修改 | Purchases/restore exist through StoreKit; customer-account restoration and blanket anti-fraud data collection not established. No speculative collection purpose retained. |
| “不为无关目的出售” | Removed as a finalized assurance / 不作为定稿保证 | No sale mechanism found does not prove all business/vendor practice. Final sharing/sale policy needs owner/provider confirmation; no implied permission to sell for related purposes. |
| Notes/bottles public by deliberate choice; avoid sensitive text | Preserved conditionally / 条件保留 | Maintained gentle warning and user choice; no invented public sending, moderation, deletion or visibility controls. Apple guideline 1.2 relevant if UGC launches. |
| Delete my data = delete account and associated data | Corrected / 纠正 | Runtime reset + privacy preference helpers reset local experience/ID and retain consent; no server diagnostic deletion. Account/CloudKit deletion must be independently verified. |
| Retain only necessary time; exceptions | Modified / 修改 | No invented duration. Specific categories/provider cleanup remain pending. PIPL Article 47 constrains deletion exceptions; a technical/legal limit is not indefinite unrestricted use. |
| Generic third-party login/cloud/analytics/IAP/push list | Replaced / 替换 | Named verified Umeng components, Apple/expo-iap and local OS functions. Local notifications are not proof of remote push; no invented login/cloud provider. |
| Opt-in/withdrawal (absent in original) | Added / 新增 | Privacy preferences and native bridge; disclosed unresolved capture remaining armed mid-process and possible later cached uploads. Current in-app “immediate complete stop” promise conflicts. |
| Storage regions/security (not specified) | Added with pending facts / 新增待确认 | Do not infer China-only/no-transfer or encryption from project intent. Vendor/location/retention/security verification needed. |
| Children: not intentional collection, delete if discovered | Modified / 修改 | Kept concern for children but no fictional compliance guarantee. PIPL Arts 28/31 and child-network rules require actual protections/guardian consent where applicable; no verified mechanism. 4+ is not minimum user age. |
| Policy update and email | Preserved / 保留 | Kept material-change notices; code has policy-version mechanism. Added confirmed company/address/postcode. No telephone as owner requested. |
| September update and October 10 effective dates | Removed / 移除 | Neither is automatically applicable. Draft preparation date clearly distinguished; final dates require owner approval. |
| Terms introduction and what the app is | Preserved / 保留 | Gentle focus/relaxation/collectibles description and no medical-service positioning. Removed implication that an unapproved draft is binding. |
| Accounts, abuse and account termination | Modified / 修改 | Account conditionality made explicit; proportionate enforcement and paid-rights protection replace blanket termination discretion. |
| Virtual fish, gear and currency | Modified / 修改 | Retained no cash/investment claim. Avoided suggesting an implemented currency/trading system. Removed blanket “not guaranteed permanent” excuse for paid benefits. |
| User ownership; necessary storage/display/transmission permission | Preserved with conditions / 条件保留 | Narrow functional permission, no ownership transfer; no claim moderation/report/block tools exist. Prohibited-content rules retain original structure. |
| “未来可能提供 Premium” | Replaced / 替换 | Plus monthly/annual auto-renewable and non-consumable lifetime exist in main. Added storefront pricing, offer eligibility, renewal/cancellation, restore, expiry/cache/refund distinctions. No hardcoded promotional amounts or invented intro duration. |
| Apple/Google/other platform billing | Narrowed / 收窄 | iOS 1.0 review uses Apple billing. Did not announce unlaunched platforms. Refund decision follows Apple/applicable law. |
| Intellectual property | Preserved + EULA alignment / 调整 | Original creative-work list retained in concise form; no conflicting custom software licence or blanket prohibition overriding law. |
| Service change and responsibility | Modified / 修改 | Retained honest stability limits and support tone; no arbitrary removal of paid rights or exclusion of mandatory consumer remedies. Apple Standard EULA/must-follow law remain controlling. |
| Agreement updates/contact | Preserved / 保留 | No unapproved venue, governing-law replacement or Chinese-authoritative clause. Verified operator/address/email; separate privacy policy. |
| App licensing structure | Added / 新增 | Owner now confirms Apple Standard EULA. Latest PlusScreen already links it; supplemental terms cover service-specific rules. Do not submit this document as a custom EULA replacing Apple's. |

## Outstanding facts and decisions / 尚待确认

1. **RC identity and entitlement scope:** final TestFlight build/commit; resolve 1/4 BGM, daily session-count semantics, notes-vs-list limits, cloud/sync, special collectibles, customization, detailed insights and bottle sharing against the newest matrix. Do not sell unverified benefits.
2. **Store configuration:** confirm source IDs in App Store Connect, group, durations, lifetime type, regions/family sharing, real storefront prices, paid introductory-offer mode/duration/eligibility and subsequent renewal amounts. Code's old annual free-week assumption must not silently survive the new pricing decisions. Need sandbox eligible/ineligible, pending, restore/second device, lifetime, expiry, cancellation/grace, refund and revocation results.
3. **Umeng:** current contract entity and full final SDK inventory; automatic fields, raw-data/aggregates retention, console access, processing regions/transfers, ID deletion capability, historical-ID lookup and reply/cleanup timelines. Verify capture/queued reports on/off/relaunch/re-enable with device/network evidence. Resolve policy/UI contradiction before approval; prose alone is not the fix.
4. **Cloud/accounts and UGC:** actual providers, login/identifiers, uploaded fields, audience/identity model, retention, encryption/access controls, server/backup deletion, export and moderation/report/block flows. If accounts are created, demonstrate in-app deletion initiation; email alone is not a substitute. No assumed guardian gate or CloudKit implementation.
5. **Support and security:** email processor/locations/retention, verified mailbox operation, security/incident-response procedures. No bank/contact record or private phone will be published.
6. **Minors:** decide legal minimum age and permitted minor use, including telemetry/cloud/public sharing/purchases. Mainland-China under-14 data protection needs legal/product evaluation and real measures. Choose and verify any age/guardian-consent route; don't claim that declining telemetry alone implements all safeguards. Review actual rating answers, UGC/messaging and storefront requirements separately from the 4+ target.
7. **Owner/legal approval:** final bilingual language, remedy/refund wording, future-world scope, EULA relationship, effective/update dates and whether either language has precedence. No venue or jurisdiction invented. Legal review should resolve all editorial pending notes before public submission.

## Final publication checklist / 发布清单

- [ ] Resolve every pending fact in both Markdown sources; review original comparison and confirm the RC matches. Keep noindex/draft until approval.
- [ ] Approve exact text, final update date and effective date. Remove draft/editorial review notes only after approval; no automatic use of the September/October dates.
- [ ] In-app Privacy Policy: update `src/privacy/policy-text.ts` privacy, personal-information and SDK lists from approved facts. Match consent/withdrawal, deletion behavior and App Store privacy answers; assess version bump/reconsent for material changes. **Not edited in this task.**
- [ ] In-app Terms: make approved supplementary terms accessible from Settings → Data & privacy and paywall as applicable; keep the Standard EULA separately identifiable. Replace outdated in-app agreement placeholders. **Not edited in this task.**
- [ ] Apple Standard EULA: verify App Store Connect selection and the existing `PlusScreen.tsx::TERMS_OF_USE_URL`; do not upload supplementary rules as a conflicting custom EULA.
- [ ] Paywall: provide accessible Privacy, Supplementary Terms and Standard EULA links as appropriate; current source has only Standard EULA + in-app Privacy in purchase view. Check Plus-user view/settings routes too. Test links, both languages, screen-reader labels, prices/currency/periods, eligibility, renewal amount and cancellation disclosure.
- [ ] Website: approve `/little-elsewhere/privacy/` and `/little-elsewhere/terms/`; regenerate from Markdown. Then remove draft notice/noindex deliberately, set approved dates and add both final legal URLs to sitemap. Keep `/privacy/` and `/terms/` company documents separate. Check header/footer/support links and mobile/no-JS reading. Don't remove generator's draft protection without an intentional approved finalization change.
- [ ] App Store Connect: enter correct Support/Privacy URLs; ensure privacy labels reflect final SDK/purchase/cloud/UGC processing; attach purchase metadata/review screenshots, group/product IDs/types, offers and localized prices. Add supplementary terms link in appropriate metadata and retain Standard EULA. Do not claim configuration already saved.
- [ ] Rating/minors: complete current questionnaire from actual functionality, not desired 4+; review under-14 safeguards and UGC moderation. No Kids Category selected as intended.
- [ ] Device sign-off: purchase/restore/expiry/refund, ID/cache behavior, cloud/account deletion, consent-off/native-crash tests and final binary manifests. Draft text is not evidence of passing tests.
- [ ] Deployment and public Released mode require separate approval. Real App Store URL remains empty until a verified listing exists. Nothing in legal approval alone authorizes publishing.

## Legal/reference basis

- [Apple Standard EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/): retained as software licence; supplementary rules do not replace it.
- [Apple subscription cancellation](https://support.apple.com/en-us/118428) and [Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): purchase transparency, UGC, privacy and account-deletion checks.
- [PIPL, official CAC text](https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm): Arts 28/31 concern under-14 sensitive data, guardian consent and special rules; Art 47 concerns deletion and constrained retention exceptions.
- [Children's Personal Information Network Protection Provisions, CAC](https://www.cac.gov.cn/2019-08/23/c_1124913903.htm): dedicated child-data rules and protection responsibilities. These requirements do not establish that this app has implemented safeguards.

This review is an approval package grounded in available source and decisions, not a representation that all legal/product requirements have been met.

Verification: generated both drafts; 8 pages/190 internal references passed the site checker; Beta/Released guard tests passed; 28 route/state/script-policy cases passed with scripts permitted or blocked. The terms page was also opened with scripts blocked: draft banner, EULA links and one h1 verified; no horizontal overflow observed. No iOS device or App Store Connect configuration was changed or tested.
