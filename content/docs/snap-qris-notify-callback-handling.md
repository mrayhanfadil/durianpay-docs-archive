---
updatedAt: 2026-07-28T04:40:11.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# SNAP QRIS Notification

When a customer completes a QRIS payment (static or dynamic), Durianpay sends a POST callback to your configured webhook URL with the payment result.

* Callbacks are delivered to the URL registered in your dashboard.
* Your endpoint must return `200 OK`**&#x20;within 5 seconds**.
* If a `200 OK` is not received in time, Durianpay retries at **2, 5, 10, 90, and 210 minutes** after the original attempt.
* Retries replay an identical payload, so your handler must be **idempotent** (see below).

For static QRIS the callback is the **only** signal the merchant receives, there is no preceding API call to correlate against, so dedup/reconciliation relies on the fields in the callback itself (`originalReferenceNo`, `additionalInfo.rrn`).

***

## 1. Setting Up the Webhook

1. In the dashboard, go to **Settings → Webhooks → Create New**.
2. Subscribe to the QRIS payment event (`payment.qr.mpm.notify`).
3. Give the webhook a name and a target URL.
4. On save, Durianpay sends a sample webhook to your URL. It must return `200 OK` for the configuration to be saved.

***

## 2. Events After QRIS Payment

| Event Name              | Trigger                                                             | Applies to       |
| ----------------------- | ------------------------------------------------------------------- | ---------------- |
| `payment.qr.mpm.notify` | Fires when a QRIS payment completes against a static or dynamic QR. | Static + Dynamic |

***

## 3. Handling the Callback

Read the outcome from the top-level `latestTransactionStatus` (mirrored in `transactionStatusDesc`):

| Status Code | Status Text | Meaning                                                    |
| ----------- | ----------- | ---------------------------------------------------------- |
| `00`        | `completed` | Payment successful; funds settle to your merchant account. |
| `08`        | `expired`   | Payment is expired                                         |

### Top-level fields

| Field                              | Description                                                                                   |
| ---------------------------------- | --------------------------------------------------------------------------------------------- |
| `originalReferenceNo`              | Durianpay's payment ID (e.g. `pay_f7RdgKc0ly4311`). Primary key for dedup and reconciliation. |
| `latestTransactionStatus`          | Outcome code (`00` = completed).                                                              |
| `transactionStatusDesc`            | Human-readable status (e.g. `completed`).                                                     |
| `amount.value` / `amount.currency` | Paid amount and currency (e.g. `"1022.00"`, `"IDR"`).                                         |

### `additionalInfo` fields

| Field             | Description                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------ |
| `terminalID`      | Terminal ID (e.g. `A01`).                                                                  |
| `externalStoreId` | NMID (National Merchant ID) — comes from your QRIS credentials.                            |
| `rrn`             | Retrieval Reference Number from the issuer; natural reconciliation key on the issuer side. |
| `issuerName`      | Paying customer's bank/issuer (e.g. `BCA`).                                                |
| `isLive`          | `true` for production, `false` for sandbox.                                                |
| `createdTime`     | When the QR/payment record was created.                                                    |
| `paidTime`        | When the customer paid.                                                                    |
| `updatedTime`     | Last status update time.                                                                   |
| `failureReason`   | Empty `{}` on success; populated object on failure.                                        |
| `customerInfo`    | Payor details — see below.                                                                 |

### `customerInfo` fields

| Field             | Description                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------ |
| `customer_id`     | Durianpay customer ID (e.g. `cus_AObLIp7MSL3730`).                                         |
| `customer_ref_id` | Merchant's customer reference, if provided (may be empty).                                 |
| `email`           | Payor email (may be a system default for static QRIS, e.g. `staticqrisdefault@email.com`). |
| `given_name`      | Payor name, if available (may be empty).                                                   |
| `mobile`          | Payor mobile number, if available.                                                         |

> ❗️ **Ensuring Callback Idempotency**
>
> Durianpay retries deliver the **same payload**. Deduplicate on `originalReferenceNo` (and, as a cross-check, `additionalInfo.rrn`):
>
> 1. On first receipt, persist `originalReferenceNo` and process your business logic once.
> 2. If the same `originalReferenceNo` arrives again, return `200 OK` **without** reprocessing.
>
> This is especially important for static QRIS, where the callback is the sole record of the transaction.

***

## 4. Digital Signature Verification

Every callback carries `X-SIGNATURE` and `X-TIMESTAMP` headers. Verify the signature before trusting the body.

**Steps:**

