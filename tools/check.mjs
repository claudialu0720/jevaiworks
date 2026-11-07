// Smoke-check local routes, asset files and fragment links without dependencies.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const pages = ['index.html','little-elsewhere/index.html','privacy/index.html','terms/index.html','404.html','support/index.html','little-elsewhere/en/index.html','little-elsewhere/privacy/index.html','little-elsewhere/terms/index.html','little-elsewhere/en/privacy/index.html','little-elsewhere/en/terms/index.html','little-elsewhere/support/index.html','little-elsewhere/en/support/index.html'];
const errors = [];
let references = 0;
for (const page of pages) {
  const source = fs.readFileSync(path.join(root,page),'utf8');
  if ((source.match(/<h1[\s>]/g)||[]).length !== 1) errors.push(`${page}: expected one h1`);
  const companyName = page === 'little-elsewhere/en/index.html' ? '© 2026 Jevai Works' : '界外造物创意科技（青岛）有限公司';
  if (page !== 'support/index.html' && !source.includes(companyName)) errors.push(`${page}: missing company name`);
  for (const match of source.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const ref = match[1];
    if (/^(https?:|mailto:|data:)/.test(ref)) continue;
    const [pathname,fragment] = ref.split('#');
    let target = pathname ? (pathname.startsWith('/') ? path.join(root,pathname) : path.resolve(root,path.dirname(page),pathname)) : path.join(root,page);
    if (fs.existsSync(target) && fs.statSync(target).isDirectory()) target = path.join(target,'index.html');
    references++;
    if (!fs.existsSync(target)) {errors.push(`${page}: missing ${ref}`);continue;}
    if (fragment && !fs.readFileSync(target,'utf8').includes(`id="${fragment}"`)) errors.push(`${page}: missing fragment ${ref}`);
  }
}
if (errors.length) {console.error(errors.join('\n'));process.exit(1);}
console.log(`PASS: ${pages.length} pages, ${references} local links/assets, headings and company identity.`);
