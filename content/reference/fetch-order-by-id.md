---
updatedAt: 2025-06-17T23:25:24.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Order Fetch by ID API

The following endpoint retrieves the details of a single Order

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
    "/orders/{id}": {
      "get": {
        "summary": "Order Fetch by ID API",
        "description": "The following endpoint retrieves the details of a single Order",
        "operationId": "fetch-order-by-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Order to be retrieved",
            "schema": {
              "type": "string",
              "default": "ord_A1B1C1D1234"
            },
            "required": true
          },
          {
            "name": "expand",
            "in": "query",
            "description": "Used to retrieve additional information about the Order. Supported values are: customer, payments. Example: /orders/ord_A1B1C1D1234?expand=customer&expand=payments",
            "schema": {
              "type": "string",
              "default": "customer"
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
                    "value": "{\n    \"id\": \"ord_A31sd3AwAgItmmXdp\",\n    \"customer_id\": \"cus_A31sd3AGtsItmmXdp\",\n    \"amount\": \"20000\",\n    \"payment_option\": \"full_payment\",\n    \"currency\": \"IDR\",\n    \"status\": \"started\",\n    \"is_live\": true,\n    \"order_ref_id\": \"order2314\",\n    \"order_ds_ref_id\": \"\",\n    \"created_at\": 1582628071,\n    \"updated_at\": 1582888071,\n    \"description\": \"Testing\",\n    \"is_live\": true,\n    \"items\": null,\n    \"shipping_fee\": \"100\"\n    \"payment_option\": \"full_payment\",\n    \"payment_link_url\": \"\",\n    \"is_notification_enabled\": false,\n    \"email_subject\": \"\",\n    \"admin_fee_method\": \"included\",\n    \"fees\": \"1001\",\n    \"email_content\": \"\",\n    \"metadata\": []\n}\n"
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
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"order does not exists\",\n    \"error_code\": \"DPAY_ORDER_NOT_FOUND\",\n}"
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
                    "value": "{\n    \"error\": \"error getting orders\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error getting orders"
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