1. Read `X-SIGNATURE` and `X-TIMESTAMP` from the request headers.
2. Compose the string-to-sign in this format:

   ```
   POST:<RELATIVE_PATH>:<LOWERCASE_HEX_SHA256_OF_MINIFIED_BODY>:<X-TIMESTAMP>
   ```

   * `<RELATIVE_PATH>` excludes the domain, e.g. `/callback/v1.0/qr/qr-mpm-notify`.
   * Minify the JSON body (no insignificant whitespace), SHA-256 hash it, then hex-encode and lowercase.
   * `<X-TIMESTAMP>` is taken verbatim from the header.
3. Verify with **SHA-256 + RSA-2048 (PKCS#8)** against Durianpay's public key.
4. Return `200 OK` only if verification succeeds; otherwise reject (`401`).

**Example string-to-sign:**

```
POST:/callback/v1.0/qr/qr-mpm-notify:5d2c90ddfdd406117ced5c2b502c05b601d435c7e5440f82e58733fdd5f15b7d:2026-06-22T11:36:12+00:00
```

> Sandbox and Live use **different public keys**. Use `additionalInfo.isLive` and your environment config to load the matching key.

### Verification (Go)

```go
package main

import (
	"crypto"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/hex"
	"encoding/pem"
	"errors"
	"fmt"
)

// VerifyQRISCallback verifies the X-SIGNATURE of a Durianpay QRIS callback.
func VerifyQRISCallback(relativePath, timestamp string, body []byte, xSignature, publicKeyPEM string) error {
	// 1. SHA-256 of the minified request body, hex-encoded lowercase.
	bodyHash := sha256.Sum256(body)
	bodyHashHex := hex.EncodeToString(bodyHash[:]) // hex.EncodeToString already lowercases

	// 2. Compose the string-to-sign.
	stringToSign := fmt.Sprintf("POST:%s:%s:%s", relativePath, bodyHashHex, timestamp)

	// 3. Parse Durianpay's public key (PKIX / PEM).
	block, _ := pem.Decode([]byte(publicKeyPEM))
	if block == nil {
		return errors.New("invalid public key PEM")
	}
	pub, err := x509.ParsePKIXPublicKey(block.Bytes)
	if err != nil {
		return err
	}
	rsaPub, ok := pub.(*rsa.PublicKey)
	if !ok {
		return errors.New("public key is not RSA")
	}

	// 4. Decode the base64 signature and verify (SHA-256, PKCS#1 v1.5).
	sig, err := base64.StdEncoding.DecodeString(xSignature)
	if err != nil {
		return err
	}
	digest := sha256.Sum256([]byte(stringToSign))
	return rsa.VerifyPKCS1v15(rsaPub, crypto.SHA256, digest[:], sig)
}
```

***

## 5. Callback Payload Example

### Completed payment (`00`)&#x20;

```json
{
  "additionalInfo": {
    "terminalID": "A01", // newly added value
    "externalStoreId": "202604234324234", // newly added value
    "createdTime": "2026-06-22T11:36:11+00:00",
    "customerInfo": {
      "customer_id": "cus_AggggP7MSL3730",
      "customer_ref_id": "",
      "email": "staticqrisdefault@email.com",
      "given_name": "",
      "mobile": "0812345678"
    },
    "failureReason": {},
    "isLive": true,
    "issuerName": "BCA",
    "paidTime": "2026-06-22T11:36:12+00:00",
    "rrn": "000360170200",
    "updatedTime": "2026-06-22T11:36:12+00:00"
  },
  "amount": {
    "currency": "IDR",
    "value": "1022.00"
  },
  "latestTransactionStatus": "00",
  "originalReferenceNo": "pay_ab7HdgKc0ly4322",
  "transactionStatusDesc": "completed"
}
```

The payload shape is identical for both dynamic & static QRIS; the difference is only in origin (a dynamic QR was generated via API first, so you can also correlate by your own stored `originalReferenceNo`).

***

## 6. Response Format

Acknowledge every callback with a minimal SNAP-shaped response. Only `responseCode` and `responseMessage` are expected — do not echo request data or add custom fields.

```json
{
  "responseCode": "2005200",
  "responseMessage": "Successful"
}
```

| responseCode | Meaning                          | When to return                                  |
| ------------ | -------------------------------- | ----------------------------------------------- |
| `2005200`    | Successful                       | Callback received and (idempotently) processed. |
| `4015200`    | Unauthorized — invalid signature | Signature verification failed.                  |
| `5005200`    | Internal server error            | Your handler errored; Durianpay will retry.     |

<br />