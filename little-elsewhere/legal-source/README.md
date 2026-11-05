# Little Elsewhere 法律原文

2026-11-05 更新：当前四个 App 法律页面使用用户提供的 V3.2 文档，原文件按字节复制，未改写正文或填写占位内容。checklist 文件未导入。

| 页面 | 当前原文 |
| --- | --- |
| `/little-elsewhere/privacy/` | `Little_Elsewhere_隐私政策_V3.2_2026-11-05.md` |
| `/little-elsewhere/terms/` | `Little_Elsewhere_用户服务协议_V3.2_2026-11-05.md` |
| `/little-elsewhere/en/privacy/` | `Little_Elsewhere_Privacy_Policy_EN_V3.2_2026-11-05.md` |
| `/little-elsewhere/en/terms/` | `Little_Elsewhere_Terms_of_Use_EN_V3.2_2026-11-05.md` |

来源目录：`D:\02 AO建外人\0 小店\FishFocus\00 current\documents`。

四份原文均标为代码核查后的待发布草稿，生效日期尚未填写；隐私政策中的数据保留期限及其他待核实事项按原文保留。页面同步显示草稿提示。此更新不代表对 App 实际行为或法律合规性的独立核验。

执行 `python tools/build-little-elsewhere.py` 重新生成页面。当前文件映射在脚本的 `LEGAL_SOURCES` 中；同目录 V2 文件、旧英文稿仅作历史留存，不再生成到页面。

验证：`node tools/check.mjs`；启动 `node tools/preview.mjs` 后执行 `python tools/check-little-elsewhere.py`，核对中英文四份法律全文、链接、强调、章节及六个页面路由。
