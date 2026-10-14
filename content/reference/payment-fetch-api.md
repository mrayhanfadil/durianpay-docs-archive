---
updatedAt: 2025-06-17T23:25:32.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Payment Fetch API

The following endpoint retrieves the details of all Payments created

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
    "/payments": {
      "get": {
        "summary": "Payment Fetch API",
        "description": "The following endpoint retrieves the details of all Payments created",
        "operationId": "payment-fetch-api",
        "parameters": [
          {
            "name": "from",
            "in": "query",
            "description": "Timestamp (in YYYY-MM-DD format) from when the Orders should be fetched",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "to",
            "in": "query",
            "description": "Timestamp (in YYYY-MM-DD format) up till when Orders are to be fetched",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "skip",
            "in": "query",
            "description": "The number of payments to be skipped. The default value is 0. This can be used for pagination, in combination with count",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of payments to be fetched. Default value is 25. This can be used for pagination, in combination with the skip parameter",
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
                    "value": "{\n  payments: [{\n    \"id\": \"pay_A31sd3AwAgItmmXdp\",\n    \"amount\": \"20000\",\n    \"currency\": \"IDR\",\n    \"status\": \"completed\",\n    \"order_id\": \"ord_B14sdfwAdmmSDF24a\",\n    \"payment_ref_id\": \"txn2314\",\n    \"created_at\": 1582628071,\n    \"is_live\": true,\n    \"expiration_date\": \"2021-09-21T05:11:09.574136Z\",\n    \"payment_details_type\": \"ewallet_details\",\n    \"method_id\": \"OVO\",\n    \"created_at\": \"2021-09-20T05:11:09.574138Z\",\n    \"updated_at\": \"2021-09-20T05:11:15.161768Z\",\n    \"metadata\": {},\n    \"retry_count\": 0,\n    \"discount\": \"\",\n    \"paid_amount\": \"\",\n    \"provider_id\": \"\",\n    \"total_fee\": \"\",\n    \"promo_id\": \"\",\n    \"shipping_fee\": \"\",\n    \"ds_error_metadata\": null,\n    \"CustomerID\": \"cus_iT1g1t74655079\",\n    \"CustomerName\": \"test\",\n    \"CustomerEmail\": \"\",\n    \"OrderRefID\": \"\",\n    \"Currency\": \"IDR\",\n    \"failure_reason\": {}\n  }],\n  total: 1\n}\n"
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
                    "value": "{\n    \"error\": \"invalid skip and limit parameter\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "invalid skip and limit parameter"
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
                    "value": "{\n    \"error\": \"invalid Authorization header in request\",\n    \"error_code\": \"DPAY_UNAUTHORIZED_ACCESS\"\n}\n"
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
                    "value": "{\n  \"error\": \"error getting payments\",\n  \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error getting payments"
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