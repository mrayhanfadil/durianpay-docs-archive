---
updatedAt: 2025-06-17T23:25:28.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# E-wallet

The following endpoint charges the payment for E-wallet

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-api-wallet",
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
        "summary": "E-wallet",
        "description": "The following endpoint charges the payment for E-wallet",
        "operationId": "payment-charge-ewallet",
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
                    "default": "EWALLET"
                  },
                  "request": {
                    "type": "object",
                    "description": "The payload object for E-wallet payment charge",
                    "required": [
                      "order_id",
                      "mobile",
                      "amount",
                      "wallet_type"
                    ],
                    "properties": {
                      "order_id": {
                        "type": "string",
                        "description": "The id returned from create order api"
                      },
                      "mobile": {
                        "type": "string",
                        "description": "Mobile number linked to the wallet. Please ensure that the number follows Indonesia's phone number format : 62xxxxxxxxxx or 08xxxxxxxxxx"
                      },
                      "amount": {
                        "type": "string",
                        "description": "Payment amount"
                      },
                      "wallet_type": {
                        "type": "string",
                        "description": "Wallet type. Available wallet types : LINKAJA, OVO, GOPAY, DANA, SHOPEEPAY"
                      },
                      "account_id": {
                        "type": "string",
                        "description": "The unique identifier assigned to a specific customer's linked e-wallet account, which is obtained after the account binding process. This parameter is required in the request for tokenized and preauthorization payment."
                      },
                      "expiry_duration": {
                        "type": "string",
                        "description": "The length of time, in minutes, that a preauthorization payment will be valid before it expires. Example: 60"
                      },
                      "is_preauth": {
                        "type": "string",
                        "description": "Flag indicating whether the payment is a preauthorization payment or a normal payment. Default Value: false"
                      },
                      "redirect_url": {
                        "type": "string",
                        "description": "Required and only applicable for pre-authorization payments, where it redirects the user to the specified URL after the PIN challenge. This parameter will be ignored for non–pre-authorization payments — please contact your account manager to configure the redirect URL manually."
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
                    "value": "{\n  \"type\": \"EWALLET\",\n  \"response\": {\n    \"payment_id\": \"pay_dAM0lqkVuk0074\",\n    \"order_id\": \"ord_TVZ6EYuBJ85268\",\n    \"mobile\": \"08123123123\",\n    \"status\": \"processing\",\n    \"expiration_time\": \"2021-04-02T15:08:57.800297779Z\",\n    \"checkout_url\": \"https://link.to/ewallet-checkout-url\",\n    \"paid_amount\": \"1000.00\",\n    \"metadata\": {}\n  }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "EWALLET"
                    },
                    "response": {
                      "type": "object",
                      "properties": {
                        "payment_id": {
                          "type": "string",
                          "example": "pay_dAM0lqkVuk0074"
                        },
                        "order_id": {
                          "type": "string",
                          "example": "ord_TVZ6EYuBJ85268"
                        },
                        "mobile": {
                          "type": "string",
                          "example": "08123123123"
                        },
                        "status": {
                          "type": "string",
                          "example": "processing"
                        },
                        "expiration_time": {
                          "type": "string",
                          "example": "2021-04-02T15:08:57.800297779Z"
                        },
                        "checkout_url": {
                          "type": "string",
                          "example": "https://link.to/ewallet-checkout-url"
                        },
                        "paid_amount": {
                          "type": "string",
                          "example": "1000.00"
                        },
                        "metadata": {
                          "type": "object",
                          "properties": {}
                        }
                      }
                    }
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