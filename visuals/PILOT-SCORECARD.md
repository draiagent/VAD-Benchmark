# Pilot Visual Evidence Scorecard

> **Visual design must clarify evidence, not decorate uncertainty.**

本模板用於 VAD-Benchmark v0.2.0 的公開 Pilot 圖卡、README 圖表或研究簡報。它不是成績排行榜模板，而是 Evidence Card。

## 1. 固定資訊層級

```text
01 STUDY CONTEXT
   benchmark version / upstream refs / date

02 COMPARISON
   task / condition / model fingerprint / n

03 PRIMARY OUTCOMES
   completion / first-pass / revisions / weighted error / human time

04 INTERACTION OUTCOMES
   prompt chars / prompt turns / clarification turns

05 EVIDENCE STATUS
   PILOT / REPLICATED / CROSS-MODEL / CROSS-TASK / EXTERNAL

06 LIMITATIONS
   capability mismatch / sample size / platform differences / missing data
```

## 2. 視覺原則

- 先顯示「比較條件」，再顯示分數。
- 所有百分比旁必須能找到 `n`。
- 不使用 3D 長條圖、誇張儀表板或無基準的雷達圖暗示精確排名。
- 正向指標與負向指標必須標示方向，例如 `↑ Completion`、`↓ Weighted Error`。
- 若模型能力不等價，卡片上直接顯示 `CAPABILITY MISMATCH`。
- Pilot 結果不得使用「Winner」「Best Model」「Proven」等超出證據範圍的字樣。

## 3. 建議卡片骨架

```text
┌─────────────────────────────────────────────┐
│ VAD-BENCHMARK · PILOT                       │
│ Task: DATA · Track: VAD · n=__             │
├─────────────────────────────────────────────┤
│ Comparison                                  │
│ B: VAC              vs D: Text SOP          │
├──────────────────────┬──────────────────────┤
│ ↑ Completion         │ ↑ First-Pass         │
│ __%                  │ __%                  │
├──────────────────────┼──────────────────────┤
│ ↓ Revisions          │ ↓ Weighted Error     │
│ __                   │ __                   │
├──────────────────────┼──────────────────────┤
│ ↓ Human Time         │ ↓ Prompt Chars       │
│ __ sec               │ __ chars             │
├─────────────────────────────────────────────┤
│ Evidence: PILOT · Model: ____@____          │
│ Limitations: _____________________________  │
└─────────────────────────────────────────────┘
```

## 4. Cross-Model Matrix

列：task family；欄：model fingerprint。每個 cell 應顯示同一 primary metric，不能在不同 cell 偷換指標。

若要比較 condition，使用 small multiples：每張圖只比較一個主要 contrast，例如 B vs D；不要把 A–F 全塞成一張難以理解的彩色排名圖。

## 5. Evidence Maturity

```text
PILOT
  ↓
REPLICATED
  ↓
CROSS-MODEL
  ↓
CROSS-TASK
  ↓
EXTERNAL
```

只有達到相應條件才升級標籤。Evidence status 是研究成熟度，不是視覺裝飾。

## 6. Export Checklist

公開前檢查：study/version/ref、task、condition、model/version、n、metric direction、限制、日期、是否為 synthetic fixture、是否有 capability mismatch。
