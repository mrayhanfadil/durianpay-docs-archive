---
updatedAt: 2025-08-14T09:37:27.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Integration Steps for SNAP

# Pre-requisite

Please follow the guidelines [Preparation / Prerequisite for SNAP API](https://docs.durianpay.id/docs/snap-preparation-prerequisite) for credentials setup, security and header creation

# Sandbox Access

Use <https://api-sandbox.durianpay.id/v1.0> as base URL for Sandbox environment and <https://api.durianpay.id/v1.0> for Live environment

# Step 1: Validate Account Number

Before doing disbursement to the beneficiary. You may want to check whether the account is valid and it's a correct beneficiary. We provide validate account API to check whether the destination account is valid and will also return the account name for you to confirm the disbursement destination.  It is currently differentiated for Bank destination and E-wallet destination

> beneficiaryAccountName requested by merchant should be the same with bank stated name, that's why we recommend merchant to do account number validation first

> 📘 Account validation will not immediately return success response but rather Accepted. You will need to hit the API again to get success value. We recommend to try it in: 2s, 10s, 30s, 1m, 5m
>
> The numbers stated above is a guideline only, you can adjust it accordingly based on your system implementation\
> Please take notes in rare cases, it can take longer to get the final status of a transaction.

<br />

## Bank Account Validation

Bank Account validation API is used to verify whether a disbursement destination account is valid/ invalid. If the account is valid, it will give information of the destination name according to the the bank/provider.

**Request Sample**\
POST Method , URL: /account-inquiry-external

```json Bash
curl --location 'https://api.durianpay.id/v1.0/account-inquiry-external' \
--header 'X-TIMESTAMP: 2024-05-14T18:54:57+07:00' \
--header 'X-SIGNATURE: pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==' \
--header 'X-PARTNER-ID: partner_id' \
--header 'X-EXTERNAL-ID: random_external_id' \
--header 'CHANNEL-ID: channel_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI' \
--data '{
    "beneficiaryAccountNo": "087783146495",
    "beneficiaryBankCode": "002",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}'
```
```python Python
import requests

url = 'https://api.durianpay.id/v1.0/account-inquiry-external'
headers = {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
}
data = {
    "beneficiaryAccountNo": "087783146495",
    "beneficiaryBankCode": "002",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"beneficiaryAccountNo\": \"087783146495\",\n    \"beneficiaryBankCode\": \"002\",\n    \"partnerReferenceNo\": \"202010290000000000000\",\n    \"additionalInfo\": {\n        \"deviceId\": \"12345679237\",\n        \"channel\": \"mobilephone\"\n    }\n}");
        
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/account-inquiry-external")
    .post(body)
    .addHeader("X-TIMESTAMP", "2024-05-14T18:54:57+07:00")
    .addHeader("X-SIGNATURE", "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==")
    .addHeader("X-PARTNER-ID", "partner_id")
    .addHeader("X-EXTERNAL-ID", "random_external_id")
    .addHeader("CHANNEL-ID", "channel_id")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI")
    .build();

Response response = client.newCall(request).execute();
System.out.println(response.body().string());
```
```javascript JavaScript
const request = require('request');

const url = 'https://api.durianpay.id/v1.0/account-inquiry-external';
const headers = {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
};
const data = {
    "beneficiaryAccountNo": "087783146495",
    "beneficiaryBankCode": "002",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
};

request.post({
    url: url,
    headers: headers,
    json: data
}, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log(body);
    }
});
```
```ruby Ruby
require 'uri'
require 'net/http'
require 'json'

url = URI("https://api.durianpay.id/v1.0/account-inquiry-external")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-TIMESTAMP"] = "2024-05-14T18:54:57+07:00"
request["X-SIGNATURE"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-PARTNER-ID"] = "partner_id"
request["X-EXTERNAL-ID"] = "random_external_id"
request["CHANNEL-ID"] = "channel_id"
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"

data = {
  "beneficiaryAccountNo": "087783146495",
  "beneficiaryBankCode": "002",
  "partnerReferenceNo": "202010290000000000000",
  "additionalInfo": {
      "deviceId": "12345679237",
      "channel": "mobilephone"
  }
}

request.body = data.to_json

response = http.request(request)
puts response.read_body
```

**Response Sample**

```json 2021600 Request In Progress
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237"
    },
    "beneficiaryAccountName": "",
    "beneficiaryAccountNo": "087783146495",
    "beneficiaryBankCode": "002",
    "beneficiaryBankName": "Bank Rakyat Indonesia",
    "currency": "IDR",
    "partnerReferenceNo": "202010290000000000000",
    "responseCode": "2021600",
    "responseMessage": "Request In Progress"
}
```
```json 2001600 Successful
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237"
    },
    "beneficiaryAccountName": "John Doe",
    "beneficiaryAccountNo": "087783146495",
    "beneficiaryBankCode": "002",
    "beneficiaryBankName": "Bank Rakyat Indonesia",
    "currency": "IDR",
    "partnerReferenceNo": "202010290000000000000",
    "responseCode": "2001600",
    "responseMessage": "Successful"
}
```
```json 4041611 Invalid Account
{
    "responseCode": "4041611",
    "responseMessage": "Invalid Card/Account/Customer Info/Virtual Account"
}
```

**Response Definition:**

| Case                | Response Code | Response Message                                   | beneficiaryAccountName                          |
| :------------------ | :------------ | :------------------------------------------------- | :---------------------------------------------- |
| Request In Progress | 2021600       | Request In Progress                                | Empty ("")                                      |
| Successful          | 2001600       | Successful                                         | Will show Account Name based on bank validation |
| Invalid Account     | 4041611       | Invalid Card/Account/Customer Info/Virtual Account | Not exist                                       |

## E-Wallet Account Validation

Validation for e-wallet account, the general flow is the same except URL used and the bank code.

* Instead of beneficiaryAccountNo, e-wallet has parameter called customerNumber
* Instead of beneficiaryBankCode, you need to put e-wallet code inside additionalInfo as platformCode. See here for more information.

**Request Sample**

POST Method , URL:  /emoney/account-inquiry

```json Bash
curl --location 'https://api.durianpay.id/v1.0/emoney/account-inquiry' \
--header 'X-TIMESTAMP: 2024-05-14T18:54:57+07:00' \
--header 'X-SIGNATURE: pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==' \
--header 'X-PARTNER-ID: partner_id' \
--header 'X-EXTERNAL-ID: random_external_id' \
--header 'CHANNEL-ID: channel_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI' \
--data '{
    "customerNumber": "087783146495",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone",
        "platformCode": "gopay"
    }
}'
```
```python Python
import requests

url = 'https://api.durianpay.id/v1.0/emoney/account-inquiry'
headers = {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
}
data = {
    "customerNumber": "087783146495",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone",
        "platformCode": "gopay"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"customerNumber\": \"087783146495\",\n    \"partnerReferenceNo\": \"202010290000000000000\",\n    \"additionalInfo\": {\n        \"deviceId\": \"12345679237\",\n        \"channel\": \"mobilephone\",\n    \"platformCode\": \"gopay\"\n    }\n}");   
        
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/emoney/account-inquiry")
    .post(body)
    .addHeader("X-TIMESTAMP", "2024-05-14T18:54:57+07:00")
    .addHeader("X-SIGNATURE", "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==")
    .addHeader("X-PARTNER-ID", "partner_id")
    .addHeader("X-EXTERNAL-ID", "random_external_id")
    .addHeader("CHANNEL-ID", "channel_id")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI")
    .build();

Response response = client.newCall(request).execute();
System.out.println(response.body().string());
```
```javascript JavaScript
const request = require('request');

const url = 'https://api.durianpay.id/v1.0/emoney/account-inquiry';
const headers = {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
};
const data = {
    "customerNumber": "087783146495",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone",
        "platformCode": "gopay"
    }
};

request.post({
    url: url,
    headers: headers,
    json: data
}, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log(body);
    }
});
```
```ruby Ruby
require 'uri'
require 'net/http'
require 'json'

url = URI("https://api.durianpay.id/v1.0/emoney/account-inquiry")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-TIMESTAMP"] = "2024-05-14T18:54:57+07:00"
request["X-SIGNATURE"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-PARTNER-ID"] = "partner_id"
request["X-EXTERNAL-ID"] = "random_external_id"
request["CHANNEL-ID"] = "channel_id"
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"

data = {
    "customerNumber": "087783146495",
    "partnerReferenceNo": "202010290000000000000",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone",
        "platformCode": "gopay"
    }
}

request.body = data.to_json

response = http.request(request)
puts response.read_body
```

**Response Sample:**

```json 2023700: Request In Progress
{
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone",
        "platformCode": "gopay"
    },
    "customerNumber": "087783146495",
    "currency": "IDR",
    "customerName": "",
    "partnerReferenceNo": "202010290000000000000",
    "responseCode": "2023700",
    "responseMessage": "Request In Progress"
}

```
```json 2003700: Successful
{
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone",
        "platformCode": "gopay"
    },
    "customerNumber": "087783146495",
    "currency": "IDR",
    "customerName": "John Doe",
    "partnerReferenceNo": "202010290000000000000",
    "responseCode": "2003700",
    "responseMessage": "Successful"
}

```
```Text 4043711: Invalid Account
{
    "responseCode": "4043711",
    "responseMessage": "Invalid Card/Account/Customer Info/Virtual Account"
}
```

<br />

**Response Definition:**

| Case                | Response Code | Response Message                                   | beneficiaryAccountName                                       |
| :------------------ | :------------ | :------------------------------------------------- | :----------------------------------------------------------- |
| Request In Progress | 2023700       | Request In Progress                                | Empty ("")                                                   |
| Successful          | 2003700       | Successful                                         | Will show Customer Name based on e-wallet account validation |
| Invalid Account     | 4043711       | Invalid Card/Account/Customer Info/Virtual Account | Not exist                                                    |

# Step 2: Submitting Disbursement

Submit Disbursement API is used to Create Disbursement in Durianpay, like account validation, it's differentiated into Bank Account Transfer API and E-Wallet Account Transfer API. This API is only used to trigger the disbursement and the response will be reflecting that disbursement is accepted and will be processed by Durianpay. To get final status of disbursement, please implement Step 3: Getting Disbursement Final status

> 📘 Before starting to do disbursement you may need to populate the destination bank that is supported here.

In case of time out or internal server error, merchant can try to submit disbursement with the same partnerReferenceNo to see if previous disbursement was submitted or not.

<br />

## Bank Account Transfer

Submit a disbursement batch or basically create a disbursement batch. The disbursement needs to be submitted via submit disbursement API.

> 📘 Submit disbursement will not immediately return success response but rather Accepted. You will need to hit the inquiry status API or handle callback to get the final status.
>
> The numbers stated above is a guideline only, you can adjust it accordingly based on your system implementation\
> Please take notes in rare cases, it can take longer to get the final status of a transaction.

**Request Sample**

POST Method , URL:  /transfer-interbank

```json Bash
curl --location 'https://api.durianpay.id/v1.0/transfer-interbank' \
--header 'X-TIMESTAMP: 2024-05-14T18:54:57+07:00' \
--header 'X-SIGNATURE: pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==' \
--header 'X-PARTNER-ID: partner_id' \
--header 'X-EXTERNAL-ID: random_external_id' \
--header 'CHANNEL-ID: 95221' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI' \
--data '{
    "partnerReferenceNo": "111111111",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "beneficiaryAccountName": "Dummy Name",
    "beneficiaryAccountNo": "888801000003301",
    "beneficiaryAddress": "Palembang",
    "beneficiaryBankCode": "002",
    "beneficiaryBankName": "Bank BRI",
    "beneficiaryEmail": "yories.yolanda@work.bri.co.id",
    "currency": "IDR",
    "customerReference": "10052019",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}'
```
```python Python
import requests

url = "https://api.durianpay.id/v1.0/transfer-interbank"
headers = {
    "X-TIMESTAMP": "2024-05-14T18:54:57+07:00",
    "X-SIGNATURE": "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==",
    "X-PARTNER-ID": "partner_id",
    "X-EXTERNAL-ID": "random_external_id",
    "CHANNEL-ID": "channel_id",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"
}
data = {
    "partnerReferenceNo": "111111111",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "beneficiaryAccountName": "Dummy Name",
    "beneficiaryAccountNo": "888801000003301",
    "beneficiaryAddress": "Palembang",
    "beneficiaryBankCode": "002",
    "beneficiaryBankName": "Bank BRI",
    "beneficiaryEmail": "yories.yolanda@work.bri.co.id",
    "currency": "IDR",
    "customerReference": "10052019",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"partnerReferenceNo\": \"111111111\",\n    \"amount\": {\n        \"value\": \"20000.00\",\n        \"currency\": \"IDR\"\n    },\n    \"beneficiaryAccountName\": \"Dummy Name\",\n    \"beneficiaryAccountNo\": \"888801000003301\",\n    \"beneficiaryAddress\": \"Palembang\",\n    \"beneficiaryBankCode\": \"002\",\n    \"beneficiaryBankName\": \"Bank BRI\",\n    \"beneficiaryEmail\": \"yories.yolanda@work.bri.co.id\",\n    \"currency\": \"IDR\",\n    \"customerReference\": \"10052019\",\n    \"transactionDate\": \"2019-07-03T12:08:56-07:00\",\n    \"additionalInfo\": {\n        \"deviceId\": \"12345679237\",\n        \"channel\": \"mobilephone\"\n    }\n}");
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/transfer-interbank")
    .post(body)
    .addHeader("X-TIMESTAMP", "2024-05-14T18:54:57+07:00")
    .addHeader("X-SIGNATURE", "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==")
    .addHeader("X-PARTNER-ID", "partner_id")
    .addHeader("X-EXTERNAL-ID", "random_external_id")
    .addHeader("CHANNEL-ID", "channel_id")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI")
    .build();

Response response = client.newCall(request).execute();
System.out.println(response.body().string());
```
```javascript JavaScript
const request = require('request');

const options = {
  method: 'POST',
  url: 'https://api.durianpay.id/v1.0/transfer-interbank',
  headers: {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
  },
  body: JSON.stringify({
    partnerReferenceNo: '111111111',
    amount: {
      value: '20000.00',
      currency: 'IDR'
    },
    beneficiaryAccountName: 'Dummy Name',
    beneficiaryAccountNo: '888801000003301',
    beneficiaryAddress: 'Palembang',
    beneficiaryBankCode: '002',
    beneficiaryBankName: 'Bank BRI',
    beneficiaryEmail: 'yories.yolanda@work.bri.co.id',
    currency: 'IDR',
    customerReference: '10052019',
    transactionDate: '2019-07-03T12:08:56-07:00',
    additionalInfo: {
      deviceId: '12345679237',
      channel: 'mobilephone'
    }
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);
  console.log(body);
});
```
```ruby Ruby
require 'net/http'
require 'uri'
require 'json'

uri = URI.parse("https://api.durianpay.id/v1.0/transfer-interbank")
request = Net::HTTP::Post.new(uri)
request.content_type = "application/json"
request["X-Timestamp"] = "2024-05-14T18:54:57+07:00"
request["X-Signature"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-Partner-Id"] = "partner_id"
request["X-External-Id"] = "random_external_id"
request["Channel-Id"] = "channel_id"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"

request.body = {
  partnerReferenceNo: "111111111",
  amount: {
    value: "20000.00",
    currency: "IDR"
  },
  beneficiaryAccountName: "Dummy Name",
  beneficiaryAccountNo: "888801000003301",
  beneficiaryAddress: "Palembang",
  beneficiaryBankCode: "002",
  beneficiaryBankName: "Bank BRI",
  beneficiaryEmail: "yories.yolanda@work.bri.co.id",
  currency: "IDR",
  customerReference: "10052019",
  transactionDate: "2019-07-03T12:08:56-07:00",
  additionalInfo: {
    deviceId: "12345679237",
    channel: "mobilephone"
  }
}.to_json

response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https") do |http|
  http.request(request)
end

puts response.body
```

**Response Sample**

```json Response
// Sample response
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237"
    },
    "amount": {
        "currency": "IDR",
        "value": "20000.00",
    },
    "beneficiaryAccountNo": "888801000003301",
    "beneficiaryBankCode": "002",
    "partnerReferenceNo": "111111111",
    "referenceNo": "dis_item_zqMYiSqsPO",
    "responseCode": "2021800",
    "responseMessage": "Request In Progress",
    "sourceAccountNo": "mer_MsCtIPhqRc8045"
}
```

## E-wallet Account Transfer

> 📘 For e-wallet, instead of beneficiaryBankCode, you will need to put platformCode inside additionalInfo containing e-wallet code
>
> See this table to see which e-wallet supported and its respective platform code

**Request Sample**

POST Method, URL: /emoney/topup

```json Bash
curl --location 'https://api.durianpay.id/v1.0/emoney/topup' \
--header 'X-TIMESTAMP: 2024-05-14T18:54:57+07:00' \
--header 'X-SIGNATURE: pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==' \
--header 'X-PARTNER-ID: partner_id' \
--header 'X-EXTERNAL-ID: random_external_id' \
--header 'CHANNEL-ID: channel_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI' \
--data '{
    "partnerReferenceNo": "111111111",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "customerName": "Dummy Name",
    "customerNumber": "888801000003301",
    "currency": "IDR",
    "customerReference": "10052019",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "additionalInfo": {
        "platformCode": "gopay",
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}'
```
```python Python
import requests

url = "https://api.durianpay.id/v1.0/emoney/topup"
headers = {
    "X-TIMESTAMP": "2024-05-14T18:54:57+07:00",
    "X-SIGNATURE": "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==",
    "X-PARTNER-ID": "partner_id",
    "X-EXTERNAL-ID": "random_external_id",
    "CHANNEL-ID": "channel_id",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"
}
data = {
    "partnerReferenceNo": "111111111",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "customerName": "Dummy Name",
    "customerNumber": "888801000003301",
    "currency": "IDR",
    "customerReference": "10052019",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "additionalInfo": {
        "platformCode": "gopay",
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n" +
    "    \"partnerReferenceNo\": \"111111111\",\n" +
    "    \"amount\": {\n" +
    "        \"value\": \"20000.00\",\n" +
    "        \"currency\": \"IDR\"\n" +
    "    },\n" +
    "    \"customerName\": \"Dummy Name\",\n" +
    "    \"customerNumber\": \"888801000003301\",\n" +
    "    \"currency\": \"IDR\",\n" +
    "    \"customerReference\": \"10052019\",\n" +
    "    \"transactionDate\": \"2019-07-03T12:08:56-07:00\",\n" +
    "    \"additionalInfo\": {\n" +
    "        \"platformCode\": \"gopay\",\n" +
    "        \"deviceId\": \"12345679237\",\n" +
    "        \"channel\": \"mobilephone\"\n" +
    "    }\n" +
    "}");
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/emoney/topup")
    .post(body)
    .addHeader("X-TIMESTAMP", "2024-05-14T18:54:57+07:00")
    .addHeader("X-SIGNATURE", "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==")
    .addHeader("X-PARTNER-ID", "partner_id")
    .addHeader("X-EXTERNAL-ID", "random_external_id")
    .addHeader("CHANNEL-ID", "channel_id")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI")
    .build();

Response response = client.newCall(request).execute();
System.out.println(response.body().string());
```
```javascript JavaScript
const request = require('request');

const options = {
  url: 'https://api.durianpay.id/v1.0/emoney/topup',
  headers: {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
  },
  body: JSON.stringify({
    "partnerReferenceNo": "111111111",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "customerName": "Dummy Name",
    "customerNumber": "888801000003301",
    "currency": "IDR",
    "customerReference": "10052019",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "additionalInfo": {
        "platformCode": "gopay",
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
  })
};

request.post(options, (error, response, body) => {
  if (error) throw new Error(error);
  console.log(body);
});
```
```ruby Ruby
require 'net/http'
require 'uri'
require 'json'

uri = URI.parse("https://api.durianpay.id/v1.0/emoney/topup")
request = Net::HTTP::Post.new(uri)
request["X-Timestamp"] = "2024-05-14T18:54:57+07:00"
request["X-Signature"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-Partner-Id"] = "partner_id"
request["X-External-Id"] = "random_external_id"
request["Channel-Id"] = "channel_id"
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"
request.body = JSON.dump({
    "partnerReferenceNo": "111111111",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "customerName": "Dummy Name",
    "customerNumber": "888801000003301",
    "currency": "IDR",
    "customerReference": "10052019",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "additionalInfo": {
        "platformCode": "gopay",
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}).to_json

response = http.request(request)
puts "Response status code: #{response.code}"
puts "Response body: #{response.body}"
```

**Response Sample**

```json Response
// Sample response
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237",
        "platformCode" : "gopay"
    },
    "customerName": "Dummy Name",
    "customerNumber": "087783146495",
    "referenceNo": "dis_item_123",
    "currency": "IDR",
    "partnerReferenceNo": "202010290000000000000",
    "responseCode": "2021600",
    "responseMessage": "Request In Progress"
}
```

<br />

# Step 3: Getting Disbursement Final Status

There are two ways to get final status of a disbursement: By doing disbursement status inquiry, or/and implement disbursement status notify

## 3.1 Disbursement Status Inquiry

> 📘 Use previous referenceNo or partnerReferenceNo from the original request get disbursement status
>
> Similar to account validation, here are recommended duration to get final disbursement status: 30s, 1m, 5m, 10m, 30m\
> The numbers stated above is a guideline only, you can adjust it accordingly based on your system implementation. Please take notes in rare cases, it can take longer to get the final status of a transaction.

### Bank Account Transfer Inquiry

**Request Sample**

POST Method , URL: /transfer/status

```json Bash
curl --location 'https://api.durianpay.id/v1.0/transfer/status' \
--header 'X-TIMESTAMP: 2024-05-14T18:54:57+07:00' \
--header 'X-SIGNATURE: pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==' \
--header 'X-PARTNER-ID: partner_id' \
--header 'X-EXTERNAL-ID: random_external_id' \
--header 'CHANNEL-ID: 95221' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI' \
--data '{
    "originalPartnerReferenceNo": "111111111",
    "originalReferenceNo": "dis_item_vhLkXOtB0s6619",
    "originalExternalId": "30443786930722726463280097920912",
    "serviceCode": "18",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}'
```
```python Python
import requests

url = "https://api.durianpay.id/v1.0/transfer/status"
headers = {
    "X-TIMESTAMP": "2024-05-14T18:54:57+07:00",
    "X-SIGNATURE": "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==",
    "X-PARTNER-ID": "partner_id",
    "X-EXTERNAL-ID": "random_external_id",
    "CHANNEL-ID": "channel_id",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"
}
data = {
    "originalPartnerReferenceNo": "111111111",
    "originalReferenceNo": "dis_item_vhLkXOtB0s6619",
    "originalExternalId": "30443786930722726463280097920912",
    "serviceCode": "18",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"originalPartnerReferenceNo\": \"111111111\",\n    \"originalReferenceNo\": \"dis_item_vhLkXOtB0s6619\",\n    \"originalExternalId\": \"30443786930722726463280097920912\",\n    \"serviceCode\": \"18\",\n    \"transactionDate\": \"2019-07-03T12:08:56-07:00\",\n    \"amount\": {\n        \"value\": \"20000.00\",\n        \"currency\": \"IDR\"\n    },\n    \"additionalInfo\": {\n        \"deviceId\": \"12345679237\",\n        \"channel\": \"mobilephone\"\n    }\n}");
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/transfer/status")
    .post(body)
    .addHeader("X-TIMESTAMP", "2024-05-14T18:54:57+07:00")
    .addHeader("X-SIGNATURE", "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==")
    .addHeader("X-PARTNER-ID", "partner_id")
    .addHeader("X-EXTERNAL-ID", "random_external_id")
    .addHeader("CHANNEL-ID", "channel_id")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI")
    .build();

Response response = client.newCall(request).execute();
System.out.println(response.body().string());
```
```javascript JavaScript
const request = require('request');

const options = {
  method: 'POST',
  url: 'https://api.durianpay.id/v1.0/transfer/status',
  headers: {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': '95221',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
  },
  body: JSON.stringify({
    originalPartnerReferenceNo: '111111111',
    originalReferenceNo: 'dis_item_vhLkXOtB0s6619',
    originalExternalId: '30443786930722726463280097920912',
    serviceCode: '18',
    transactionDate: '2019-07-03T12:08:56-07:00',
    amount: {
      value: '20000.00',
      currency: 'IDR'
    },
    additionalInfo: {
      deviceId: '12345679237',
      channel: 'mobilephone'
    }
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);
  console.log(body);
});
```
```ruby Ruby
require 'net/http'
require 'uri'
require 'json'

uri = URI.parse("https://api.durianpay.id/v1.0/transfer/status")
request = Net::HTTP::Post.new(uri)
request.content_type = "application/json"
request["X-Timestamp"] = "2024-05-14T18:54:57+07:00"
request["X-Signature"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-Partner-Id"] = "partner_id"
request["X-External-Id"] = "random_external_id"
request["Channel-Id"] = "95221"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"

request.body = {
  originalPartnerReferenceNo: "111111111",
  originalReferenceNo: "dis_item_vhLkXOtB0s6619",
  originalExternalId: "30443786930722726463280097920912",
  serviceCode: "18",
  transactionDate: "2019-07-03T12:08:56-07:00",
  amount: {
    value: "20000.00",
    currency: "IDR"
  },
  additionalInfo: {
    deviceId: "12345679237",
    channel: "mobilephone"
  }
}.to_json

response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https") do |http|
  http.request(request)
end

puts response.body
```

> 📘 There are 3 state of disbursement/transfer: success, processing, and failed
>
> Success will have transaction status "00"\
> Processing will have transaction status "03"
> Failed will have transaction status "06"

> The HTTP Code itself might show 200, but the transfer status can be failed, since call to the API is success, but not the transfer, please refer to "latestTransactionStatus" attribute

```json Success Response
// Sample Response if transfer is success
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237"
    },
    "amount": {
        "currency": "IDR",
        "value": "12345678"
    },
    "beneficiaryAccountNo": "123123123",
    "beneficiaryBankCode": "002",
    "currency": "IDR",
    "latestTransactionStatus": "00",
    "originalExternalId": "30443786930722726463280097920912",
    "originalPartnerReferenceNo": "111111111",
    "originalReferenceNo": "dis_item_vhLkXOtB0s6619",
    "previousResponseCode": "2021800",
    "referenceNumber": "123123",
    "responseCode": "2003600",
    "responseMessage": "Successful",
    "serviceCode": "18",
    "sourceAccountNo": "123123",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "transactionId": "123123",
    "transactionStatusDesc": "success"
    }
}
```
```json Processing Response
// Sample Response if transfer is still processing
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237"
    },
    "amount": {
        "currency": "IDR",
        "value": "20000.00",
    },
    "beneficiaryAccountNo": "123123123",
    "beneficiaryBankCode": "002",
    "currency": "IDR",
    "latestTransactionStatus": "03",
    "originalExternalId": "30443786930722726463280097920912",
    "originalPartnerReferenceNo": "111111111",
    "originalReferenceNo": "dis_item_vhLkXOtB0s6619",
    "previousResponseCode": "2021800",
    "referenceNumber": "123123",
    "responseCode": "2003600",
    "responseMessage": "OK",
    "serviceCode": "18",
    "sourceAccountNo": "123123",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "transactionId": "123123",
    "transactionStatusDesc": "processing"
    }
}
```
```json Failed Response
// Sample Response if transfer is failed
{
    "additionalInfo": {
        "channel": "mobilephone",
        "deviceId": "12345679237"
    },
    "amount": {
        "currency": "IDR",
        "value": "20000.00",
    },
    "beneficiaryAccountNo": "123123123",
    "beneficiaryBankCode": "002",
    "currency": "IDR",
    "latestTransactionStatus": "06",
    "originalExternalId": "30443786930722726463280097920912",
    "originalPartnerReferenceNo": "111111111",
    "originalReferenceNo": "dis_item_vhLkXOtB0s6619",
    "previousResponseCode": "2021800",
    "referenceNumber": "123123",
    "responseCode": "2003600",
    "responseMessage": "OK",
    "serviceCode": "18",
    "sourceAccountNo": "123123",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "transactionId": "123123",
    "transactionStatusDesc": "failed"
    }
}
```

### E-wallet Transfer Inquiry Status

**Request Sample**

POST Method , URL: /emoney/account-inquiry

```json Bash
require 'net/http'
require 'uri'
require 'json'

uri = URI.parse("https://api.durianpay.id/v1.0/transfer/status")
request = Net::HTTP::Post.new(uri)
request.content_type = "application/json"
request["X-Timestamp"] = "2024-05-14T18:54:57+07:00"
request["X-Signature"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-Partner-Id"] = "partner_id"
request["X-External-Id"] = "random_external_id"
request["Channel-Id"] = "channel_id"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"

request.body = {
  originalPartnerReferenceNo: "111111111",
  originalReferenceNo: "dis_item_vhLkXOtB0s6619",
  originalExternalId: "30443786930722726463280097920912",
  serviceCode: "18",
  transactionDate: "2019-07-03T12:08:56-07:00",
  amount: {
    value: "20000.00",
    currency: "IDR"
  },
  additionalInfo: {
    deviceId: "12345679237",
    channel: "mobilephone"
  }
}.to_json

response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https") do |http|
  http.request(request)
end

puts response.body
```
```python Python
import requests

url = "https://api.durianpay.id/v1.0/transfer/status"
headers = {
    "X-TIMESTAMP": "2024-05-14T18:54:57+07:00",
    "X-SIGNATURE": "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==",
    "X-PARTNER-ID": "partner_id",
    "X-EXTERNAL-ID": "random_external_id",
    "CHANNEL-ID": "channel_id",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"
}
data = {
    "originalPartnerReferenceNo": "111111111",
    "originalReferenceNo": "dis_item_vhLkXOtB0s6619",
    "originalExternalId": "30443786930722726463280097920912",
    "serviceCode": "18",
    "transactionDate": "2019-07-03T12:08:56-07:00",
    "amount": {
        "value": "20000.00",
        "currency": "IDR"
    },
    "additionalInfo": {
        "deviceId": "12345679237",
        "channel": "mobilephone"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"originalPartnerReferenceNo\": \"111111111\",\n    \"originalReferenceNo\": \"dis_item_vhLkXOtB0s6619\",\n    \"originalExternalId\": \"30443786930722726463280097920912\",\n    \"serviceCode\": \"18\",\n    \"transactionDate\": \"2019-07-03T12:08:56-07:00\",\n    \"amount\": {\n        \"value\": \"20000.00\",\n        \"currency\": \"IDR\"\n    },\n    \"additionalInfo\": {\n        \"deviceId\": \"12345679237\",\n        \"channel\": \"mobilephone\"\n    }\n}");
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/transfer/status")
    .post(body)
    .addHeader("X-TIMESTAMP", "2024-05-14T18:54:57+07:00")
    .addHeader("X-SIGNATURE", "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==")
    .addHeader("X-PARTNER-ID", "partner_id")
    .addHeader("X-EXTERNAL-ID", "random_external_id")
    .addHeader("CHANNEL-ID", "channel_id")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI")
    .build();

Response response = client.newCall(request).execute();
System.out.println(response.body().string());

```
```javascript JavaScript
const request = require('request');

const options = {
  method: 'POST',
  url: 'https://api.durianpay.id/v1.0/transfer/status',
  headers: {
    'X-TIMESTAMP': '2024-05-14T18:54:57+07:00',
    'X-SIGNATURE': 'pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ==',
    'X-PARTNER-ID': 'partner_id',
    'X-EXTERNAL-ID': 'random_external_id',
    'CHANNEL-ID': 'channel_id',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI'
  },
  body: JSON.stringify({
    originalPartnerReferenceNo: '111111111',
    originalReferenceNo: 'dis_item_vhLkXOtB0s6619',
    originalExternalId: '30443786930722726463280097920912',
    serviceCode: '18',
    transactionDate: '2019-07-03T12:08:56-07:00',
    amount: {
      value: '20000.00',
      currency: 'IDR'
    },
    additionalInfo: {
      deviceId: '12345679237',
      channel: 'mobilephone'
    }
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);
  console.log(body);
});
```
```ruby Ruby
require 'net/http'
require 'uri'
require 'json'

uri = URI.parse("https://api.durianpay.id/v1.0/transfer/status")
request = Net::HTTP::Post.new(uri)
request.content_type = "application/json"
request["X-Timestamp"] = "2024-05-14T18:54:57+07:00"
request["X-Signature"] = "pCA+q832pxHnTPm1Kdbfu1am37J9XFeGH13JGYqHv7Ww4Tb3Hrc5xRew+4y2tN4wiAPnHmvXcJ1Tyf94jK5gHQ=="
request["X-Partner-Id"] = "partner_id"
request["X-External-Id"] = "random_external_id"
request["Channel-Id"] = "channel_id"
request["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTM3NTYsImlhdCI"

request.body = {
  originalPartnerReferenceNo: "111111111",
  originalReferenceNo: "dis_item_vhLkXOtB0s6619",
  originalExternalId: "30443786930722726463280097920912",
  serviceCode: "18",
  transactionDate: "2019-07-03T12:08:56-07:00",
  amount: {
    value: "20000.00",
    currency: "IDR"
  },
  additionalInfo: {
    deviceId: "12345679237",
    channel: "mobilephone"
  }
}.to_json

response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: uri.scheme == "https") do |http|
  http.request(request)
end

puts response.body
```

**Response Sample**

```json Success  Response
{
    "amount": {
        "currency": "IDR",
        "value": "12345678.00"
    },
    "latestTransactionStatus": "00",
    "originalPartnerReferenceNo": "2020102900000000000011",
    "originalReferenceNo": "dis_item_SgWsZEAh1m5870",
    "responseCode": "2003900",
    "responseMessage": "Successful",
    "serviceCode": "38",
    "transactionStatusDesc": "success"
}
```
```json Processing Response
{
    "amount": {
        "currency": "IDR",
        "value": "12345678.00"
    },
    "latestTransactionStatus": "03",
    "originalPartnerReferenceNo": "2020102900000000000011",
    "originalReferenceNo": "dis_item_SgWsZEAh1m5870",
    "responseCode": "2003900",
    "responseMessage": "Successful",
    "serviceCode": "38",
    "transactionStatusDesc": "processing"
}
```
```json Failed Response
{
    "amount": {
        "currency": "IDR",
        "value": "12345678.00"
    },
    "latestTransactionStatus": "06",
    "originalPartnerReferenceNo": "2020102900000000000011",
    "originalReferenceNo": "dis_item_SgWsZEAh1m5870",
    "responseCode": "2003900",
    "responseMessage": "Successful",
    "serviceCode": "38",
    "transactionStatusDesc": "failed"
}
```

<br />

## 3.2 Disbursement Notify / Callback Handling

Whenever certain transaction actions occur on your Durianpay SNAP Disbursement integration, we trigger events which your application can listen to. This is where webhooks come in. A webhook is a URL on your server where we send payloads for such events. For example, if you implement webhooks, once a disbursement is successful, we will immediately notify your server with a transfer-bank.notify event.

Durianpay will send the webhook to you directly when an event change occurred, followed by 2, 5, 10, 90, 210 minutes retry if the webhook is not acknowledged with 200 OK status.

You can specify your webhook URL on your dashboard `Settings - Webhook` where we would send POST requests to whenever an event occurs.

### Setting Up Webhook

* Create Webhooks in Settings > Create New

  <Image align="center" width="600px" src="https://files.readme.io/89617874a25e8ac655f32d9022819ca447b01d51722db92a586303c5aae04175-image.png" />
* Fill up the event you want to subscribe to, give a name to webhook event and add your url which you want us to call

  <Image align="center" width="600px" src="https://files.readme.io/7cf5a4795a191fcbd38c4200996518361c62d46b6e8f8dc524200ec741313e3b-image.png" />
* You need to configure only the base url, the path will be appended as per the selected webhook

  <Image align="center" width="600px" src="https://files.readme.io/9e47bd14f23986295e8db87d65b42f9de2b21df4fc0fccd5ce100af17b34f854-image.png" />
* Once you click create button, there will be sample webhook from Durianpay to be sent to the URL. In order to successfuly setup a webhook the URL should return 200 OK.
* Once you receive success notification on setting up webhook, you are ready to accept Durianpay webhook according to the event specified.

<br />

### Events after Pay Outs:

| Name                 | Description                                                          |
| :------------------- | :------------------------------------------------------------------- |
| transfer-bank.notify | This event is triggered when a disbursement is successful or failed. |

<Callout icon="📘" theme="info">
  Currently transfer-bank.notify event will be sent for both Bank Transfer & E-Wallet transfer API. So you need to only handle 1 webhook to get the final status for both bank transfer and e-wallet transfer.
</Callout>

### Webhook Sample

```json SNAP.transfer-bank.notify
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

### Handling Webhooks

Handle the webhook by checking the following fields in the additionalInfo parameter of the webhook body

| latestTransactionStatus | transactionStatusDesc | Description                               |
| :---------------------- | :-------------------- | :---------------------------------------- |
| 00                      | done                  | The transaction is successfully completed |
| 06                      | failed                | The transaction is failed                 |

### Digital Signature Verification

Follow these steps to validate the digital signature of the webhook

1. Take the signature from HTTP header "X-SIGNATURE"\
   The following is an example:
   `X-SIGNATURE`: VpByUVbCd1rf/K5sMBGJk2Nz2zLsH9L9PWCMzb/ouVB/rVh/wPTfzr4AIfW9LGzyKrXTihS75uIiKqhIRexS9sAsu+AXyPKVULKGBRIZJ1yNdbQQQfUS3HT4sbn+JgLlBWS7DozJGqR5LY6F0cQ8wceErqSGEiHQGut5bpCaUC3wEfDynujO33BIvKLF5Gy9XnDMRVvRs+r6pjlew5uCX0Z3vmYEVCHE/6pWvkvRONhwQfqzSvIc56MVInnPFraz5l0DdendQbHhiCg0VIqhsp/aG7Ubxd2hS3o1PbnKiVjr07/mU5nhKhNlT8WtES7/5zh/Argl2Fkea8X+n70RBQ==
2. Compose the string to verify
   1. Sample Webhook payload:
      ```json Webhook Payload
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
      ```json Pseudo Code
      <HTTP METHOD> + ":" + <RELATIVE PATH URL> + ":" + LowerCase(HexEncode(SHA-256(Minify(<HTTP BODY>)))) + ":" + <X-TIMESTAMP>
      ```
      * For a webook url <https://www.example.com/callback/v1.0/transfer/notify>, the relative path url will be /callback/v1.0/transfer/notify
      * X-TIMESTAMP will be part of the webhook header
      * HTTP Method will be POST
   3. Example: POST:/callback/v1.0/transfer/notify:5d2c90ddfdd406117ced5c2b502c05b601d435c7e5440f82e58733fdd5f15b7d:2024-11-07T16:04:55.667+07:00
3. Verify the correctness of the signature based on SHA-256 with RSA-2048 encryption using PKCS#8 signing against the string to sign with provided Durianpay public key (please take notes that the public key will be different for Sandbox vs Live).
4. If the verification  is correct, you can safely consume the request and return HTTP 200 response.

**Script to verify digital signature**

```go
/*
script to verify webhook signature
to verify the signature, fill the necessary parametes inside main() method
and run the script using the command

`go run main.go`

*/

package main

import (
	"bytes"
	"crypto"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"encoding/pem"
	"errors"
	"fmt"
	"net/http"
	"strings"
)

func main() {
	// fill data here for the parameters
	requestBody := []byte(`{}`)
	relativeURL := ""
	timestamp := ""
	rsaPublicKey := ""
	xSignature := ""

	err := VerifyWebhookSignature(requestBody, relativeURL, timestamp, rsaPublicKey, xSignature)
	if err != nil {
		fmt.Println("signature verification failed")
		return
	}
	fmt.Println("signature verified")
}

func VerifyWebhookSignature(requestBody []byte, relativeURL string, timestamp string, rsaPublicKey string, xSignature string) (err error) {
	// body should be added to signature as Lowercase(HexEncode(SHA-256(minify(RequestBody))))
	var minifiedRequest bytes.Buffer
	err = json.Compact(&minifiedRequest, requestBody)
	if err != nil {
		fmt.Println("error minifying request body, error: ", err.Error())
		return
	}
	encodedRequest := generateHexEncodedSHA256(minifiedRequest.String())

	// Format -> SHA256withRSA (HTTPMethod + ":" + RelativeUrl + ":" + Lowercase(HexEncode(SHA-256(minify(RequestBody)))) + ":" + TimeStamp)
	verificationBody := strings.Join([]string{http.MethodPost, relativeURL, strings.ToLower(encodedRequest), timestamp}, ":")

	err = verifySignature([]byte(verificationBody), rsaPublicKey, xSignature)
	if err != nil {
		fmt.Println("error verifying signature, error: ", err.Error())
		return
	}
	return
}

func verifySignature(requestPayload []byte, rsaPublicKey string, signature string) (err error) {
	// base64 decode the signature
	decodedSignature, err := base64.StdEncoding.DecodeString(signature)
	if err != nil {
		fmt.Println("error base64 decoding signature, error: ", err.Error())
		return
	}

	rsaKey, err := getPKIXPublicKey(rsaPublicKey)
	if err != nil {
		fmt.Println("error parsing rsa public key, error: ", err.Error())
		return
	}

	hashed := sha256.Sum256(requestPayload)

	err = rsa.VerifyPKCS1v15(rsaKey, crypto.SHA256, hashed[:], decodedSignature)
	if err != nil {
		fmt.Println("error verifying signature, error: ", err.Error())
		return
	}
	return
}

func generateHexEncodedSHA256(msg string) string {
	h := sha256.New()
	h.Write([]byte(msg))
	return hex.EncodeToString(h.Sum(nil))
}

// getPKIXPublicKey takes in an RSA public key string.
// decode the PEM string and constructs an RSA public key with PKIX format
func getPKIXPublicKey(publicKey string) (rsaPublicKey *rsa.PublicKey, err error) {
	block, _ := pem.Decode([]byte(publicKey))
	if block == nil {
		err = errors.New("no key found")
		fmt.Println("error verifying signature, error: ", err.Error())
		return
	}

	key, err := x509.ParsePKIXPublicKey(block.Bytes)
	if err != nil {
		fmt.Println("error in parsing public key, error: ", err.Error())
		return
	}

	rsaPublicKey, ok := key.(*rsa.PublicKey)
	if !ok {
		err = errors.New("cannot type assert as rsa public key pointer")
		fmt.Println("error parsing public key, error: ", err.Error())
		return
	}
	return
}

```

<br />

# Step 4: Verifying Your Implementation in Sandbox

## 4.1 Bank Account Validation & E-Wallet Account Validation API

To simulate success case and failed case on bank account validation & e-wallet account validation you can use following rules:

| Case            | How to simulate                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------ |
| Valid account   | Use even number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation) |
| Invalid account | Use odd number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation)  |

