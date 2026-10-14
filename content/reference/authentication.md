---
updatedAt: 2026-01-30T20:33:11.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Authentication

# Normal / Legacy API Authentication

When you're calling any of Durianpay's API, you have to pass `Authorization` parameter in the header. Value for `Authorization`can be received by going through these steps:

1. **Get your respective API Keys from Durianpay's dashboard, by going to Settings > API Keys**

   <Image border={false} src="https://files.readme.io/3a57c6fe5380f1082356477042c71bb3baa8293ec80a258512bf0ab5af0af97d-image.png" />
2. **Formatting the API Key to`BASIC AUTH` format**\
   The BASIC AUTH will have the following format: `Username`:`Password`.\
   Replace Username with your API Key and leave value for password as Blank.\
   The result for this combination will be: string `{Your_API_Key}:`
3. **Encode the previously generated combination to Base64 format**
4. **Include the Base64 encoded string in the HTTP(S) header**\
   Prepend the authorization method `(Basic)` and a space `()` to the encoded string. The authorization header is as given below: `Authorization: Basic [Base64({Your_API_Key}:)]`

> 🚧 Important things to note:
>
> 1. Before you encode the keys value, Please ensure the format of the API Key follows the aforementioned Basic Auth format, `{Your_API_Key}:` . Where there will be `:` after your API Key.
> 2. The Authorization Header given in the example is for reference only. Please use your own Sandbox/Production Server Key to create your API key.
> 3. The API keys for Sandbox and Production are different. When going live, please switch to the LIVE API Keys.

<br />

# SNAP API Authentication:

When you're calling any of Durianpay's SNAP API, you have to provide several parameter in the header. Value for these header parameter can be received via  dashboard under Menu Settings > API Key:

* Client Key (Will be used as X-Client-Key and X-Partner-ID in request header)
* Client Secret Key (Will be used for encrypting symmetric X-Signature)
* Merchant ID (Will be used for several API request body such as Balance Inquiry)
* Public Key given by Durianpay (Will be used to verify signature from us)

Additionally you need to generate Merchant's Private & Public Key Pair from your end

* Merchant Private Key will be used for encrypting asymmetric X-Signature
* Merchant Public Key will be used by Durianpay to verify signature of request transaction from the merchant

All credentials above will need to be setup for both live and sandbox environment. Live credentials will be given only after merchant 's legal document & functionality test is approved by Durianpay.

## Generate Your Private/Public Key Pair

You can refer to following steps to generate private/public key pair from your system.

### Generate Private Key

```Text bash
openssl genrsa -out rsa_private_key.pem 2048
```

### Generate Public Key

```Text bash
openssl rsa -in rsa_private_key.pem -out rsa_public_key.pem -pubout
```

> You need to generate different public-private key pair for sandbox mode and live mode

## Configuration of Public Key

To configure your public key in Durianpay, you can set it up via our dashboard. It is supported separately for your sandbox public key and live  public key.

1. Please ensure the file of your public key to be in a .pem format
2. Open Settings-API Key menu and you will see `Upload Public Key` button. Click the button to upload your public key
3. Select the public key file you want to submit or drag the file to the upload box then click `Upload` button.
4. Once public key is stored in Durianpay side you will see rsa\_public\_key.pem and delete button.

## Request Header

Each SNAP Request requires specific header value. There are 2 kind of header for requests, to generate B2B Access Token, and Transaction (disbursement, payment, etc)

### B2B Access Token Header

