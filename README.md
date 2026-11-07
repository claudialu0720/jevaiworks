# JEVAI WORKS · 界外造物

界外造物创意科技（青岛）有限公司官网。背景使用 cloudesign.space/product/ 线上新版的原始参数：#F7F8FA 底色、三层固定 OKLCH 渐变、26px 点阵、190px 鼠标影响半径，以及发光光标与 BROWSE 标签。保留简洁双语结构，突出数字产品、AI 与设计，包含 Little Elsewhere（别境）独立产品页。

纯静态 HTML / CSS / JavaScript，无安装依赖。字体与图片在本地；网站通过 Google Analytics 4 统计访问数据。Little Elsewhere 页面由 `tools/build-little-elsewhere.py` 生成。

## 网站访问统计（2026-11-03）

- 公司官网首页、网站隐私、条款和 404 页使用 `G-616N96L3W2`（Jevaiworks）。
- `/little-elsewhere/` 下的中英文介绍、法律及支持页面使用 `G-212DEYMSND`（Little Elsewhere）。每页只配置一个 ID，避免向两个流重复发送同一页面浏览。
- 使用 Google 官方异步 `gtag.js`，自动发送页面浏览；滚动、出站点击等由 GA 后台的增强型衡量设置控制。代码关闭 Google signals 和广告个性化信号。
- 产品页生成模板同步保留 Google tag，重新生成页面不会丢失统计代码。网站统计说明见 `/privacy/`；App 法律原文不作为网站统计说明。
- 发布至 GitHub Pages 后，打开正式网址并在 GA 的实时报告或“Test installation”中验证。普通报告可能需要 24–48 小时处理；接入前的访问无法补录。
- 两个数据流若位于同一媒体资源，默认报告可合并展示；按数据流名称或页面路径筛选可分别查看。网站数据流的 URL 字段不会自动限制采集路径，实际归属由各页面的衡量 ID 决定。
- 在本地浏览器预览时，Google tag 也会执行；只检查布局时可屏蔽第三方统计请求，避免测试访问进入报表。

## 本地预览

在本目录打开终端，运行：

```powershell
node tools/preview.mjs
```

访问 http://127.0.0.1:4173/ 。终端按 Ctrl+C 停止。也可以直接打开 index.html 查看首页；完整路由与 404 建议用本地预览。

## 页面

- `index.html`：首页（关于、领域、产品、联系）。
- `little-elsewhere/index.html`：别境产品介绍，以六张当前内测截图呈现专注、声景与发现，提供中英双语 iOS TestFlight 安装指南。
- `/little-elsewhere/support/` 和 `/little-elsewhere/en/support/`：中英文别境帮助页。旧地址 `/support/` 自动跳转到中文帮助页。
- `little-elsewhere/product.css`：产品页独立配色与响应式图文布局，不影响官网其他页面。
- `little-elsewhere/product.js`：点击截图打开原生图片预览弹窗，支持关闭按钮、Esc、点击遮罩关闭和焦点返回；关闭 JavaScript 时图片链接仍可访问。
- `privacy/index.html`：公司官网隐私政策，不是 App 隐私政策。
- `terms/index.html`：公司网站使用条款。
- `404.html`：不存在的地址，按自定义域名根目录运行。
- `styles.css`：公共设计系统与响应式布局。
- `atmosphere.css`：与线上参考一致的渐变、点阵图层和光标样式。
- `script.js`：背景点阵与联系邮箱渲染；直接移植参考页的点阵位移、半径与透明度公式。鼠标邻近点阵放大变紫并轻微外移；触屏不显示光标标签；减少动态效果模式隐藏点阵和光标，保留静态渐变。
- `site.config.js`：公共邮箱配置。

## 发布前需要补充

1. **联系邮箱**：已按站点所有者提供的信息设置为 `hello@jevaiworks.com`，同时写入 `site.config.js` 和首页 `data-contact` 中的 mailto 链接，关闭 JavaScript 时也可使用。以后更换邮箱时同步修改两处；发布前测试邮箱收发。
2. **产品素材**：首页使用当前内测版 `icon.png` 和 `arrival.png` 优化后的 WebP。产品页采用「little elsewhere images」中的六张真实截图，优化为 WebP，并为横屏界面生成 800px 响应式版本。当前 iOS 内测已开放，页面链接到真实 TestFlight 邀请。手机端可点击横屏截图，左右滑动查看放大细节。
3. **产品状态**：当前为「iOS 内测已开放」，邀请地址为 https://testflight.apple.com/join/Uk9rZz5B 。正式上线后更新状态、平台及下载链接，并根据 App 实际数据处理提供独立 App 隐私政策。
4. **对外信息**：`JEVAI WORKS` 是按域名采用的品牌写法；中文完整法人名称已经在首页、页脚和产品页呈现。若需要英文法人名称，请使用与登记 / D-U-N-S 一致的正式名称，不要将品牌名当作英文法人名称。
5. **政策确认**：网站政策按本版静态站实际功能撰写。发布前确认内容；上线后将隐私页中的「计划通过 GitHub Pages 提供」更新为实际托管事实。以后接入分析、表单或其他第三方服务时同步更新政策。

