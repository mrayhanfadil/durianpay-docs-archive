---
updatedAt: 2026-02-03T04:29:26.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Verifying Recipients

Before starting to send pay outs, we recommend merchant to verify whether the destination account is valid and correct. Durianpay provides a means to verify the recipient account via Dashboard or API.

### Dashboard

If you are transacting via dashboard, no need to worry. We always cover account validation flow to ensure your transactions run through the correct destination. We will inform you on whether the destination account is valid and also the name associated with the account based on bank/provider information.

### API

If you are transacting  via API, You can use our `Account Validation` API  to verify the account information. You will need to provide bank code destination and bank account number and Durianpay will return following information via the SNAP API response or callback in Legacy API

* Status of the account:  valid or invalid (closed account, inactivate/dormant account, blacklisted)
* Account name according to bank/provider.\
  For e-wallet destination it's a common practice from the bank/provider to mask the name of the account destination as the account number is generated from recipient phone number. Example of masking: Adi Purnomo will become Axx Pxxxxxx.

### SNAP API

[Bank Account Inquiry API](https://docs.durianpay.id/reference/bank-account-inquiry-api)

`Bank Account Inquiry` API is used to verify whether a disbursement destination account is valid/ invalid. If the account is valid, it will give information of the account name according to the the bank/provider.

**Response on POST Method , URL: /account-inquiry-external**

```Text JSON
{
    "beneficiaryAccountName": "Jane Doe",
    "beneficiaryAccountNo": "087783146495",
    "beneficiaryBankCode": "002",
    "beneficiaryBankName": "BNI",
    "currency": "IDR",
    "responseCode": "2001600",
    "responseMessage": "Successful"
}
```

<br />

[E-Wallet Account Inquiry API](https://docs.durianpay.id/reference/ewallet-account-inquiry-api)

`E-Wallet Account Inquiry` API is used to verify whether an e-wallet destination account is valid/ invalid. If the account is valid, it will give information of the destination name according to the the bank/provider.

**Response on POST Method , URL:  /emoney/account-inquiry**

```Text JSON
{
    "additionalInfo": {
        "platformCode": "gopay"
    },
    "amount": {
        "currency": "IDR",
        "value": "10000.00"
    },
    "customerName": "Jane Doe",
    "customerNumber": "87783146495",
    "responseCode": "2003700",
    "responseMessage": "Successful"
}
```

You can find more details in [Integration Steps for SNAP](https://docs.durianpay.id/docs/snap-disbursement-api-implementation)

### Legacy API (will be deprecated in Q2 2025)

[Validate Disbursement](https://docs.durianpay.id/reference/validate-disbursement)

After hitting `Validate Disbursement API` above, we will trigger webhook `account_validation.completed`in which your application can listen to get the account validation result. You can specify your webhook URL on your dashboard via Settings - Webhook page where we would send POST requests to whenever an event occurs.

### Events

| Event Name                    | Description                                                                                                                                                                                                                                        |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account\_validation.completed | This webhook is triggered after validation is completed for account details sent in the validate API request account\_validation.completed webhook is used to retrieve validity of account destination and get the bank stated account holder name |

### Handling Webhook Details

Following information is the important field to be handled  for the event`account_validation.completed`

* `status`
  * valid - Account details are valid
  * invalid - Account details are invalid
* `account_holder`: name shown according to the bank stated name

> Please note that account\_validation.completed is currently not available in sandbox, it's available only in live mode

The following are the example specification for the webhook:

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

You can find more details in  [Disbursement APIs Implementation](https://docs.durianpay.id/docs/disbursement-apis-implementation)