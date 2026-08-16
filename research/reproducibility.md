# Reproducibility Checklist

一份可重現的 VAD-Benchmark study 應讓第三方能回答：你測了什麼、用什麼版本、給了什麼素材、允許哪些工具、怎麼評分、哪些資料被排除、如何重算結果。

## Required Artifacts

- preregistration / study config
- task pack version + input hashes
- condition definitions
- model fingerprints
- upstream commit SHAs
- raw run records
- scoring rubric
- blind scores
- processed summaries
- analysis commands / code version
- protocol deviations

## Reproduction Levels

1. **Run reproduction**：同一 task/condition/model 環境可再跑。
2. **Protocol replication**：不同時間重複同一 protocol。
3. **Cross-model replication**：其他模型在等價能力下測試。
4. **Cross-task replication**：至少三類 task family。
5. **External replication**：由非原開發團隊執行。

報告不得把 Level 1 pilot 宣稱成 Level 5 外部驗證。
