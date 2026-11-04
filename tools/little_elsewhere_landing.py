"""V4 compact editorial landing composition and language-specific copy."""
from pathlib import Path
TEXT = {
 'zh-CN': {
  'title': '把专注变成一场安静的垂钓。',
  'description': '一款可以边专注、边钓鱼的番茄钟。',
  'support': '选一段时间，让风景、水声和音乐陪你完成眼前的事。',
  'how': '专注片刻，收获一点小惊喜。',
  'steps': [('选择时间', '学习、工作或阅读，从这里开始。'), ('沉浸湖畔', '让水声与音乐陪你慢慢专注。'), ('钓起惊喜', '专注结束，看看今天钓到了什么。')],
  'discover': '让认真度过的时间，变成看得见的回忆。',
  'discoverText': '收集不同的鱼类和奇妙物品，把喜欢的小鱼放进池塘。探索更多风景与声音，让每次专注都有一点期待。',
  'labels': ['渔获收集', '自然音景', '更多风景'],
  'closing': '先从一段专注、一条小鱼开始吧。',
  'closingText': '不用急着成为更自律的人。按照自己的节奏，慢慢来。',
  'alts': ['专注设置：时长、目标与声音', '专注进行中：彩虹下的湖畔垂钓时光', '完成专注后，钓起一条小鱼'],
  'duoAlt': 'iPhone Duo 横屏画面：瀑布前的湖面与垂钓小舟',
  'journalDuo': ('查看 iPhone Duo 画面', '返回普通 iPhone 画面', 'iPhone Duo 横屏上的别境：湖畔垂钓与中文灵感及待办面板'),
  'duoLabel': '查看 iPhone Duo 屏幕',
  'soloLabel': '返回普通 iPhone 屏幕',
  'lakeAlt': '蓝天下，湖水倒映着云朵与山峦',
  'heroAlt': '别境中文首页：秘境飞瀑、专注时长与开始专注',
  'collectionAlt': '原版应用商店画面：鱼类、宝藏收藏与个人池塘',
  'musicAlt': '背景音乐与自然环境音的独立调节界面',
  'mapAlt': '探索不同环境的地图界面',
 },
 'en': {
  'title': 'A little focus. A little fishing.',
  'description': 'A cozy Pomodoro timer with soothing sounds<br>and little discoveries.',
  'support': 'Set a timer, settle by the water, and focus on what matters.',
  'how': 'A little surprise after every session.',
  'steps': [('Set your timer', 'Choose a little time to study, work, or read.'), ('Settle by the water', 'Let gentle music and nature sounds keep you company.'), ("See what you've caught", 'A fish, a treasure, or something unexpected.')],
  'discover': 'Little discoveries, lasting memories.',
  'discoverText': 'Collect fish and treasures, fill your personal pond, and explore peaceful worlds at your own pace.',
  'labels': ['Collect your catches', 'Peaceful soundscapes', 'More worlds to explore'],
  'closing': 'Focus for a little while. Let the water take care of the rest.',
  'closingText': '',
  'alts': ['Focus setup: duration, intention, and sound controls', 'An active focus session fishing beneath a rainbow', 'Discovering a fish after a completed focus session'],
  'duoAlt': 'Little Elsewhere on iPhone Duo: a fishing boat on a lake by the waterfall',
  'journalDuo': ('View iPhone Duo screen', 'Back to standard iPhone screen', 'Little Elsewhere on iPhone Duo with the English Inspiration and To-do panel'),
  'duoLabel': 'View iPhone Duo screen',
  'soloLabel': 'Back to standard iPhone screen',
  'lakeAlt': 'Clouds and mountains reflected in a bright, peaceful lake',
  'heroAlt': 'Little Elsewhere English home screen: Hidden Falls, focus duration, and Start focus',
  'collectionAlt': 'Original English App Store artwork: fish, treasure collections, and your personal pond',
  'musicAlt': 'Music and natural ambience with independent volume controls',
  'mapAlt': 'The map of peaceful environments to explore',
 }
}


def focus_switch(duo_label, solo_label, image_attrs=''):
    return (f'<button class="focus-switch" type="button" hidden {image_attrs}'
            f'data-duo-label="{duo_label}" data-solo-label="{solo_label}" '
            f'aria-pressed="false">{duo_label}</button>')