## GitHub Pages 发布

1. 官网仓库为 [claudialu0720/jevaiworks](https://github.com/claudialu0720/jevaiworks)，网站文件位于 `main` 分支根目录。GitHub Free 可使用公开仓库发布 Pages。
2. 仓库 **Settings → Pages → Build and deployment**：Source 选 **Deploy from a branch**，Branch 选 `main` 和 `/(root)`，保存。这里使用分支发布，不需要 GitHub Actions 工作流。
3. **Custom domain** 填 `www.jevaiworks.com`。仓库已附同名 `CNAME`，不要在里面写 `https://`、路径或反斜杠。
4. 在域名服务商 DNS 中添加：类型 **CNAME**，主机 **www**，值为 **claudialu0720.github.io**。这里填账户 Pages 域名，不是仓库名，也不带 https://。
5. 如需裸域 `jevaiworks.com` 也可以访问，给主机 `@` 添加四条 A 记录：`185.199.108.153`、`185.199.109.153`、`185.199.110.153`、`185.199.111.153`。正确配置两端后，GitHub Pages 会将裸域重定向至已选择的 www 域名。
6. 等待 DNS 检查及证书生成完成，在 Pages 中启用 **Enforce HTTPS**。DNS 生效可能需要至多 24 小时。
7. 检查首页、`/little-elsewhere/`、`/privacy/`、`/terms/` 和不存在地址的 404 页面，并实际测试公开邮箱收发。

域名服务商已有同名冲突记录时，只调整相应网站记录，不要覆盖邮箱使用的 MX / SPF / DKIM / DMARC 记录。可先在 GitHub 的 Pages 设置验证域名所有权。

正式网址为 https://www.jevaiworks.com/ 。此交付没有替你创建 GitHub 仓库、修改 DNS 或发布网站。

部署参考：[GitHub 官方自定义域名说明](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)。

## Apple Developer 组织注册

Apple 要求公开可访问且正常工作的组织官网、关联组织的域名和域名工作邮箱；组织还需满足法人资格、D-U-N-S、授权等要求。网站完成不等于组织注册已经获批。

详见 [Apple 官方注册要求](https://developer.apple.com/programs/enroll/)。

## 素材来源

`assets/little-elsewhere-icon.png` 与 `assets/little-elsewhere-world.png` 为用户本地提供的产品素材。`assets/little-elsewhere/` 的五张原始 PNG 来自用户提供的 Figma board 截图：`0 enter.png` → `arrival.png`、`1 home.png` → `lakeside.png`、`2 setting.png` → `prepare.png`、`3 focus.png` → `focus.png`、`4 after focus.png` → `discovery.png`。没有复制合域网站的 Google Analytics 配置、联系信息或项目。

## 产品页素材更新（2026-09-22）

页面使用 arrival、lakeside、focus、ambience、discovery、loot 六张 WebP。ambience 对应 `3.5 focus setting.png`，loot 对应 `4.5 after focus loot.png`；其余对应同名原始 PNG 来源。原始 PNG 保留供后续维护，页面不再加载它们。未提供池塘或收藏界面，因此该部分仅使用简短文案，不制作替代 UI。

页脚 Privacy 与 Terms 仍为现有官网政策；产品专属隐私与帮助页面尚不存在。日后在产品结尾加入真实链接，不将官网政策标为 App 政策。

## 产品页内测更新（2026-10-19）

保留中英双语，缩短产品描述，移除重复的四步功能介绍。首页同步更新产品图标、场景图和 iOS 内测状态。产品页首屏与页尾提供真实 TestFlight 邀请，并新增三步安装说明、反馈方式和加入失败帮助；Apple 官方安装说明见 https://testflight.apple.com/ 。

当前页面使用用户「little elsewhere images」目录根层的新素材（不使用 `ss/` 中的旧图）：`arrival.png`、`lakeside.png`、`focus.png`、`ambience.png`、`dicovery 1.png`、`discovery 2.png`、`icon.png`。发布素材以 `-beta.webp` 命名，横屏同时提供 800px 版本，实际尺寸写入 HTML；全部七张主素材约 0.86 MiB。旧素材保留，页面不再引用旧截图。

内测指南可直接分享 https://www.jevaiworks.com/little-elsewhere/#beta 。当前仅支持 iOS，设备与系统兼容性以 TestFlight 显示为准。产品页未宣称正式上架，也没有虚构 Android 下载入口。

## Little Elsewhere 新版（2026-11-02）

产品页已分为中文和英文独立 URL，并新增 App 专属中英文法律入口。以 [LITTLE-ELSEWHERE-IMPLEMENTATION.md](LITTLE-ELSEWHERE-IMPLEMENTATION.md) 的改版说明、素材清单、构建/检查命令和法律待审事项为准；上文产品页双语并排及“App 法律页尚不存在”等历史描述已由本次实现替代。没有部署生产环境。
