# Model Adapters & Fingerprints

VAD-Benchmark 不把模型品牌名稱當成固定能力。每次 run 必須記錄實際環境。

## Minimum Fingerprint

```text
provider
model_name
model_version
platform
run_date
vision_capability
file_capability
tool_capability
connector_or_mcp_access
sampling_parameters (if exposed)
system_constraints
```

## Fair Comparison

跨模型比較時優先追求「等價能力條件」，而不是假設所有平台完全相同。若某平台缺少必要能力，標記 `capability_mismatch` 並在報告中分層呈現。

## Adapter Boundary

v0.1.0 不綁定單一 API SDK。模型輸出可以由人工標準化流程、平台匯出或未來的 automated adapters 匯入；但 run record schema 必須一致。

未來 provider adapter 應只處理：啟動、輸入封裝、事件/工具紀錄、輸出匯出。不得在 adapter 內偷偷改寫 condition 或 acceptance criteria。
