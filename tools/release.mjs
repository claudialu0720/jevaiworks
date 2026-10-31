// Generate static pages so the selected release state also works without JavaScript.
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export function render(source, config) {
  const released = config.APP_RELEASE_STATUS === 'released';
  if (!['beta', 'released'].includes(config.APP_RELEASE_STATUS)) throw Error('Invalid release status');
  let url = '';
  if (released) {
    try {
      const candidate = new URL(config.APP_STORE_URL);
      if (candidate.protocol !== 'https:' || candidate.hostname !== 'apps.apple.com' ||
          candidate.username || candidate.password || candidate.port ||
          !/\/id[0-9]+\/?$/.test(candidate.pathname) || config.APP_STORE_URL_VERIFIED !== true) throw Error();
      url = candidate.href;
    } catch { throw Error('Release requires a valid, owner-verified public apps.apple.com app URL'); }
  }
  return source.replace(/\{\{(BETA|RELEASE)\}\}([\s\S]*?)\{\{\/\1\}\}/g,
    (_, state, content) => (state === 'RELEASE') === released ? content : '')
    .replaceAll('{{APP_STORE_URL}}', url.replaceAll('&', '&amp;').replaceAll('"', '&quot;'));
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const context = { window: {} };
  vm.runInNewContext(fs.readFileSync(path.join(root, 'site.config.js'), 'utf8'), context);
  const pages = [['home','index.html'],['product','little-elsewhere/index.html'],['terms','terms/index.html']];
  // Validate every page before writing any output.
  const outputs = pages.map(([name, target]) => [target, render(fs.readFileSync(path.join(root, 'tools/templates', name+'.html'), 'utf8'), context.window.JEVAI_CONFIG)]);
  for (const [target, html] of outputs) fs.writeFileSync(path.join(root, target), html);
  console.log('Generated static pages: '+context.window.JEVAI_CONFIG.APP_RELEASE_STATUS);
}
