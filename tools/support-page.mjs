// Root App Store Support URL; reuse the established product support shell.
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
const root = new URL('../',import.meta.url);
const source = fs.readFileSync(new URL('little-elsewhere/support/index.html',root),'utf8');
function links(html) {
  return html.replace(/(href|src)="([^"]+)"/g,(match,attr,ref)=>{
    if (/^(https?:|mailto:|#)/.test(ref)) return match;
    const url = new URL(ref,'https://jevaiworks.com/little-elsewhere/support/');
    return `${attr}="${url.pathname}${url.hash}"`;
  });
}
const head=links(source.slice(0,source.indexOf('<article class="legal')))
  .replaceAll('https://www.jevaiworks.com/little-elsewhere/support/','https://jevaiworks.com/support/')
  .replaceAll('帮助与支持 / Help & Support — Little Elsewhere','Little Elsewhere 帮助与支持 / Support — JEVAI WORKS');
const foot=links(source.slice(source.indexOf('</main>'))).replaceAll('href="/little-elsewhere/support/"','href="/support/"');
const contact=source.match(/<section id="contact">[\s\S]*?<\/section>/)?.[0];
if (!contact) throw Error('Missing verified support contact section');
const body=`<article class="legal le-help">
<a class="breadcrumb" href="/little-elsewhere/">← 返回别境 / Back to Little Elsewhere</a>
<h1>帮助与支持<span lang="en">Little Elsewhere Support</span></h1>
<p>需要一点帮助？无论是专注计时、垂钓发现，还是购买与数据问题，我们都愿意帮你找到答案。</p>
<p class="translation" lang="en">Need a little help? We’re here for questions about focus sessions, fishing discoveries, purchases and your data.</p>
${contact}
<h2>常见问题 / Frequently asked questions</h2>
<details><summary>如何开始专注？<span lang="en">How do I start a focus session?</span></summary><div>
<p>在湖畔主页选择时长，再轻点 Start focus。可用时长与功能以你安装的版本和权益为准。</p>
<p class="translation" lang="en">Choose a duration on the lakeside home screen, then tap Start focus. Available durations and features depend on your installed version and access.</p></div></details>
<details><summary>如何恢复 Plus 购买？<span lang="en">How do I restore Plus purchases?</span></summary><div>
<p>在「设置 → 会员与订阅」打开 Plus 页面，轻点底部「恢复购买」，并使用购买时的 Apple 账户。如果已经扣款但仍未解锁，请不要重复购买，欢迎邮件联系我们。恢复购买与恢复专注记录或收藏是不同操作。</p>
<p class="translation" lang="en">Open the Plus page from Settings → Membership &amp; subscription and tap Restore purchases at the bottom, using the Apple account used for purchase. If charged but access is missing, do not buy again; email us. Restoring purchases is separate from restoring focus history or collections.</p></div></details>
<details><summary>如何管理或取消订阅？<span lang="en">How do I manage or cancel a subscription?</span></summary><div>
<p>月度与年度 Plus 是自动续期订阅，可在 <a href="https://apps.apple.com/account/subscriptions/">Apple 订阅管理页面</a>查看、管理或取消。终身方案为一次性非消耗型购买，不按月或按年续费。删除 App 或本机数据不会取消订阅；取消订阅也不会删除 App 数据。</p>
<p class="translation" lang="en">Monthly and annual Plus plans are auto-renewable subscriptions. Review, manage or cancel them in <a href="https://apps.apple.com/account/subscriptions/">Apple subscription management</a>. Lifetime is a one-time, non-consumable purchase without monthly or annual renewal. Deleting the app or local data does not cancel a subscription, and cancellation does not delete app data.</p></div></details>
<details><summary>本机数据如何备份或删除？<span lang="en">How do I back up or delete local data?</span></summary><div>
<p>在「设置 → 数据与隐私」中可导出、导入备份或选择「删除我的数据」。重置前请先保存需要的副本。删除本机数据不会删除已导出的文件，也不会自动删除已发送的第三方诊断；如需咨询已分享数据，请先复制该页显示的统计 ID 并邮件联系我们。</p>
<p class="translation" lang="en">Settings → Data &amp; privacy offers backup export/import and Delete my data. Save any needed copy before resetting. Local deletion does not remove exported files or automatically erase third-party diagnostics already sent. Copy the analytics ID displayed on that page before emailing us about shared data.</p></div></details>
<details><summary>如何申请 Apple 购买退款？<span lang="en">How do I request an Apple purchase refund?</span></summary><div>
<p>可通过 <a href="https://reportaproblem.apple.com/">Apple 问题报告页面</a>提出退款申请。是否符合退款条件由 Apple 和适用规则决定。</p>
<p class="translation" lang="en">Request a refund through <a href="https://reportaproblem.apple.com/">Apple’s Report a Problem page</a>. Eligibility is determined by Apple and applicable rules.</p></div></details>
<nav class="help-links" aria-label="相关链接 / Related links">
<a href="/little-elsewhere/">了解别境 / About Little Elsewhere</a>
<a href="/little-elsewhere/privacy/">App 隐私政策草稿 / App Privacy draft</a>
<a href="/little-elsewhere/terms/">App 补充条款草稿 / Supplementary App Terms draft</a>
<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Standard EULA</a></nav>
</article>`;
fs.mkdirSync(new URL('support/',root),{recursive:true});
fs.writeFileSync(new URL('support/index.html',root),head+body+foot);
console.log('Generated /support/ with verified contact details and bilingual help.');
