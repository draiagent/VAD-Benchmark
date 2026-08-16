# CHATGPT.md｜VAD-Benchmark Entry

使用本 Repo 進行 benchmark 時：

1. 先讀 `AGENTS.md`、`UPSTREAMS.md`、`BENCHMARK.md`、`PROTOCOL.md`。
2. 不自行改寫 A–F 或 P0–P2 condition。
3. 任何模型比較都保存 provider / model / version / platform / tool access。
4. 原始 run 不覆寫；修正建立新 run。
5. 評分依 task acceptance contract 與 `rubrics/`，不要因模型品牌調整標準。
6. 不能實際執行的模型不得生成虛構 benchmark 成績。
7. VAD Core 與 Promptless 定義分別以上游兩個 Repo 為準。

> Benchmark 的任務是建立可重算的證據，不是替模型或方法製造漂亮排名。
