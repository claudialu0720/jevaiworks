# Privacy Policy (V3.2 · Draft aligned to source-code review)

**Little Elsewhere (别境)**  
**Operator:** 界外造物创意科技（青岛）有限公司 (Jevai Works Creative Technology (Qingdao) Co., Ltd.; trading as Jevai Works)  
**Effective date:** [Insert publication date]  
**Contact:** hello@jevaiworks.com

Little Elsewhere is a focus app that turns quiet moments of concentration into a fishing experience. We have designed it to work without an account and to keep your personal progress on your device. This policy explains what stays on your device, what limited information may be sent to service providers with your permission, and the choices you have.

## 1. Who we are

Little Elsewhere is operated by **界外造物创意科技（青岛）有限公司** (English name: Jevai Works Creative Technology (Qingdao) Co., Ltd.), trading as **Jevai Works** ("we," "us," or "our").

**Registered address:** 山东省青岛市黄岛区滨海大道路2059号内4栋办公1519户, China (postal code 266500)  
**Privacy contact:** hello@jevaiworks.com

## 2. How the app chooses regional analytics services

At launch, the app **first attempts to read your App Store Storefront country or region** to select the analytics and crash-reporting services. If that lookup fails or times out, it falls back, in order, to the last successfully resolved region, your device region, and finally the app language. The chosen language is therefore not normally the deciding factor, but may be used as a last resort. Only one regional set is enabled in a given launch.

| Region determined by the app | Analytics | Crash diagnostics | Configured hosting region |
| --- | --- | --- | --- |
| Mainland China | Umeng+ U-App | Umeng+ U-APM, including the Woodpecker / Yueying SDK | Mainland China Umeng route; Woodpecker storage location to be confirmed |
| Other regions | PostHog | Sentry | European Union (Germany) |

If the app determines that the regional service group has changed, it asks for permission again before enabling the new group. **This technical routing decision does not determine your physical location or which data protection laws apply.** For example, a person using the app in mainland China with an overseas App Store account, or whose device takes an overseas fallback route, may be assigned to PostHog and Sentry services hosted in the EU. Where such processing requires additional notice, consent, or other safeguards for cross-border data transfers, we will meet those requirements before the affected processing begins.

## 3. Information kept on your device

The app stores the following information locally so that its features work:

