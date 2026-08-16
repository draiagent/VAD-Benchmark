# Datasets

本目錄放 benchmark 用的可公開或可合法分享資料說明，不直接假設任何真實資料可以公開。

## Dataset Rules

- 每個資料集要有來源、授權、版本、hash 與使用限制。
- 個資、商業機密、受限資料不得直接提交到 public repo。
- 若 benchmark 需要受限資料，只提交 manifest / synthetic substitute / reproduction instructions。
- 同一 study 的 task pack 必須引用固定 dataset version。

## Suggested Layout

```text
datasets/
├── manifests/
├── synthetic/
└── README.md
```

Raw user/company data 不應因 benchmark 方便而被公開。
