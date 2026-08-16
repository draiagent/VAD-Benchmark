# VAD-Benchmark｜Visual Agent Design Evidence & Evaluation Lab

> **把 VAD 從方法論變成可重複驗證、跨模型比較、量化追蹤的證據系統。**

**版本：0.1.0**  
**定位：Cross-model Benchmark / Evaluation / Reproducibility / Human–AI Collaboration Research**

VAD-Benchmark 是 Visual Agent Design 生態系的 **Evidence Layer**。它不重新定義 VAD Core，也不複製 Promptless 實作；它用可重複的研究設計與工程化紀錄回答三個問題：VAD 是否提升任務品質？VAD-Promptless 是否降低提示詞與操作負擔？這些效果能否跨模型與跨任務被重複驗證？

## Ecosystem Role

```mermaid
flowchart TD
    VAD[Visual-Agent-Design\nCore / Standard] --> BENCH[VAD-Benchmark\nEvidence / Evaluation]
    VAD --> PROMPT[VAD-Promptless\nInteraction / Implementation]
    PROMPT --> BENCH
    BENCH --> EVIDENCE[Cross-Model Evidence]
```

- **Visual-Agent-Design**：TRC-3D、VAC-8、Five-Pack、VAD Agent Blueprint、Core QA / Research。
- **VAD-Promptless**：Zero Prompting、Self-Describing Visual Card、Machine Layer、Integrity。
- **VAD-Benchmark**：實驗條件、紀錄、評分、跨模型比較與可重現性。

> **Source-of-truth：VAD Core 只以上游 `draiagent/Visual-Agent-Design` 為準；Promptless 行為只以上游 `draiagent/VAD-Promptless` 為準。**

## Benchmark Conditions

VAD Core 主實驗保留 A–F：A 純文字 Prompt、B VAC、C VAC + minimal text、D 等資訊量文字 SOP、E decorative card、F TRC-3D + VAC + Agent。

另設 Promptless Extension：P0 傳統完整 Prompt、P1 Self-Describing Card + Zero-Prompt launch、P2 Self-Describing Card + minimal override。

## Standard Tasks

Five-Pack 與 VAD Core 對齊：`video`、`slides`、`web`、`data`、`report`。每個 Task Pack 必須固定素材、輸出規格、驗收規則、時間限制與工具權限。

## Primary Metrics

Completion Rate、First-Pass Yield、Revision Count、Human Active Time、Agent Wait Time、Weighted Error (`Critical×5 + Major×3 + Minor`)、Consistency、Routing Accuracy、Prompt Characters / Turns、TUS-VA、HASTU、Satisfaction。

詳見 [`METRICS.md`](METRICS.md)。

## Reproducibility Contract

每次正式 run 至少保存 study/run ID、condition、task、模型指紋、VAD/Promptless commit SHA、工具權限、input hash、時間戳、raw interaction、驗收結果、錯誤數、人工/Agent 時間與 final status。**Raw results 不覆寫。**

## Pinned Baseline for v0.1.0

- Visual-Agent-Design v1.0.0: `9781df292270ec9c2abbec911d3263f245974fa7`
- VAD-Promptless v0.5.0: `304537ad22437050598a956bfab0ed24169452a4`

詳見 [`UPSTREAMS.md`](UPSTREAMS.md)。

## Quick Start

```bash
python -m pip install jsonschema
python scripts/validate_study.py --config configs/study-v0.1.0.json --run examples/sample-run.json
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/score.py examples/sample-run.json
```

## Evidence Policy

不得捏造 benchmark 結果、不得用單一漂亮案例代表整體效果、不得把探索性 composite score 當成已驗證標準。跨模型比較必須揭露模型版本、工具權限與條件差異。正式學術研究仍需依研究倫理、樣本數估算與統計分析計畫執行。

## License

MIT License。

> **VAD 定義工作；VAD-Promptless 降低啟動摩擦；VAD-Benchmark 建立證據。**
