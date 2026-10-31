// Render approval drafts only. No finalization, date assignment or sitemap changes.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = p => fs.readFileSync(path.join(root,p),'utf8');
const escape = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const inline = s => escape(s).replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+|mailto:[^\s)]+)\)/g,'<a href="$2">$1</a>');
const old = read('little-elsewhere/privacy/index.html');
const prefix = old.slice(0, old.indexOf('<article class="legal'));
const suffix = old.slice(old.indexOf('</main>'));
for (const slug of ['privacy','terms']) {
  const blocks = read('legal-review/'+slug+'.md').trim().split(/\r?\n\r?\n/);
  const title = blocks.shift().replace(/^# /,'');
  const english = blocks.shift();
  const heading = slug==='privacy' ? 'App 隐私政策 / App Privacy Policy' : 'App 补充使用条款 / Supplementary App Terms';
  let head = prefix.replace(/<title>[\s\S]*?<\/title>/, '<title>'+heading+' — Little Elsewhere</title>')
    .replace(/https:\/\/www\.jevaiworks\.com\/little-elsewhere\/privacy\//g,'https://www.jevaiworks.com/little-elsewhere/'+slug+'/')
    .replace(/(<meta (?:name="description"|property="og:description") content=")[^"]*/g,'$1'+heading+' · 待批准草稿 / Draft for owner approval')
    .replace(/(<meta property="og:title" content=")[^"]*/g,'$1'+heading+' — Little Elsewhere');
  if (!head.includes('name="robots" content="noindex"')) throw Error('Draft must remain noindex');
  const body = blocks.map(block => block.startsWith('## ')
    ? '<h2>'+inline(block.slice(3))+'</h2>'
    : '<p'+(block.startsWith('待负责人') ? ' class="draft-notice"' : /^[A-Za-z]/.test(block) && (block.match(/[\u3400-\u9fff]/g)||[]).length < 20 ? ' lang="en" class="translation"' : '')+'>'+inline(block.replace(/\r?\n/g,' '))+'</p>').join('\n');
  const links='<nav class="help-links" aria-label="App 政策 / App policies"><a href="../privacy/">App 隐私 / App Privacy</a><a href="../terms/">补充条款草稿 / Supplementary Terms draft</a><a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Standard EULA</a><a href="../support/">帮助与支持 / Help &amp; Support</a></nav>';
  const html=head+'<article class="legal le-help"><a class="breadcrumb" href="../">← 返回别境 / Back to Little Elsewhere</a><h1>'+inline(title)+'<span lang="en">'+inline(english)+'</span></h1>\n'+body+links+'</article>'+suffix;
  fs.mkdirSync(path.join(root,'little-elsewhere',slug),{recursive:true});
  fs.writeFileSync(path.join(root,'little-elsewhere',slug,'index.html'),html);
}
console.log('Generated bilingual privacy and supplementary terms approval drafts; noindex retained.');
