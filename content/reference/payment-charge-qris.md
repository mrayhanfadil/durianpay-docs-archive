---
updatedAt: 2025-06-17T23:25:28.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# QRIS

The following endpoint charges the payment for QRIS

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-api-qris",
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
        "summary": "QRIS",
        "description": "The following endpoint charges the payment for QRIS",
        "operationId": "payment-charge-qris",
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
                    "default": "QRIS"
                  },
                  "request": {
                    "type": "object",
                    "description": "The payload object for QRIS payment charge",
                    "required": [
                      "order_id",
                      "name",
                      "amount"
                    ],
                    "properties": {
                      "order_id": {
                        "type": "string",
                        "description": "The id returned from create order api"
                      },
                      "name": {
                        "type": "string",
                        "description": "QRIS Name"
                      },
                      "amount": {
                        "type": "string",
                        "description": "Payment amount"
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
                    "value": "{\n  \"type\": \"QRIS\",\n  \"response\": {\n    \"payment_id\": \"pay_s2sSBlDSWv4167\",\n    \"order_id\": \"ord_QETgbs2UGL3100\",\n    \"status\": \"processing\",\n    \"expiration_time\": \"2021-09-15T15:44:37Z\",\n    \"creation_time\": \"2021-09-12T15:44:37ZZ\",\n    \"qr_string\": \"data:image/png;base64, long_qr_string\",\n    \"unique_id\": \"QRIS\",\n    \"metadata\":{\n      \"merchant_name\": \"Durianpay\",\n      \"merchant_id\" : \"sample_national_merchant_id\"\n    },\n    \"amount\": \"80001.00\",\n    \"qr_code\": \"00020101021226590013ID.CO.BNI.WWW011893600009150002286002092107061320303UME51470015ID.OR.GPNQR.WWW0217ID2107271315771960303UME520454995303360540880001.005802ID5905Ajesh6013JAKARTA PUSAT6105101406214011038291492856304E1F\"\n  }\n }\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "QRIS"
                    },
                    "response": {
                      "type": "object",
                      "properties": {
                        "payment_id": {
                          "type": "string",
                          "example": "pay_s2sSBlDSWv4167"
                        },
                        "order_id": {
                          "type": "string",
                          "example": "ord_QETgbs2UGL3100"
                        },
                        "status": {
                          "type": "string",
                          "example": "processing"
                        },
                        "expiration_time": {
                          "type": "string",
                          "example": "2021-09-15T15:44:37Z"
                        },
                        "creation_time": {
                          "type": "string",
                          "example": "2021-09-12T15:44:37ZZ"
                        },
                        "qr_string": {
                          "type": "string",
                          "example": "data:image/png;base64, long_qr_string"
                        },
                        "unique_id": {
                          "type": "string",
                          "example": "QRIS"
                        },
                        "metadata": {
                          "type": "object",
                          "properties": {
                            "merchant_name": {
                              "type": "string",
                              "example": "Durianpay"
                            },
                            "merchant_id": {
                              "type": "string",
                              "example": "sample_national_merchant_id"
                            }
                          }
                        },
                        "amount": {
                          "type": "string",
                          "example": "80001.00"
                        },
                        "qr_code": {
                          "type": "string",
                          "example": "00020101021226590013ID.CO.BNI.WWW011893600009150002286002092107061320303UME51470015ID.OR.GPNQR.WWW0217ID2107271315771960303UME520454995303360540880001.005802ID5905Ajesh6013JAKARTA PUSAT6105101406214011038291492856304E1F"
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