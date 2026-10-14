---
updatedAt: 2025-06-17T23:22:16.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Creation via API

If you are looking to streamline your payment workflows with automation, creating payment links via the API is the perfect solution. Follow these steps to learn how to use Durianpay’s **Order Creation API** to generate payment links effortlessly.

## Step 1: Get your API Keys from the Durianpay Dashboard

Log in to your Durianpay Dashboard. Navigate to **Settings** and select the **API Keys** tab. Copy your API keys to use in the integration.

## Step 2: Create an Order via API with `is_payment_link` Set to `true`

Use your API keys to make a request to the **Order Creation API**. Ensure the `is_payment_link` parameter is set to `true`. Fill in all mandatory fields such as:

* **Amount**: The total amount for the payment link.
* **Expiry Date**: Specify the number of days the payment link will remain active.
* **Customer Details**: Include required fields like **Name**, **Phone**, and **Email**. These details will also be used to send notifications and updates to your customers.

> 🚧 Specific Fields to be added for a payment method
>
> 1. For **BNPL**, make sure to include additional fields such as **customer address** (Address, City, Province, Post Code).
> 2. For **BNPL** or **LinkAja**, provide item details by adding an item object to the order.

<br />

Ensure all relevant fields are completed to create a valid payment link that meets your business and customer needs.

**Endpoint**

| Method | URL                                  |
| :----- | :----------------------------------- |
| POST   | <https://api.durianpay.id/v1/orders> |

**Request Body**

```
{
    "amount": "10000",
    "payment_option": "full_payment",
    "currency": "IDR",
    "is_payment_link":true,											//Must be set to TRUE to generate Payment Link  
    "order_ref_id": "order_ref_001", 						
    "customer": {																
        "customer_ref_id": "cust_001",
        "given_name": "Jane Doe", 							//Mandatory for Payment Link creation
        "email": "jane_doe@nomail.com",					//Mandatory for Payment Link creation
        "mobile": "8510987651",									//Mandatory for Payment Link creation
        "address": {														//Mandatory for BNPL method
            "receiver_name": "Jude Casper",
            "receiver_phone": "8987654321",
            "label": "Home Address",
            "address_line_1": "123 Sample Street",
            "address_line_2": "Apartment #786",
            "city": "Test City",
            "region": "Example Province",
            "country": "New Country",
            "postal_code": "12345",
            "landmark": "Near Park"
        }
    },
    "items": [																	//Mandatory for BNPL and LINKAJA method
        {
            "name": "LED Television",
            "qty": 1,
            "price": "10000",
            "logo": "https://merchant.com/tv_image.jpg"
        }
    ],
    "expiry_date": "2025-03-29T10:00:00.000Z",
    "admin_fee_method": "included" 							//Modify this to change fee preference
}
```

## Step 3: Extract the Payment Link Code from the Response

If your API request is successful, you will receive a `200 OK` response. The response body will include a unique payment link code in the `payment_link_url` field. For example the payment link code in the response below is `ur9g8h` . Extract this code and save it for the next step.

**Response Body**

```
{
    "data": {
        "id": "ord_tgOwIf4dYy1263",
        "customer_id": "cus_2QQtfJpdLR7793",
        "order_ref_id": "order_ref_001",
        "order_ds_ref_id": "",
        "amount": "10000.00",
        "payment_option": "full_payment",
        "pending_amount": null,
        "currency": "IDR",
        "status": "started",
        "is_live": true,
        "created_at": "2024-11-05T10:48:09.152054Z",
        "updated_at": "2024-11-05T10:48:09.152054Z",
        "metadata": {},
        "items": [
            {
                "id": "pro_I67J0oPMzD6206",
                "order_id": "ord_tgOwIf4dYy1263",
                "name": "LED Television",
                "brand": "",
                "category": "",
                "sku": "",
                "price": "10000.00",
                "qty": 1,
                "total_price": "",
                "logo": "https://merchant.com/tv_image.jpg",
                "metadata": "{}",
                "created_at": "0001-01-01T00:00:00Z",
                "updated_at": "0001-01-01T00:00:00Z"
            }
        ],
        "access_token": "10803623203503b2016a7521ed240a51787a5cb851327ddafe3a7db1a3fe5706",
        "expire_time": "2024-12-05T10:48:10.18228866Z",
        "expiry_date": "2025-03-29T10:00:00Z",
        "payment_link_url": "ur9g8h", 							//Save this unique code
        "fees": null,
        "shipping_fee": "",
        "admin_fee_method": "included",
        "internal_metadata": "{\"address\":{\"receiver_name\":\"Jude Casper\",\"receiver_phone\":\"\",\"label\":\"Home Address\",\"address_line_1\":\"123 Sample Street\",\"address_line_2\":\"Apartment #786\",\"city\":\"Test City\",\"region\":\"Example Province\",\"country\":\"New Country\",\"postal_code\":\"12345\",\"landmark\":\"Near Park\",\"customer_id\":\"\",\"is_default\":false},\"customer\":{\"id\":\"cus_2QQtfJpdLR7793\",\"customer_ref_id\":\"\",\"given_name\":\"Jane Doe\",\"middle_name\":\"\",\"sur_name\":\"\",\"email\":\"3378c9401252c1ce61811546ff0ba6bfb69d46e8\",\"mobile\":\"5e31c04ecb98c04b1150eeede396109a5d340f1c\",\"address_info\":{\"id\":0,\"receiver_name\":\"\",\"receiver_phone\":\"\",\"label\":\"\",\"address_line_1\":\"\",\"address_line_2\":\"\",\"city\":\"\",\"region\":\"\",\"country\":\"\",\"postal_code\":\"\",\"landmark\":\"\",\"customer_id\":\"\",\"is_default\":false,\"created_at\":\"0001-01-01T00:00:00Z\",\"updated_at\":\"0001-01-01T00:00:00Z\"},\"created_at\":\"0001-01-01T00:00:00Z\",\"updated_at\":\"0001-01-01T00:00:00Z\",\"is_live\":false,\"ip_address\":\"\"},\"products\":[{\"id\":\"pro_I67J0oPMzD6206\",\"order_id\":\"ord_tgOwIf4dYy1263\",\"name\":\"LED Television\",\"brand\":\"\",\"category\":\"\",\"sku\":\"\",\"price\":\"10000.00\",\"qty\":1,\"total_price\":\"\",\"logo\":\"https://merchant.com/tv_image.jpg\",\"metadata\":\"{}\",\"created_at\":\"0001-01-01T00:00:00Z\",\"updated_at\":\"0001-01-01T00:00:00Z\"}]}"
    }
}
```

## Step 4: Form the Complete Payment Link URL and Share It with Your Customers!

Attach the code to the base Durianpay payment link URL format: `https://links.durianpay.id/payment/`. In the example, the full Payment Link URL will be: <https://links.durianpay.id/payment/ur9g8h>. You can then share this generated URL with your customers so they can complete their payments.