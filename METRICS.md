# METRICS.md｜Metric Definitions

## Objective Metrics

### Completion Rate

`passed_acceptance_items / total_acceptance_items × 100`

### First-Pass Yield

第一次正式輸出即通過全部 required acceptance items：1；否則 0。

### Revision Count

每一次實質內容、規格或方法修正要求記 1 次。單純確認、下載或系統錯誤重試不計。

### Time

- `human_active_seconds`：人類閱讀、輸入、選擇、修正的主動時間。
- `agent_wait_seconds`：等待模型/工具執行時間。
- `wall_clock_seconds`：整體經過時間。

### Weighted Error

`critical_errors × 5 + major_errors × 3 + minor_errors`

Critical = 使成果無法使用或違反必要條件；Major = 明顯影響品質/驗收；Minor = 不影響核心可用性的局部問題。

### Prompt Burden

- `prompt_chars`：使用者為啟動/修正任務輸入的字元總數。
- `prompt_turns`：需要使用者提供指令的回合數。
- `clarification_turns`：Agent 主動要求補充資訊的回合數。

Promptless extension 的主要效率比較可使用：

`prompt_reduction = 1 - condition_prompt_chars / baseline_prompt_chars`

只有 baseline > 0 時才計算。

### Routing Accuracy

TRC-3D / router 的推薦是否與預先定義的 reference route 一致。若 reference 本身不唯一，使用 expert-rated appropriateness，不強迫二元判定。

### Output Consistency

同 task/condition/model 多次 replicate 的 acceptance、結構與關鍵規格一致程度。v0.1.0 先保存可重算原始欄位，不強制單一公式。

## Subjective / Human-Rated Metrics

- **TUS-VA**：任務理解。
- **HASTU**：人機共享任務理解。
- **Satisfaction**：易用、信任、再使用意願。
- **VAC-QI**：若評估 VAC 品質，量表定義仍以上游 Visual-Agent-Design 為準。

## Primary vs Secondary

每個 study 必須在 `configs/*.json` 指定 `primary_metrics`。看過結果後變更主要指標屬 protocol deviation，必須揭露。

## Exploratory Composite Score

可以建立探索性的 VAD Benchmark Score，但必須：公開權重、保留原始指標、不得宣稱為已驗證常模、不得用 composite 掩蓋某項嚴重失敗。
