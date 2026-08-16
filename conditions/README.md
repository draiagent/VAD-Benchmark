# Conditions

## VAD Core A–F

- `A`：素材 + 純文字 Prompt，baseline。
- `B`：素材 + VAC，測 visual structure。
- `C`：素材 + VAC + minimal text，測精準補充。
- `D`：素材 + 等資訊量文字 SOP，控制資訊完整度。
- `E`：素材 + decorative card，控制純美觀效果。
- `F`：TRC-3D + VAC + Agent，測完整 VAD。

主要 contrast：`B vs D`、`C vs B`、`F vs C`。

## Promptless Extension P0–P2

- `P0`：傳統完整 Prompt 組裝。
- `P1`：Self-Describing Visual Card + Zero-Prompt launch。
- `P2`：Self-Describing Visual Card + minimal override。

Promptless extension 與 A–F 分開分析，避免把 VAD Core 效果與互動摩擦混為同一因果問題。

所有 condition 的資訊內容、工具權限與時間窗需由 study config 固定；偏差必須記錄。
