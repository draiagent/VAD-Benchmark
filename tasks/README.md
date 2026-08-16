# Task Packs

VAD-Benchmark v0.1.0 使用與 Visual-Agent-Design 對齊的五類任務：`video`、`slides`、`web`、`data`、`report`。

## Task Pack Contract

每一個 task pack 必須包含：

```text
task_id
version
task_family
goal
input_manifest
input_hashes
critical_inputs
output_specification
acceptance_criteria
allowed_tools
time_limit
reference_route (if applicable)
scoring_notes
```

## Versioning

素材、Acceptance Criteria、時間限制或必要工具只要有實質改變，就建立新 task pack version。舊 run 不回寫。

## Five-Pack Alignment

若任務直接使用標準 VAC，Card ID 與 VAC 內容以上游 `draiagent/Visual-Agent-Design` 的現行/指定 commit 為準。本 Repo 只記錄 card ID、version/ref 與 benchmark outcome。

## Fairness

不同 condition 應使用相同 task pack。若某模型無法使用必要媒體或工具，標記 `capability_mismatch`，不要自行替它換一個更簡單任務。