[Generate Access Token (B2B) API](https://docs.durianpay.id/reference/access-token-b2b)

| Header       | Description                | Format                |
| :----------- | :------------------------- | :-------------------- |
| X-TIMESTAMP  | Request timestamp	ISO 8601 | datetime              |
| X-SIGNATURE  | Security signature         | Base64 encoded string |
| X-CLIENT-KEY | Merchant identifier key    | String                |
| Content-Type | Type of data being sent    | MIME type             |

### Transaction Request Header

| Header        | Description                                                                                          | Format                       |
| :------------ | :--------------------------------------------------------------------------------------------------- | :--------------------------- |
| X-TIMESTAMP   | Request timestamp                                                                                    | ISO 8601 datetime            |
| X-SIGNATURE   | Security signature                                                                                   | Base64 encoded string        |
| X-PARTNER-ID  | Partner identifier                                                                                   | Alphanumeric string          |
| X-EXTERNAL-ID | Unique messaging reference identifier generated by merchant and should be unique within the same day | Random Alphanumeric string   |
| CHANNEL-ID    | Channel identifier                                                                                   | Numeric string               |
| Content-Type  | Type of data being sent                                                                              | MIME type                    |
| Authorization | Authorization token                                                                                  | JWT (Started with 'Bearer ') |

## Generate Signature

There are two use kind of signature to be generated, one is to obtain access token, and another is for transaction. Signature for B2B Access Token is encrypted in an asymmetrically way, while for transaction signature is encrypted in a symmetrically way.

### Generate Signature To Obtain Access Token (B2B)

You can find the required structure of the string to be encrypted as below:

```text Input
<X-CLIENT-KEY>|<X-TIMESTAMP> // (on ISO8601 format)
//Example: merchant_client_key|2024-05-13T14:53:06.991+07:00
```

which then signed using SHA256withRSA with Private/Public Key pair merchant has generated.

```Text Output
X-Signature: aw3o6HM68vJDLO4nxAPgK0it5nd6zik3bUgMzqLiTrIB7w1QbnCLDo/IMVjaYsbPk9s=
```

This is already handled by the pre-request script in our [Postman collection](https://www.postman.com/durianpay-dev/durianpay-merchant-api/collection/sw9cmuf/durianpay-snap-merchant-api-v1-0) when generating the B2B access token. Alternatively, you can use the provided script to generate it manually.

```javascript
const crypto = require('crypto');
const fs = require('fs');

function pad(num, size = 2) {
    let s = String(Math.floor(Math.abs(num)));
    while (s.length < size) s = '0' + s;
    return s;
}

// Custom ISO string formatter (same as Postman)
Date.prototype.toIsoString = function () {
    const tzo = -this.getTimezoneOffset();
    const dif = tzo >= 0 ? '+' : '-';

    return this.getFullYear() +
        '-' + pad(this.getMonth() + 1) +
        '-' + pad(this.getDate()) +
        'T' + pad(this.getHours()) +
        ':' + pad(this.getMinutes()) +
        ':' + pad(this.getSeconds()) +
        '.' + pad(this.getMilliseconds(), 3) +  // fixed: pad milliseconds to 3 digits
        dif + pad(Math.floor(Math.abs(tzo) / 60)) +
        ':' + pad(Math.abs(tzo) % 60);
};

// Load private key
const privateKey = fs.readFileSync('./rsa_private_key.pem', 'utf8').trim(); // same as Postman
const clientId = 'your-client-id'; // replace as needed

const dt = new Date();
const timestamp = dt.toIsoString();
console.log("Timestamp:", timestamp);

// Create signature (same algorithm)
const sign = crypto.createSign('RSA-SHA256');
sign.update(clientId + '|' + timestamp, 'utf8');
sign.end();

// Signature in base64 (Postman uses hexToBase64)
const signature = sign.sign(privateKey);
const signatureBase64 = signature.toString('base64');

console.log("Signature (Base64):", signatureBase64);
```
```go
package main

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"fmt"
	"io/ioutil"
	"log"
	"time"
)

// Custom timestamp formatter like Postman's script
func toIsoString(t time.Time) string {
	_, offset := t.Zone()
	sign := "+"
	if offset < 0 {
		sign = "-"
		offset = -offset
	}
	hours := offset / 3600
	minutes := (offset % 3600) / 60

	return fmt.Sprintf("%04d-%02d-%02dT%02d:%02d:%02d.%03d%s%02d:%02d",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second(), t.Nanosecond()/1e6,
		sign, hours, minutes,
	)
}

func main() {
	// === CHANGE THIS ===
	clientID := "your-client-id"
	privateKeyPath := "./rsa_private_key.pem"

	// Generate timestamp
	timestamp := toIsoString(time.Now())
	fmt.Println("Timestamp:", timestamp)

	// Read and parse private key
	privKeyBytes, err := ioutil.ReadFile(privateKeyPath)
	if err != nil {
		log.Fatalf("Failed to read private key file: %v", err)
	}

	block, _ := pem.Decode(privKeyBytes)
	if block == nil || (block.Type != "PRIVATE KEY" && block.Type != "RSA PRIVATE KEY") {
		log.Fatal("Failed to decode PEM block containing private key")
	}

	var privKey *rsa.PrivateKey
	if block.Type == "PRIVATE KEY" {
		key, err := x509.ParsePKCS8PrivateKey(block.Bytes)
		if err != nil {
			log.Fatalf("Failed to parse PKCS8 private key: %v", err)
		}
		privKey = key.(*rsa.PrivateKey)
	} else {
		key, err := x509.ParsePKCS1PrivateKey(block.Bytes)
		if err != nil {
			log.Fatalf("Failed to parse PKCS1 private key: %v", err)
		}
		privKey = key
	}

	// Create data to sign
	data := clientID + "|" + timestamp
	hashed := sha256.Sum256([]byte(data))

	// Sign the hash
	signature, err := rsa.SignPKCS1v15(rand.Reader, privKey, crypto.SHA256, hashed[:])
	if err != nil {
		log.Fatalf("Failed to sign data: %v", err)
	}

	// Encode in base64
	sigBase64 := base64.StdEncoding.EncodeToString(signature)
	fmt.Println("Signature (Base64):", sigBase64)
}
```
```ruby
require 'openssl'
require 'base64'
require 'time'

def pad(num, size = 2)
  num.to_s.rjust(size, '0')
end

def custom_iso8601(dt)
  tzo = -dt.utc_offset / 60  # in minutes
  dif = tzo >= 0 ? '+' : '-'
  hours_offset = pad((tzo.abs / 60).floor)
  mins_offset = pad(tzo.abs % 60)

  "#{dt.year}-#{pad(dt.month)}-#{pad(dt.day)}T" +
  "#{pad(dt.hour)}:#{pad(dt.min)}:#{pad(dt.sec)}." +
  "#{pad((dt.usec / 1000).floor, 3)}" +
  "#{dif}#{hours_offset}:#{mins_offset}"
end

# Sample client ID
client_id = 'your-client-id'

# Load private key from PEM file or environment
private_key_pem = File.read('./rsa_private_key.pem')
private_key = OpenSSL::PKey::RSA.new(private_key_pem)

# Generate timestamp
dt = Time.now
timestamp = custom_iso8601(dt)

puts "Timestamp: #{timestamp}"

# Prepare message
data = "#{client_id}|#{timestamp}"

# Create signature using SHA256withRSA
digest = OpenSSL::Digest::SHA256.new
signature = private_key.sign(digest, data)

# Convert signature to Base64
signature_base64 = Base64.strict_encode64(signature)

puts "Signature (Base64): #{signature_base64}"

```
```python
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime, timezone, timedelta
import base64

def load_private_key(path: str):
    with open(path, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

def get_custom_iso_timestamp():
    now = datetime.now().astimezone()
    offset = now.utcoffset()
    offset_minutes = int(offset.total_seconds() // 60)
    sign = '+' if offset_minutes >= 0 else '-'
    hours_offset = abs(offset_minutes) // 60
    mins_offset = abs(offset_minutes) % 60

    iso = now.strftime(f"%Y-%m-%dT%H:%M:%S.{int(now.microsecond / 1000):03d}")
    return f"{iso}{sign}{hours_offset:02}:{mins_offset:02}"

def generate_signature(private_key, message: str):
    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode("utf-8")

if __name__ == "__main__":
    private_key = load_private_key("rsa_private_key.pem")
    client_id = "your-client-id"
    timestamp = get_custom_iso_timestamp()

    print("Timestamp:", timestamp)

    data_to_sign = f"{client_id}|{timestamp}"
    signature_base64 = generate_signature(private_key, data_to_sign)

    print("Signature (Base64):", signature_base64)

```

Use these values as the `X-TIMESTAMP` and `X-SIGNATURE` headers when requesting a B2B access token

### Generate Signature For Transaction API

You can find the required structure of the string to be encrypted as below:

```Text Input
<HTTP METHOD> + ":" + <RELATIVE PATH URL> + ":" + <B2B ACCESS TOKEN> + ":" + LowerCase(HexEncode(SHA-256(Minify(<HTTP BODY>)))) + ":" + <X-TIMESTAMP>
  // Example: POST:/v1.0/balance-inquiry:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLC :f806c49e8cd175aa9dd5dd8e0a49648c885954d:2024-05-13T15:07:07+07:00
```

which then encrypted using HMAC-SHA512 with merchant's Secret Key that Durianpay give.

```Text Output
X-Signature: tnNHFw5ZCWjnHFd9UGAB5iDLuwo+89efml8F1CP8vaqut/PfNWac/XLiCkLt3zGHTppZKPxz/PPptqM2alsOFA==
```

This is already handled by the pre-request script in our [Postman collection](https://www.postman.com/durianpay-dev/durianpay-merchant-api/collection/sw9cmuf/durianpay-snap-merchant-api-v1-0) in each transactional APIs. Alternatively, you can use the provided script to generate it manually.

```javascript
const crypto = require('crypto');

Date.prototype.toIsoString = function () {
    const tzo = -this.getTimezoneOffset();
    const dif = tzo >= 0 ? '+' : '-';
    const pad = num => (Math.floor(Math.abs(num)) < 10 ? '0' : '') + Math.floor(Math.abs(num));

    return this.getFullYear() +
        '-' + pad(this.getMonth() + 1) +
        '-' + pad(this.getDate()) +
        'T' + pad(this.getHours()) +
        ':' + pad(this.getMinutes()) +
        ':' + pad(this.getSeconds()) +
        dif + pad(tzo / 60) +
        ':' + pad(tzo % 60);
};

// Convert hex to base64
function hexToBase64(hex) {
    return Buffer.from(hex, 'hex').toString('base64');
}

// Create HMAC signature
function getAuthHeader(httpMethod, requestPath, requestBody, token, clientSecret, timestamp) {
    const body = (httpMethod === 'GET' || !requestBody) ? '' : JSON.stringify(JSON.parse(requestBody));
    const hash = crypto.createHash('sha256').update(body).digest('hex');

    const payload = `${httpMethod}:${requestPath}:${token}:${hash}:${timestamp}`;
    const hmac = crypto.createHmac('sha512', clientSecret).update(payload).digest('hex');

    return hexToBase64(hmac);
}

// Generate random external ID
function generateExternalId() {
    return Math.floor(Math.random() * 99999999) + 100000000;
}

// === Begin ===
// Replace this with your actual http method request
const httpMethod = 'POST';
// Replace this with your actual path
const requestPath = '/v1.0/balance-inquiry';
// Replace this with your actual response body if any
const requestBody = JSON.stringify({
    accountNo: "mer_4tET9ovZKc3467"
});

// Replace these with your actual b2b token and secret
const token = 'your_token_here';
const clientSecret = 'your_client_secret_here';

// Generate values
const timestamp = new Date().toIsoString();
const xExternalID = generateExternalId();
const signature = getAuthHeader(httpMethod, requestPath, requestBody, token, clientSecret, timestamp);

// Print values to stdout
console.log('timestamp:', timestamp);
console.log('x_external_id:', xExternalID);
console.log('signature:', signature);

```
```go
package main

import (
	"bytes"
	"crypto/hmac"
	"crypto/sha256"
	"crypto/sha512"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func toIsoString(t time.Time) string {
	// Format with timezone offset like "2025-04-21T12:34:56+07:00"
	return t.Format("2006-01-02T15:04:05-07:00")
}

func hexToBase64(hexStr string) string {
	bytes, _ := hex.DecodeString(hexStr)
	return base64.StdEncoding.EncodeToString(bytes)
}

func getAuthHeader(httpMethod, requestPath, requestBody, token, clientSecret, timestamp string) string {
	var body string
	if strings.ToUpper(httpMethod) == "GET" || len(requestBody) == 0 {
		body = ""
	} else {
		var buf bytes.Buffer
		err := json.Compact(&buf, []byte(requestBody)) // ensure minified JSON
		if err != nil {
			panic("Invalid JSON body: " + err.Error())
		}
		body = buf.String()
	}

	// SHA-256 hash
	sha256Hasher := sha256.New()
	sha256Hasher.Write([]byte(body))
	hash := hex.EncodeToString(sha256Hasher.Sum(nil))

	// Create the HMAC payload and signature
	payload := fmt.Sprintf("%s:%s:%s:%s:%s", httpMethod, requestPath, token, hash, timestamp)
	hmacHasher := hmac.New(sha512.New, []byte(clientSecret))
	hmacHasher.Write([]byte(payload))
	signatureHash := hex.EncodeToString(hmacHasher.Sum(nil))

	// Convert signature from hex to base64
	return hexToBase64(signatureHash)
}

func generateExternalId() int {
	return rand.Intn(89999999) + 100000000
}

func main() {
	// Simulated request input
	// Replace this with your actual http method request
	httpMethod := "POST"
	// Replace this with your actual path
	requestPath := "/v1.0/balance-inquiry"
	// Replace this with your actual response body if any
	requestBody := `{
		"accountNo": "mer_4tET9ovZKc3467"
	}`
	// Replace these with your actual b2b token and secret
	token := "your_token_here"
	clientSecret := "your_client_secret_here"

	// Generate timestamp and external ID
	now := time.Now()
	timestamp := toIsoString(now)
	xExternalID := generateExternalId()
	signature := getAuthHeader(httpMethod, requestPath, requestBody, token, clientSecret, timestamp)

	// Output the environment-style variables
	fmt.Println("timestamp:", timestamp)
	fmt.Println("x_external_id:", xExternalID)
	fmt.Println("signature:", signature)
}

```
```ruby
require 'json'
require 'openssl'
require 'base64'
require 'securerandom'
require 'time'

# Format ISO8601 timestamp with timezone
def iso_timestamp
  Time.now.iso8601
end

# Convert hex to base64
def hmac_to_base64(hmac_bytes)
    Base64.strict_encode64(hmac_bytes)
end

# Generate HMAC-SHA512 signature and encode it in base64
def get_auth_header(http_method, request_path, request_body, token, client_secret, timestamp)
  body = if http_method.upcase == 'GET' || request_body.nil? || request_body.empty?
           ''
         else
           JSON.dump(JSON.parse(request_body)) # Minify JSON
         end

  sha256_hash = OpenSSL::Digest::SHA256.hexdigest(body)

  payload = "#{http_method}:#{request_path}:#{token}:#{sha256_hash}:#{timestamp}"

  hmac = OpenSSL::HMAC.digest(OpenSSL::Digest.new('sha512'), client_secret, payload)

  hmac_to_base64(hmac)
end

# Generate random x_external_id
def generate_external_id
  rand(100_000_000..199_999_999)
end

# === Input ===
# Replace this with your actual http method request
http_method = 'POST'
# Replace this with your actual path
request_path = '/v1.0/balance-inquiry'
# Replace this with your actual response body if any
request_body = {
  accountNo: 'mer_4tET9ovZKc3467'
}.to_json

# Replace these with your actual b2b token and secret
token = 'your_token_here'
client_secret = 'your_client_secret_here'

# === Execution ===
timestamp = iso_timestamp
x_external_id = generate_external_id
signature = get_auth_header(http_method, request_path, request_body, token, client_secret, timestamp)

# === Output (stdout) ===
puts "timestamp: #{timestamp}"
puts "x_external_id: #{x_external_id}"
puts "signature: #{signature}"

```
```python
import json
import hashlib
import hmac
import base64
import random
from datetime import datetime, timezone, timedelta

def to_iso_string():
    now = datetime.now().astimezone()
    return now.isoformat(timespec='seconds')

def hex_to_base64(hex_str):
    return base64.b64encode(bytes.fromhex(hex_str)).decode()

def get_auth_header(http_method, request_path, request_body, token, client_secret, timestamp):
    if http_method.upper() == 'GET' or not request_body:
        body = ''
    else:
        # Ensure minified JSON
        body = json.dumps(json.loads(request_body), separators=(',', ':'))

    # SHA-256 hash of the body
    sha256_hash = hashlib.sha256(body.encode()).hexdigest()

    # Create the payload
    payload = f"{http_method}:{request_path}:{token}:{sha256_hash}:{timestamp}"

    # HMAC-SHA512
    hmac_digest = hmac.new(client_secret.encode(), payload.encode(), hashlib.sha512).digest()

    # Base64 encode the HMAC
    return base64.b64encode(hmac_digest).decode()

def generate_external_id():
    return random.randint(100000000, 199999999)

# === Input ===
# Replace this with your actual http method request
http_method = 'POST'
# Replace this with your actual path
request_path = '/v1.0/balance-inquiry'
# Replace this with your actual response body if any
request_body = json.dumps({
    "accountNo": "mer_4tET9ovZKc3467"
})

# Replace these with actual values
token = 'your_token_here'
client_secret = 'your_client_secret_here'

# === Generate Values ===
timestamp = to_iso_string()
x_external_id = generate_external_id()
signature = get_auth_header(http_method, request_path, request_body, token, client_secret, timestamp)

# === Output ===
print("timestamp:", timestamp)
print("x_external_id:", x_external_id)
print("signature:", signature)

```

Use these values as the `X-TIMESTAMP`, `X-EXTERNAL-ID`, and `X-SIGNATURE` headers when sending a request to transactional APIs

## Generate Access Token (B2B)

> 📘 B2B Access Token will be used for all transactional APIs. The token itself will have 900 seconds (15 minutes) valid time by default.

> There is no refresh access token nor the access token will be auto refreshed, so you will need to generate another access token if it has passed its expiry time

```text Bash
curl --location 'https://api.durianpay.id/v1.0/access-token/b2b' \
--header 'X-TIMESTAMP: 2024-05-13T15:32:36.422+07:00' \
--header 'X-SIGNATURE: KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=' \
--header 'X-CLIENT-KEY: client_id' \
--header 'Content-Type: application/json' \
--data '{
    "grantType": "AUTHORIZATION_CODE"
}'
```
```Text Python
import requests

url = 'https://api.durianpay.id/v1.0/access-token/b2b'
headers = {
    'X-TIMESTAMP': '2024-05-13T15:32:36.422+07:00',
    'X-SIGNATURE': 'KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=',
    'X-CLIENT-KEY': 'client_id',
    'Content-Type': 'application/json'
}
data = {
    "grantType": "AUTHORIZATION_CODE"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
```
```Text Java
OkHttpClient client = new OkHttpClient();

String url = "https://api.durianpay.id/v1.0/access-token/b2b";
String timestamp = "2024-05-13T15:32:36.422+07:00";
String signature = "KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=";
String clientKey = "client_id";
String contentType = "application/json";

Gson gson = new Gson();
String jsonBody = gson.toJson(Map.of("grantType", "AUTHORIZATION_CODE"));

RequestBody requestBody = RequestBody.create(MediaType.parse(contentType), jsonBody);

Request request = new Request.Builder()
    .url(url)
    .addHeader("X-TIMESTAMP", timestamp)
    .addHeader("X-SIGNATURE", signature)
    .addHeader("X-CLIENT-KEY", clientKey)
    .addHeader("Content-Type", contentType)
    .post(requestBody)
    .build();
Response response = client.newCall(request).execute();
```
```Text JavaScript
const request = require('request');

const url = 'https://api.durianpay.id/v1.0/access-token/b2b';
const headers = {
    'X-TIMESTAMP': '2024-05-13T15:32:36.422+07:00',
    'X-SIGNATURE': 'KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=',
    'X-CLIENT-KEY': 'client_id',
    'Content-Type': 'application/json'
};
const data = {
    "grantType": "AUTHORIZATION_CODE"
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
```Text Ruby
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

```Text Response
{
    "responseCode": "2007300",
    "responseMessage": "Successful",
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTAwNTYsImlhdCI6MTcxNTU4OTE1NiwibWVyY2",
    "tokenType": "BearerToken",
    "expiresIn": "2024-05-13 08:47:36.452492159 +0000 UTC"
  }
```