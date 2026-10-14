---
updatedAt: 2026-05-28T12:34:38.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch Subaccount Balance API

The following endpoint retrieves balance of a single subaccount

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
    "/merchants/subaccount/balance/{id}": {
      "get": {
        "summary": "Fetch Subaccount Balance API",
        "description": "The following endpoint retrieves balance of a single subaccount",
        "operationId": "fetch-sub-account-fees-1",
        "parameters": [
          {
            "in": "query",
            "name": "as_of",
            "schema": {
              "type": "string",
              "default": "2022-03-29T10:00:00.000+07:00"
            },
            "required": false,
            "description": "The specific date for which you wish to retrieve the closing balance. Defaults to current time if not specified.\n\nPlease ensure that the value is in RFC3339 format. Example: \"2022-03-29T10:00:00.000+07:00\""
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "default": "mer_1234"
            },
            "required": true,
            "description": "Unique identifier of the subaccount, which can be taken from the response of Register subaccount API or Fetch Subaccount API"
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "message": "Sub-account balance retrieved successfully",
                      "data": {
                        "id": "mer_987654321",
                        "account_name": "Sub-Account Alpha",
                        "currency": "IDR",
                        "balance": 15250000,
                        "as_of": "2026-01-22T10:00:00Z"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "subaccounts": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "example": "mer_6VFgScbAcL7612"
                              },
                              "name": {
                                "type": "string",
                                "example": "Demo Sub Mercahnt"
                              },
                              "is_enabled": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "subaccount_ref_id": {
                                "type": "string",
                                "example": "reference_demo_001"
                              }
                            }
                          }
                        },
                        "total_count": {
                          "type": "integer",
                          "example": 2,
                          "default": 0
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
              "application/json": {}
            }
          },
          "500": {
            "description": "500",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "internal server error"
                    }
                  }
                }
              }
            }
          }
        },
        "x-readme": {}
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