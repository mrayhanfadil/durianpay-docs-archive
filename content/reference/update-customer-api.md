---
updatedAt: 2026-09-24T08:59:44.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Update Customer API

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-api-card",
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
    "/customers/{id}": {
      "patch": {
        "description": "",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "examples": {
                  "OK": {
                    "summary": "OK",
                    "value": {
                      "data": {
                        "id": "cus_DXAasdasd34312",
                        "customer_ref_id": "",
                        "given_name": "Jane Doe",
                        "middle_name": "",
                        "sur_name": "",
                        "email": "Jane.doe@durianpay.id",
                        "mobile": "+6281213420555",
                        "address_info": {
                          "id": 0,
                          "receiver_name": "",
                          "receiver_phone": "",
                          "label": "",
                          "address_line_1": "",
                          "address_line_2": "",
                          "city": "",
                          "region": "",
                          "country": "",
                          "postal_code": "",
                          "landmark": "",
                          "customer_id": "",
                          "is_default": false,
                          "created_at": "0001-01-01T00:00:00Z",
                          "updated_at": "0001-01-01T00:00:00Z"
                        },
                        "created_at": "2026-04-16T14:07:02.995706Z",
                        "updated_at": "2026-04-17T11:20:16.150864Z",
                        "metadata": {},
                        "is_live": true,
                        "ip_address": "",
                        "merchant_id": ""
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "query",
            "name": "id",
            "schema": {
              "type": "string",
              "default": "123"
            },
            "description": "Durianpay's Customer ID. Returned during payment/virtual account creation. ",
            "required": true
          }
        ],
        "operationId": "patch_customers-id",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "given_name": {
                    "type": "string",
                    "description": "The customer's name"
                  },
                  "email": {
                    "type": "string",
                    "description": "The customer's email address. Should of the format jane.doe@gmail.com and should not contain any invalid special characters (¢,£,§,©,etc)"
                  },
                  "mobile": {
                    "type": "string",
                    "description": "The customer's mobile number. Please ensure that the number follows Indonesia's phone number format : +62xxxxxxxxxx or 08xxxxxxxxxx."
                  },
                  "customer_ref_id": {
                    "type": "string",
                    "description": "A unique reference ID from the merchant to identify the customer\n"
                  },
                  "payor_name_aliases": {
                    "type": "array",
                    "description": "Other names the payer may use, such as alternate spellings or nicknames. Used together with `given_name` when matching the name on the incoming payment. Accepts up to 5 values. Only applies to crypto merchants; ignored for all other merchants.",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "summary": "Update Customer API"
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