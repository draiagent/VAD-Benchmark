# Pilot Condition Handling｜A–F / P0–P2

此文件規範 v0.2.0 Pilot 執行時如何避免 condition leakage。任務本體、素材與 Acceptance Criteria 來自同一 Task Pack；condition 只能改變「任務介面 / 啟動方式」，不能偷偷改變完成標準。

## VAD Track

| ID | 允許介面 | 禁止 |
|---|---|---|
| A | 素材 + 一般純文字 Prompt | 顯示 VAC 版面、TRC-3D 結果或 Agent 藍圖 |
| B | 素材 + VAC | 額外加入超出卡片內容的長文字 SOP |
| C | 素材 + VAC + ≤100 字 minimal text | 把 minimal text 寫成另一份完整 SOP |
| D | 素材 + 與 VAC 核心資訊等值的文字 SOP | 使用 VAC 圖像結構 |
| E | 素材 + decorative card | decorative card 不得攜帶可執行 VAC-8 結構 |
| F | TRC-3D + VAC + Agent | 不得替換 task pack 或降低 Acceptance Criteria |

### B vs D

兩組應盡量保持資訊量與語意內容等值；主要差異是 **visual structure**，不是 B 組資訊更多。

### C vs B

C 組只允許少量 override / precision supplement。上限由 study config 的 `minimal_text_max_chars` 定義。

### F vs C

F 組增加的是路由與 Agent 動態執行能力；不能同時給更多素材或更寬鬆時間。

## Promptless Track

| ID | 啟動方式 | 核心測量 |
|---|---|---|
| P0 | 使用者自行組裝完整 Prompt | baseline prompt burden |
| P1 | Self-Describing Visual Card，零額外 Prompt 啟動 | zero-prompt launch |
| P2 | Self-Describing Visual Card + minimal override | precision vs interaction cost |

P1 / P2 的 Self-Describing protocol 以上游 `draiagent/VAD-Promptless` pinned ref 為準，本 Repo 不重新定義 protocol。

## Cross-Condition Freeze

所有 condition 必須固定：

- 同一 Task Pack version
- 同一 input fixture / binary hash
- 同一 output contract
- 同一 acceptance criteria
- 同一最大 revision 次數
- 可比的 tool access
- 相同或事先規範的時間限制

若平台差異導致工具能力不等價，記錄 `capability_mismatch`，不要默默補工具或換任務。

## Human Assistance

主持人只能依預先定義逐字規則回答程序問題，不得針對某一 condition 額外提示如何完成任務。所有實質協助都應記錄為 interaction / clarification event。
