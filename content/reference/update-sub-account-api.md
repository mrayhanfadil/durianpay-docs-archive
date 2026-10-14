---
updatedAt: 2025-06-17T23:25:56.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Update Sub-Account

The following endpoint updates subaccount's informations

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "subaccount-temporary-api",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://api.durianpay.id"
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
    "/merchants/subaccount/{id}": {
      "put": {
        "summary": "Update Sub-Account",
        "description": "The following endpoint updates subaccount's informations",
        "operationId": "update-sub-account-api",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the subaccount, which can be taken from the response of Register subaccount API or Fetch Subaccount API",
            "schema": {
              "type": "string",
              "default": "mer_123456"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the sub account"
                  },
                  "ref_id": {
                    "type": "string",
                    "description": "The unique identifier of Subaccount from the merchant"
                  },
                  "is_enabled": {
                    "type": "boolean",
                    "description": "Enable/Disable the respective subaccount"
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
                    "value": "{\n  \"data\": {\n      \"id\": \"sub_123\",\n      \"name\": \"Awesome Sub Organization 001\",\n      \"email\": \"organization_001@masterorg.biz\",\n      \"is_enabled\": true,\n      \"ref_id\": \"organization_001\",\n  }\n}"
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