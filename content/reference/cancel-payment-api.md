---
updatedAt: 2025-06-17T23:25:34.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Cancel Payment API

The following endpoint cancels a single Payment

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
    "/payments/{id}/cancel": {
      "put": {
        "summary": "Cancel Payment API",
        "description": "The following endpoint cancels a single Payment",
        "operationId": "cancel-payment-api",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Payment to be cancelled",
            "schema": {
              "type": "string",
              "default": "pay_123456"
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
                    "value": "{\n    \"data\": {\n        \"id\": \"pay_ohXLNm2fPw6868\",\n        \"status\": \"cancelled\",\n        \"order_id\": \"ord_Dg0Dz9wwKP1602\",\n        \"created_at\": \"2020-11-19T22:09:48Z\",\n        \"updated_at\": \"2020-11-26T20:02:24.561169Z\"\n    }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "pay_ohXLNm2fPw6868"
                        },
                        "status": {
                          "type": "string",
                          "example": "cancelled"
                        },
                        "order_id": {
                          "type": "string",
                          "example": "ord_Dg0Dz9wwKP1602"
                        },
                        "created_at": {
                          "type": "string",
                          "example": "2020-11-19T22:09:48Z"
                        },
                        "updated_at": {
                          "type": "string",
                          "example": "2020-11-26T20:02:24.561169Z"
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
                    "value": "{\n    \"error\": \"invalid payment id\",\n    \"error_code\": \"DPAY_INVALID_PAYMENT_ID\",\n    \"request_id\": \"not-set\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "invalid payment id"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INVALID_PAYMENT_ID"
                    },
                    "request_id": {
                      "type": "string",
                      "example": "not-set"
                    }
                  }
                }
              }
            }
          },
          "401": {
            "description": "401",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"invalid Authorization header in request\",\n    \"error_code\": \"DPAY_UNAUTHORIZED_ACCESS\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "invalid Authorization header in request"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_UNAUTHORIZED_ACCESS"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "500",
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"error cancelling payment\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error cancelling payment"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INTERNAL_ERROR"
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