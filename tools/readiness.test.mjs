// Start node tools/readiness-preview.mjs first. No production files are written.
import assert from 'node:assert/strict';
import fs from 'node:fs';
const root = new URL('../',import.meta.url);
const paths = ['/','/support/','/little-elsewhere/','/little-elsewhere/support/','/little-elsewhere/privacy/','/privacy/','/terms/','/little-elsewhere/terms/'];
const original = fs.readFileSync(new URL('site.config.js',root),'utf8');
let count = 0;
for (const state of ['beta','released']) for (const nojs of [0,1]) for (const pathname of paths) {
  const response = await fetch('http://127.0.0.1:4174'+pathname+'?state='+state+'&nojs='+nojs);
  assert.equal(response.status,200);
  if (nojs) assert.equal(response.headers.get('content-security-policy'),"script-src 'none'");
  const html = await response.text();
  assert.doesNotMatch(html,/\{\{|https:\/\/apps.apple.com\/app\/id0/);
  if (state==='released') assert.doesNotMatch(html,/TestFlight|testflight.apple.com|iOS Beta|iOS beta/);
  if (pathname==='/little-elsewhere/') {
    if (state==='beta') {
      assert.match(html,/testflight.apple.com\/join\/Uk9rZz5B/);
      assert.doesNotMatch(html,/Download on the App Store/);
    } else {
      assert.match(html,/Download on the App Store/);
      assert.equal((html.match(/aria-disabled="true"/g)||[]).length,2);
      assert.doesNotMatch(html,/id="beta"|href="#beta"/);
    }
  }
  if (['/support/','/little-elsewhere/support/'].includes(pathname)) {
    assert.match(html,/mailto:hello@jevaiworks.com/);
    assert.match(html,/https:\/\/apps.apple.com\/account\/subscriptions\//);
    assert.match(html,/2059/);
  }
  if (['/little-elsewhere/privacy/','/little-elsewhere/terms/'].includes(pathname)) {
    assert.match(html,/name="robots" content="noindex"/);
    assert.match(html,/Draft for owner approval/);
  }
  count++;
}
assert.equal(fs.readFileSync(new URL('site.config.js',root),'utf8'),original);
console.log(`PASS: ${count} isolated route/state/script-policy combinations; actual App Store URL still required`);
