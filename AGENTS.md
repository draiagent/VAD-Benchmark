# AGENTS.md｜VAD-Benchmark Agent Rules

本 Repository 是 Visual Agent Design 生態系的 **Evidence / Evaluation Layer**。

## Source of Truth

- VAD Core：`https://github.com/draiagent/Visual-Agent-Design`
- Promptless implementation：`https://github.com/draiagent/VAD-Promptless`

本 Repo **不得重新定義** TRC-3D、VAC-8、Standard VAC Five-Pack、VAD Agent Blueprint 或 Promptless protocol。若需使用，應記錄上游 commit SHA。

## Required Order

1. 讀 `UPSTREAMS.md`
2. 讀 `BENCHMARK.md`
3. 讀 `PROTOCOL.md`
4. 讀 `METRICS.md`
5. 依任務讀 `tasks/`、`conditions/`、`rubrics/`
6. 寫入結果前驗證 `schemas/run-record.schema.json`

## Evidence Rules

- 不捏造 benchmark 結果。
- Raw run 不覆寫；重跑必須建立新 `run_id`。
- 不把模型名稱當成固定能力假設；記錄實際 provider / model / version / date / tool access。
- 不因某次失敗自行刪除樣本；排除必須符合預註冊條件並保留原因。
- A–F 的主要比較不得偷偷改變素材、驗收標準或工具權限。
- Promptless P0/P1/P2 extension 與 VAD A–F 主實驗分開分析。
- 高風險或不可逆外部行為不屬於本 benchmark 的預設自動執行範圍。

## Execution Flow

```text
Study Config
→ Validate Upstreams
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

完成任何 benchmark 任務前確認：資料可追溯、條件一致、計分公式可重算、結果沒有超出證據範圍、上游版本已記錄。
