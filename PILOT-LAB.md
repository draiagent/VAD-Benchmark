# VAD-Benchmark v0.2.0｜Five-Pack Pilot Lab

> **把「可以評測」推進到「可以用固定任務包開始跑第一批可重現 Pilot」。**

## 1. 目的

v0.2.0 將 v0.1.0 的 Evidence / Evaluation Foundation 落地成 Five-Pack Pilot Lab。此階段不是宣稱 VAD 已被學術驗證，而是建立第一套可固定、可重跑、可盲評、可跨模型比較的工程 Pilot。

## 2. Five-Pack Pilot Tasks

| Task ID | Family | Upstream VAC | 核心交付 |
|---|---|---|---|
| `PILOT-VIDEO-001` | video | `VAC-VIDEO-001` | 45–60 秒 9:16 MP4 |
| `PILOT-SLIDE-001` | slides | `VAC-SLIDE-001` | 10 頁 PPTX + PDF |
| `PILOT-WEB-001` | web | `VAC-WEB-001` | 單頁 RWD 網站 |
| `PILOT-DATA-001` | data | `VAC-DATA-001` | 清理資料 + 至少 3 圖表 + 分析摘要 |
| `PILOT-REPORT-001` | report | `VAC-REPORT-001` | 5–8 頁 DOCX + PDF |

Task Pack 定義位於 `tasks/<family>/pilot-v1.0.json`，結構由 `schemas/task-pack.schema.json` 驗證。

## 3. 兩條 Pilot Track

### Track V｜VAD Core A–F

```text
A  素材 + 純文字 Prompt
B  素材 + VAC
C  素材 + VAC + minimal text
D  素材 + 等資訊量文字 SOP
E  素材 + decorative card
F  TRC-3D + VAC + Agent
```

主要對比：`B vs D`、`C vs B`、`F vs C`。

### Track P｜Promptless P0–P2

```text
P0  Traditional Full Prompt
P1  Self-Describing Visual Card + Zero-Prompt Launch
P2  Self-Describing Visual Card + Minimal Override
```

主要對比：`P1 vs P0` 測 Prompt burden；`P2 vs P1` 測少量 override 對精準度與操作成本的影響。

兩條 Track 分開分析，不把 Promptless 效果混進 VAD Core 主因果比較。

## 4. Pilot Run Contract

每一個 run 必須固定：

- task pack ID / version
- condition
- provider / model / version / platform
- tool access
- upstream VAD / Promptless commit SHA
- input asset hashes
- start/end timestamp
- raw interaction
- final output references
- acceptance item results
- error counts
- revision count
- human active time / agent wait time / wall-clock time
- prompt chars / prompt turns / clarification turns
- exclusion or capability mismatch reason（若有）

Raw run 不覆寫；任何重跑都建立新 `run_id`。

## 5. Pilot Matrix

建議工程 Pilot 先採：

```text
5 task packs
× 2–4 model/platform fingerprints
× A–F（VAD track）
× 每格 2–3 replicates
```

Promptless P0–P2 可獨立跑第二張 matrix。

Pilot 目的先檢查：流程是否可執行、評分規則是否一致、資料欄位是否足夠、跨平台是否存在 capability mismatch。正式研究樣本數不得由 Pilot matrix 直接推定。

## 6. Video Fixture 特別規則

影片任務需要固定二進位原始影片。Repo 不捏造或以不同影片代替。`fixtures/video/README.md` 提供固定腳本與建立規則；正式 Pilot 執行前，研究者需產生一次 `source.mp4`，計算 SHA-256，之後所有 condition / model 必須使用同一份檔案。

其餘文字與 CSV fixture 可直接由 Repo 提供。

## 7. 執行順序

```text
Pin upstream refs
→ Validate study config
→ Validate Five-Pack task packs
→ Freeze fixture hashes
→ Generate pilot matrix
→ Execute run
→ Save raw record
→ Blind acceptance scoring
→ Compute metrics
→ Aggregate by task / condition / model
→ Produce scorecard with limitations
```

## 8. 成功門檻（Pilot Readiness Gate）

v0.2.0 可進入第一批 Pilot 的最低條件：

- 5 個 task packs 全部通過 schema validation
- 所有 repo fixture 路徑存在
- condition 與 task 不互相偷改 acceptance contract
- run-record 可完整保存模型、工具與上游版本
- scoring / aggregation 可重算
- 至少兩位評分者能使用相同 acceptance criteria
- capability mismatch 有明確紀錄方式
- CI 綠燈

## 9. 不應宣稱的內容

Pilot 尚未完成前，不應宣稱：

- VAD 一定優於文字 Prompt
- Promptless 一定降低某個百分比成本
- 某模型在 VAD 上一定最好
- VAC-QI、TUS-VA、HASTU 已具有正式常模

公開內容應標示 `PILOT` / `REPLICATED` / `CROSS-MODEL` 等 Evidence Maturity，避免把早期結果包裝成已驗證結論。

> **v0.2.0 的任務不是做漂亮排行榜，而是建立第一批能被別人重跑的證據。**
