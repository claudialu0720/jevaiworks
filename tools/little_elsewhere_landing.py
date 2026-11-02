"""V3 landing-page composition and bilingual marketing copy only."""

TEXT = {
    'zh-CN': {
        'title': '把繁忙留在岸上。<br>我们湖心见。',
        'description': '一款把专注变成钓鱼时光的温柔计时器。',
        'intro': '留一点时间，<br>给眼前的事。',
        'introText': '选好专注时长，写下一个小目标。<br>剩下的，就交给湖水和风。',
        'details': [('选一段时间', '按自己的节奏，慢慢开始。'), ('带上一点声音', '音乐、自然声，或只是安静。')],
        'focus': '你专心，风景陪着你。',
        'focusText': '云在走，水在流。让眼前的事，慢慢有了自己的节奏。',
        'focusCaption': '在瀑布前，安静地度过这一段时间。',
        'catch': '认真度过的时间，<br>会带来一点小惊喜。',
        'catchText': '完成一段专注，钓起一条鱼，或是一件意外的小收藏。<br>每次回到湖边，都有新的期待。',
        'catchNote': '专注结束，看看今天遇见了谁。',
        'world': '还有一些别处，<br>等你慢慢发现。',
        'worldText': '雨后的湖、月下的水面，还有喜欢的自然声音。<br>换一处风景，为日常留一点新鲜。',
        'rainbow': '雨过，天晴。', 'moon': '月亮也来作伴。',
        'sound': '把世界的声音，调到刚刚好。',
        'soundText': '背景音乐与自然环境音，陪你安静一会儿。',
        'setupAlt': '别境准备专注界面：时长、专注目标及声音设置',
        'catchAlt': '别境专注后的真实渔获界面',
        'lakeAlt': '开阔蓝天下的湖水、山峦、云朵倒影与一叶小舟',
        'focusAlt': '真实专注界面：瀑布、湖水和垂钓者',
        'underwaterAlt': '小舟下方，阳光穿过清澈的蓝色湖水',
        'musicAlt': '别境背景音乐与环境音调节界面',
    },
    'en': {
        'title': 'A little focus.<br>A little fishing.',
        'description': 'A cozy focus timer where quiet moments<br>turn into little discoveries.',
        'intro': 'A little time for<br>what’s in front of you.',
        'introText': 'Choose a duration. Set a small intention.<br>Let the lake and the breeze take it from here.',
        'details': [('Go at your own pace', 'A little time is a lovely place to start.'), ('Find your sound', 'Gentle music, nature, or a little quiet.')],
        'focus': 'You focus. The world keeps you company.',
        'focusText': 'Clouds drift. Water flows. Find a little rhythm of your own.',
        'focusCaption': 'A quiet moment by the waterfall.',
        'catch': 'Time well spent.<br>A little surprise to keep.',
        'catchText': 'Finish a focus session and discover a fish or a curious little find.<br>There’s something to look forward to, each time you return.',
        'catchNote': 'Focus done. See who came along.',
        'world': 'A little more world<br>to wander into.',
        'worldText': 'A lake after the rain. Water under moonlight. Your favourite sounds.<br>A change of scenery for an ordinary day.',
        'rainbow': 'A little rainbow after the rain.', 'moon': 'An evening with the moon.',
        'sound': 'Make yourself at home in the sound.',
        'soundText': 'Gentle music and natural ambience, mixed your way.',
        'setupAlt': 'Little Elsewhere focus setup: duration, intention, and sound settings',
        'catchAlt': 'A real catch screen after a Little Elsewhere focus session',
        'lakeAlt': 'An open blue sky, cloud reflections, mountains, and a little boat on the lake',
        'focusAlt': 'The real focus screen: a waterfall, calm water, and an angler',
        'underwaterAlt': 'Sunlight falls through the clear blue water beneath a little boat',
        'musicAlt': 'Little Elsewhere music and natural ambience controls',
    },
}


def landing_content(lang, common, image, button):
    t = TEXT[lang]
    suffix = 'cn' if lang == 'zh-CN' else 'en'
    # All scenery keeps its complete native aspect ratio. Screens sit in their own
    # device frames, not in pastel cards; no fake timer or generated artwork.
    def phone(slug, alt, cls=''):
        return f'<div class="device {cls}">{image(slug, alt, cls="device-screen")}</div>'

    return f'''<main id="main">
  <section class="arrival" aria-labelledby="arrival-title">
    <div class="arrival-copy">
      <h1 id="arrival-title">{t['title']}</h1>
      <p>{t['description']}</p>
      {button(common)}
      <span class="beta-status">{common['status']}</span>
    </div>
    <figure class="arrival-scenery">{image('lake-wide', t['lakeAlt'], False, 'panorama')}</figure>
    <div class="arrival-device">{phone('prefocus-'+suffix,t['setupAlt'])}</div>
    <a class="journey-link" href="#explore">{common['explore']} <span aria-hidden="true">↓</span></a>
  </section>

  <section class="settle content" id="explore" aria-labelledby="settle-title">
    <div class="settle-copy">
      <h2 id="settle-title">{t['intro']}</h2>
      <p>{t['introText']}</p>
      <dl>{''.join(f'<div><dt>{heading}</dt><dd>{description}</dd></div>' for heading,description in t['details'])}</dl>
    </div>
    <figure class="settle-interface">{phone('prefocus-'+suffix,t['setupAlt'])}</figure>
  </section>

  <section class="immersion" aria-labelledby="immersion-title">
    <div class="immersion-copy content">
      <h2 id="immersion-title">{t['focus']}</h2>
      <p>{t['focusText']}</p>
    </div>
    <figure class="immersive-scene">
      {image('waterfall-wide',t['focusAlt'],cls='panorama')}
      <figcaption>{t['focusCaption']}</figcaption>
    </figure>
  </section>

  <section class="discover" aria-labelledby="discover-title">
    <div class="discovery-copy content">
      <h2 id="discover-title">{t['catch']}</h2>
      <p>{t['catchText']}</p>
    </div>
    <div class="discovery-water">
      <figure class="underwater">{image('underwater-wide',t['underwaterAlt'],cls='panorama')}</figure>
      <figure class="catch-interface">{phone('catch-'+suffix,t['catchAlt'])}<figcaption>{t['catchNote']}</figcaption></figure>
    </div>
  </section>

  <section class="wander" aria-labelledby="wander-title">
    <div class="wander-intro content">
      <h2 id="wander-title">{t['world']}</h2>
      <p>{t['worldText']}</p>
    </div>
    <div class="changing-light">
      <figure>{image('rainbow',t['rainbow'],cls='panorama')}<figcaption>{t['rainbow']}</figcaption></figure>
      <figure>{image('moon',t['moon'],cls='panorama')}<figcaption>{t['moon']}</figcaption></figure>
    </div>
    <div class="soundscape content">
      <figure>{image('music',t['musicAlt'],cls='panorama')}</figure>
      <div><h3>{t['sound']}</h3><p>{t['soundText']}</p></div>
    </div>
  </section>

  <section class="invitation" id="beta" aria-labelledby="invitation-title">
    <div class="content">
      <h2 id="invitation-title">{common['final']}</h2>
      {button(common)}
      <p class="beta-status">{common['status']}</p>
      <details class="beta-help"><summary>{common['faq']}</summary><div class="answer"><p>{common['instructions']}</p><p>{common['help']}</p></div></details>
    </div>
    <figure class="return-to-lake" aria-hidden="true">{image('lake-wide','',cls='panorama')}</figure>
  </section>
</main>'''
