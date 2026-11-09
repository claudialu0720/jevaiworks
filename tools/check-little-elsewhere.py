"""Regression checks: complete legal wording, routes and redirects.
Run after node tools/preview.mjs. Standard library only.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.request import build_opener, ProxyHandler
import re, subprocess
ROOT=Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r'\[([^\]]+)\]\(((?:https?://|mailto:)[^\s)]+)\)')
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.text=[]
    def handle_data(self,data): self.text.append(data)
for route,name in [
    ('privacy','privacy.zh-CN.2026-11-09.md'),
    ('terms','terms.zh-CN.2026-11-09.md'),
    ('en/privacy','privacy.en.2026-11-09.md'),
    ('en/terms','terms.en.2026-11-09.md'),
]:
    source=(ROOT/'little-elsewhere/legal-source'/name).read_text(encoding='utf-8')
    page=(ROOT/'little-elsewhere'/route/'index.html').read_text(encoding='utf-8')
    assert f'data-legal-source="{name}"' in page, f'{route}: wrong source'
    article=page.split('<article data-legal-source=')[1].split('>',1)[1].split('</article>')[0]
    is_en = route.startswith('en/')
    if route.endswith('privacy'):
        other_path = '/little-elsewhere/privacy' if is_en else '/little-elsewhere/en/privacy'
        other_lang = 'zh-CN' if is_en else 'en'
        assert f'href="{other_path}" lang="{other_lang}" hreflang="{other_lang}"' in page, f'{route}: missing language switch'
        alternate_url = 'https://jevaiworks.com' + other_path + '/'
        language_link = next(line for line in source.splitlines() if (link := MARKDOWN_LINK.fullmatch(line)) and link[2] == alternate_url)
        source = source.replace(language_link + '\n\n', '', 1)
    parser=Text(); parser.feed(article)
    rendered=re.sub(r'\s+','',''.join(parser.text))
    expected=[]
    for line in source.splitlines():
        if re.fullmatch(r'\|[-| ]+\|',line): continue
        line=re.sub(r'^(#{1,6} |\d+\. |- )','',line).replace('**','')
        line=MARKDOWN_LINK.sub(r'\1',line)
        if line.startswith('|'): line=line.replace('|','')
        expected.append(line)
    assert rendered==re.sub(r'\s+','',''.join(expected)), f'{route}: legal wording changed'
    for _,url in MARKDOWN_LINK.findall(source):
        assert f'href="{url}"' in article, f'{route}: missing legal link {url}'
    assert article.count('<strong>') == source.count('**') // 2, f'{route}: missing emphasis'
    assert article.count('<h2>') == len(re.findall(r'^## ',source,re.M)), f'{route}: missing section'
    assert not re.search(r'V3\.2|草[稿案]|待确认|待核实|\b(?:draft|TBC|TBD|TODO)\b', page, re.I), f'{route}: draft marker'
    if route.endswith('terms'):
        effective_date = 'Effective date:</strong> November 9, 2026' if is_en else '生效日期：</strong> 2026年11月9日'
        assert effective_date in article, f'{route}: wrong effective date'
        other_path = '/little-elsewhere/terms/' if is_en else '/little-elsewhere/en/terms/'
        other_lang = 'zh-CN' if is_en else 'en'
        assert f'href="{other_path}" lang="{other_lang}" hreflang="{other_lang}"' in page, f'{route}: missing language switch'
        assert not re.search(r'\d|%', source.split('## 6. ' if is_en else '## 六、')[1].split('\n## ')[0]), f'{route}: numeric BUBS rule'
    else:
        effective_date = 'Effective date</strong>　November 9, 2026' if is_en else '生效日期</strong>　2026年11月9日'
        assert effective_date in article, f'{route}: wrong effective date'
        assert '<aside class="notice">' not in page, f'{route}: unexpected notice'
    print('PASS complete legal wording, links, emphasis and sections:',route)
for route in ['','en/','privacy','terms','en/privacy','en/terms','support/','en/support/']:
    url='http://127.0.0.1:4173/little-elsewhere/'+route
    for attempt in range(2):
        with build_opener(ProxyHandler({})).open(url, timeout=10) as res:
            body=res.read().decode('utf-8'); assert res.status==200
            assert f'lang="{"en" if route.startswith("en") else "zh-CN"}"' in body
            assert 'hreflang="zh-CN"' in body and 'hreflang="en"' in body
            if route and not route.endswith('/'):
                assert res.url.endswith(route+'/'), 'directory redirect missing'
    print('PASS direct navigation + repeat request:',url)
for name in ['privacy/index.html','terms/index.html']:
    expected=subprocess.check_output(['git','show','HEAD:'+name],cwd=ROOT)
    assert (ROOT/name).read_bytes().replace(b'\r\n',b'\n')==expected.replace(b'\r\n',b'\n'),name+' changed'
print('PASS corporate legal pages unchanged')
