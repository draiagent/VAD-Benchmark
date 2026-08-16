# GEMINI.md｜VAD-Benchmark Entry

使用 Gemini CLI / Gemini 平台參與 VAD-Benchmark v0.2.0 時，先遵循 `AGENTS.md`、`UPSTREAMS.md`、`BENCHMARK.md`、`PILOT-LAB.md`、`PROTOCOL.md`、`METRICS.md` 與對應 Task Pack。

不得因平台差異默默改變 task pack、fixture、condition 或 acceptance criteria。Repo fixture 必須原樣使用；binary input 保存 SHA-256。若必要能力不存在，記錄 `capability_mismatch`。每個 run 保存實際模型指紋、工具權限、上游 refs 與原始互動。未實際完成的測試不得產生虛構分數或排行榜；公開結果必須揭露 `n`、限制與 Evidence maturity。
