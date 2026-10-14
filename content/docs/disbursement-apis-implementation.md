---
updatedAt: 2025-06-17T23:23:19.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Disbursement APIs Implementation

## Steps Overview

* Step 1: Submit the disbursement batch
* Step 2: Approval of batch (Optional)
* Step 3: Webhooks / Store fields on your server (optional)
* Step 4: Verify disbursement status (optional)

***

## Step 1: Submit a disbursement batch

Submit a disbursement batch or basically create a disbursement batch. The disbursement needs to be submitted via submit disbursement API. There are two optional parameters that can alter the normal flow of disbursement:

1. force\_disburse - Approval is automatic if we use this parameter. It will proceed to disburse once the items validation is completed. (force\_disburse=true)
2. skip\_validation - If this parameter is true then the bank validation will be skipped and batch items will be disbursed directly. skip\_validation can be combined with force\_disburse.(skip\_validation=true)\
   (Note : How to use the above parameters is shown below in the code snippet)

Once user submits disbursement and validation is completed, Durianpay will send a disbursement.validation\_completed webhook to the configured webhook url.

Use the following endpoint to submit a disbursement:

**Endpoint**

| Method | URL                                                                                          |
| :----- | :------------------------------------------------------------------------------------------- |
| POST   | <https://api.durianpay.id/v1/disbursements/submit?force_disburse=true&skip_validation=false> |

```Text Bash
curl -X POST \'https://api.durianpay.id/v1/disbursements/submit?force_disburse=true&skip_validation=false'
-u '[Base64({Your_Server_Key}:)]' \
-H 'content-type: application/json' \
-H 'idempotency_key: <YOUR_IDEMPOTENCY_KEY>' \
-d '{
    "name": "sample disbursement",
    "description": "this is a sample disbursement",
    "items": [
        {
            "account_owner_name": "Jane Doe",
            "bank_code": "bca",
            "amount": "10000",
            "account_number": "8422647",
            "email_recipient": "jane_doe@nomail.com",
            "phone_number": "85722173217",
            "notes": "salary"
        },
        {
            "account_owner_name": "Jack",
            "bank_code": "bca",
            "amount": "10000",
            "account_number": "235464",
            "email_recipient": "jack@nomail.com",
            "phone_number": "85609873209",
            "notes": "salary"
        }
    ]
}'
```

```Text Response
{
  {
    "data": {
        "id": "dis_LjxhDKq8Am3427",
        "name": "test disb",
        "total_amount": "20000.00",
        "total_disbursements": 2,
        "description": "description"
    }
}
```

## Step 2: Approval of the submitted disbursement batch (Optional)

This step will help you to approve the disbursement.

If the force\_disburse parameter is not used in `step 1` then approve API needs to be called. Once you call the approve API the actual disbursement is triggered and money is disbursed to customer's account. Once all batch items are disbursed, durianpay will send `disbursement.completed` webhook.

**Endpoints**

| Method | URL                                                           |
| :----- | :------------------------------------------------------------ |
| POST   | <https://api.durianpay.id/v1/disbursements/dis_XXXXX/approve> |

```Text Bash
curl -u [Base64({Your_Server_Key}:)] \
-X POST https://api.durianpay.id/v1/disbursements/dis_XXXXX/approve \
-H "content-type: application/json" \
```

```Text Response
{
    "data": {
        "id": "dis_XXXX",
        "name": "sample disbursement",
        "type": "batch",
        "status": "approved",
        "total_amount": "10000.00",
        "total_disbursements": 1,
        "description": "this is a sample disbursement"
    }
}
```

## Step 3: Webhooks / Store fields on your server

Whenever certain event occurs on your Durianpay's Disbursement, we trigger webhooks which your application can listen to. A webhook is a URL on your server where we send payloads for such events. For example, if you implement webhooks, once a disbursement is successful, we will immediately notify your server with a disbursement.completed event.

You can specify your webhook URL on your dashboard (or through your dedicated Customer success manager) where we would send POST requests to whenever an event occurs. Here is a list of events we can send to your webhook URL.

### List of Webhook Events in Disbursement

| Event Name                        | Description                                                                                                                                                                                                                                         |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| disbursement.validation.completed | This webhook is triggered after the disbursement is submitted and the validation is completed for all the items in the batch.                                                                                                                       |
| disbursement.completed            | This webhook is triggered when the disbursement is completed for all(valid) items in the batch disbursement.completed webhook is used to retrieve final status of the disbursement.                                                                 |
| account\_validation.completed     | This webhook is triggered after validation is completed for account details sent in the validate API request account\_validation.completed webhook is used to retrieve validity of account destination and get the bank stated account holder name. |

<br />

### Handling Webhook Details

Following information is the important field to be handled  for each of the event. We recommend you to implement `disbursement.completed` at the minimal to get final status of a disbursement.

