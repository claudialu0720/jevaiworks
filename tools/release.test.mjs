import assert from 'node:assert/strict';
import fs from 'node:fs';
import { render } from './release.mjs';
const source = fs.readFileSync(new URL('./templates/product.html', import.meta.url), 'utf8');
const beta = render(source, { APP_RELEASE_STATUS: 'beta' });
assert.match(beta, /id="beta"/);
assert.match(beta, /testflight.apple.com\/join/);
assert.doesNotMatch(beta, /Download on the App Store|\{\{/);
// Synthetic URL only in test memory; never written to public pages.
const valid = { APP_RELEASE_STATUS: 'released', APP_STORE_URL: 'https://apps.apple.com/app/id1234567890', APP_STORE_URL_VERIFIED: true };
const released = render(source, valid);
assert.match(released, /Download on the App Store/);
assert.match(released, /id="download"/);
assert.doesNotMatch(released, /TestFlight|testflight.apple.com|href="#beta"|iOS beta|\{\{/);
for (const url of ['', 'https://example.com/app/id123', 'javascript:alert(1)', 'https://apps.apple.com/account/subscriptions/']) {
  assert.throws(() => render(source, { ...valid, APP_STORE_URL: url }));
}
assert.throws(() => render(source, { ...valid, APP_STORE_URL_VERIFIED: false }));
assert.throws(() => render(source, { APP_RELEASE_STATUS: 'typo' }));
for (const name of ['home','terms']) {
  const template = fs.readFileSync(new URL('./templates/'+name+'.html', import.meta.url), 'utf8');
  assert.doesNotMatch(render(template, valid), /iOS Beta|in development|处于开发阶段|\{\{/);
}
console.log('PASS: beta/released static content and release URL guard');
