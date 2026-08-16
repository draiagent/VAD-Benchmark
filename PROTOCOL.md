# PROTOCOL.md｜Reproducible Benchmark Protocol

## Phase 0｜Preregister

固定研究問題、主要指標、樣本數/replicate、排除條件、conditions、task packs、模型版本、工具權限、時間限制與統計計畫。

## Phase 1｜Freeze Inputs

對素材包建立 hash；固定檔名、順序、內容與 acceptance contract。任何素材變更都建立新 task pack version。

## Phase 2｜Fingerprint Environment

紀錄：provider、model name/version、平台、日期、temperature/seed（若可用）、vision/file/tool capability、MCP/connector access、系統限制與上游 commit SHA。

## Phase 3｜Assign Condition

依 preregistration 執行隨機化或固定矩陣。不得因模型表現改變後續 condition 配置。

## Phase 4｜Execute

使用標準起始狀態。完整保存所有 user input、assistant output、tool calls、errors、retries 與 timestamps。系統故障重試與內容修正必須分開標記。

## Phase 5｜Freeze Raw Run

run 結束後立刻保存 immutable raw record。若資料缺漏，標記 invalid / incomplete，不在原檔補寫結果。

## Phase 6｜Blind Score

成果評分者不可知道 condition 或模型來源。至少兩位評分者時，分開保存原始評分，再計算一致性。

## Phase 7｜Compute Metrics

使用 `METRICS.md` 與 `scripts/score.py`。公式與原始欄位必須可重算。

## Phase 8｜Aggregate

依 condition / task / model 分組。預設同時回報 mean、median、n；小樣本時避免過度解讀排名。

## Phase 9｜Report

報告必須包含：study config、upstream refs、task pack versions、模型指紋、工具差異、缺失資料、排除原因、主要結果、次要結果、限制與可重現命令。

## Control Rules

- A/B/C/D 核心資訊量盡量等值。
- C 的 minimal text 在 study config 固定上限。
- P2 的 override 也固定上限。
- 修改次數上限與時間上限事先固定。
- 不允許評分者因知道模型品牌而調整標準。
- 跨模型若缺少關鍵能力，記為 capability mismatch，不補給其他模型沒有的額外人工協助。

## Exclusion Rules

可排除情況只包含 preregistered system failure、corrupt input、無法啟動的 capability mismatch、紀錄損毀等。任務做得差不是排除理由。
