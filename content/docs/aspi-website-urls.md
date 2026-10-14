---
updatedAt: 2025-07-31T14:23:53.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# ASPI Website URLs

To make your testing smoother, this table pairs each Durianpay API with its exact match on ASPI’s developer portal. Use it to locate the right simulator on ASPI’s site (currently only available in Bahasa Indonesia) and verify your API flow step by step without confusion.

<br />

| **API**                              | **Durianpay’s API Docs**                                                  | **Endpoint**                                                             | **ASPI’s Simulator URL**                                                                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generate B2B Access Token            | <https://docs.durianpay.id/reference/access-token-b2b>                    | [/v1.0/access-token/b2b](https://api.durianpay.id/v1.0/access-token/b2b) | <https://apidevportal.aspi-indonesia.or.id/api-services/keamanan#/Keamanan/post_api_v1_0_access_token_b2b>                                                           |
| Bank Account Inquiry API             | <https://docs.durianpay.id/reference/bank-account-inquiry-api>            | /v1.0/account-inquiry-external                                           | <https://apidevportal.aspi-indonesia.or.id/api-services/transfer-kredit/account-inquiry#/AccountInquiry/post_api_v1_0_account_inquiry_external>                      |
| Bank Transfer API                    | <https://docs.durianpay.id/reference/bank-transfer-api>                   | /v1.0/transfer-interbank                                                 | <https://apidevportal.aspi-indonesia.or.id/api-services/transfer-kredit/trigger-transfer#/TriggerTransfer/post_api_v1_0_transfer_interbank>                          |
| Bank Transfer Inquiry Status API     | <https://docs.durianpay.id/reference/bank-transfer-inquiry-status-api>    | /v1.0/transfer-interbank                                                 | <https://apidevportal.aspi-indonesia.or.id/api-services/transfer-kredit/transaction-status-inquiry-bank#/TransactionStatusInquiryBank/post_api_v1_0_transfer_status> |
| E-Wallet Account Inquiry API         | <https://docs.durianpay.id/reference/ewallet-account-inquiry-api>         | /v1.0/emoney/account-inquiry                                             | <https://apidevportal.aspi-indonesia.or.id/api-services/transfer-kredit/customer-top-up#/CustomerTopUp/post_api_v1_0_emoney_account_inquiry>                         |
| E-Wallet Transfer API                | <https://docs.durianpay.id/reference/ewallet-transfer-api>                | /v1.0/emoney/topup                                                       | <https://apidevportal.aspi-indonesia.or.id/api-services/transfer-kredit/customer-top-up#/CustomerTopUp/post_api_v1_0_emoney_topup>                                   |
| E-Wallet Transfer Inquiry Status API | <https://docs.durianpay.id/reference/ewallet-transfer-inquiry-status-api> | /v1.0/emoney/topup-status                                                | <https://apidevportal.aspi-indonesia.or.id/api-services/transfer-kredit/customer-top-up#/CustomerTopUp/post_api_v1_0_emoney_topup_status>                            |
| Balance Inquiry API                  | <https://docs.durianpay.id/reference/balance-inquiry-api>                 | /v1.0/balance-inquiry                                                    | <https://apidevportal.aspi-indonesia.or.id/api-services/informasi-saldo#/BalanceInquiry/post_api_v1_0_balance_inquiry>                                               |