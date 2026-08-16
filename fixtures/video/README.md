# Video Pilot Fixture

`PILOT-VIDEO-001` 需要一份固定 3–5 分鐘原始影片。為避免把大型二進位檔直接綁死在 Repo，本版採 **operator_fixed_asset**。

## 固定建立方式

1. 使用 `transcript.md` 的完整文字製作或錄製單一講者影片。
2. 畫面保持固定：單一講者 / 中性背景 / 不加字幕 / 不加 Logo / 不加背景音樂。
3. 影片長度控制 3–5 分鐘，至少 1080p。
4. 檔名固定為 `source.mp4`。
5. 建立後計算 SHA-256；同一 study 的所有模型與 condition 使用完全相同檔案。
6. 若需要轉碼，只允許建立一次標準化版本，並固定該版本 hash。

## 目的

Pilot 要測的是介面與 Agent 執行差異，不是不同攝影素材造成的差異。若無法取得同一份 `source.mp4`，該 run 應標記為不具跨 condition 可比性。
