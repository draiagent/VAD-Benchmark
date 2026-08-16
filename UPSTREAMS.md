# UPSTREAMS.md｜Source-of-Truth & Compatibility Contract

VAD-Benchmark 是 consumer / evaluator，不是新的核心標準來源。

## Authoritative Upstreams

| Upstream | Responsibility | v0.2.0 pinned ref |
|---|---|---|
| `draiagent/Visual-Agent-Design` | TRC-3D、VAC-8、Five-Pack、Agent Blueprint、Core QA / Research | `9781df292270ec9c2abbec911d3263f245974fa7` |
| `draiagent/VAD-Promptless` | Promptless UX、Self-Describing Card、Machine Layer、Integrity / Binding | `304537ad22437050598a956bfab0ed24169452a4` |

v0.2.0 Five-Pack Pilot Lab 沿用與 v0.1.0 相同的兩個 pinned refs，目的在於先凍結 benchmark 變因。Task Packs 不改寫上游標準，只固定 Pilot fixture、output contract 與 acceptance scoring。

## Compatibility Rules

1. 正式 study 必須 pin commit SHA，不可只記 `main`。
2. 若 upstream 升級，建立新的 study config 或 benchmark release，不回寫舊結果。
3. 不複製上游 schema 後自行修改名稱卻仍宣稱相容。
4. Benchmark 專用 schema 只描述「實驗紀錄 / task pack」，不重新描述 VAC 或 Promptless protocol。
5. 若上游規格互相不一致，停止 benchmark run，先記錄 dependency conflict。
6. Pilot Task Pack 的 `upstream_card.ref` 必須與 study config 的 `vad_core_ref` 完全一致。

## Provenance Fields

每次 run 至少記錄：

```text
vad_core_repo
vad_core_ref
promptless_repo
promptless_ref
benchmark_version
study_config_version
task_id
task_pack_version
```

P0 或不使用 Promptless 的條件可將 Promptless 使用狀態標為 `not_applicable`，但 study provenance 仍應保存 pinned ref，讓整個研究環境可重建。