Event: `disbursement.validation.completed`

* `valid_disbursements.status`
  * valid - Destination account is valid, and transaction continue to be processed
* `invalid_disbursements.status`
  * invalid - Destination account is invalid, and transaction is not processed further

Event: `disbursement.completed`

* `status`
  * success - All items in the batch is successfully completed
  * partially\_success - Some items in the batch are success and some are not
  * failed - All items in batch is failed
* `item_status.status`
  * done - Transaction is successfully done
  * invalid - Transaction validation failed
  * failed - Transaction is failed to be processed by provider\
    account\_validation.completed

Event: `account_validation.completed`

* `status`
  * valid - Account details are valid
  * invalid - Account details are invalid
* `account_holder`: name shown according to the bank stated name

> please note that account\_validation.completed is currently not available in sandbox, it's available only in live mode

### Webhooks Sample

The following are the request body for each of the webhooks:

```Text disbursement.completed
{
  "event": "disbursement.completed",
  "data": {
    "created_at": "2021-06-22T15:20:20.840353Z",
    "currency": "IDR",
    "description": "test Apr13",
    "failed_item_amount": "200000.00",
    "failed_item_count": 2,
    "id": "dis_4hjykf9KK99186",
    "is_live": true,
    "item_status": [
      {
        "id": "dis_item_PVusz7D0jF2144",
        "status": "invalid"
      },
      {
        "id": "dis_item_0Hm7Clzh4j3788",
        "status": "invalid"
      },
      {
        "id": "dis_item_Cr8c1Rv3Kk7183",
        "status": "done"
      }
    ],
    "items_count": 3,
    "merchant_id": "mer_MsCtIPhqRc8045",
    "name": "test Apr13",
    "signature": "61a1af026de7fbed3eac0f35b5c5bb177ef35d9f1059d8ff07f98786d770adbf",
    "status": "partially_success",
    "success_item_amount": "100000.00",
    "success_item_count": 1,
    "total_amount": "300000.00",
    "type": "batch"
  },
  "retry_count": 0
}
```
```Text disbursement.validation_completed
{
  "event": "disbursement.validation_completed",
  "data": {
    "amount": "210000.00",
    "created_at": "2021-06-22T15:05:10.803274Z",
    "description": "test Apr13",
    "id": "dis_xHbeiO162C6172",
    "invalid_disbursements": [
      {
        "account_number": "0",
        "amount": "100000.00",
        "bank_code": "cimb",
        "id": "dis_item_MQh1YjwABm4913",
        "invalid_fields": [
          {
            "key": "bank_code",
            "message": "Invalid BankCode/AccountNumber"
          },
          {
            "key": "account_number",
            "message": "Invalid BankCode/AccountNumber"
          }
        ],
        "owner_name": "riza@gmail.com",
        "status": "invalid"
      },
      {
        "account_number": "1",
        "amount": "100000.00",
        "bank_code": "cimb",
        "id": "dis_item_QJQ6BGlfDv9766",
        "invalid_fields": [
          {
            "key": "bank_code",
            "message": "Invalid BankCode/AccountNumber"
          },
          {
            "key": "account_number",
            "message": "Invalid BankCode/AccountNumber"
          }
        ],
        "owner_name": "riza@gmail.com",
        "status": "invalid"
      }
    ],
    "is_live": true,
    "merchant_id": "mer_MsCtIPhqRc8045",
    "name": "test Apr13",
    "signature": "61a1af026de7fbed3eac0f35b5c5bb177ef35d9f1059d8ff07f98786d770adbf",
    "total_invalid_amount": "200000.00",
    "total_invalid_items": 2,
    "total_items": 3,
    "total_valid_amount": "10000.00",
    "total_valid_items": 1,
    "type": "batch",
    "valid_disbursements": [
      {
        "account_number": "0845210387",
        "amount": "10000.00",
        "bank_code": "bca",
        "id": "dis_item_pey2Mb5Osu7149",
        "owner_name": "riza@gmail.com",
        "status": "valid"
      }
    ]
  },
  "retry_count": 0
}
```
```Text account_validation.completed
{
  "event": "account_validation.completed",
  "data": {
    "account_holder": "Dummy Name",
    "account_number": "8888105",
    "bank_code": "bca",
    "signature": "a7df932e5064e17e757e880fd846849bde14c6da2f2cce474e2f71fbd1c6ce0d",
    "status": "valid"
  },
  "retry_count": 0
}
```

<br />

## Step 4: Verify disbursement status (Optional)

You will get `disbursement_id` through webhook callback (if configured). You should ideally try to validate the disbursement and store the details in your server/database against the transaction accordingly.

First, you need to get verification `signature` from Durianpay which would have been provided to you in your webhook callback.

If you didn't receive it for any reason, you can call disbursement status check API from your server/backend which will respond back with signature if status of disbursement is completed.

