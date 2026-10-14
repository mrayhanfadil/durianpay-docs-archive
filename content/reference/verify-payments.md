---
updatedAt: 2025-06-17T23:25:33.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Verify Payments

The following endpoint verifies the signature of payment callback

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
    "/payments/{id}/verify": {
      "post": {
        "summary": "Verify Payments",
        "description": "The following endpoint verifies the signature of payment callback",
        "operationId": "verify-payments",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Payment to be verified",
            "schema": {
              "type": "string",
              "default": "pay_123456"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "verification_signature"
                ],
                "properties": {
                  "verification_signature": {
                    "type": "string",
                    "description": "Signature which has been provided to you while you successfully made a charge. Would have recived directly as a response to payments/charge API call OR as a payload on payment.completed webhook response",
                    "default": "adf9a1a37af514c91225f6680e2df723fefebb7638519bcc7e7c9de02f2a3ab2"
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
                    "value": "{\n  \"data\": true // or false depending on verification\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "boolean",
                      "example": true,
                      "default": true
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
                    "value": "{\n    \"error\": \"error reading request body\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\",\n}"
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
                    "value": "{\n    \"error\": \"invalid Authorization header in request\",\n    \"error_code\": \"DPAY_UNAUTHORIZED_ACCESS\"\n}\n"
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
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"error verifying payment\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error verifying payment"
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