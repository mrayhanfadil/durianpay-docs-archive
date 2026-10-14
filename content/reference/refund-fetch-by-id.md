---
updatedAt: 2025-06-17T23:26:02.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Refund Fetch by ID

The following endpoint retrieves the details of a single refund

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
    "/refunds/{id}": {
      "get": {
        "summary": "Refund Fetch by ID",
        "description": "The following endpoint retrieves the details of a single refund",
        "operationId": "refund-fetch-by-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Refund to be retrieved",
            "schema": {
              "type": "string",
              "default": "rfn_Ct2uKVFwts5080"
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
                    "value": "{\n  \"data\": {\n    \"id\": \"rfn_lCs4X0M9gB0135\",\n    \"ref_id\": null,\n    \"amount\": \"10000.00\",\n    \"refund_type\": \"partial\",\n    \"status\": \"approved\",\n    \"created_at\": \"2021-06-29T15:43:49.998179Z\",\n    \"updated_at\": \"2021-06-29T15:43:54.634024Z\",\n    \"approved_at\": \"2021-06-29T15:43:54.634024Z\",\n    \"source\": \"api\",\n    \"customer_id\": \"cus_0lyb30V7O16812\",\n    \"customer_name\": \"John Doe\",\n    \"customer_email\": \"john@doe.com\",\n    \"customer_phone\": \"0812778161\"\n  }\n}\n"
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
                          "example": "rfn_lCs4X0M9gB0135"
                        },
                        "ref_id": {},
                        "amount": {
                          "type": "string",
                          "example": "10000.00"
                        },
                        "refund_type": {
                          "type": "string",
                          "example": "partial"
                        },
                        "status": {
                          "type": "string",
                          "example": "approved"
                        },
                        "created_at": {
                          "type": "string",
                          "example": "2021-06-29T15:43:49.998179Z"
                        },
                        "updated_at": {
                          "type": "string",
                          "example": "2021-06-29T15:43:54.634024Z"
                        },
                        "approved_at": {
                          "type": "string",
                          "example": "2021-06-29T15:43:54.634024Z"
                        },
                        "source": {
                          "type": "string",
                          "example": "api"
                        },
                        "customer_id": {
                          "type": "string",
                          "example": "cus_0lyb30V7O16812"
                        },
                        "customer_name": {
                          "type": "string",
                          "example": "John Doe"
                        },
                        "customer_email": {
                          "type": "string",
                          "example": "john@doe.com"
                        },
                        "customer_phone": {
                          "type": "string",
                          "example": "0812778161"
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
                    "value": "{\n    \"error\": \"error getting refund\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error getting refund"
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