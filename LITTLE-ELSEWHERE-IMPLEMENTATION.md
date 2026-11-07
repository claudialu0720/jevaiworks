> 2026-11-05：App 中英文法律页面已替换为 V3.2 原文；当前维护与来源说明见 [法律来源说明](little-elsewhere/legal-source/README.md)。下文 V2 状态及待审记录为历史说明。

> 2026-11-02 V3 已更新营销视觉与维护入口，请以 [V3 改版说明](LITTLE-ELSEWHERE-V3.md) 为准；下文法律审阅事项继续适用。

# Little Elsewhere 改版交付与审阅说明

## 已实现

现有纯静态 HTML/CSS/JS 架构，保留 GitHub Pages 的目录路由，不引入前端框架、外部字体、追踪脚本或运行时依赖。公司主页、`/privacy/`、`/terms/` 未改动。

- `/little-elsewhere/`：中文落地页。
- `/little-elsewhere/en/`：英文落地页。
- `/little-elsewhere/privacy`、`/little-elsewhere/terms`：完整中文 V2 原文，显著标注原文的草稿状态。
- `/little-elsewhere/en/privacy`、`/little-elsewhere/en/terms`：英文状态说明和中文原文入口。英文导航返回英文产品页；切换语言保持当前文档类型。

法律页采用目录 `index.html`，GitHub Pages 及本地服务器会将无尾斜杠入口重定向到带斜杠目录。无需 SPA 回退规则，刷新无需登录。按需求 canonical 和 hreflang 使用 `https://jevaiworks.com/`；现有 CNAME 是 `www.jevaiworks.com`，实际托管域名跳转保持现状，部署后需核对裸域到 www 的行为。

## 维护

- 修改 `tools/build-little-elsewhere.py` 中的 `COPY` 文案、`BETA` 链接和模板，再执行 `python tools/build-little-elsewhere.py`。
- 构建脚本仅使用 Python 标准库，输出可直接发布的八个静态页面，不需安装依赖。帮助页文案位于 `tools/little_elsewhere_support.py`。
- 产品样式与语言记录逻辑：`little-elsewhere/product.css`、`product.js`。语言由 URL 明确指定，每次访问保存到本地存储，不将中文入口自动跳转为英文。关闭 JS 或拒绝存储时导航仍可用。
- 法律原文：`little-elsewhere/legal-source/` 中两个原始中文文件（字节一致复制）。取得新的正式原文后替换并重新生成；不要直接修改生成后的 HTML。
- 英文译稿：同目录 `privacy.en.draft.md` 和 `terms.en.draft.md`，仅供审阅，未接入页面，也不声称具备法律效力。公司法定名称保留中文，未虚构英文登记名称。
- 发布使用静态仓库根目录；不需要先安装 Python 或运行构建才能提供网页服务。

## 素材

实际查看了根层全部 23 张 PNG；选用 hero1、hero2、icon、prefocus_cn/en、caught a fish_cn/en、focus_new、focus_night_moon、focus_rainbow_morning、music。未使用包含营销标题的 frame 组合图，避免文案叠加。

转为 WebP，横图最长 1600px、竖图最长 1300px，质量 88；适用的横图提供 800px 版本（质量 86）。发布目录 `assets/little-elsewhere/redesign/` 共约 1.96 MiB。保留原始色彩。图像声明尺寸、首屏优先加载、其余懒加载。未使用 AI 或图库替代素材。

现有 TestFlight 链接 `https://testflight.apple.com/join/Uk9rZz5B` 经直接 HTTPS 请求返回 200，标题为“Join the 别境 beta”。仅校验邀请页，没有加入测试或安装 App；名额、设备资格和邀请有效性仍以用户打开时的 Apple 页面为准。

## 法律发布前待审阅

完整来源：

- `D:\02 AO建外人\0 小店\FishFocus\00 current\documents\Little_Elsewhere_隐私政策_V2.md`
- `D:\02 AO建外人\0 小店\FishFocus\00 current\documents\Little_Elsewhere_用户服务协议_V2.md`

V2 原文明确写明“2026年11月2日（修订草稿，非正式生效日期）”，生效日期仍为空。所有原始发布前确认注释均已保留；页面不会将其表示为正式生效文件。发布前需要确认 SDK 地区分流、具体采集清单、后台实际保留期限、跨境链路、隐私开关 UI 路径、儿童保护安排、续费前五日提醒、漂流瓶公开分享机制。

对本机 App 代码的定点只读核对发现：

1. `apps/mobile/src/privacy/policy-text.ts` 仍标为待审草稿（版本 1），不是获批英文 V2。该文件披露 Umeng U-App、U-APM 及 Woodpecker/啄木鸟，V2 清单仅列友盟移动统计、PostHog、Sentry。需统一实际 SDK 披露。
2. `apps/mobile/src/telemetry/telemetry.ts` 的注释写明 `umeng-adapter.ts` 是唯一实现；本次核对未验证 V2 所述境外 PostHog/Sentry 分流。不能将计划当作已经上线的实现。
3. `apps/mobile/src/platform/privacy-preferences.ts` 和遥测接口存在同意/撤回控制，默认 shareUsage=false；开关称为“Help improve Little Elsewhere”，与 V2 的“设置 → 隐私 → 使用数据分析”路径需核实。代码存在控制不代表已验证打包后所有原生 SDK 行为。
4. 现有 App 政策的保留期限仍为待确认项，网站没有自行填入 180/90 天。账号、本地记录、会员、提醒、权限的最终行为应由正式 App 版本和后台配置核准；本次没有运行或改动 App。

这些属于来源差异和待确认事项，未据此重写条款，也未给出新的法律结论。

## 验证

- `python tools/build-little-elsewhere.py`
- `node tools/check.mjs`：覆盖 11 页和本地资源/锚点。
- 启动 `node tools/preview.mjs` 后执行 `python tools/check-little-elsewhere.py`：两份法律全文字符一致、六路由直达/重复请求及目录跳转、公司页面与 HEAD 一致。
- `node --check little-elsewhere/product.js`、`node --check tools/check.mjs`。
- `git diff --check`。
- 浏览器检查中英文页面、语言切换、英文政策回退、中文法律页、FAQ 交互及桌面/平板/手机布局；实测宽度 320、375、390、768、1440px，未发现页面横向溢出；六个入口也在浏览器中逐一刷新，图片无损坏；FAQ 展开正常。

当前项目没有 TypeScript 或 lint 配置，故无对应命令。所有交付保留在本地，未提交、推送、修改 DNS 或部署。正式上线仍需完成法律待审项并按现有 GitHub Pages 流程发布，随后复验生产域名和所有路由。