<br />

## 4.2 Bank Account Transfer & E-Wallet Account Transfer API

To simulate success case or failed case, you can use following rules. The callback or inquiry status will be affected with the status of the transaction you simulate with.

| Case                              | How to Simulate                                                                                    |
| :-------------------------------- | :------------------------------------------------------------------------------------------------- |
| Accepted Transaction - Processing | Use even number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation)  |
| Failed transaction                | Use odd number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation)   |
| Success transaction               | Simulate in `Sandbox Mode` using `Simulator` Menu `Disbursements` tab then click `Mark as success` |

We provide simulator in `Sandbox Mode` to simulate real success/failed transaction via dashboard. You can find this `Simulator` menu at the bottom left of the menu bar.

<Image align="center" width="750px" src="https://files.readme.io/1b882fb9ff7347924048d6af37340e79ef4957c5c2db72e363f256c326f9309c-image.png" />

<br />

You can see the SNAP transaction details you created in the `Disbursements` -`Item Details`menu on the left side of the menu bar.

<Image align="center" width="750px" src="https://files.readme.io/b1a06e30f821a5a47efa21c036d20fd7eb446d153c246b1937f6d4738cfb0287-image.png" />

<br />

## 4.3 Handling final status : Inquiry status & Callback handling

After creating a transaction and simulating either a success or failed status, Durianpay will send a callback to the webhook URL you configured, based on the simulation status you selected. The inquiry status will also reflect the current status recorded in sandbox mode.