- Your detailed focus history, session goals, and saved progress;
- Inspiration notes, to-do items, and message bottles;
- Fish and other catches, your Collection, Pond, and badges;
- BUBS (the app's virtual currency) and maps unlocked with BUBS;
- Your display name, preferences, and settings.

We do not upload these complete local records to our own servers. **With your permission, certain limited events about focus sessions, catches, and other app interactions are sent to analytics providers**, as explained in Section 4. The content of your notes, to-dos, and message bottles is not included in those events.

If you use **Export a backup**, the resulting readable copy is saved wherever you choose. **The current public App Store build cannot import that file to restore your progress.** Your device's operating-system backup service (such as an iCloud device backup or a computer backup) may retain a copy of local app data. **Little Elsewhere does not currently provide its own in-app iCloud backup or cross-device cloud sync service.** Deleting the app or using **Delete my data** removes data from the app's local storage, but may not remove existing device backups or analytics records previously sent to providers. How **Delete my data** handles the analytics ID depends on whether optional data sharing is enabled, as explained in Section 9.

## 4. Optional analytics and crash information

**Optional analytics and crash-reporting services remain inactive unless you select “Agree & Continue” on the initial privacy screen or enable “Help improve Little Elsewhere” in Settings > Data & privacy.** Alternatively, you can choose **“Basic features only.”** The same switch controls both service types. Declining or withdrawing consent does not prevent use of the core features.

If you opt in, the relevant analytics and diagnostic services may process the following information. The specific fields and event types may vary by provider and app version:

| Category | Information | Purpose |
| --- | --- | --- |
| Device and app details | Device model, operating-system version, app version and build, language, time zone, and screen size; in mainland China, carrier and network type | Compatibility, usage statistics, and crash investigation |
| Analytics identifiers | A random analytics ID (UUID) created on the device after consent and used with Umeng, PostHog, and Sentry; PostHog may also use its SDK-generated initial anonymous and session IDs; mainland China reports may contain IDFV and Umeng device identifier (UMID) | Linking usage and diagnostic reports and supporting privacy requests |
| Feature-use events | Onboarding; focus session starts, completions, and early exits; planned and actual focus duration (which may include integer seconds), and times the app was left; catalogue entry IDs and rarity for catches kept or released; Pond, Collection, and Map use; map unlocks, sharing, failed saves; BUBS earned or spent (some events include exact amounts); and pageview or duration events for main screens. Events may also include the scene, app language, and version | Understanding feature usage and improving the experience |
| App lifecycle | App launches, backgrounding, installs, and updates | Understanding overall use and performance |
| Crash and error diagnostics | Technical errors, stack traces, app and device information, and scene in use. Mainland China Umeng U-APM sample reports have also included IP addresses and city-level location inferred from IP. We aim to exclude private note content | Diagnosing and fixing errors |

We do not request your precise GPS location for analytics or use a valid advertising identifier (IDFA) for advertising tracking. We do not request access to your contacts, photos, or microphone for analytics. We do not read your clipboard; the app writes to it only when you choose **Copy**. If you choose to receive focus-completion reminders, the app may request notification permission; denying it does not prevent use of the core timer. 

**Mainland China Umeng U-APM sample reports have included IP addresses and city-level location inferred from IP.** The related Woodpecker / Yueying service may also handle network type and connection status. Outside mainland China, our PostHog client uses `disableGeoip: true`, and our Sentry client disables default personal information and filters some IP fields in its JavaScript reporting path. **Providers may still encounter IP data through network connections or native crash processing, and the actual production server-side retention and scrubbing settings remain to be confirmed.** We do not use precise GPS tracking.

Analytics identifiers and device identifiers are not your name or email address, but may still be considered personal information under applicable law. We do not describe identifiable or pseudonymised records as fully anonymous.

## 5. Purchases and Plus entitlements

Purchases of monthly, annual, or Lifetime Plus are processed by Apple through the App Store. We do not receive your payment-card number or payment password. To recognise and restore purchases, the app uses Apple StoreKit to access product IDs, subscription and purchase status, expiry and grace periods, renewal, trial and revocation status, and the App Store Storefront country code. Its local Plus cache holds the plan, expiry, renewal and trial flags, and verification time. **The app does not ask for or directly read your Apple Account email or password, and its current implementation does not store transaction IDs in the Plus status cache or intentionally send them as analytics events.**

Apple's processing is explained in [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).

## 6. Service providers

We use the following services for the purposes described in this policy, subject to your optional analytics choice where applicable:

| Service | Provider | Role | Privacy information |
| --- | --- | --- | --- |
| Umeng+ U-App and U-APM (mainland China) | Umeng-related entities; public materials name Umeng Tongxin (Beijing) Technology Co., Ltd. and Beijing Ruixun Lingtong Technology Co., Ltd.; the specific contracting entity remains to be checked | Analytics and app performance diagnostics | [Umeng+ privacy policy](https://www.umeng.com/page/tube/privacypolicy) |
| Woodpecker / Yueying SDK, included with U-APM (mainland China) | Guangzhou Dongjing Computer Technology Co., Ltd. (广州市动景计算机科技有限公司) | Crash diagnostics | [Yueying SDK privacy policy](https://yueying-docs.effirst.com/privacy.html) |
| PostHog (outside mainland China) | PostHog Inc. | Product analytics | [PostHog privacy policy](https://posthog.com/privacy) |
| Sentry (outside mainland China) | Functional Software, Inc. | Error and crash diagnostics | [Sentry privacy policy](https://sentry.io/privacy/) |
| Apple App Store | Apple | In-app purchases and purchase verification | [Apple privacy policy](https://www.apple.com/legal/privacy/) |

We do not use advertising SDKs, display third-party advertisements, sell personal information, or track you across other companies' apps and websites for advertising.

## 7. Why we process information

We use local information to provide the app's features and verify Plus entitlements. If you consent to optional analytics and diagnostics, we use the information described in Section 4 to understand usage and improve reliability. You can withdraw that consent at any time in **Settings > Data & privacy**; this stops future optional collection but does not automatically erase information already processed.

Where the GDPR or UK GDPR applies, the legal basis may be performance of our agreement with you for core functionality and purchase access, consent for optional analytics and diagnostics, or another basis permitted by law for necessary security and legal obligations. Accepting this policy alone is not treated as consent to optional analytics.

## 8. Storage, transfers, and retention

Your detailed saved progress and notes stay on your device unless you export or back them up yourself. The mainland China route uses Umeng services; the specific storage location of the Woodpecker / Yueying SDK remains to be confirmed. PostHog uses its EU Cloud region and Sentry is configured for a Germany-based ingestion endpoint. The production projects’ actual hosting and access arrangements still need confirmation. Where data is accessed from another country, we will apply the protections required by applicable law. **A device physically in mainland China may be routed to the overseas services and transmit optional data to the EU, depending on its App Store and fallback settings.** We will assess the applicable requirements for notification, separate consent where required, and lawful cross-border transfers based on the actual data flow, not on App Store region alone.

We retain information only as long as needed for the purposes described above, subject to applicable legal obligations. **Before publication, we will confirm and disclose the configured retention periods for Umeng+, PostHog, and Sentry.** Until those periods are confirmed, the following must be completed:

- Umeng+ analytics and diagnostics: **[Confirm retention period]**
- PostHog analytics: **[Confirm retention period]**
- Sentry diagnostics: **[Confirm retention period]**

Local data remains on your device until you delete it, uninstall the app, or it is otherwise removed by your device or operating system. Copies in device backups may remain until removed through the relevant backup service.

## 9. Your choices and rights

You can use the app without an account and without agreeing to optional analytics.

| Choice or right | How to exercise it |
| --- | --- |
| View your saved progress | Use the relevant screens in Little Elsewhere |
| Obtain a copy of local information | Use **Export a backup** in Settings > Data & privacy |
| Correct your display name or settings | Change them in the app |
| Stop optional analytics and diagnostics | Turn off **Help improve Little Elsewhere** in Settings > Data & privacy |
| Delete local app data | Use **Delete my data** in Settings > Data & privacy |
| Ask about information held by service providers | Contact **hello@jevaiworks.com** |

Depending on where you live, you may also have rights to access, correct, delete, restrict, object to processing of, or obtain a copy of personal information, and to complain to a data-protection authority. We will review requests and respond as required by applicable law. The first eight characters of your analytics ID are displayed in Settings > Data & privacy; using **Copy** provides the full ID for a privacy request. **If the full analytics ID is still available, you may provide it to help us locate records. It is useful to copy it before clearing local data, but it is not a condition for making a request. If the ID has already changed, been deleted, or cannot be found, you can still contact us.** With **Delete my data**, the app immediately creates a new analytics ID if sharing remains on; otherwise it clears the old ID and creates another only if you later opt in. **Turning sharing off by itself does not reset the existing ID.**

PostHog provides a server-side process to delete users and associated events; the operational steps for our production project, and the deletion scope of Umeng and Sentry, still need verification. We will review requests and, where legally required and technically possible, search for and handle relevant data. If the available information is not sufficient to locate records, we will explain the limitation, any available next steps, and applicable rights or remedies. We will not refuse to consider a request solely because the full analytics ID is unavailable. Pressing **Delete my data** does **not** erase analytics already sent to providers.

There is currently no Little Elsewhere account to close. We do not offer account registration.

## 10. Children

Little Elsewhere is not designed specifically for children. If you are younger than the age at which your local law requires parent or guardian consent, please use the app with their guidance and choose **Basic features only** unless the required permission has been obtained. In mainland China, processing personal information of children under 14 generally requires consent from a parent or other guardian and specific rules for handling such information. If we learn that information was collected without legally required permission, we will take appropriate steps in accordance with applicable law. An app-store age rating does not replace these requirements.

## 11. Security

We use encrypted connections when communicating with the service providers described above and aim to limit the information transmitted. Your local records are also protected by your device's own security settings. No method of storing or transmitting information can guarantee absolute security. If a data security incident requires action or notice under applicable law, we will take appropriate remedial steps and provide legally required notifications or reports.

## 12. Changes to this policy

We may update this policy as the app changes. We will update its effective date and provide notice when required. If a change requires new consent, we will ask before beginning that processing.

## 13. Contact us

For questions or privacy requests, contact **hello@jevaiworks.com** or write to **界外造物创意科技（青岛）有限公司** at **山东省青岛市黄岛区滨海大道路2059号内4栋办公1519户, China (postal code 266500)**.
