---
updatedAt: 2025-06-17T23:25:27.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Virtual Account

The following endpoint charges the payment for virtual account

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "durianpay-api",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://api.durianpay.id/v1"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "http",
        "scheme": "basic"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/payments/charge": {
      "post": {
        "summary": "Virtual Account",
        "description": "The following endpoint charges the payment for virtual account",
        "operationId": "payment-charge-virtual-account",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type",
                  "request"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "default": "VA"
                  },
                  "request": {
                    "type": "object",
                    "description": "The payload object for virtual account payment charge",
                    "required": [
                      "order_id",
                      "bank_code",
                      "name",
                      "amount"
                    ],
                    "properties": {
                      "order_id": {
                        "type": "string",
                        "description": "The id returned from create order api"
                      },
                      "bank_code": {
                        "type": "string",
                        "description": "Bank codes for the relevant bank. Available banks: BCA, BNI, BRI, MANDIRI, PERMATA, CIMB, BTPN, SAHABAT_SAMPOERNA, SINARMAS, MAYBANK, SYARIAH, DANAMON, NOBU, OTHERS"
                      },
                      "name": {
                        "type": "string",
                        "description": "Name that should appear in ATM"
                      },
                      "amount": {
                        "type": "string",
                        "description": "Payment amount"
                      },
                      "payment_ref_id": {
                        "type": "string",
                        "description": "Merchant's payment reference ID"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n {\n    \"data\": {\n        \"type\": \"VA\",\n        \"response\": {\n            \"payment_id\": \"pay_bfmIT8sczc2277\",\n            \"order_id\": \"ord_WkJWY1ysZ57194\",\n            \"account_number\": \"7001400009085556\",\n            \"payment_ref_id\":\"pay_ref_123\",\n            \"expiration_time\": \"2022-06-24T05:30:20.24670162Z\",\n            \"paid_amount\": \"104000.00\",\n            \"payment_instruction\": {\n                \"en\": {\n                    \"atm\": {\n                        \"heading\": \"ATM Mandiri\",\n                        \"instruction_text\": \"<ol><li>Insert your ATM card and select ENGLISH</li><li>Enter PIN, then select ENTER</li><li>Enter Virtual Account Number, then press CORRECT</li><li>Enter the amount to transfer, then press CORRECT</li><li>Customer details will be displayed. Choose number 1 according to the amount billed and then press YES</li><li>Payment confirmation will be displayed. Select YES to proceed</li><li>Keep your receipt as a formal proof of payment from Mandiri Bank</li><li>Your transaction is successful</li></ol>\"\n                    },\n                    \"mobile_app\": {\n                        \"heading\": \"Mandiri Online\",\n                        \"appstore_url\": \"http://onelink.to/dvs8pn\",\n                        \"playstore_url\": \"http://onelink.to/dvs8pn\",\n                        \"instruction_text\": \"<ol><li>Login to Livin' by Mandiri application</li><li>Select \"Payment\"</li><li>Select \"E-commerce\"</li><li>Select Transferpay \"70014\"</li><li>Enter virtual account number</li><li>Select \"Continue\"</li><li>Check transaction amount and source of fund</li><li>Select \"Continue\"</li><li>Check details on payment confirmation page</li><li>Select \"Continue Payment\"</li><li>Input \"PIN\" and the transaction will be completed</li></ol>\"\n                    },\n                    \"internet_banking\": {\n                        \"heading\": \"Internet Banking\",\n                        \"instruction_text\": \"<ol><li>Go to Mandiri Internet Banking website: https://ibank.bankmandiri.co.id/retail3/</li><li>Login with your USER ID and PIN</li><li>Select Payment</li><li>Select Multi Payment</li><li>Select My Account Number</li><li>Select Virtual Account Number</li><li>Enter your virtual account number</li><li>Go to confirmation page 1</li><li>Click on TOTAL if all details are correct and then click on CONTINUE</li><li>Go to confirmation page 2</li><li>Enter Challenge Code from your Internet Banking Token, then click on Send</li><li>You will be directed to the confirmation page once your payment has</li></ol>\"\n                    }\n                },\n                \"id\": {\n                    \"atm\": {\n                        \"heading\": \"ATM Mandiri\",\n                        \"instruction_text\": \"<ol><li>Masukkan kartu ATM dan pilih Bahasa Indonesia</li><li>Ketik nomor PIN dan tekan BENAR</li><li>Pilih menu “BAYAR/BELI”</li><li>Masukkan nomor Virtual Account</li><li>Isi NOMINAL, kemudian tekan BENAR</li><li>Muncul konfirmasi data customer. Pilih Nomor 1 sesuai tagihan yang akan dibayar, kemudian tekan YA</li><li>Muncul konfirmasi pembayaran. Tekan YA untuk melakukan pembayaran</li><li>Bukti pembayaran dalam bentuk struk agar disimpan sebagai bukti pembayaran yang sah dari Bank Mandiri</li><li>Transaksi Anda sudah selesai</li></ol>\"\n                    },\n                    \"mobile_app\": {\n                        \"heading\": \"Mandiri Online\",\n                        \"appstore_url\": \"http://onelink.to/dvs8pn\",\n                        \"playstore_url\": \"http://onelink.to/dvs8pn\",\n                        \"instruction_text\": \"<ol><li>Login ke aplikasi Livin` by Mandiri</li><li>Pilih menu \"Bayar\"</li><li>Pilih \"E-commerce\"</li><li>Pilih Penyedia Jasa Transferpay \"70014\"</li><li>Masukkan no virtual account pada kolom kode bayar</li><li>Tekan \"Lanjutkan\"</li><li>Cek nominal yang akan dibayarkan dan rekening sumber</li><li>Tekan \"Lanjutkan\"</li><li>Cek detail di tampilan konfirmasi pembayaran</li><li>Tekan \"Lanjut Bayar\"</li><li>Masukkan \"PIN\" dan transaksi anda selesai</li></ol>\"\n                    },\n                    \"internet_banking\": {\n                        \"heading\": \"Internet Banking\",\n                        \"instruction_text\": \"<ol><li>Kunjungi website Mandiri Internet Banking: https://ibank.bankmandiri.co.id/retail3/</li><li>Login dengan memasukkan USER ID dan PIN</li><li>Pilih Pembayaran</li><li>Pilih Multi Payment</li><li>Pilih No Rekening Anda</li><li>Pilih Penyedia Jasa Xendit 88908</li><li>Pilih No Virtual Account</li><li>Masukkan nomor Virtual Account anda</li><li>Masuk ke halaman konfirmasi 1</li><li>Apabila benar/sesuai, klik tombol tagihan TOTAL, kemudian klik Lanjutkan</li><li>Masuk ke halaman konfirmasi 2</li><li>Masukkan Challenge Code yang dikirimkan ke Token Internet Banking Anda, kemudian klik Kirim</li><li>Anda akan masuk ke halaman konfirmasi jika pembayaran telah selesai</li></ol>\"\n                    }\n                }\n            },\n            \"metadata\": {}\n        }\n    }\n  }\n}\n"
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```