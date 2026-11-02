# Little Elsewhere V3 — 2026-11-02

## 视觉与结构

重新查看 frame1/2/3 中英文宣传图和 hero1/hero2 原始素材。沿用它们的明亮天空、云朵、水面与自然光；采用独立截图重新组织页面，没有直接套用包含营销文案的宣传组合图。

本次不是换色：移除原三列步骤、圆角场景卡及反复的左右分栏，改为五个主要段落与结尾邀请：

1. 抵达：全宽湖景、浅色天空过渡、左侧邀请文字与右侧真实准备界面。手机上重新安排文字、CTA 和较小的界面，保留完整横向湖景。
2. 安顿：白色留白中的准备专注界面，配两点简短说明。
3. 专注：完整比例的全宽瀑布场景，不叠加大段文字。
4. 发现：真实渔获屏幕与水下全景搭配，手机改为居中的独立构图。
5. 探索：彩虹与月夜错位展开，声音界面作为较安静的收尾。
6. 邀请：简短文案、相同 TestFlight CTA 与折叠安装说明，再回到开头的湖景。

背景为云白、浅天蓝，文字使用深蓝青；以低字重、自然字距区分标题和说明。CTA 使用白色/浅水蓝、小圆角、细边框，无深绿色填充和厚重阴影。没有加入动画库、假计时器、追踪、字体服务或新运行时依赖。

所有风景图保留原始比例，以 contain 显示；只在上下边缘使用线性白色渐隐，不裁去船、瀑布、天空或屏幕内容。界面截图保持完整。新增较高分辨率的景观 WebP，源自原始 PNG，非网站截图。

## 本次文件

- `little-elsewhere/index.html`、`little-elsewhere/en/index.html`：更新的中英文落地页。
- `little-elsewhere/landing-v3.css`：仅作用于 `.landing-page` 的新视觉系统和响应式构图。
- `tools/little_elsewhere_landing.py`：V3 双语营销文案与版面模板；今后营销编辑以此为准。
- `tools/build-little-elsewhere.py`：接入独立营销模板，法律生成流程保持原样。
- `assets/little-elsewhere/redesign/{lake-wide,underwater-wide,waterfall-wide}.webp` 及对应 `-1000.webp`：较高分辨率全景素材。

原有 `product.css` 继续提供基础及法律页样式，V3 没有修改它。四个法律 HTML、中文原文与英文译稿均与 V3 开始时字节一致。公司主页及公司法律页未改动。

构建：`python tools/build-little-elsewhere.py`，仅使用 Python 标准库。预览：`node tools/preview.mjs`。

## 验证与迭代

实际检查桌面、平板及手机画面。首轮手机检查发现装饰柔光造成 8px 横向溢出，已收紧该范围；缩短手机首屏及中文准备区标题，避免不自然的换行；将渔获说明移到浅色区域以改善阅读。

最终浏览器检查：

- 中英文各在 1440、1024、390px 检查，均无横向溢出、无已加载图片损坏、无风景比例变形。
- 实际查看全宽湖景、准备界面、瀑布、渔获与水下场景、世界探索的桌面和手机构图。
- 中/EN 切换、原 TestFlight 目标地址、折叠安装说明、法律链接与英文法律回退保留。

静态检查：

- `python tools/build-little-elsewhere.py`：通过。
- `node tools/check.mjs`：11 页，205 个本地链接/资源/锚点通过。
- `python tools/check-little-elsewhere.py`：法律全文、六路由直达及重复加载、目录跳转、公司页面未变检查通过。
- `node --check little-elsewhere/product.js`、`git diff --check`：通过。
- V3 修改前保存的哈希与修改后比对：四个法律页和四个法律原文/译稿均一致。

现有项目没有 lint 或 TypeScript 配置；未新增对应依赖。预览继续在本机运行，未提交、推送或部署生产环境。法律文件此前已注明的待审状态不变。
