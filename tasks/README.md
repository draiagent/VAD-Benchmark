# Task Packs｜Five-Pack Pilot Lab

VAD-Benchmark v0.2.0 將與 Visual-Agent-Design 對齊的五類任務正式封裝為可驗證 Pilot Task Packs：`video`、`slides`、`web`、`data`、`report`。

## v0.2.0 Canonical Packs

| Task ID | Family | File | Upstream VAC |
|---|---|---|---|
| `PILOT-VIDEO-001` | video | `video/pilot-v1.0.json` | `VAC-VIDEO-001` |
| `PILOT-SLIDE-001` | slides | `slides/pilot-v1.0.json` | `VAC-SLIDE-001` |
| `PILOT-WEB-001` | web | `web/pilot-v1.0.json` | `VAC-WEB-001` |
| `PILOT-DATA-001` | data | `data/pilot-v1.0.json` | `VAC-DATA-001` |
| `PILOT-REPORT-001` | report | `report/pilot-v1.0.json` | `VAC-REPORT-001` |

結構由 `../schemas/task-pack.schema.json` 驗證。

## Task Pack Contract

每個 pack 必須固定：

```text
task_id
version
task_family
upstream_card (repo/ref/path)
goal
inputs + source policy
output_specification
acceptance_criteria + severity
allowed_tools
time_limit_minutes
reference_route
scoring_notes
```

## Fixtures

公開合成素材位於 `../fixtures/`。`repo_fixture` 必須存在於 Repo；`operator_fixed_asset`（例如影片 binary）可放在外部，但正式執行前必須凍結並記錄 SHA-256。

## Versioning

素材、Acceptance Criteria、時間限制或必要工具只要有實質改變，就建立新 task pack version。舊 run 不回寫，也不可把新版 pack 套回舊結果重新命名。

## Five-Pack Alignment

Task Pack 不重新定義 VAC。Card ID、核心任務與限制以上游 `draiagent/Visual-Agent-Design` pinned commit 為準；本 Repo 負責把它轉成固定 Pilot 輸入、評分與執行 contract。

## Fairness

不同 condition 使用相同 task pack、fixture、acceptance contract 與可比的工具權限。若某平台缺少必要媒體或輸出能力，標記 `capability_mismatch`，不要替它換較簡單任務。

## Validation

```bash
python scripts/validate_task_packs.py --config configs/study-v0.2.0.json
```

> **Task Pack 的目的不是讓任務變簡單，而是讓比較變公平。**
