"""Generate Little Elsewhere's static pages. Run from any directory.
No runtime dependencies. Legal renderer covers the Markdown used by the V3.2 sources.
"""
from pathlib import Path
from html import escape
import re
import sys
sys.dont_write_bytecode = True
from little_elsewhere_landing import landing_content, TEXT
from little_elsewhere_support import SUPPORT, support_content

ROOT = Path(__file__).resolve().parents[1]
BASE = '/little-elsewhere/'
ASSET = '/assets/little-elsewhere/redesign/'
ORIGIN = 'https://jevaiworks.com'
ASSET_SIZES = {'catch-cn': (600, 1300), 'catch-en': (600, 1300), 'icon': (600, 600), 'lake-800': (800, 290), 'lake': (1600, 580), 'moon-800': (800, 369), 'moon': (1600, 738), 'music-800': (800, 369), 'music': (1600, 738), 'prefocus-cn': (600, 1300), 'prefocus-en': (600, 1300), 'rainbow-800': (800, 369), 'rainbow': (1600, 738), 'underwater-800': (800, 290), 'underwater': (1600, 580), 'waterfall-800': (800, 369), 'waterfall': (1600, 738)}
ASSET_SIZES.update({'lake-wide': (2083, 755), 'underwater-wide': (2083, 755), 'waterfall-wide': (2200, 1015)})
ASSET_SIZES.update({'collection-cn': (1500, 1106), 'collection-en': (1500, 1088), 'map': (400, 867), 'hero-focus': (1400, 646), 'hero-banner-frame': (1516, 736), 'focus-session-rainbow': (1517, 736)})
ASSET_SIZES.update({'home-cn': (403, 831), 'home-en': (404, 831)})
ASSET_SIZES.update({'pre-cn': (403, 831), 'pre-en': (403, 831), 'fish-cn': (800, 1651), 'fish-en': (800, 1650)})
BETA = 'https://testflight.apple.com/join/Uk9rZz5B'
# Keep generated pages connected to the Little Elsewhere web stream.
GOOGLE_TAG = '''
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-212DEYMSND"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-212DEYMSND', {
    allow_google_signals: false,
    allow_ad_personalization_signals: false
  });
</script>
'''
COPY = {
'zh-CN': dict(name='别境', explore='探索别境', cta='加入 iOS 内测', title='专注一会儿，<br>去湖边钓条鱼。', desc='一款把专注变成钓鱼时光的温柔计时器。', support='设定时间，让风景与声音陪你专注。<br>完成之后，钓起一份属于自己的小惊喜。', status='iOS 内测 · 通过 TestFlight', caption='把喧嚣留在岸上。', caption2='湖水、小舟，和属于你的时间。', how='一段专注，<br>三点小小的快乐。', howdesc='不用急着做更多。<br>从给眼前的事留一点时间开始。', steps=[('设定专注时间','选好时长，写下此刻想做的事。'),('沉浸湖畔时光','让小舟停在水面，让思绪回到眼前。'),('钓起意外惊喜','完成专注，看看这次遇见了谁。')], world='一点风景，<br>一点声音，<br>一点发现。', worlddesc='在瀑布边听水声，在月光下坐一会儿。换一处风景，也给日常换一种心情。', rainbow='雨过天晴，等一道彩虹。', moon='夜深了，还有月亮作伴。', more='不止是计时，<br>也是自己的小天地。', moredesc='让每次专注，都多一点值得期待的事。', features=[('听见喜欢的安静','背景音乐与自然环境音，陪你慢慢进入状态。'),('留下小小的收获','收集遇见的鱼和物品，记住一段湖畔时光。')], final='给自己一小段别处的时间。', faq='如何加入内测？', instructions='在 iPhone 上安装 Apple 的 <a href="https://apps.apple.com/app/testflight/id899247664">TestFlight</a>，再打开本页的内测邀请，在 TestFlight 中接受邀请并安装别境。', help='若暂时无法加入，请查看邀请页的名额和设备要求。可通过 TestFlight 发送 Beta 版反馈，或联系 <a href="mailto:hello@jevaiworks.com">hello@jevaiworks.com</a>。', privacy='隐私政策', terms='用户服务协议', contact='联系', credit='界外造物出品', back='← 返回别境', skip='跳至主要内容'),
'en': dict(name='Little Elsewhere', explore='Explore', cta='Join the iOS Beta', title='A little focus.<br>A little fishing.', desc='A cozy focus timer that turns quiet moments into little discoveries.', support='Set a timer, settle by the water,<br>and see what you catch along the way.', status='iOS beta · via TestFlight', caption='Leave the noise on the shore.', caption2='A lake, a little boat, a moment for yourself.', how='A little time.<br>Three little joys.', howdesc='Make a little room for the thing in front of you. The lake will keep you company.', steps=[('Set a focus timer','Choose a little time for what matters to you.'),('Focus by the water','Let the scenery and sounds help you settle in.'),('Catch little surprises','Finish your session. See who comes along.')], world='A little scenery.<br>A little sound.<br>A little discovery.', worlddesc='Listen to a waterfall. Sit beneath the moon. A change of scenery for an ordinary day.', rainbow='A little rainbow after the rain.', moon='A quiet evening, with the moon for company.', more='More than a timer.<br>A little world of your own.', moredesc='Something to look forward to, each time you focus.', features=[('Find your quiet','Gentle music and natural ambience help you ease into the moment.'),('Keep a little discovery','Collect fish and little finds to remember your time by the water.')], final='Find your little elsewhere.', faq='How do I join the beta?', instructions='On your iPhone, install Apple’s <a href="https://apps.apple.com/app/testflight/id899247664">TestFlight</a>, then open the beta invitation on this page. Accept the invitation and install Little Elsewhere in TestFlight.', help='If you can’t join, check availability and device requirements on the invitation page. Send Beta Feedback through TestFlight or email <a href="mailto:hello@jevaiworks.com">hello@jevaiworks.com</a>.', privacy='Privacy Policy', terms='Terms of Service', contact='Contact', credit='A Jevai Works creation', back='← Back to Little Elsewhere', skip='Skip to content')}

