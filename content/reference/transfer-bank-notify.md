---
updatedAt: 2025-08-07T11:25:07.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Transfer Bank Notify

## Webhook: `transfer-bank.notify`

This is a **server-to-server callback (webhook)** sent by Durianpay to your system. You do **not** need to poll or request status from our API. Instead, you just need to configure your webhook listener endpoint, and Durianpay will push transaction status updates directly to your server via POST request. It can be configured via menu `Settings - Webhook`

***

### Webhook Specifications

* **Method**: `POST`
* **Content-Type**: `application/json`
* **Retries**: 2, 5, 10, 90, 210 minutes after the initial attempt if no `200 OK` is received
* **Configuration**: Set your webhook URL in `Dashboard > Settings > Webhook`

***

### Subscribed Event

| Event Name             | Description                                   |
| ---------------------- | --------------------------------------------- |
| `transfer-bank.notify` | Sent when a disbursement reaches final status |

***

### Field Definition

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        originalPartnerReferenceNo
      </td>

      <td>
        string
      </td>

      <td>
        Reference merchant send when submitting bank / e-wallet transfer request
      </td>
    </tr>

    <tr>
      <td>
        originalReferenceNo
      </td>

      <td>
        string
      </td>

      <td>
        Durianpay's reference returned when submitting bank/  e-wallet transfer request (dis\_item\_xxx)
      </td>
    </tr>

    <tr>
      <td>
        responseCode
      </td>

      <td>
        string
      </td>

      <td>
        HTTP status code (4 digit) + Service code  (2 digit)+ Case code (2 digit)
      </td>
    </tr>

    <tr>
      <td>
        responseMessage
      </td>

      <td>
        string
      </td>

      <td>
        Response message information
      </td>
    </tr>

    <tr>
      <td>
        amount.value
      </td>

      <td>
        string
      </td>

      <td>
        String representing value of the transaction : "20000.00".
      </td>
    </tr>

    <tr>
      <td>
        amount.currency
      </td>

      <td>
        string
      </td>

      <td>
        Currency of the transaction: "IDR"
      </td>
    </tr>

    <tr>
      <td>
        beneficiaryAccountNo
      </td>

      <td>
        string
      </td>

      <td>
        The account number of the recipient.
      </td>
    </tr>

    <tr>
      <td>
        beneficiaryBankCode
      </td>

      <td>
        string
      </td>

      <td>
        The bank code of the recipient account
      </td>
    </tr>

    <tr>
      <td>
        sourceAccountNo
      </td>

      <td>
        string
      </td>

      <td>
        Identifier of source account. its value is the same as merchant id
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo.latestTransactionStatus
      </td>

      <td>
        string
      </td>

      <td>
        Current  transaction status
        00 - done
        06 - failed
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo.transactionStatusDesc
      </td>

      <td>
        string
      </td>

      <td>
        Description  current transaction status
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo.failureReason
      </td>

      <td>
        string
      </td>

      <td>
        Error information when the transaction status is failed. Will only be shown for failed transaction
      </td>
    </tr>
  </tbody>
</Table>

<br />

### Webhook Payload Example

```json Success Case
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
```json Failed Case
{
  "additionalInfo": {
   "failureReason": "Unknown disburse error, please ask customer support for further information",
   "latestTransactionStatus": "06",
   "transactionStatusDesc": "failed"
 },
  "amount": {
   "currency": "IDR",
   "value": "10000.00"
 },
  "beneficiaryAccountNo": "3370018285",
  "beneficiaryBankCode": "014",
  "originalPartnerReferenceNo": "1000-1000-1000-1655511",
  "originalReferenceNo": "dis_item_2OgsLYYZji1085",
  "responseCode": "2000000",
  "responseMessage": "Request has been processed successfully",
  "sourceAccountNo": "mer_MsCtIPhqRc8045"
}
```

<br />

### 📘 Status Handling

Inspect the additionalInfo object in the webhook payload:

```json
"additionalInfo": {
  "latestTransactionStatus": "00",
  "transactionStatusDesc": "done"
}
```

| latestTransactionStatus | transactionStatusDesc | Meaning                |
| :---------------------- | :-------------------- | :--------------------- |
| 00                      | done                  | Transaction successful |
| 06                      | failed                | Transaction failed     |

✅ **Action Required:**\
Always respond with HTTP 200 OK to acknowledge receipt of the webhook. If not acknowledged, Durianpay will retry based on this schedule: 2, 5, 10, 90, 210 minutes.

<br />

### 🔐 Digital Signature Verification

Durianpay signs every webhook to ensure integrity and authenticity. You must validate the signature before processing.

**Webhook Headers:**

| Header      | Description                                 |
| :---------- | :------------------------------------------ |
| X-SIGNATURE | Base64-encoded RSA-2048 signature (SHA-256) |
| X-TIMESTAMP | Timestamp used to sign the payload          |

**Signature Format**:

```
POST:<relative path>:<lowercase hex sha256 of minified JSON body>:<X-TIMESTAMP>
```

**Example**:

```ruby
POST:/callback/v1.0/transfer/notify:5d2c90ddfdd406117ced5c2b502c05b601d435c7e5440f82e58733fdd5f15b7d:2024-11-07T16:04:55.667+07:00
```

Use Durianpay's public key (Live/Sandbox-specific) to verify the signature.

### 🧪 Go Code: Signature Verification

```go
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
	requestBody := []byte(`{}`)
	relativeURL := "" // e.g., "/callback/v1.0/transfer/notify"
	timestamp := ""   // from X-TIMESTAMP header
	rsaPublicKey := "" // PEM-formatted RSA public key
	xSignature := ""   // from X-SIGNATURE header

	err := VerifyWebhookSignature(requestBody, relativeURL, timestamp, rsaPublicKey, xSignature)
	if err != nil {
		fmt.Println("signature verification failed")
	} else {
		fmt.Println("signature verified")
	}
}

func VerifyWebhookSignature(requestBody []byte, relativeURL, timestamp, rsaPublicKey, xSignature string) error {
	var minifiedRequest bytes.Buffer
	if err := json.Compact(&minifiedRequest, requestBody); err != nil {
		return err
	}

	hashedPayload := generateHexEncodedSHA256(minifiedRequest.String())
	stringToSign := fmt.Sprintf("%s:%s:%s:%s", http.MethodPost, relativeURL, strings.ToLower(hashedPayload), timestamp)

	return verifySignature([]byte(stringToSign), rsaPublicKey, xSignature)
}

func verifySignature(payload []byte, publicKey string, signature string) error {
	sigBytes, err := base64.StdEncoding.DecodeString(signature)
	if err != nil {
		return err
	}

	rsaKey, err := parseRSAPublicKey(publicKey)
	if err != nil {
		return err
	}

	hashed := sha256.Sum256(payload)
	return rsa.VerifyPKCS1v15(rsaKey, crypto.SHA256, hashed[:], sigBytes)
}

func generateHexEncodedSHA256(data string) string {
	hash := sha256.Sum256([]byte(data))
	return hex.EncodeToString(hash[:])
}

func parseRSAPublicKey(pemKey string) (*rsa.PublicKey, error) {
	block, _ := pem.Decode([]byte(pemKey))
	if block == nil {
		return nil, errors.New("no key found in PEM")
	}

	pubKey, err := x509.ParsePKIXPublicKey(block.Bytes)
	if err != nil {
		return nil, err
	}

	rsaKey, ok := pubKey.(*rsa.PublicKey)
	if !ok {
		return nil, errors.New("not a valid RSA public key")
	}

	return rsaKey, nil
}

```