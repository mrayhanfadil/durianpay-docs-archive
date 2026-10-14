---
updatedAt: 2025-08-13T02:34:41.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Response Code Handling

# Response Definition

## Format

SNAP API has its own standardized Response Code and Response Message for each of endpoint. In general, the response code will consist of 7 digits with HTTP code, Service Code, and Case Code scheme.

When doing request of balance query to <https://api.durianpay.id/v1.0/balance-inquiry> with the same X-External-ID twice, merchant will receive error with code 4091100 where:

* 409 is HTTP code for Conflict
* 11 is service code for balance inquiry, and
* 00 together with 409 HTTP code indicates same X-External-ID or partnerReferenceNo is being used twice.\
  Reference

HTTP code used is following the standard defined by [RFC 9110](https://httpwg.org/specs/rfc9110.html#overview.of.status.codes)

## Service Code

Service Code is the code that indicates which service being requested depending of its relative path. For example, B2B Access Token generation has a service code of 73, Balance Inquiry has a service code of 11, etc. Please refer to the table below for list of services implemented by Durianpay.

Table of Service Code

| Service Name                     | Service Code | Relative Path                    |
| :------------------------------- | :----------- | :------------------------------- |
| Access Token (B2B)               | 73           | `/v1.0/access-token/b2b`         |
| Balance Inquiry                  | 11           | `/v1.0/balance-inquiry`          |
| Bank Account Inquiry             | 16           | `/v1.0/account-inquiry-external` |
| Bank Transfer                    | 18           | `/v1.0/transfer-interbank`       |
| Bank Transfer Status Inquiry     | 36           | `/v1.0/transfer/status`          |
| E-Wallet Account Inquiry         | 37           | `/v1.0/emoney/account-inquiry`   |
| E-Wallet Transfer                | 38           | `/v1.0/emoney/topup`             |
| E-Wallet Transfer Inquiry Status | 39           | `/v1.0/emoney/topup-status`      |

## Response Code List

In general, there are two types of response to a request in SNAP, Successful and Failed. Successful response is indicated with HTTP code of 2xx while 4xx and 5xx indicates error (from client side or server/Durianpay side).

Please refer to table below for list of Response Code, Response Message, and its meaning.

**Successful Response**

| HTTP Code | Service Code | Case Code | Response Message    | Description                                                                                 |
| :-------- | :----------- | :-------- | :------------------ | :------------------------------------------------------------------------------------------ |
| 200       | any          | 00        | Successful          | Successfully received in Durianpay's side (does not mean sent  to beneficiary successfully) |
| 202       | any          | 00        | Request In Progress | Transaction is still  processing                                                            |

**Error Response**

| HTTP Code | Service Code | Case Code | Response Message                                      | Description                                                                                                                                                                           |
| :-------- | :----------- | :-------- | :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400       | any          | 00        | Bad Request                                           | General request failed error, including message parsing failed.                                                                                                                       |
| 400       | any          | 01        | Invalid Field Format \{field name}                    | Invalid format                                                                                                                                                                        |
| 400       | any          | 02        | Invalid Mandatory Field \{field name}                 | Missing or invalid format on mandatory field                                                                                                                                          |
| 401       | any          | 00        | Unauthorized \[reason]                                | General unauthorized error (No Interface Def, API is Invalid, Oauth Failed, Verify Client Secret Fail, Client Forbidden Access API, Unknown Client, Key not Found, Invalid Signature) |
| 401       | any          | 01        | Invalid Token (B2B)                                   | Token found in request is invalid (Access Token Not Exist, Access Token Expiry)                                                                                                       |
| 401       | any          | 03        | Token Not Found (B2B)                                 | Token not found in the system. This occurs on any API that requires token as input parameter                                                                                          |
| 403       | any          | 00        | Transaction Expired                                   | Transaction expired                                                                                                                                                                   |
| 403       | any          | 18        | Inactive Card/Account/Customer                        | Indicates inactive account                                                                                                                                                            |
| 404       | any          | 01        | Transaction Not Found                                 | Transaction not found                                                                                                                                                                 |
| 404       | any          | 11        | Invalid Card/Account/Customer \[info]/Virtual Account | Card information may be invalid, or the card account may be blacklisted, or Virtual Account number may be invalid.                                                                    |
| 409       | any          | 00        | Conflict                                              | Cannot use same X-EXTERNAL-ID in same day                                                                                                                                             |
| 409       | any          | 01        | Duplicate partnerReferenceNo                          | Transaction has previously been processed indicates the same partnerReferenceNo already created                                                                                       |
| 500       | any          | 00        | General Error                                         | General Error                                                                                                                                                                         |
| 500       | any          | 01        | Internal Server Error                                 | Unknown Internal Server Failure, Please inquiry the status or retry the process again                                                                                                 |
| 504       | any          | 00        | Timeout                                               | Timeout from the issue                                                                                                                                                                |

<br />

## Handling Guideline for Response Code

### SNAP transfer APIs (Bank Transfer  & E-Wallet Transfer) responses

| HTTP Code                     | Handling                                                                                |
| :---------------------------- | :-------------------------------------------------------------------------------------- |
| 2XX                           | Keep status as "processing" and update to success/failed based on callback/check status |
| 4XX                           | Mark transaction as "failed"                                                            |
| 5XX                           | Keep status as "processing" and update to success/failed based on callback/check status |
| Unexpected response / Timeout | Keep status as "processing" and update to success/failed based on callback/check status |

<br />

### SNAP Inquiry Status API (Bank Transfer  & E-Wallet Transfer) responses

| HTTP Code                     | Handling                                                                                                          |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| 2XX                           | Update the status according to the latestTransactionStatus/ transactionStatusDesc parameters in the response body |
| 4XX                           | Retry inquiry status / raise to Durianpay                                                                         |
| 5XX                           | Retry inquiry status / raise to Durianpay                                                                         |
| Unexpected response / Timeout | Retry inquiry status / raise to Durianpay                                                                         |

<br />

### SNAP Inquiry Status API: 2XX status handling

| latestTransactionStatus | transactionStatusDesc | Description                               |
| :---------------------- | :-------------------- | :---------------------------------------- |
| 00                      | done                  | The transaction is successfully completed |
| 06                      | failed                | The transaction is failed                 |
| 03                      | processing            | The transaction is being processed        |