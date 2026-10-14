---
updatedAt: 2025-06-17T23:22:05.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Quick Start: JavaScript

> 🚧 Durian Checkout is built on Plain JavaScript, please ensure that your application is suitable for this method

## Step 1: Create an order/token from the server

**Endpoint**

| Method | URL                                  |
| :----- | :----------------------------------- |
| POST   | <https://api.durianpay.id/v1/orders> |

```Text Request
var options = {
  amount: "20000",
  currency: "IDR",
  order_ref_id: "order2314",              // optional, your order reference
  customer: {
    customer_ref_id: "cust_001",          // optional, your customer reference
    given_name: "Imam Sugiarto",
    email: "imam.sugiarto@koss.info",     // mandatory
    mobile: "08972638003",
    address: {                            // mandatory for BNPL
        receiver_name: "Jude Casper",
        receiver_phone: "8987654321",
        label: "Judes Address",
        address_line_1: "Cambridge layout",
        address_line_2: "Apartment #786",
        city: "Bangalore",
        region: "Jogupalya",
        country: "Indonesia",
        postal_code: "560008",
        landmark: "Kota Jakarta Selatan"
    }
  },
  items: [
    {
        "name": "LED Television",
        "qty": 1,
        "price": "925001.55",
        "logo": "/static/tv_image.jpg"
    }
  ]
};
// Create Orders 
dpay.orders.create(options).then(resp => {
    console.log(resp);
    // order_id = resp.order_id;
})
.catch(error => {
    console.log(error.err + ' | ' + JSON.stringify(error.data));
});
```

```Text Response
// Sample response
{
  "id": "ord_A31sd3AwAgItmmXdp",
  "customer_id": "cus_rX2ABaMbZJ0050",
  "amount": "20000",
  "currency": "IDR",
  "payment_option": "full_payment",
  "status": "started",
  "order_ref_id": "order2314",
  "address_id": 3863,
  "created_at": "2021-08-04T06:06:37.849813Z",
  "updated_at": "2021-08-04T06:06:37.849813Z",
  "metadata": {},
  "access_token": "adsyoi12sdASd123ASX@qqsda231",
  ...
}
```

<br />

## Step 2: Initialize Checkout

This step will help you create a checkout button on your website which will initiate Durianpay checkout flow for your users seamlessly. The Durianpay checkout modal opens in place without redirecting user to any new tab or url, hence is a much better customer experience leading to better conversions and lower drop offs. You can configure the payment methods in backend with the help of your dedicated Customer success manager easily. Also, you can customize the look and feel at the time of onboarding itself which will forever apply to all your checkout sessions across all devices and users.

> 📘 You should pass `order_id` and `access_token` you received in previous step while creating Order. These need to be passed during checking initialization.

Put the following `script` tag in your `<head>` or at any other appropriate place.

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

After the above script is loaded, you can initialize SDK as below.

```Text client.js
var dpay = Durianpay.init({
    locale: "id",
    environment: "production", // Value should be 'production' for both sandbox and live mode
    access_key: "<ACCESS_TOKEN>",
    site_name: "testmerchant.com",
    dark_mode: <true/false>
    pre_selected_payment_method: "VA", // only for flexible checkout
    pre_selected_payment_code: "BCA", // only for flexible checkout
    back_url: "http://merchant.com/redirect", // only for flexible checkout
    order_info: {
        id: "<ORDER_ID>",                     // e.g. ord_XASDadse2312asd31
        customer_info: {
            id: "cus_F5OHtM2L6u4292",
            email: "jose@testmerchant.com",
            phone: "+6285722173217",
            name: "Jose",
        }
    },
    container_elem: "pay-btn-container",
});

// If you want to show Durianpay checkout button, use this 
// function to pass the parent container and css class
dpay.getCheckoutButton("pay-btn-container", "btn filled");

// OR

// If you want to trigger checkout from your button click handler
dpay.checkout();
```

| Field                 | Data attribute       | Description                                                                  |
| :-------------------- | :------------------- | :--------------------------------------------------------------------------- |
| environment           | data-environment     | `production` (default)                                                       |
| locale                | data-locale          | `en` OR `id` (default)                                                       |
| access\_key           | data-access-key      | Your token which you have generated on server side by calling Durianpay APIs |
| dark\_mode            | data-dark\_mode      | Set to true to enable dark mode                                              |
| order\_info.id        | data-order-id        | Order Id received on your server side by calling Durianpay APIs              |
| site\_name            | data-site-name       | Your domain name                                                             |
| customer\_info.id     | data-customer-id     | Customer Id received on your server side by calling Durianpay APIs           |
| customer\_info.name   | data-customer-name   | Customer Name, if present                                                    |
| customer\_info.email  | data-customer-email  | Customer Email, if present                                                   |
| customer\_info.mobile | data-customer-mobile | Customer Mobile, if present                                                  |
| method                | data-method          | `getCheckoutButton`, `Checkout` (default)                                    |
| container\_elem       | data-container-id    | Id of container which should be root of checkout button and popup            |
| btn\_class\_name      | data-btn-class-name  | CSS class you want to apply for checkout button, if required                 |

Successful creation of order returns an id (referred to as order\_id) that should be stored against the Order defined in your system.

<br />

## Step 3: handle callbacks payment success and failures

You can pass javascript handlers which will be called when payment flow is completed in Durian Checkout flow. The onSuccess method is fired when the transaction is successful. This is where you include any action you want to perform when the transaction is successful. The onFailure method is fired when the transaction has failed. This is where you include any action you want to perform when the transaction is unsuccessful.

```Text Javascript
var dpay = Durianpay.init({
    locale: "id",
    environment: "production", // Value should be 'production' for both sandbox and live mode
    access_key: "c6e8ed8e650b08bef67808617c25fbfa",
    site_name: "test.com",
    order_info: {
        id : "ord_XASDadse2312asd31"
    },
    customer_id: "cust_001",
    container_elem: "pay-btn-container",
    onSuccess: function(response) {
      // this happens after the payment is completed successfully
      var paymentId = response.payment_id;
      alert('Payment complete! Payment Id: ' + paymentId);
      // Make an AJAX call to your server with the reference to verify the transaction
    },
    onFailure: function() {
      alert('Transaction was not completed, transaction failed!');
    },
});
```

<br />

## Step 4: Webhooks / Store fields on your servers (Optional)

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

## Step 5: Verify signature on your server side (Optional)

You will get `payment_id` through webhook callback (if configured). You should ideally try to validate the payment and store the details in your server/database against the order/transaction accordingly.

First, you need to get verification `signature` from Durianpay which would have been provided to you in your webhook callback.

If you didn't receive it for any reason, you can call payment status check API from your server/backend which will respond back with `signature` if status of payment is completed.

| Action | URL                                               |
| :----- | :------------------------------------------------ |
| GET    | <https://api.durianpay.id/v1/payments/:id/status> |

<br />

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