<br />

# Other Supporting API

## Balance Inquiry

This API can be used to check merchant's current balance.

**Request Sample**

POST Method , URL: /balance-inquiry

```json Bash
curl --location 'https://api.durianpay.id/v1.0/balance-inquiry' \
--header 'X-TIMESTAMP: 2023-07-31T10:55:00+07:00' \
--header 'X-SIGNATURE: SlCb5OKordx8WVhAE5bkg4M8U1vbI7hyHb07G/ydStvTIBmNgEzHj8PdLVbp2iWY1k2e/jgwWmKsrIj/AvH9rw==' \
--header 'X-PARTNER-ID: client_8045' \
--header 'X-EXTERNAL-ID: 202001' \
--header 'CHANNEL-ID: 95521' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1Nzk0MjYsImlhdCI6MTcxNTU3ODUyNiwibWVyY2hhbnRfaWQiOiJtZXJfTXNDdElQaHFSYzgwNDUiLCJncmFudF90eXBlIjoiQVVUSE9SSVpBVElPTl9DT0RFIiwiY2xpZW50X2tleSI6ImNsaWVudF84MDQ1In0.H2IMBY0MiGNvjHwVwXoYekajhPocBxflmodiHxbm0XA' \
--data '{
    "partnerReferenceNo": "2020102900000000000001",
    "accountNo": "7382382957893840",
    "bankCardToken": "12312312",
    "additionalInfo": {
        "deviceId": "123456",
        "channel": "phone"
    }
}'
```
```python Python
import requests

url = "https://api.durianpay.id/v1.0/balance-inquiry"
headers = {
    "X-TIMESTAMP": "2023-07-31T10:55:00+07:00",
    "X-SIGNATURE": "SlCb5OKordx8WVhAE5bkg4M8U1vbI7hyHb07G/ydStvTIBmNgEzHj8PdLVbp2iWY1k2e/jgwWmKsrIj/AvH9rw==",
    "X-PARTNER-ID": "client_8045",
    "X-EXTERNAL-ID": "202001",
    "CHANNEL-ID": "95521",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1Nzk0MjYsImlhdCI6MTcxNTU3ODUyNiwibWVyY2hhbnRfaWQiOiJtZXJfTXNDdElQaHFSYzgwNDUiLCJncmFudF90eXBlIjoiQVVUSE9SSVpBVElPTl9DT0RFIiwiY2xpZW50X2tleSI6ImNsaWVudF84MDQ1In0.H2IMBY0MiGNvjHwVwXoYekajhPocBxflmodiHxbm0XA"
}
data = {
    "partnerReferenceNo": "2020102900000000000001",
    "accountNo": "7382382957893840",
    "bankCardToken": "12312312",
    "additionalInfo": {
        "deviceId": "123456",
        "channel": "phone"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
```
```java Java
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"partnerReferenceNo\": \"2020102900000000000001\",\n    \"accountNo\": \"7382382957893840\",\n    \"bankCardToken\": \"12312312\",\n    \"additionalInfo\": {\n        \"deviceId\": \"123456\",\n        \"channel\": \"phone\"\n    }\n}");
Request request = new Request.Builder()
    .url("https://api.durianpay.id/v1.0/balance-inquiry")
    .post(body)
    .addHeader("X-TIMESTAMP", "2023-07-31T10:55:00+07:00")
    .addHeader("X-SIGNATURE", "SlCb5OKordx8WVhAE5bkg4M8U1vbI7hyHb07G/ydStvTIBmNgEzHj8PdLVbp2iWY1k2e/jgwWmKsrIj/AvH9rw==")
    .addHeader("X-PARTNER-ID", "client_8045")
    .addHeader("X-EXTERNAL-ID", "202001")
    .addHeader("CHANNEL-ID", "95521")
    .addHeader("Content-Type", "application/json")
    .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1Nzk0MjYsImlhdCI6MTcxNTU3ODUyNiwibWVyY2hhbnRfaWQiOiJtZXJfTXNDdElQaHFSYzgwNDUiLCJncmFudF90eXBlIjoiQVVUSE9SSVpBVElPTl9DT0RFIiwiY2xpZW50X2tleSI6ImNsaWVudF84MDQ1In0.H2IMBY0MiGNvjHwVwXoYekajhPocBxflmodiHxbm0XA")
    .build();

Response response = client.newCall(request).execute();
System.out.println("Response status code: " + response.code());
System.out.println("Response body: " + response.body().string());
```
```javascript JavaScript
const request = require('request');

const url = 'https://api.durianpay.id/v1.0/balance-inquiry';
const headers = {
    'X-TIMESTAMP': '2023-07-31T10:55:00+07:00',
    'X-SIGNATURE': 'SlCb5OKordx8WVhAE5bkg4M8U1vbI7hyHb07G/ydStvTIBmNgEzHj8PdLVbp2iWY1k2e/jgwWmKsrIj/AvH9rw==',
    'X-PARTNER-ID': 'client_8045',
    'X-EXTERNAL-ID': '202001',
    'CHANNEL-ID': '95521',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1Nzk0MjYsImlhdCI6MTcxNTU3ODUyNiwibWVyY2hhbnRfaWQiOiJtZXJfTXNDdElQaHFSYzgwNDUiLCJncmFudF90eXBlIjoiQVVUSE9SSVpBVElPTl9DT0RFIiwiY2xpZW50X2tleSI6ImNsaWVudF84MDQ1In0.H2IMBY0MiGNvjHwVwXoYekajhPocBxflmodiHxbm0XA'
};
const data = {
    "partnerReferenceNo": "2020102900000000000001",
    "accountNo": "7382382957893840",
    "bankCardToken": "12312312",
    "additionalInfo": {
        "deviceId": "123456",
        "channel": "phone"
    }
};

request.post({
    url: url,
    headers: headers,
    json: data
}, (error, response, body) => {
    if (error) {
        console.error('Request error:', error);
    } else {
        console.log('Response status code:', response.statusCode);
        console.log('Response body:', body);
    }
});
```
```ruby Ruby
require 'net/http'
require 'uri'
require 'json'

url = URI.parse('https://api.durianpay.id/v1.0/access-token/b2b')
headers = {
  'X-TIMESTAMP' => '2024-05-13T15:32:36.422+07:00',
  'X-SIGNATURE' => 'KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=',
  'X-CLIENT-KEY' => 'client_id',
  'Content-Type' => 'application/json'
}
data = { 'grantType' => 'AUTHORIZATION_CODE' }

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url.request_uri, headers)
request.body = data.to_json

response = http.request(request)
puts "Response code: #{response.code}"
puts "Response body: #{response.body}"
```

**Sample Response**

```json Success Response
// Sample Response
{
    "accountInfos": [
        {
            "availableBalance": {
                "currency": "IDR",
                "value": "100000.00"
            }
        }
    ],
    "responseCode": "2001100",
    "responseMessage": "Successful"
}
```

## Non SNAP Supporting API

**Credentials Setup :** [Legacy API](https://docs.durianpay.id/docs/legacy-api)

**List of API:**

* [Get Banks](https://docs.durianpay.id/reference/get_v1-disbursements-banks)