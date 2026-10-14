---
updatedAt: 2026-09-30T10:21:56.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Card

The following endpoint charges the payment for Card

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-api-card",
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
        "summary": "Card",
        "description": "The following endpoint charges the payment for Card",
        "operationId": "payment-charge-card",
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
                    "default": "CARD"
                  },
                  "request": {
                    "type": "object",
                    "description": "The payload object for Card payment charge",
                    "required": [
                      "order_id",
                      "amount"
                    ],
                    "properties": {
                      "order_id": {
                        "type": "string",
                        "description": "The id returned from create order api"
                      },
                      "amount": {
                        "type": "string",
                        "description": "Payment amount"
                      },
                      "customer_info": {
                        "type": "object",
                        "properties": {}
                      },
                      "installment": {
                        "type": "object",
                        "description": "",
                        "properties": {
                          "tenor": {
                            "type": "integer",
                            "default": "",
                            "description": "Specifies which tenor you want this transaction to be processed with"
                          },
                          "tenor_type": {
                            "type": "string",
                            "default": "",
                            "description": "Specify the units of the selected tenor, available values: `M` (Month)"
                          }
                        }
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
                    "value": "{\n  \"type\": \"CARD\",\n  \"response\": {\n      \"payment_id\": \"pay_1Ylb1r122v1860\",\n      \"order_id\": \"ord_sipQEaBnkX0407\",\n      \"payment_ref_id\": \"pay_ref_123\",\n      \"token_id\": \"\",\n      \"status\": \"processing\",\n      \"paid_amount\": \"10000.00\",\n      \"metadata\": {},\n      \"checkout_url\": \"https://link.to/card-checkout-url\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "example": "CARD"
                    },
                    "response": {
                      "type": "object",
                      "properties": {
                        "payment_id": {
                          "type": "string",
                          "example": "pay_1Ylb1r122v1860"
                        },
                        "order_id": {
                          "type": "string",
                          "example": "ord_sipQEaBnkX0407"
                        },
                        "payment_ref_id": {
                          "type": "string",
                          "example": "pay_ref_123"
                        },
                        "token_id": {
                          "type": "string",
                          "example": ""
                        },
                        "status": {
                          "type": "string",
                          "example": "processing"
                        },
                        "paid_amount": {
                          "type": "string",
                          "example": "10000.00"
                        },
                        "metadata": {
                          "type": "object",
                          "properties": {}
                        },
                        "checkout_url": {
                          "type": "string",
                          "example": "https://link.to/card-checkout-url"
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
        }
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