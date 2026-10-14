---
updatedAt: 2026-09-04T08:34:21.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Unbind E-Wallet Account

The following endpoint unbinds E-wallet Account.

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
    "/ewallet/account/{id}/unbind": {
      "put": {
        "summary": "Unbind E-Wallet Account",
        "description": "The following endpoint unbinds E-wallet Account.",
        "operationId": "unbind-e-wallet-account",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The unique identifier of the account to be unbind",
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
                    "value": "{\n  \"data\": {\n    \"account_id\": \"ewa_abc123def456\",\n    \"wallet_type\": \"DANA\",\n    \"mobile\": \"81234567890\",\n    \"status\": \"not_linked\",\n    \"message\": \"account unbinded\"\n  }"
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