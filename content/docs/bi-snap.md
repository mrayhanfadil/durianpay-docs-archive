---
updatedAt: 2026-09-23T08:23:14.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# BI SNAP

# SNAP vs Legacy API

## What is SNAP?

SNAP (Standar Nasional Open API Pembayaran) is National Standard of Payment API established by Central Bank of Indonesia to build a healthy, competitive and innovative payment industry market; encourage integration, interconnection and interoperability also security and advanced payment infrastructure; and improve an efficient and reasonable market practice in payment activity over Indonesia.

## Why SNAP?

* Standardized security and API format across provider in Indonesia
* Easy interconnection & interoperability to apply other financial service API in Indonesia
* Compliant to Financial Regulation in Indonesia to avoid any future implications in Indonesia (BI require all merchants in Indonesia to use SNAP standard by End of June 2025)

## What is Legacy API?

Before proceeding with SNAP standard for Pay Outs API, Durianpay provide our own API standard and we call this legacy API. It is designed to empower your pay out needs with a strong flexibility to support normal and advanced use case.

## Comparison of SNAP and Legacy API

| Comparison Criteria        | SNAP                                                    | Legacy API                                                            |
| :------------------------- | :------------------------------------------------------ | :-------------------------------------------------------------------- |
| Authentication & Security  | Incorporate Public/Private Key Scheme, B2B Token Access | Live Key                                                              |
| Interoperability           | Across Financial Industry in Indonesia                  | Specific for Durianpay                                                |
| Granularity of transaction | Support item transaction level only for now             | Support Batch transaction which can contain several item transaction. |