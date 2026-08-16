# Changelog

## 0.2.0 - 2026-08-16

### Five-Pack Pilot Lab

- 建立 `PILOT-LAB.md`，將 benchmark 從架構層推進到可執行 Pilot。
- 建立 Five-Pack canonical task packs：video / slides / web / data / report。
- 建立 `task-pack.schema.json` 與自動驗證器。
- 建立公開合成 fixtures：簡報、網站、數據、報告，以及影片固定建立規則。
- 建立 neutral `VAD BENCHMARK` SVG mark，避免品牌風格成為不必要變因。
- 固定 A–F 與 P0–P2 condition handling，防止 condition leakage。
- 建立 deterministic pilot matrix builder，可依 track / model / replicate 產生 run plan。
- 建立 Task Pack / matrix regression tests。
- 建立 Pilot Visual Evidence Scorecard，要求顯示 context、n、metric direction、evidence status 與 limitations。
- CI 升級：同時驗證 v0.1 foundation 與 v0.2 Pilot Lab config、Five-Pack packs、tests 與 matrix generation。

## 0.1.0 - 2026-08-16

### Foundation

- 建立 VAD-Benchmark 作為 Visual Agent Design 生態系的 Evidence / Evaluation Layer。
- 建立 VAD Core A–F 六組 benchmark 與 Promptless P0–P2 extension。
- 固定 Five-Pack task families：video / slides / web / data / report。
- 建立 upstream source-of-truth / pinned commit contract。
- 建立 run-record JSON Schema、canonical study config 與 sample run。
- 建立 completion、first-pass、revision、weighted error、time、prompt burden 等計分工具。
- 建立 TUS-VA、HASTU pilot instruments 與跨任務 performance rubric。
- 建立 reproducibility / preregistration 文件與 raw-result immutability 規則。
- 建立 GitHub-native Visual Evidence System。
- 建立 ChatGPT / Codex / Claude / Gemini benchmark entry rules。
- 建立 CI：config/schema validation、unit tests、scoring 與 aggregation smoke tests。
