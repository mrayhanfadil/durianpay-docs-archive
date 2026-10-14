---
updatedAt: 2025-06-17T23:25:29.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Retail Store

The following endpoint charges the payment for Retail Store

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-api-retail-store",
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
        "summary": "Retail Store",
        "description": "The following endpoint charges the payment for Retail Store",
        "operationId": "payment-charge-retail-store",
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
                    "default": "RETAILSTORE"
                  },
                  "request": {
                    "type": "object",
                    "description": "The payload object for retail store payment charge",
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
                        "description": "Retail store to be charged. Available values: ALFAMART, INDOMARET"
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
                    "value": "{\n  \"type\": \"RETAILSTORE\",\n  \"response\": {\n    \"payment_id\": \"pay_XUwAkgIoru9966\",\n    \"order_id\": \"ord_Zwcd3aNiZR5608\",\n    \"account_number\": \"889089999561424\",\n    \"payment_ref_id\": \"pay_ref_123\",\n    \"expiration_time\": \"2021-05-01T15:12:14.437734082Z\",\n    \"paid_amount\": \"1000.00\",\n    \"metadata\": {}\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "RETAILSTORE"
                    },
                    "response": {
                      "type": "object",
                      "properties": {
                        "payment_id": {
                          "type": "string",
                          "example": "pay_XUwAkgIoru9966"
                        },
                        "order_id": {
                          "type": "string",
                          "example": "ord_Zwcd3aNiZR5608"
                        },
                        "account_number": {
                          "type": "string",
                          "example": "889089999561424"
                        },
                        "payment_ref_id": {
                          "type": "string",
                          "example": "pay_ref_123"
                        },
                        "expiration_time": {
                          "type": "string",
                          "example": "2021-05-01T15:12:14.437734082Z"
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