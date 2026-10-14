---
updatedAt: 2026-09-04T08:34:10.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Bind E-Wallet Account

The following endpoint binds E-wallet Account.

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
    "/ewallet/account/bind": {
      "post": {
        "summary": "Bind E-Wallet Account",
        "description": "The following endpoint binds E-wallet Account.",
        "operationId": "bind-e-wallet-account",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "mobile",
                  "wallet_type",
                  "redirect_url"
                ],
                "properties": {
                  "mobile": {
                    "type": "string",
                    "description": "The mobile number to link e-wallet account",
                    "default": "081213420562"
                  },
                  "wallet_type": {
                    "type": "string",
                    "description": "The e-wallet you want to link. Available wallet types: `GOPAY` `DANA` `SHOPEEPAY``OVO`",
                    "default": "DANA"
                  },
                  "redirect_url": {
                    "type": "string",
                    "description": "Redirect the user to the specified URL after they have completed the account linking flow",
                    "default": "https://redirect_url.com/"
                  },
                  "customerInfo": {
                    "type": "object",
                    "description": "The customerInfo fields including customer_ref_id, given_name, email, mobile. Either mobile or email is a mandatory field whereas others are optional",
                    "properties": {
                      "customer_ref_id": {
                        "type": "string",
                        "description": "Merchant’s customer reference."
                      },
                      "given_name": {
                        "type": "string",
                        "description": "Customer name."
                      },
                      "email": {
                        "type": "string",
                        "description": "Customer email address."
                      },
                      "mobile": {
                        "type": "string",
                        "description": "Customer phone number."
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
                  "OK - Binding Initiated": {
                    "value": {
                      "data": {
                        "account_id": "ewa_xyz789ghi012",
                        "wallet_type": "DANA",
                        "mobile": "81234567890",
                        "status": "pending",
                        "app_redirect_url": "https://m.dana.id/authorize?token=eyJhbGciOi...",
                        "web_redirect_url": "https://link.dana.id/web/authorize?token=eyJhbGciOi...",
                        "message": "binding initiated"
                      }
                    },
                    "summary": "OK - Binding Initiated"
                  },
                  "OK - Account Already Linked": {
                    "summary": "OK - Account Already Linked",
                    "value": {
                      "data": {
                        "account_id": "ewa_abc123def456",
                        "wallet_type": "DANA",
                        "mobile": "81234567890",
                        "status": "enabled",
                        "message": "account already linked"
                      }
                    }
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