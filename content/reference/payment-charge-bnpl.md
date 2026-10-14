---
updatedAt: 2025-06-17T23:25:31.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Buy Now Pay Later (BNPL)

The following endpoint charges the payment for Buy Now Pay Later

> 📘 When creating a BNPL (Buy Now, Pay Later) payment, it is mandatory that the associated order entity contains both the address and items objects.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-api-bnpl",
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
        "summary": "Buy Now Pay Later (BNPL)",
        "description": "The following endpoint charges the payment for Buy Now Pay Later",
        "operationId": "payment-charge-bnpl",
        "parameters": [
          {
            "name": "type",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "default": "BNPL"
            }
          },
          {
            "name": "request",
            "in": "query",
            "description": "The payload object for BNPL payment charge",
            "required": true,
            "schema": {
              "properties": {
                "order_id": {
                  "type": "string",
                  "description": "The id returned from create order api"
                },
                "payment_method_unique_id": {
                  "type": "string",
                  "description": "BNPL types. Available BNPL type: \"INDODANA\"",
                  "default": "INDODANA"
                },
                "amount": {
                  "type": "string",
                  "description": "Payment amount"
                }
              },
              "required": [
                "order_id",
                "payment_method_unique_id",
                "amount"
              ],
              "type": "object"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"type\": \"BNPL\",\n  \"response\": {\n    \"payment_id\": \"pay_s2sSBlDSWv4167\",\n    \"order_id\": \"ord_ZSHipeBgUd4740\",\n    \"payment_ref_id\": \"pay_ref_123\",\n    \"redirect_url\": \"https://redirect-url.com/\"\n    \"paid_amount\": \"80001.00\",\n    \"metadata\":{},\n  }\n }"
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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