// Isolated local review only. Never writes release settings or production HTML.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
import { render } from './release.mjs';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root,'site.config.js'),'utf8'),context);
const config = context.window.JEVAI_CONFIG;
const templates = {'/':'home','/little-elsewhere/':'product','/terms/':'terms'};
const types = {'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.webp':'image/webp','.png':'image/png','.svg':'image/svg+xml'};
http.createServer((req,res)=>{
  try {
    const url = new URL(req.url,'http://localhost');
    const released = url.searchParams.get('state') === 'released';
    const nojs = url.searchParams.get('nojs') === '1';
    const file = path.resolve(root,'.'+decodeURIComponent(url.pathname));
    const relative = path.relative(root,file);
    if (relative.startsWith('..') || path.isAbsolute(relative) || relative.split(path.sep).some(p=>p.startsWith('.')) || relative.startsWith('tools')) {res.writeHead(403);res.end();return;}
    const target = fs.existsSync(file) && fs.statSync(file).isDirectory() ? path.join(file,'index.html') : file;
    if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {res.writeHead(404);res.end();return;}
    const html = path.extname(target)==='.html';
    let content = fs.readFileSync(target);
    if (html) {
      if (templates[url.pathname]) {
        // Synthetic value stays inside this process. It is removed from the response.
        const fixture = 'https://apps.apple.com/app/id0';
        const settings = released ? {...config,APP_RELEASE_STATUS:'released',APP_STORE_URL:fixture,APP_STORE_URL_VERIFIED:true} : {...config,APP_RELEASE_STATUS:'beta'};
        content = render(fs.readFileSync(path.join(root,'tools/templates',templates[url.pathname]+'.html'),'utf8'),settings);
        if (released) content = content.replaceAll('href="'+fixture+'"','aria-disabled="true" title="Preview only: actual App Store URL required"');
      } else content = content.toString();
      // Preserve review state while navigating local pages. mailto and external links untouched.
      content = content.replace(/href="([^"?]+)"/g,(match,href)=>{
        if (/^(https?:|mailto:|#)/.test(href) || !/\/(?:#.*)?$/.test(href)) return match;
        const [pathname,fragment] = href.split('#');
        return 'href="'+pathname+'?state='+(released?'released':'beta')+(nojs?'&amp;nojs=1':'')+(fragment?'#'+fragment:'')+'"';
      });
      content = content.replace('<body ', '<body data-review-state="'+(released?'released':'beta')+'" ');
    }
    const headers = {'Content-Type':types[path.extname(target)]||'application/octet-stream','Cache-Control':'no-store'};
    if (nojs && html) headers['Content-Security-Policy'] = "script-src 'none'";
    res.writeHead(200,headers);res.end(content);
  } catch {res.writeHead(500);res.end('Preview failed');}
}).listen(4174,'127.0.0.1',()=>console.log('Local review: http://127.0.0.1:4174/little-elsewhere/?state=beta&nojs=1 (state=released for isolated demo; download disabled)'));
