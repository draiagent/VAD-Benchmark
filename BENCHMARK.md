# BENCHMARK.md｜Benchmark Design

## 1. Purpose

VAD-Benchmark 將「方法有效嗎？」拆成可測量問題：視覺結構效果、少量文字補充效果、任務路由效果、Promptless 啟動摩擦、跨模型穩定性與跨任務遷移。

## 2. VAD Core Conditions A–F

| ID | Interface | Main contrast |
|---|---|---|
| A | 素材 + 純文字 Prompt | baseline |
| B | 素材 + VAC | B vs D：visual structure |
| C | 素材 + VAC + minimal text | C vs B：precision supplement |
| D | 素材 + 等資訊量文字 SOP | information-equivalence control |
| E | 素材 + decorative card | aesthetic-only control |
| F | TRC-3D + VAC + Agent | F vs C：routing / agent effect |

A–F 定義與上游 Visual-Agent-Design 研究協議一致。本 Repo 只負責執行與紀錄。

## 3. Promptless Extension P0–P2

為避免把 Promptless 效果混入 VAD 主實驗，另設 extension：

- **P0**：使用者自行組裝完整 Prompt。
- **P1**：Self-Describing Visual Card，零額外 Prompt 啟動。
- **P2**：Self-Describing Visual Card + 預先限制的 minimal override。

主要比較：P1 vs P0 測 Prompt burden；P2 vs P1 測少量 override 是否改善精準度而不顯著增加操作成本。

## 4. Standard Task Families

`video / slides / web / data / report`

每類任務需建立 Task Pack：固定素材、任務目標、輸出規格、Acceptance Criteria、Critical inputs、允許工具、時間限制與評分表。

## 5. Unit of Analysis

最小單位為一個 `run`：一個固定 task pack × 一個 condition × 一個 model fingerprint × 一次執行。

同一模型重複執行時必須建立不同 `run_id`。若研究設計允許多次 sampling，必須事先固定 replicate 數。

## 6. Cross-Model Fairness

跨模型比較原則：相同素材、相同 acceptance contract、等價工具權限、相同時間窗、清空或標準化對話狀態。若平台能力無法等價，標記 `capability_mismatch`，不可直接宣稱模型能力差異。

## 7. Main Outcomes

主要 outcome 應在 study config 預先指定，不應看到結果後才選最有利指標。建議至少包含 completion rate、first-pass yield、revision count、weighted error、human active time。

TUS-VA、HASTU、滿意度與 Prompt burden 作為重要次要指標。

## 8. Reporting Rule

報告必須同時呈現平均值/中位數、樣本數、變異與限制。探索性 composite score 可以使用，但不得取代主要終點，也不得包裝成已驗證常模。