def image(slug,alt,lazy=True,cls=''):
    p=ROOT/ASSET.lstrip('/')/(slug+'.webp')
    w,h=ASSET_SIZES[slug]
    small = '-1000' if (p.parent/(slug+'-1000.webp')).exists() else '-800'
    small_width = 1000 if small == '-1000' else 800
    responsive=f' srcset="{ASSET}{slug}{small}.webp {small_width}w, {ASSET}{slug}.webp {w}w" sizes="100vw"' if (p.parent/(slug+small+'.webp')).exists() else ''
    return f'<img class="{cls}" src="{ASSET}{slug}.webp"{responsive} width="{w}" height="{h}" alt="{escape(alt)}" '+('loading="lazy" decoding="async"' if lazy else 'fetchpriority="high"')+'>'

def button(c): return f'<a class="button" href="{BETA}">{c["cta"]}<span aria-hidden="true">↗</span></a>'
def route(lang,kind=''): return BASE+('en/' if lang=='en' else '')+kind+('/' if kind=='support' else '')

def shell(lang,body,kind='',description=None):
    c=COPY[lang] | {'support': SUPPORT[lang]['title']}
    title=('Little Elsewhere — '+TEXT[lang]['title']) if not kind else c[kind]+' — Little Elsewhere'
    description=description or c['desc']; url=route(lang,kind)
    langs=''.join(f'<a href="{route(l,kind)}" lang="{l}" hreflang="{l}"'+(' aria-current="page"' if l==lang else '')+f'>{label}</a>'+('<span aria-hidden="true">/</span>' if l=='zh-CN' else '') for l,label in [('zh-CN','中'),('en','EN')])
    theme_color = '#f1f9fc' if not kind else '#f4fbff'
    landing_css = f'<link rel="stylesheet" href="{BASE}landing-v4.css?v=2">' if not kind else ''
    body_class = ' class="landing-page"' if not kind else ' class="legal-page"'
    if kind:
        nav_links = f'<a class="explore" href="{route(lang)}#explore">{c["explore"]}</a>'
        nav_cta = button(c)
        footer_contact = '#contact' if kind == 'support' else f'{route(lang, "support")}#contact'
        support_label = c['support']
    else:
        privacy_label = '隐私政策' if lang == 'zh-CN' else 'Privacy'
        nav_links = f'<a href="{route(lang,"privacy")}/">{privacy_label}</a><a href="#contact">{c["contact"]}</a>'
        nav_cta = ''
        footer_contact = '#contact'
        support_label = '支持' if lang == 'zh-CN' else 'Support'
    copyright_name = 'Jevai Works' if lang == 'en' and not kind else '界外造物创意科技（青岛）有限公司'
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">{GOOGLE_TAG}<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="{theme_color}"><title>{escape(title)}</title><meta name="description" content="{escape(description)}"><link rel="canonical" href="{ORIGIN+url}"><link rel="alternate" hreflang="zh-CN" href="{ORIGIN+route('zh-CN',kind)}"><link rel="alternate" hreflang="en" href="{ORIGIN+route('en',kind)}"><link rel="alternate" hreflang="x-default" href="{ORIGIN+route('zh-CN',kind)}"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN+url}"><meta property="og:locale" content="{'zh_CN' if lang=='zh-CN' else 'en_US'}"><meta property="og:image" content="{ORIGIN+ASSET}lake.webp"><meta property="og:image:alt" content="{'别境湖畔风景' if lang=='zh-CN' else 'A peaceful lake in Little Elsewhere'}"><link rel="icon" href="{ASSET}icon.webp"><link rel="stylesheet" href="{BASE}product.css"><script defer src="{BASE}product.js"></script>{landing_css}</head><body{body_class}>
<a class="skip" href="#main">{c['skip']}</a><header class="header wrap"><a class="brand" href="{route(lang)}"><img src="{ASSET}icon.webp" width="42" height="42" alt=""><span>{c['name']}</span></a><nav aria-label="{'主导航' if lang=='zh-CN' else 'Main navigation'}">{nav_links}<div class="languages" role="group" aria-label="{'语言' if lang=='zh-CN' else 'Language'}">{langs}</div>{nav_cta}</nav></header>
{body}
<footer class="footer wrap"><div class="footer-top"><a href="{route(lang)}">Little Elsewhere</a><nav aria-label="{'页脚导航' if lang=='zh-CN' else 'Footer navigation'}"><a href="{route(lang,'privacy')}">{c['privacy']}</a><a href="{route(lang,'terms')}">{c['terms']}</a><a href="{route(lang,'support')}"{' aria-current="page"' if kind=='support' else ''}>{support_label}</a><a href="{footer_contact}">{c['contact']}</a></nav></div><div class="footer-bottom"><a class="footer-credit" href="/">{c['credit']}</a><p>© 2026 {copyright_name}</p></div></footer></body></html>'''

def landing(lang):
    body = '\n'.join(line.rstrip() for line in landing_content(lang, COPY[lang], image, button).splitlines())
    description = re.sub('<[^>]+>', ' ', TEXT[lang]['description'])
    return shell(lang, body, description=description)


def inline(s):
    s=escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^\s<|)]+)\)|(https?://[^\s<|]+)',lambda m:f'<a href="{m[2] or m[3]}">{m[1] or m[3]}</a>',s)
    return s

def markdown(source, lang='zh-CN'):
    lines=source.splitlines(); out=[]; i=0
    while i<len(lines):
        s=lines[i]
        if not s.strip(): i+=1; continue
        if s.startswith('#'):
            m=re.match(r'(#{1,6}) (.*)',s); level=len(m[1]); out.append(f'<h{level}>{inline(m[2])}</h{level}>'); i+=1
        elif s.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=lines[i].strip('|').split('|'); i+=1
                if all(re.fullmatch(r'[:\- ]+',x) for x in cells): continue
                tag='th' if not rows else 'td'; rows.append('<tr>'+''.join(f'<{tag}>{inline(x.strip())}</{tag}>' for x in cells)+'</tr>')
            label = '政策信息表' if lang == 'zh-CN' else 'Policy information table'
            out.append(f'<div class="table-scroll" tabindex="0" role="region" aria-label="{label}"><table><thead>'+rows[0]+'</thead><tbody>'+''.join(rows[1:])+'</tbody></table></div>')
        elif re.match(r'(- |\d+\. )',s):
            ordered=s[0].isdigit(); tag='ol' if ordered else 'ul'; items=[]
            while i<len(lines) and re.match(r'(- |\d+\. )',lines[i]):
                items.append('<li>'+inline(re.sub(r'^(- |\d+\. )','',lines[i]))+'</li>'); i+=1
            out.append(f'<{tag}>'+''.join(items)+f'</{tag}>')
        else:
            parts=[]
            while i<len(lines) and lines[i].strip():
                parts.append(inline(lines[i].rstrip())+('<br>' if lines[i].endswith('  ') else '')); i+=1
            out.append('<p>'+''.join(parts)+'</p>')
    return '\n'.join(out)

LEGAL_SOURCES = {
    'zh-CN': {
        'privacy': 'Little_Elsewhere_隐私政策_V3.2_2026-11-05.md',
        'terms': 'Little_Elsewhere_用户服务协议_V3.2_2026-11-05.md',
    },
    'en': {
        'privacy': 'Little_Elsewhere_Privacy_Policy_EN_V3.2_2026-11-05.md',
        'terms': 'Little_Elsewhere_Terms_of_Use_EN_V3.2_2026-11-05.md',
    },
}


def generate():
    for lang in COPY:
        folder=ROOT/route(lang).strip('/'); folder.mkdir(parents=True,exist_ok=True); (folder/'index.html').write_text(landing(lang),encoding='utf-8')
        support_folder=ROOT/route(lang,'support').strip('/')
        support_folder.mkdir(parents=True,exist_ok=True)
        support_body=support_content(lang, route(lang), COPY[lang]['back'])
        (support_folder/'index.html').write_text(shell(lang,support_body,'support',SUPPORT[lang]['intro']),encoding='utf-8')
        for kind,filename in LEGAL_SOURCES[lang].items():
            c=COPY[lang]
            source=(ROOT/'little-elsewhere/legal-source'/filename).read_text(encoding='utf-8-sig')
            if lang=='zh-CN':
                notice='V3.2 · 代码核查后的待发布草稿。生效日期及原文中的待确认事项尚未填写或核实，以下按所提供文档完整展示。'
                description='别境 '+c[kind]+' V3.2（待发布草稿）。'
            else:
                notice=('V3.2 · Draft aligned to source-code review. The effective date and pending confirmations '
                        'remain as provided in the source document. '
                        f'<a href="{route("zh-CN",kind)}/" lang="zh-CN">阅读中文原文</a>')
                description=c[kind]+' for Little Elsewhere. V3.2 draft aligned to source-code review.'
            content=f'<aside class="notice">{notice}</aside><article data-legal-source="{filename}">{markdown(source, lang)}</article>'
            body=f'<main id="main" class="legal wrap "><a class="back" href="{route(lang)}">{c["back"]}</a>{content}</main>'
            p=ROOT/route(lang,kind).strip('/'); p.mkdir(parents=True,exist_ok=True)
            (p/'index.html').write_text(shell(lang,body,kind,description),encoding='utf-8')
if __name__=='__main__': generate()