| Method | URL                                                  |
| :----- | :--------------------------------------------------- |
| GET    | <https://api.durianpay.id/v1/disbursements/{dis_id}> |

This signature is computed by us using `disbursement_id`, `amount` and your `secret key`. You need to create the hash on your server/backend where you have all these elements and match with the signature provided by us.

Here are sample code for `signature` generation for **submit disbursement**

```Text Go
// Function to generate the signature for verification of disbursement
//use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key
func GenerateSignature(disbursementID string, amount string, accessKey string) (generatedSignature string) {
  //message passed includes disbursement_id + “|” + amount. Amount is in “15000.00” format
  secretData := disbursementID + "|" + amount
  // Create a new HMAC by defining the hash type and the key (as byte array)
  h := hmac.New(sha256.New, []byte(accessKey))
  // Write Data to it
  h.Write([]byte(secretData))
  // Get result and encode as hexadecimal string
  generatedSignature = hex.EncodeToString(h.Sum(nil))
  return
}
```
```Text JavaScript
var crypto = require('crypto'); 
//creating hmac object  
//use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key 
var hmac = crypto.createHmac('sha256', 'your_api_key');  
//passing the data to be hashed 
//message passed includes disbursement_id + “|” + amount. Amount is in “15000.00” format
data = hmac.update('disbursement_id|amount'); 
//Creating the hmac in the required format 
gen_hmac= data.digest('hex'); 
//Printing the output on the console 
console.log("hmac : " + gen_hmac);
```
```Text Python
import hmac
import hashlib
def generate_signature(secret_key, message):
    secret_key_bytes = bytes(secret_key, 'utf-8')
    message_bytes = bytes(message, 'utf-8')
    signature = hmac.new(secret_key_bytes, message_bytes, hashlib.sha256).hexdigest()
    return signature

#use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key
secret_key = "your_api_key"

#message passed includes disbursement_id + “|” + amount. Amount is in “15000.00” format
message = "disbursement_id|amount"
print(generate_signature(secret_key, message))
```
```Text Ruby
require 'openssl'; 
def generateSignature(secret_key, message) 
    key = secret_key 
    data = message
    digest = OpenSSL::Digest.new('sha256') 
    signature = OpenSSL::HMAC.hexdigest(digest, key, data) 
    
    return signature
end 

#use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key
secret_key = 'your_api_key' 

#message passed includes disbursement_id + “|” + amount. Amount is in “15000.00” format
message = 'disbursement_id|amount' 
result = generateSignature secret_key, message
puts result
```

<br />

Here are sample code for `signature` generation for **account validation**

```Text JavaScript
var crypto = require('crypto'); 
//creating hmac object  
//use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key 
var hmac = crypto.createHmac('sha256', 'your_api_key');  
//passing the data to be hashed 
//message passed includes accountNumber + “|” + bankCode + "|" + status. Amount is in “15000.00” format
data = hmac.update('accountNumber|bankCode|status'); 
//Creating the hmac in the required format 
gen_hmac= data.digest('hex'); 
//Printing the output on the console 
console.log("hmac : " + gen_hmac);
```
```Text Go
// Function to generate the signature for verification of account validation completed webhook
func GenerateAccountValidationSignature(accountNumber string, bankCode string, status string, accessKey string) (generatedSignature string) {
    secretData := accountNumber + "|" + bankCode + "|" + status
    // Create a new HMAC by defining the hash type and the key (as byte array)
    h := hmac.New(sha256.New, []byte(accessKey))
    // Write Data to it
    h.Write([]byte(secretData))
    // Get result and encode as hexadecimal string
    generatedSignature = hex.EncodeToString(h.Sum(nil))
    return
}
```
```Text Python
import hmac
import hashlib
def generate_signature(secret_key, message):
    secret_key_bytes = bytes(secret_key, 'utf-8')
    message_bytes = bytes(message, 'utf-8')
    signature = hmac.new(secret_key_bytes, message_bytes, hashlib.sha256).hexdigest()
    return signature

#use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key
secret_key = "your_api_key"

#message passed includes accountNumber + “|” + bankCode + "|" + status. Amount is in “15000.00” format
message = "accountNumber|bankCode|status"
print(generate_signature(secret_key, message))
```
```Text Ruby
require 'openssl'; 
def generateSignature(secret_key, message) 
    key = secret_key 
    data = message
    digest = OpenSSL::Digest.new('sha256') 
    signature = OpenSSL::HMAC.hexdigest(digest, key, data) 
    
    return signature
end 

#use appropriate key if it is a sandbox order please use dp_test key and if it is a live order then use dp_live key
secret_key = 'your_api_key' 

#message passed includes accountNumber + “|” + bankCode + "|" + status. Amount is in “15000.00” format
message = 'accountNumber|bankCode|status' 
result = generateSignature secret_key, message
puts result
```