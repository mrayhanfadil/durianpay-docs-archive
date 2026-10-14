---
updatedAt: 2025-06-17T23:25:05.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Integration Steps

## Step 1: Create your Subaccount

Currently, subaccount creation is only available via API. Please use the following endpoint to create your subaccount:

[**Endpoints**](https://durianpay.readme.io/reference/register-sub-account)

| Method | URL                                                |
| :----- | :------------------------------------------------- |
| POST   | <https://api.durianpay.id/v1/merchants/subaccount> |

```Text Bash
curl -X POST \
  https://api.durianpay.id/v1/merchants/subaccount \
  -H 'authorization: [Base64({Your_Secret_Key}:)]' \
  -H 'content-type: application/json' \
  -d '{
    "name": "Awesome Sub Organization 001",
    "email": "organization_001@masterorg.biz",
    "ref_id": "organization_001"    
  }'
```

You will then receive an API Response as following:

```Text Response
{
  "data": {
    "id": "mer_Y8fl6QL7pB9559",
    "name": "Awesome Sub Organization 001",
    "email": "testing@testing.co.it",
    "ref_id": "mer_123"
  }
}
```

## Step 2: Configure the fees of the subaccount

> ❗️ If fees are not yet configured for the subaccount, then Durianpay will charge the subaccount transaction based on the fees Durianpay charged to you as the master account

> ❗️ You can't set your subaccount fees lower than what Durianpay charges you for the transaction

Before you can start accepting any transaction, you have to first configure the fees of your subaccount.

The following are the endpoints along with the sample request body to configure your subaccount's fees

**Endpoints**

| Method | URL                                                    |
| :----- | :----------------------------------------------------- |
| POST   | <https://api.durianpay.id/v1/merchants/subaccount/fee> |

```Text Bash
curl --request POST \
     --url https://api.durianpay.id/v1/merchants/subaccount/fee \
     --header 'accept: application/json' \
     --header 'authorization: Basic ZHBfbGl2ZV9uUVA5VURybEVnRG5iMEVQOg==' \
     --header 'content-type: application/json' \
     --data '
{
  "id": "mer_Y8fl6QL7pB9559",
  "disbursement_fees": {
    "type": "fixed",
    "fee": "25"
  },
  "payment_fees": [
    {
      "payment_method_id": "BCA",
      "fixed_fee": "1000",
      "percentage_fee": "10"
    }
  ]
}
'
```

## Step 3: Get your subaccount activated

After you have configured your subaccount's fees, the subaccount will still stuck on sandbox mode until Durianpay activated the subaccount. Please contact our operations team (<merchantops@durianpay.id>) via email to enable your subaccount.

You can follow this email guideline to request the activation of your subaccount

> 📘 Subaccount Activation Email Format:
>
> 1. Subaccount Name:
> 2. Subaccount's merchant ID:
> 3. Subaccount's legal documents

After you have done all of these steps, your subaccount will then ready to start accepting their first transactions!