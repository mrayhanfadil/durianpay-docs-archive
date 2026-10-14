---
updatedAt: 2025-06-17T23:25:33.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Check Payment Status

The following endpoint checks the status of a single Payment

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
    "/payments/{id}/status": {
      "get": {
        "summary": "Check Payment Status",
        "description": "The following endpoint checks the status of a single Payment",
        "operationId": "check-payment-status",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Payment to be retrieved",
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
                    "value": "{\n    \"data\": {\n        \"status\": \"completed\",\n        \"is_completed\": true,\n        \"signature\": \"9e892f199d026d06a56669e658a56f264610431d24e8b4d07f7bd46f6d5062d2\"\n    }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "status": {
                          "type": "string",
                          "example": "completed"
                        },
                        "is_completed": {
                          "type": "boolean",
                          "example": true,
                          "default": true
                        },
                        "signature": {
                          "type": "string",
                          "example": "9e892f199d026d06a56669e658a56f264610431d24e8b4d07f7bd46f6d5062d2"
                        }
                      }
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
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"error getting payment status\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error getting payment status"
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