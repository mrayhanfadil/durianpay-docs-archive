---
updatedAt: 2025-06-17T23:24:30.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Integration Steps

## Steps Overview

* Step 1: Create refund
* Step 2: Handling Create Refund API Response

***

## Step 1: Create Refund

Use the following endpoint to submit your refund request

**Endpoint**

<br />

| Method | URL                                   |
| :----- | :------------------------------------ |
| POST   | <https://api.durianpay.id/v1/refunds> |

The following are the sample request body for creating a refund:

```Text Bash
curl -X POST \
  https://api.durianpay.id/v1/refunds \
  -H 'authorization: [Base64({Your_Server_Key}:)]' \
  -H 'content-type: application/json' \
  -d '{
    "ref_id": "abc",
    "payment_id": "pay_IsL5nOCW4M2790",
    "amount": "10000",
    "use_refund_link": "true"
    "notes": "rejected product"
}'

```
```Text Python
import http.client
import json

conn = http.client.HTTPSConnection("api.durianpay.id")

payload = json.dumps(
    {
        "ref_id": "abc",
        "payment_id": "pay_IsL5nOCW4M2790",
        "amount": "10000",
        "use_refund_link": "true",
        "notes": "rejected product",
    }
)

headers = {
    "content-type": "application/json",
    "authorization": "[Base64({Your_Server_Key}:)]",
}

conn.request("POST", "/v1/refunds", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


```
```Text JavaScript
var request = require('request');

var options = {
  method: 'POST',
  url: 'https://api.durianpay.id/v1/refunds',
  headers: {
    authorization: '[Base64({Your_Server_Key}:)]',
    'content-type': 'application/json'
  },

  body: JSON.stringify({
    ref_id: 'abc',
    payment_id: 'pay_IsL5nOCW4M2790',
    amount: '10000',
    use_refund_link: 'true',
    notes: 'rejected product'
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});


```

<br />

## Step 2: Handle create refund API Process

> 📘 Refund process happened synchronously. Hence, you'll be able to identify the full status of the refund from the Create Refund API's Response

The following are the API Response example of a refund creation:

```Text Response
{
  "data": {
    "id": "rfn_qfrsL0tlnT0308",
    "ref_id": "reference_1",
    "amount": "20000.00",
    "refund_type": "partial",
    "status": "done",
    "created_at": "2021-07-20T10:43:42.201587Z",
    "updated_at": "2021-07-20T10:43:42.401256Z",
    "approved_at": "2021-07-20T10:43:42.401256Z",
    "source": "api",
    "customer_name": "joe",
    "customer_email": "jade@sfs.com",
    "customer_phone": ""
  }
}

```

<br />

Based on the API Response, there are some parameters of the API Response which you need to handle. Mainly, `status`which signifies the status of the refund. If the status is `done`, then the transaction has been successfully refunded and your customer should already be able to see that the funds is already refunded to their account.