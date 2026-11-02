"""Regression checks: complete legal wording, routes and redirects.
Run after node tools/preview.mjs. Standard library only.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.request import build_opener, ProxyHandler
import re, subprocess
ROOT=Path(__file__).resolve().parents[1]
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.text=[]
    def handle_data(self,data): self.text.append(data)
for kind,name in [('privacy','Little_Elsewhere_隐私政策_V2.md'),('terms','Little_Elsewhere_用户服务协议_V2.md')]:
    source=(ROOT/'little-elsewhere/legal-source'/name).read_text(encoding='utf-8')
    page=(ROOT/'little-elsewhere'/kind/'index.html').read_text(encoding='utf-8')
    article=page.split('<article data-legal-source=')[1].split('>',1)[1].split('</article>')[0]
    parser=Text(); parser.feed(article)
    rendered=re.sub(r'\s+','',''.join(parser.text))
    expected=[]
    for line in source.splitlines():
        if re.fullmatch(r'\|[-| ]+\|',line): continue
        line=re.sub(r'^(#{1,6} |\d+\. |- )','',line).replace('**','')
        if line.startswith('|'): line=line.replace('|','')
        expected.append(line)
    assert rendered==re.sub(r'\s+','',''.join(expected)), f'{kind}: legal wording changed'
    print('PASS complete legal wording:',kind)
for route in ['','en/','privacy','terms','en/privacy','en/terms']:
    url='http://127.0.0.1:4173/little-elsewhere/'+route
    for attempt in range(2):
        with build_opener(ProxyHandler({})).open(url, timeout=10) as res:
            body=res.read().decode('utf-8'); assert res.status==200
            assert f'lang="{"en" if route.startswith("en") else "zh-CN"}"' in body
            assert 'hreflang="zh-CN"' in body and 'hreflang="en"' in body
            if route and not route.endswith('/'):
                assert res.url.endswith(route+'/'), 'directory redirect missing'
    print('PASS direct navigation + repeat request:',url)
for name in ['index.html','privacy/index.html','terms/index.html']:
    expected=subprocess.check_output(['git','show','HEAD:'+name],cwd=ROOT)
    assert (ROOT/name).read_bytes().replace(b'\r\n',b'\n')==expected.replace(b'\r\n',b'\n'),name+' changed'
print('PASS corporate home/privacy/terms unchanged')
