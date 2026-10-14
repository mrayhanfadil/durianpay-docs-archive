---
updatedAt: 2025-06-17T23:24:17.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Cancelling a Payment

The Payment Cancellation API provides merchants with the ability to cancel payments that are still in the "processing" stage, giving them control to halt transactions before they reach a final status. This API is invaluable in situations like managing inventory when an item is out of stock, enforcing time-sensitive requirements where payments must be completed within a certain timeframe, and applying custom business rules that might require stopping a transaction early, such as ensuring alignment with the merchant’s inventory and operational policies or honoring customer requests. By enabling these controls, the Payment Cancellation API helps merchants uphold their transaction policies, streamline operations, and enhance the overall customer experience.

<br />

## How to Cancel a Payment

### Steps Overview

* Step 1: Call Durianpay's Cancel Payment API
* Step 2: Handle the API Response

***

### Step 1: Call Durianpay's Cancel Payment API

Here's the endpoint that you need to call:

**Endpoint**

| Method | URL                                                |
| :----- | :------------------------------------------------- |
| GET    | <https://api.durianpay.id/v1/payments/{id}/cancel> |

You can replace the \{id} param with the payment\_id that you wish to cancel

> 📘 You can only cancel a `payment` , if and only if the status of the `payment` is still processing

### Step 2: Handle the API Response

In the API Response, Durianpay will specify the final status of the transaction that you just attempt to cancel. If the status is `cancelled` then you can safely assume that the transaction is successfully cancelled and you can proceed accordingly. The following is an example for the Cancel Payment API's response:

```Text API Response
{
    "data": {
        "id": "pay_ohXLNm2fPw6868",
        "status": "cancelled",
        "order_id": "ord_Dg0Dz9wwKP1602",
        "created_at": "2020-11-19T22:09:48Z",
        "updated_at": "2020-11-26T20:02:24.561169Z"
    }
}
```

<br />

<br />

###