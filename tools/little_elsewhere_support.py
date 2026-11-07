"""Localized FAQ and contact content for the Little Elsewhere support pages."""

SUPPORT = {
    'zh-CN': {
        'title': '帮助与支持',
        'intro': '这里有关于专注计时、Plus 购买和本机数据的常见问题解答。',
        'faq': '常见问题',
        'contact': '联系别境',
        'contact_link': '联系我们',
        'contact_intro': '请在邮件中附上设备型号、iOS 版本、App 版本和问题经过。若附上截图，请先遮挡个人信息。',
        'operator': '运营方：界外造物创意科技（青岛）有限公司（Jevai Works）',
        'address': '注册地址：中国山东省青岛市黄岛区滨海大道路2059号内4栋办公1519户（邮编：266500）',
        'eula': 'Apple 标准最终用户许可协议',
        'questions': [
            ('如何开始专注？',
             '在湖畔主页选择时长，再轻点「开始专注」。可用时长与功能取决于你的 App 版本和权益。'),
            ('如何恢复 Plus 购买？',
             '使用购买时的 Apple 账户，在「设置 → 会员与订阅」打开 Plus 页面，再轻点「恢复购买」。'
             '如果已扣款但仍未解锁，请通过邮件联系我们。恢复购买只会恢复符合条件的 Plus 权益。'),
            ('如何管理或取消订阅？',
             '月度与年度 Plus 会自动续期。你可以在 <a href="https://apps.apple.com/account/subscriptions/">Apple 订阅管理页面</a>'
             '查看、管理或取消订阅。终身 Plus 为一次性购买。删除 App 或本机数据后，仍需通过 Apple 取消订阅。'),
            ('如何导出或删除本机数据？',
             '打开「设置 → 数据与隐私」，选择「导出备份」或「删除我的数据」。删除前请先保存需要的数据副本。'
             '当前公开发行版本仅支持导出，无法通过导入该文件恢复进度。',
             '删除本机数据后，已导出的文件和已发送的第三方统计或诊断记录仍可能保留。'
             '如需查询这些记录，可以邮件联系我们，并在可取得时通过该设置页面复制并附上完整统计 ID。'),
            ('如何申请 Apple 购买退款？',
             '通过 <a href="https://reportaproblem.apple.com/">Apple 问题报告页面</a>提出退款申请。'
             '是否符合退款条件由 Apple 按适用规则处理。'),
        ],
    },
    'en': {
        'title': 'Support',
        'intro': 'Find answers about focus sessions, Plus purchases, and data stored on your device.',
        'faq': 'Frequently asked questions',
        'contact': 'Contact Little Elsewhere',
        'contact_link': 'Email us',
        'contact_intro': 'Include your device model, iOS version, app version, and what happened. Hide any personal information in screenshots.',
        'operator': 'Operated by <span lang="zh-CN">界外造物创意科技（青岛）有限公司</span> (Jevai Works).',
        'address': 'Registered office: Office 1519, Building 4, No. 2059 Binhai Dadao Road, Huangdao District, Qingdao, Shandong, China, 266500.',
        'eula': 'Apple Standard EULA',
        'questions': [
            ('How do I start a focus session?',
             'Choose a duration on the lakeside home screen, then tap Start focus. Available durations and features depend on your app version and access.'),
            ('How do I restore Plus purchases?',
             'Open the Plus page from Settings → Membership &amp; subscription and tap Restore purchases using the Apple Account you purchased with. '
             'If you were charged and still can’t access Plus, email us. Restore purchases only recovers eligible Plus access.'),
            ('How do I manage or cancel a subscription?',
             'Monthly and annual Plus plans renew automatically. Review, manage, or cancel them in '
             '<a href="https://apps.apple.com/account/subscriptions/">Apple subscription management</a>. '
             'Lifetime Plus is a one-time purchase. If you delete the app or its data, you still need to cancel through Apple.'),
            ('How do I export or delete local data?',
             'Open Settings → Data &amp; privacy and choose Export a backup or Delete my data. Save a copy of any data you want to keep before deleting it. '
             'The current public release can export a copy. It cannot import that file to restore progress.',
             'Exported files and analytics or diagnostics already sent to third parties may remain after you delete local data. '
             'If you email us about those records, you can copy and include your full analytics ID from that settings screen if it is available.'),
            ('How do I request an Apple purchase refund?',
             'Request a refund through <a href="https://reportaproblem.apple.com/">Apple’s Report a Problem page</a>. '
             'Apple determines eligibility under its applicable rules.'),
        ],
    },
}


def support_content(lang, home, back):
    copy = SUPPORT[lang]
    questions = []
    for question, *paragraphs in copy['questions']:
        answer = ''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs)
        questions.append(f'<details><summary>{question}</summary>{answer}</details>')
    faq = '\n'.join(questions)
    return f'''<main id="main" class="legal wrap support">
<a class="back" href="{home}">{back}</a>
<h1>{copy['title']}</h1>
<p>{copy['intro']} <a href="#contact">{copy['contact_link']}</a></p>
<section aria-labelledby="faq-heading" class="support-faq">
<h2 id="faq-heading">{copy['faq']}</h2>
{faq}
</section>
<section id="contact" aria-labelledby="contact-heading">
<h2 id="contact-heading">{copy['contact']}</h2>
<div class="support-contact">
<a href="mailto:hello@jevaiworks.com"><strong>hello@jevaiworks.com</strong></a>
<p>{copy['contact_intro']}</p>
</div>
<p>{copy['operator']}<br>{copy['address']}</p>
<p><a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">{copy['eula']}</a></p>
</section>
</main>'''
