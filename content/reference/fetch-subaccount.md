---
updatedAt: 2025-06-17T23:25:57.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch Sub-Account

This following endpoint retrieves the details of all created subaccounts

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
    "/merchants/subaccount": {
      "get": {
        "summary": "Fetch Sub-Account",
        "description": "This following endpoint retrieves the details of all created subaccounts",
        "operationId": "fetch-subaccount",
        "parameters": [
          {
            "name": "skip",
            "in": "query",
            "description": "The number of subaccount to be skipped. The default value is 0. This can be used for pagination. in combination with count",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of subaccount to be fetch. This can be used for pagination. in combination with the skip parameter",
            "schema": {
              "type": "integer",
              "format": "int32"
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
                    "value": "{\n    \"data\": {\n        \"subaccounts\": [\n            {\n                \"id\": \"mer_6VFgScbAcL7612\",\n                \"name\": \"Demo Sub Mercahnt\",\n                \"is_enabled\": true,\n                \"subaccount_ref_id\": \"reference_demo_001\"\n            },\n            {\n                \"id\": \"mer_x6EzWyIeVX3831\",\n                \"name\": \"Subaccount - Nobel\",\n                \"is_enabled\": false,\n                \"subaccount_ref_id\": \"Nobel - Subaccount\"\n            }\n        ],\n        \"total_count\": 2\n    }\n}\n"
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
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"invalid skip and limit parameter\"\"\n    }\n"
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
                    "value": "{\n    \"error\": \"internal server error\"\n}"
                  }
                },
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