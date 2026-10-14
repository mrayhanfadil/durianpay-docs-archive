---
updatedAt: 2025-06-17T23:26:02.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Refund Fetch by Payment ID

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
    "/refunds/payment/{id}": {
      "get": {
        "summary": "Refund Fetch by Payment ID",
        "description": "",
        "operationId": "get-refund-by-payment-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The payment ID which being refunded",
            "schema": {
              "type": "string",
              "default": "pay_abcdefg1234"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"data\": [\n        {\n            \"id\": \"rfn_abcdefg1234\",\n            \"ref_id\": \"rfn_ref_00\",\n            \"amount\": \"10000.00\",\n            \"refund_type\": \"\",\n            \"status\": \"done\",\n            \"created_at\": \"2024-11-12T06:49:21.501177Z\",\n            \"updated_at\": \"2024-11-12T06:49:21.501178Z\",\n            \"approved_at\": null,\n            \"source\": \"dashboard\",\n            \"customer_id\": \"cus_abcdefg1231232\",\n            \"customer_name\": \"\",\n            \"customer_email\": \"\",\n            \"customer_phone\": \"\",\n            \"failure_reason\": \"\"\n        }\n    ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "example": "rfn_abcdefg1234"
                          },
                          "ref_id": {
                            "type": "string",
                            "example": "rfn_ref_00"
                          },
                          "amount": {
                            "type": "string",
                            "example": "10000.00"
                          },
                          "refund_type": {
                            "type": "string",
                            "example": ""
                          },
                          "status": {
                            "type": "string",
                            "example": "done"
                          },
                          "created_at": {
                            "type": "string",
                            "example": "2024-11-12T06:49:21.501177Z"
                          },
                          "updated_at": {
                            "type": "string",
                            "example": "2024-11-12T06:49:21.501178Z"
                          },
                          "approved_at": {},
                          "source": {
                            "type": "string",
                            "example": "dashboard"
                          },
                          "customer_id": {
                            "type": "string",
                            "example": "cus_abcdefg1231232"
                          },
                          "customer_name": {
                            "type": "string",
                            "example": ""
                          },
                          "customer_email": {
                            "type": "string",
                            "example": ""
                          },
                          "customer_phone": {
                            "type": "string",
                            "example": ""
                          },
                          "failure_reason": {
                            "type": "string",
                            "example": ""
                          }
                        }
                      }
                    }
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