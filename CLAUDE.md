# CLAUDE.md｜VAD-Benchmark Entry

本 Repo 是 Evidence / Evaluation layer，不是 VAD Core fork。

執行 v0.2 Pilot 前讀：`AGENTS.md` → `UPSTREAMS.md` → `BENCHMARK.md` → `PILOT-LAB.md` → `PROTOCOL.md` → `METRICS.md` → 對應 `tasks/<family>/pilot-v1.0.json`。

固定原則：Task Pack / fixture / Acceptance Criteria 不偷改、conditions 不偷改、binary input 保存 SHA-256、模型/工具版本可追溯、raw run 不覆寫、評分盲化、錯誤與排除原因保留。必要能力不存在時記錄 `capability_mismatch`，不得替模型降低任務或虛構未執行成績。VAD Core 與 Promptless protocol 分別以上游官方 Repo 為唯一標準來源。
