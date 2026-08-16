# Pilot Fixtures

本資料夾存放 VAD-Benchmark v0.2.0 Five-Pack Pilot 的固定公開素材。目標是讓不同 condition 與不同模型使用相同輸入，不因素材差異污染比較。

## 原則

- 所有公開文字 / CSV fixture 都是合成資料，不代表真實公司、人物或營運數據。
- 執行前應對實際輸入檔案計算 SHA-256，寫入 run record。
- 不得在不同 condition 間臨時替換素材。
- 若因平台能力限制必須轉檔，需保存原始 hash、轉檔規則與轉檔後 hash。

## Five-Pack

- `video/`：固定逐字稿與二進位原始影片建立規則；真正的 `source.mp4` 由 operator 一次生成/錄製後凍結。
- `slides/`：固定簡報主題資料。
- `web/`：固定虛構專案網站資料。
- `data/`：固定 CSV 與資料字典。
- `report/`：固定會議逐字稿與背景資料。

> Binary media 若未直接進 Git，必須以外部固定資產方式管理，且每個 run 都記錄同一 SHA-256。
