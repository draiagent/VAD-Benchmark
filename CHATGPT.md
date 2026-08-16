# CHATGPT.md｜VAD-Benchmark Entry

使用本 Repo 進行 benchmark 時：

1. 先讀 `AGENTS.md`、`UPSTREAMS.md`、`BENCHMARK.md`；v0.2 Pilot 再讀 `PILOT-LAB.md`。
2. 正式 Pilot 只使用 `configs/study-v0.2.0.json` 列出的 Five-Pack Task Packs。
3. 不自行改寫 A–F 或 P0–P2 condition，也不改 Acceptance Criteria。
4. 任何模型比較都保存 provider / model / version / platform / tool access。
5. `repo_fixture` 使用固定 Repo 檔；binary asset 必須凍結 SHA-256。
6. 原始 run 不覆寫；修正建立新 run。
7. 評分依 task acceptance contract 與 `rubrics/`，不要因模型品牌調整標準。
8. 能力不等價時記錄 `capability_mismatch`；不能實際執行的模型不得生成虛構 benchmark 成績。
9. VAD Core 與 Promptless 定義分別以上游兩個 Repo 為準。
10. 公開視覺結果遵循 `visuals/PILOT-SCORECARD.md`，明示 `n`、模型版本、限制與 Evidence maturity。

> Benchmark 的任務是建立可重算的證據，不是替模型或方法製造漂亮排名。
