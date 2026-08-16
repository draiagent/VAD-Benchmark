# Results

```text
results/
├── raw/        # immutable run records
├── processed/  # derived summaries
└── reports/    # human-readable evidence reports
```

## Rule: Raw Is Immutable

`results/raw/` 的正式 run 一旦寫入，不覆寫。若發現錯誤：

1. 保留原 run。
2. 建立 correction / exclusion record。
3. 必要時建立新的 run ID。
4. processed summary 明確標記排除與原因。

## Public Result Policy

任何公開排名或結論都要附：study ID、n、task distribution、model fingerprint、condition、benchmark version、upstream refs 與限制。

沒有實際執行的模型不得出現在真實排行榜中。`examples/` 的資料只能標示為 example / synthetic。
