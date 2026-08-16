# PILOT-DATA-001 Data Dictionary

本資料為完全合成之 Benchmark 測試資料。

| Field | Type | Meaning | Unit |
|---|---|---|---|
| `month` | YYYY-MM | 月份 | month |
| `region` | category | 區域：North / South | — |
| `channel` | category | 通路：Online / Partner | — |
| `orders` | integer | 訂單數 | orders |
| `revenue` | integer | 營收 | synthetic currency units |
| `cost` | integer | 直接成本 | synthetic currency units |
| `returns` | integer | 退貨訂單數 | orders |

## Analysis Question

請分析 2026-01 至 2026-06 的：

1. 總營收與月度成長趨勢。
2. North / South 的營收與毛利差異。
3. Online / Partner 的訂單與退貨率差異。
4. 至少 3 張核心圖表。
5. 提出 3 項只根據資料證據得出的管理洞察，並明確列出資料限制。

## Definitions

- `gross_profit = revenue - cost`
- `gross_margin = gross_profit / revenue`
- `return_rate = returns / orders`

不得自行把這些合成數據解讀成真實產業資料，也不得引入檔案之外的公司背景。
