---
updatedAt: 2025-06-17T23:24:48.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Handling Webhooks

Whenever certain event occurs on your Durianpay's Pay Outs, we trigger webhooks which your application can listen to. A webhook is a URL on your server where we send payloads for such events. For example, if you implement a `disbursement.completed` webhook, once a pay out is successful, we will immediately notify your server with a `disbursement.completed`event.

Durianpay will send the webhook to you directly when an event change occurred, followed by 2, 5, 10, 90, 210 minutes retry if the webhook is not acknowledged with 200 OK status.

You can specify your webhook URL on your dashboard in `Settings - Webhook` where we would send POST requests to whenever an event occurs.

## Setting Up Webhook

* Create Webhooks in Settings > Create New

  ![](https://files.readme.io/89617874a25e8ac655f32d9022819ca447b01d51722db92a586303c5aae04175-image.png)
* Fill up the event you want to subscribe to, give a name to webhook event and add your url which you want us to call

  ![](https://files.readme.io/7cf5a4795a191fcbd38c4200996518361c62d46b6e8f8dc524200ec741313e3b-image.png)
* You need to configure only the base url, the path will be appended as per the selected webhook

  ![](https://files.readme.io/9e47bd14f23986295e8db87d65b42f9de2b21df4fc0fccd5ce100af17b34f854-image.png)
* Once you click create button, there will be sample webhook from Durianpay to be sent to the URL. In order to successfuly setup a webhook the URL should return 200 OK.
* Once you receive success notification on setting up webhook, you are ready to accept Durianpay webhook according to the event specified.

## SNAP Disbursement API

### Events after Pay Outs:

| Event Name             | Description                                                                                                                                                                              |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transfer-bank.notify` | This webhook is triggered when a disbursement is completed. It will be triggered  when the money is already sent to the destination or the transaction status is confirmed to be failed. |

### Handling Webhook Details

Following information is the important field to be handled  for each of the event. We recommend you to implement `transfer-bank.notify`to get final status of a disbursement in addition to implement `Inquiry Status` API on Bank Transfer/ E-Wallet.

Event: `transfer-bank.notify`\
Handle the following webhook by checking the following fields in the additionalInfo parameter of the webhook body

| latestTransactionStatus | transactionStatusDesc | Description                               |
| :---------------------- | :-------------------- | :---------------------------------------- |
| 00                      | done                  | The transaction is successfully completed |
| 06                      | failed                | The transaction has failed                |

<br />

### Webhooks Sample

```Text transfer-bank.notify
{
  "originalReferenceNo": "dis_item_123",
  "originalPartnerReferenceNo": "123456789",
  "responseCode": "2000000",
  "responseMessage": "Request has been processed successfully",
  "amount": {
    "value": "12345678.00",
    "currency": "IDR"
  },
  "beneficiaryAccountNo": "1234567890",
  "beneficiaryBankCode": "002",
  "sourceAccountNo": "mer_123",
  "additionalInfo": {
    "latestTransactionStatus": "00",
    "transactionStatusDesc": "done"
  }
}

```

### Digital Signature Verification

Follow these steps to validate the digital signature of the webhook

1. Take the signature from HTTP header "X-SIGNATURE"\
   The following is an example:\
   `X-SIGNATURE`: VpByUVbCd1rf/K5sMBGJk2Nz2zLsH9L9PWCMzb/ouVB/rVh/wPTfzr4AIfW9LGzyKrXTihS75uIiKqhIRexS9sAsu+AXyPKVULKGBRIZJ1yNdbQQQfUS3HT4sbn+JgLlBWS7DozJGqR5LY6F0cQ8wceErqSGEiHQGut5bpCaUC3wEfDynujO33BIvKLF5Gy9XnDMRVvRs+r6pjlew5uCX0Z3vmYEVCHE/6pWvkvRONhwQfqzSvIc56MVInnPFraz5l0DdendQbHhiCg0VIqhsp/aG7Ubxd2hS3o1PbnKiVjr07/mU5nhKhNlT8WtES7/5zh/Argl2Fkea8X+n70RBQ==
2. Compose the string to verify
   1. Sample Webhook payload:
      ```Text Webhook Payload
      {
        "additionalInfo": {
          "latestTransactionStatus": "00",
          "transactionStatusDesc": "success"
        },
        "amount": {
          "currency": "IDR",
          "value": "10000.00"
        },
        "beneficiaryAccountNo": "3370018285",
        "beneficiaryBankCode": "014",
        "originalPartnerReferenceNo": "1000-1000-1000-1180",
        "originalReferenceNo": "dis_item_Jl2HIglkQN4340",
        "responseCode": "2000000",
        "responseMessage": "Request has been processed successfully",
        "sourceAccountNo": "mer_1HYN9axnbi6806"
      }
      ```
   2. String To Verify Format:
      ```Text Pseudo Code
      <HTTP METHOD> + ":" + <RELATIVE PATH URL> + ":" + LowerCase(HexEncode(SHA-256(Minify(<HTTP BODY>)))) + ":" + <X-TIMESTAMP>
      ```
      * For a webook url <https://www.example.com/callback/v1.0/transfer/notify>, the relative path url will be /callback/v1.0/transfer/notify
      * X-TIMESTAMP will be part of the webhook header
      * HTTP Method will be POST
   3. Example: POST:/callback/v1.0/transfer/notify:5d2c90ddfdd406117ced5c2b502c05b601d435c7e5440f82e58733fdd5f15b7d:2024-11-07T16:04:55.667+07:00
3. Verify the correctness of the signature based on SHA-256 with RSA-2048 encryption using PKCS#8 signing against the string to sign with provided Durianpay public key (please take notes that the public key will be different for Sandbox vs Live).
4. If the verification  is correct, you can safely consume the request and return HTTP 200 response.

<br />

## Legacy Disbursement API

### Events after Pay Outs:

| Event Name                        | Description                                                                                                                                                                         |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| disbursement.validation.completed | This webhook is triggered after the disbursement is submitted and the validation is completed for all the items in the batch.                                                       |
| disbursement.completed            | This webhook is triggered when the disbursement is completed for all(valid) items in the batch disbursement.completed webhook is used to retrieve final status of the disbursement. |

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

### Webhooks Sample

The following are the request body for each of the webhooks:

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

##