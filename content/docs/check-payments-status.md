---
updatedAt: 2025-06-17T23:24:21.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Check Payment Status

The Check Status Mechanism is a proactive approach for merchants to verify the current status of a payment transaction by actively calling our Get Payment by ID API. This mechanism ensures that the merchant's systems remain up-to-date with the latest information regarding a payment, even if there are delays, network issues, or other factors that may affect real-time updates (i.e., webhook delays) .

## Why should I Impement this mechanism ?

The Check Status Mechanism ensures that your system stays synchronized with the latest transaction status, even if a webhook update is delayed or missed. While Durianpay provides real-time payment updates via webhooks, network issues, server downtimes, or other technical challenges can occasionally cause webhooks to fail. In these cases, the Check Status Mechanism serves as a dependable fallback, allowing you to verify the payment status directly and maintain up-to-date transaction information in your system.

## How to Implement the Check Status mechanism

### Steps Overview

* Step 1: Call Durianpay's Get Payment by ID API
* Step 2: Handle the API Response

### Step 1: Call Durianpay's Get Payment by ID API

Here's the endpoint that you need to call:

**Endpoint**

| Method | URL                                         |
| :----- | :------------------------------------------ |
| GET    | <https://api.durianpay.id/v1/payments/{id}> |

You can replace the \{id} param with the payment\_id that you wish to check

> 📘 For accurate payment updates, we recommend using an interval-based Check Status Mechanism with exponentially increasing intervals

### Step 2: Handle the API Response

From the API Response, you can identify some key informations of the transactions. Most importantly, we inform the final status of the transaction from the `status` parameter in the API response. Please handle them accordingly on your server.

The following is the API response for the Get Payment by ID API:

```Text Response
{
    "id": "pay_76n67eK9Fq4137",
    "amount": "20000",
    "currency": "IDR",
    "status": "completed",
    "order_id": "ord_B14sdfwAdmmSDF24a",
    "payment_ref_id": "txn2314",
    "created_at": 1582628071,
    "is_live": true,
    "expiration_date": "2021-09-21T05:11:09.574136Z",
    "payment_details_type": "ewallet_details",
    "method_id": "OVO",
    "created_at": "2021-09-20T05:11:09.574138Z",
    "updated_at": "2021-09-20T05:11:15.161768Z",
    "metadata": {},
    "retry_count": 0,
    "discount": "",
    "paid_amount": "",
    "provider_id": "",
    "total_fee": "",
    "promo_id": "",
    "shipping_fee": "",
    "ds_error_metadata": null,
    "CustomerID": "cus_iT1g1t74655079",
    "CustomerName": "test",
    "CustomerEmail": "",
    "OrderRefID": "",
    "Currency": "IDR",
    "failure_reason": {}
}
```