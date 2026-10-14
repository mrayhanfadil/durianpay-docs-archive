---
updatedAt: 2026-07-28T05:16:29.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# SNAP Virtual Account Notification

Whenever certain transaction actions occur on your Durianpay SNAP Virtual Account integration, we trigger events which your application can listen to. This is where webhooks come in. A webhook is a URL on your server where we send payloads for such events. For example, if you implement webhooks, once a virutal account payment is successful, we will immediately notify your server with a `SNAP.payment.va.payment` event.

Durianpay will send the webhook to you directly when an event change occurred, followed by 2, 5, 10, 90, 210 minutes retry if the webhook is not acknowledged with 200 OK status.

You can specify your webhook URL on your dashboard `Settings - Webhook` where we would send POST requests to whenever an event occurs.

### Setting Up Webhook

* Create Webhooks in Settings > Create New

  <Image src="https://files.readme.io/89617874a25e8ac655f32d9022819ca447b01d51722db92a586303c5aae04175-image.png" align="center" width="600px" />

* Fill up the event you want to subscribe to, give a name to webhook event and add your url which you want us to call

<Image src="https://files.readme.io/ba590d6d022963e3a0022a278be59eaf90df3344a28ded4f3033ed38bc55f263-image.png" align="center" width="600px" />

* Once you click create button, there will be sample webhook from Durianpay to be sent to the URL. In order to successfuly setup a webhook the URL should return 200 OK.
* Once you receive success notification on setting up webhook, you are ready to accept Durianpay webhook according to the event specified.

<br />

### Events after payment to virtual account

| Name               | Description                                                                         |
| :----------------- | :---------------------------------------------------------------------------------- |
| payment.va.payment | This event is triggered when a payment to virtual account is completed or rejected. |

<br />

### Handling Webhooks

Handle the webhook by checking the following fields in the additionalInfo parameter of the webhook body

| latestTransactionStatus | transactionStatusDesc | Description                                                        | Trigger Condition                                                                                                        |
| :---------------------- | :-------------------- | :----------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| 00                      | completed             | The payment is completed, the fund will be settled to your account | Fired when the payor has successfully paid the virtual account                                                           |
| 09                      | rejected              | The payment is rejected, the fund will be refunded to the payor    | Fired when the payor has successfully paid the virtual account but the payment is rejected due to regulatory requirement |

<Callout icon="❗️" theme="error">
  **Ensuring Callback Idempotency**

  Durianpay retries any callback that does not receive a 200 OK within 5 seconds (retry schedule: 2, 5, 10, 90, 210 minutes), so the same event may arrive more than once. Your handler must be idempotent.

  Deduplicate on `paymentRequestId` - the unique Durianpay payment ID included in every callback payload. Store it on first receipt; if the same value arrives again, skip your business logic but still return 200 OK so Durianpay stops retrying.
</Callout>

<br />

### Digital Signature Verification

Follow these steps to validate the digital signature of the webhook

1. Take the signature from HTTP header "X-SIGNATURE"<br />The following is an example

| Parameter     | Example Value                                                                                                                                                                                                                                                                                                                                            |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `X-SIGNATURE` | VpByUVbCd1rf/K5sMBGJk2Nz2zLsH9L9PWCMzb/ouVB/rVh/wPTfzr4AIfW9LGzyKrXTihS75uIiKqhIRexS9sAsu+AXyPKVULKGBRIZJ1yNdbQQQfUS3HT4sbn+JgLlBWS7DozJGqR5LY6F0cQ8wceErqSGEiHQGut5bpCaUC3wEfDynujO33BIvKLF5Gy9XnDMRVvRs+r6pjlew5uCX0Z3vmYEVCHE/6pWvkvRONhwQfqzSvIc56MVInnPFraz5l0DdendQbHhiCg0VIqhsp/aG7Ubxd2hS3o1PbnKiVjr07/mU5nhKhNlT8WtES7/5zh/Argl2Fkea8X+n70RBQ== |

2. Compose the string to verify

   1. Sample Webhook payload:

      ```json Webhook Payload (completed)
      {
          "trxId": "trx-1760606842571",
          "customerNo": "82311689",
          "paidAmount": {
              "value": "20000.00",
              "currency": "IDR"
          },
          "trxDateTime": "2026-04-23T10:51:38.167934Z",
          "additionalInfo": {
            "bankCode": "BRI",
            "payerBank": "BRINIDJA", 
            "payerName": "DEMETRIUS NOBEL",
            "expiredDate": "0001-01-01T00:00:00Z",
            "customerInfo": {
                  "email": "",
                  "mobile": "+6281234567890",
                  "given_name": "Jane Doe",
                  "customer_id": "cus_6SmXXXXXXX3",
                  "customer_ref_id": "6aa891c0-99ef-4d4c-84b2-a723245376b3"
              },
            "failureReason": {},  
            "transactionStatusDesc": "completed", // new parameter
            "latestTransactionStatus": "00" // new parameter
          },
          "partnerServiceId": "12345678",
          "paymentRequestId": "pay_xZvyXXXXXXXX",
          "virtualAccountNo": "1234567882311689"
      }
      ```
      ```Text Webhook Payload (rejected)
      {
          "trxId": "trx-1760606842570",
          "customerNo": "82311689",
          "paidAmount": {
              "value": "10000.00",
              "currency": "IDR"
          },
          "trxDateTime": "2025-10-22T09:44:18.086348Z",
          "additionalInfo": {
              "bankCode": "BRI",
              "payerBank": "BRINIDJA", 
              "payerName": "DEMETRIUS NOBEL",
              "expiredDate": "0001-01-01T00:00:00Z",
              "customerInfo": {
                  "email": "",
                  "mobile": "",
                  "given_name": "",
                  "customer_ref_id": ""
              },
              "rejectionFee": 0,
              "failureReason": {
                  "code": 20010,
                  "message": "Payor Information Doesn't Match"
              },
              "rejectionReason": "Payor Information Doesn't Match",
              "transactionStatusDesc": "rejected",
              "latestTransactionStatus": "09"
          },
          "partnerServiceId": "12345678",
          "paymentRequestId": "pay_5hD63nDtpw7185",
          "virtualAccountNo": "1234567882311689"
      }
      ```
   2. String To Verify Format:
      ```json Pseudo Code
      <HTTP METHOD> + ":" + <RELATIVE PATH URL> + ":" + LowerCase(HexEncode(SHA-256(Minify(<HTTP BODY>)))) + ":" + <X-TIMESTAMP>
      ```
      * For a webook url [https://www.example.com/callback/v1.0/transfer-va/payment](https://www.example.com/callback//v1.0/transfer-va/payment), the relative path url will be /callback/v1.0/transfer-va/payment
      * X-TIMESTAMP will be part of the webhook header
      * HTTP Method will be POST
   3. Example: POST:/callback/v1.0/transfer-va/payment:5d2c90ddfdd406117ced5c2b502c05b601d435c7e5440f82e58733fdd5f15b7d:2024-11-07T16:04:55.667+07:00
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

<Callout icon="📘" theme="info">
  ### Changelog 28/07/2026&#x20;

  Adding 2 new conditional parameters on the callback: `payerBank` & `payerName` where these 2 parameters will be included if the bank passed the information
</Callout>

<br />