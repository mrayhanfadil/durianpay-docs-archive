---
updatedAt: 2026-09-04T08:34:27.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch E-Wallet Account Details

The following endpoint fetch E-wallet Account details.

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
    "/ewallet/account/{id}": {
      "get": {
        "summary": "Fetch E-Wallet Account Details",
        "description": "The following endpoint fetch E-wallet Account details.",
        "operationId": "fetch-e-wallet-account-details",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier assigned to a specific customer's linked e-wallet account, which is obtained after the account binding process.",
            "schema": {
              "type": "string",
              "default": "ewa_123"
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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
        "x-internal": false
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