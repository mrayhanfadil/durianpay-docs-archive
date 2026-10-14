---
updatedAt: 2025-06-17T23:22:20.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Integration Steps

Looking to create a tailored payment experience for your customers? The Durianpay API enables customizable payment flows that fit your unique business needs. Follow this guide to easily set up personalized payment links.

## Step 1: Authorization Header Generation

When you're calling any of Durianpay's API, you have to pass `Authorization` parameter in the header. Value for `Authorization` can be received by going through these steps:

1. **Get your respective API Keys from Durianpay's dashboard, by going to Settings > API Keys**

   ![](https://files.readme.io/6a81b3f81943562c0723d82765e7d0af463ae628bbd50e2f74acd8b396fc3ac3-image.png)
2. **Formatting the API Key to`BASIC AUTH` format**\
   The BASIC AUTH will have the following format: `Username`:`Password`.\
   Replace Username with your API Key and leave value for password as Blank.\
   The result for this combination will be: string `{Your_API_Key}:`
3. **Encode the previously generated combination to Base64 format**
4. **Include the Base64 encoded string in the HTTP(S) header**\
   Prepend the authorization method `(Basic)` and a space `()` to the encoded string. The authorization header is as given below: `Authorization: Basic [Base64({Your_API_Key}:)]`

> 🚧 Important things to note:
>
> 1. Before you encode the keys value, Please ensure the format of the API Key follows the aforementioned Basic Auth format, `{Your_API_Key}:` . Where there will be `:` after your API Key.
> 2. The Authorization Header given in the example is for reference only. Please use your own Sandbox/Production Server Key to create your API key.
> 3. The API keys for Sandbox and Production are different. When going live, please switch to the LIVE API Keys.

## Step 2: Create an order

**Endpoint**

| Method | URL                                  |
| :----- | :----------------------------------- |
| POST   | <https://api.durianpay.id/v1/orders> |

**Request Body**

```Text Request
{
    "amount": "10000.67",
    "payment_option": "full_payment",
    "currency": "IDR",
    "order_ref_id": "order_ref_001",
    "customer": {
        "customer_ref_id": "cust_001",
        "given_name": "Jane",
        "middle_name": "Mary",
        "sur_name": "Doe",
        "email": "jane_doe@nomail.com",
        "mobile": "85722173217",
        "address": {
            "receiver_name": "Jude Casper",
            "receiver_phone": "8987654321",
            "label": "Home Address",
            "address_line_1": "Jl. HR. Rasuna Said",
            "address_line_2": "Apartment #786",
            "city": "Jakarta Selatan",
            "region": "Jakarta",
            "country": "Indonesia",
            "postal_code": "560008",
            "landmark": "Kota Jakarta Selatan"
        }
    },
    "items": [
        {
            "name": "LED Television",
            "qty": 1,
            "price": "10001.00",
            "logo": "https://merchant.com/tv_image.jpg",
            "brand": "Samsung",
            "category": "Electronics",
            "sku": "TV_123",
            "total_price": "10001.00",
            "metadata": "Model No: SG_123"
        }
    ],
    "metadata": {},
    "description": "Pesan untuk TV",
    "admin_fee_method": "included",
    "expiry_date": "2022-03-29T10:00:00.000Z"
}
```

## Step 3: Create a payment

Create a payment for your order. The request body will differs based on the payment method that you choose.

> 📘 For example purposes, we'll only be creating a QRIS payment. To see the request body for other payment methods, please refer here: [Payment Charge API](https://docs.durianpay.id/reference/payment-apis-payment-charge-bnpl-1)

**Endpoint**

| Method | URL                                            |
| :----- | :--------------------------------------------- |
| POST   | <<https://api.durianpay.id/v1/payments/charge> |

```
'
{
  "type": "QRIS",
  "request": {
    "order_id": "ord_abcde", //Order ID which returned from the previous step
    "name": "Nobel",
    "amount": "10000"
  }
}
'
```

## Step 4: Handle the API Response

After creating a payment using the Payment Charge API, you’ll receive an API response containing payment details required for your customer to complete the transaction. The response parameters differ based on the payment method, so you’ll need to handle at least these specific parameters accordingly.

For example, in a QRIS transaction, you must handle either the `QR_code` or `QR_string` parameter to enable successful completion. Here’s an example of a successful QRIS Payment Charge API response.

```
{
  "data": {
    "type": "QRIS",
    "response": {
      "payment_id": "pay_dummy1234567890",
      "order_id": "ord_dummy9876543210",
      "status": "processing",
      "expiration_time": "2024-04-30T23:32:24.714051541Z",
      "creation_time": "2024-04-30T22:32:24.720110839Z",
      "qr_string": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAJYAQMAAACEqAqfAAAABlBMVEX///8AAAAAAACAAAABBBBBCCCCAAAEECCAAA111111BBCCAAAQQQQAAAABBBBBBAAACCCCBBAAAA11AA==",
      "unique_id": "QRIS",
      "metadata": {
        "merchant_name": "",
        "merchant_id": ""
      },
      "amount": "7880.00",
      "paid_amount": "7880.00",
      "qr_code": "00020101021226610016ID.CO.RANDOM.WWW011893600918002091234567082091234567303UME51440014ID.CO.RANDOM.WWW0215ID20223456789030303UME52045399530336054077880.005802ID5912Random Store6014KOTA RANDOM61052829662220518pay_dummy1234567890363048718"
    }
  }
}
```

<br />

## Step 5: Webhooks / storing fields on your servers (Optional)

Whenever certain transaction actions occur on your Durianpay Checkout integration, we trigger events which your application can listen to. This is where webhooks come in. A webhook is a URL on your server where we send payloads for such events. For example, if you implement webhooks, once a payment is successful, we will immediately notify your server with a payment.completed event. Here is a list of events we can send to your webhook URL.

You can specify your webhook URL on your dashboard (or through your dedicated Customer success manager) where we would send POST requests to whenever an event occurs.

**Valid events**

`payment.completed` `payment.failed` `payment.cancelled` `order.created` `order.completed`

```Text payment.completed
{  
  "event": "payment.completed",
  "data":{  
    "id": "pay_dAS123ad123Asd",
    "signature": "9e892f199d026d06a56669e658a56f264610431d24e8b4d07f7bd46f6d5062d2",
    "order_id": "ord_XXXXXXXXX",
    "amount": "10000",
    "currency": IDR,
    "paid_at": "2016-09-30T21:10:19.000Z",
    "created_at":"2016-09-30T21:09:56.000Z",
    "metadata": {
      "key": "value"
    },
}
```
```Text payment.failed
// This event will be triggered when a payment is started but failed later.
{
  "event": "payment.failed",
  "data": {
    "amount": 92500200,
    "amount_str": "925002.00",
    "created_at": "2021-05-10T11:14:10.500067Z",
    "currency": "IDR",
    "id": "pay_0UHr5QFPwm3593",
    "is_live": true,
    "merchant_id": "mer_MsCtIPhqRc8045",
    "metadata": { "key": "value" },
    "order_id": "ord_8c23OgJFIA5384",
    "payment_method": "CARD",
    "failure_reason": {
      "code": 20010,
      "message": "error due to end user action"
    }
  },
  "retry_count": 0
}
```
```Text payment.cancelled
// This event will be triggered when payment is cancelled.
{
  "event": "payment.cancelled",
  "data": {
    "amount": 92500200,
    "amount_str": "925002.00",
    "created_at": "2021-05-10T11:14:10.500067Z",
    "currency": "IDR",
    "id": "pay_0UHr5QFPwm3593",
    "is_live": true,
    "merchant_id": "mer_MsCtIPhqRc8045",
    "metadata": { "key": "value" },
    "order_id": "ord_8c23OgJFIA5384",
    "payment_method": "CARD",
    "failure_reason": {
      "code": 20014,
      "message": "payment cancelled by merchant"
    }
  },
  "retry_count": 0
}
```
```Text order.created
// This event will be triggered when order is created. This event is also valid for orders associated with payment links.
{
  "event": "order.created",
  "data": {
    "amount": 100000000,
    "amount_str": "1000000.00",
    "created_at": "2021-05-10T16:41:38.668844Z",
    "currency": "IDR",
    "customer_id": "cus_pWZu3yHhhc9548",
    "description": "description notes",
    "expiry_date": "2021-05-13T16:41:38.653Z",
    "id": "ord_LleWCP2T3B8368",
    "is_live": true,
    "merchant_id": "mer_MsCtIPhqRc8045",
    "meta_data": { "key": "value" },
    "payment_link_url": "https://durianpay.id/payment-link/SxHac7", //this field will be omitted when payment link is not associated with order
    "status": "started"
  },
  "retry_count": 0
}
// Please note, `expiry_date` and `payment_link_url` are optional fields which will appear for orders associated with payment links.
```
```Text order.completed
// This event will be triggered when order is completed. This event is also valid for orders associated with payment links.
{
  "event": "order.completed",
  "data": {
    "amount": 92500200,
    "amount_str": "925002.00",
    "created_at": "2021-05-10T16:40:01.635743Z",
    "currency": "IDR",
    "customer_id": "cus_fMMugWnnAw3274",
    "description": "",
    "id": "ord_8c23OgJFIA5384",
    "is_live": true,
    "merchant_id": "mer_MsCtIPhqRc8045",
    "meta_data": { "key": "value" },
    "status": "completed"
  },
  "retry_count": 0
}

```

<br />

## Step 6: Verify signature on your server side (Optional)

You will get `payment_id` through webhook callback (if configured). You should ideally try to validate the payment and store the details in your server/database against the order/transaction accordingly.

First, you need to get verification `signature` from Durianpay which would have been provided to you in your webhook callback.

If you didn't receive it for any reason, you can call payment status check API from your server/backend which will respond back with `signature` if status of payment is completed.

| Action | URL                                               |
| :----- | :------------------------------------------------ |
| GET    | <https://api.durianpay.id/v1/payments/:id/status> |

This signature is computed by Durianpay using `payment_id`, `amount` and your `secret key`. You need to create the hash on your server/backend where you have all these elements and match with the `signature` provided by Durianpay.

Sample code for signature generation

```Text Go
// Function to generate the signature for verification of payment
//use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key
func GenerateSignature(paymentID string, amount string, accessKey string) (generatedSignature string) {
  //message passed includes payment_id + “|” + amount. Amount is in “15000.00” format
  secretData := paymentID + "|" + amount
  // Create a new HMAC by defining the hash type and the key (as byte array)
  h := hmac.New(sha256.New, []byte(accessKey))
  // Write Data to it
  h.Write([]byte(secretData))
  // Get result and encode as hexadecimal string
  generatedSignature = hex.EncodeToString(h.Sum(nil))
  return
}
```