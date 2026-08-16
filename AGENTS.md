# AGENTS.md｜VAD-Benchmark Agent Rules

本 Repository 是 Visual Agent Design 生態系的 **Evidence / Evaluation Layer**。

## Source of Truth

- VAD Core：`https://github.com/draiagent/Visual-Agent-Design`
- Promptless implementation：`https://github.com/draiagent/VAD-Promptless`

本 Repo **不得重新定義** TRC-3D、VAC-8、Standard VAC Five-Pack、VAD Agent Blueprint 或 Promptless protocol。若需使用，應記錄上游 commit SHA。

## Required Order

1. 讀 `UPSTREAMS.md`
2. 讀 `BENCHMARK.md`
3. v0.2 Pilot 任務再讀 `PILOT-LAB.md`
4. 讀 `PROTOCOL.md` 與 `METRICS.md`
5. 依任務載入 `tasks/<family>/pilot-v1.0.json`
6. 讀 `conditions/PILOT-CONDITIONS.md`
7. 依需求讀 `rubrics/` 與 `visuals/PILOT-SCORECARD.md`
8. 寫入結果前驗證 `schemas/run-record.schema.json`

## Pilot Task Rules

- v0.2.0 正式 Pilot 只使用 `configs/study-v0.2.0.json` 列出的 Five-Pack Task Packs。
- `repo_fixture` 必須使用 Repo 內指定檔案；不得臨時換內容。
- `operator_fixed_asset` 必須在執行前凍結 SHA-256，所有可比較 run 使用同一資產。
- Acceptance Criteria 在 A–F / P0–P2 間保持不變。
- condition 只能改變任務介面或啟動方式，不得改變目標、素材、時間或完成條件。
- 先執行 `scripts/validate_task_packs.py`；未通過不得開始 Pilot。

## Evidence Rules

- 不捏造 benchmark 結果。
- Raw run 不覆寫；重跑必須建立新 `run_id`。
- 不把模型名稱當成固定能力假設；記錄實際 provider / model / version / date / tool access。
- 不因某次失敗自行刪除樣本；排除必須符合預註冊條件並保留原因。
- A–F 的主要比較不得偷偷改變素材、驗收標準或工具權限。
- Promptless P0/P1/P2 extension 與 VAD A–F 主實驗分開分析。
- 能力不等價時記錄 `capability_mismatch`，不得替某模型降低任務難度。
- 高風險或不可逆外部行為不屬於本 benchmark 的預設自動執行範圍。

## Execution Flow

```text
Study Config
→ Validate Upstreams
→ Validate Task Packs
→ Freeze Fixture Hashes
→ Build Pilot Matrix
→ Load Task Pack
→ Assign Condition
→ Fingerprint Model / Tools
→ Execute
→ Save Raw Record
→ Blind Score
→ Compute Metrics
→ Aggregate
→ Report uncertainty / limitations
```

## Completion Check

完成任何 benchmark 任務前確認：資料可追溯、條件一致、計分公式可重算、結果沒有超出證據範圍、上游版本已記錄、Evidence maturity 標示正確。