def landing_content(lang, common, image, button):
    t = TEXT[lang]
    suffix = 'cn' if lang == 'zh-CN' else 'en'
    rewards = (Path(__file__).resolve().parent / f'rewards-{suffix}.html').read_text(encoding='utf-8')
    worlds = (Path(__file__).resolve().parent / f'worlds-{suffix}.html').read_text(encoding='utf-8')
    journal = (Path(__file__).resolve().parent / f'journal-{suffix}.html').read_text(encoding='utf-8')
    duo_label, solo_label, duo_alt = t['journalDuo']
    journal_duo = (f'<img class="journal-duo" data-duo-preview hidden '
                   f'src="/assets/little-elsewhere/journal/duo-{suffix}.webp" '
                   f'width="1204" height="875" alt="{duo_alt}" loading="lazy" decoding="async">\n'
                   f'      {focus_switch(duo_label, solo_label)}')
    journal = journal.replace('<!-- journal-duo-preview -->', journal_duo)
    def phone(slug, alt):
        return f'<div class="device">{image(slug, alt, cls="device-screen")}</div>'
    headline = t['title'].replace('变成', '变成<br>') if lang == 'zh-CN' else t['title'].replace('focus. ', 'focus.<br> ')
    slugs = ['pre-'+suffix, 'focus-session-rainbow', 'fish-'+suffix]
    focus_duo_attrs = ('data-duo-src="/assets/little-elsewhere/redesign/duo-focus.webp" '
                       'data-duo-width="1323" data-duo-height="908" '
                       f'data-duo-alt="{t["duoAlt"]}" ')
    focus_preview = (f'<div class="focus-preview">'
                     f'{image(slugs[1], t["alts"][1], cls="landscape-screen focus-preview-image")}'
                     f'{focus_switch(t["duoLabel"], t["soloLabel"], focus_duo_attrs)}</div>')
    steps = ''.join(f'<li class="journey-step"><figure>{phone(slugs[i], t["alts"][i]) if i != 1 else focus_preview}<figcaption><h3><span class="step-number">{i+1}</span>{heading}</h3><p>{description}</p></figcaption></figure></li>' for i,(heading,description) in enumerate(t['steps']))
    return f'''<main id="main">
  <section class="arrival" aria-labelledby="arrival-title">
    <div class="arrival-inner content">
      <div class="arrival-copy">
        <h1 id="arrival-title">{headline}</h1>
        <p class="description">{t['description']}</p>
        <p class="support">{t['support']}</p>
        {button(common)}
      </div>
    </div>
    <figure class="hero-interface">{image('home-'+suffix, t['heroAlt'], False, 'landscape-screen')}</figure>
    <figure class="arrival-scenery">{image('lake-wide', t['lakeAlt'], False, 'panorama')}</figure>
  </section>
  <section class="experience content" id="explore" aria-labelledby="experience-title">
    <h2 id="experience-title">{t['how']}</h2>
    <ol class="journey">{steps}</ol>
  </section>
  <section class="discover rewards-scene" aria-labelledby="discover-title">
    {rewards}
  </section>
  <section class="journal-scene" aria-labelledby="journal-record-title journal-notes-title">
    <svg class="journal-color-filters" width="0" height="0" aria-hidden="true">
      <filter id="journal-lake-color" color-interpolation-filters="sRGB">
        <feColorMatrix type="matrix" values="
          1.4168 -.3640 -.0418 0 -.0366
          .0452 1.0009 .0196 0 -.0074
          .0204 .0321 1.0080 0 .0007
          0 0 0 1 0"/>
      </filter>
    </svg>
    {journal}
  </section>
  <section class="worlds-scene" aria-labelledby="worlds-music-title worlds-map-title">
    {worlds}
  </section>
  <section class="invitation" id="beta" aria-labelledby="invitation-title">
    <div class="content">
      <h2 id="invitation-title">{t['closing']}</h2>
      {('<p>'+t['closingText']+'</p>') if t['closingText'] else ''}
      {button(common)}
    </div>
  </section>
</main>'''
