---
updatedAt: 2025-06-17T23:25:32.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Payment Fetch by ID

The following endpoint retrieves the details of a single payment

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
    "/payments/{id}": {
      "get": {
        "summary": "Payment Fetch by ID",
        "description": "The following endpoint retrieves the details of a single payment",
        "operationId": "fetch-payment-by-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Payment to be retrieved",
            "schema": {
              "type": "string",
              "default": "pay_12345678"
            },
            "required": true
          },
          {
            "name": "expand",
            "in": "query",
            "description": "Used to retrieve additional information about the Order. Supported values are: customer, payments. Example: /orders/ord_A1B1C1D1234?expand=customer&expand=payments",
            "schema": {
              "type": "string",
              "default": "order"
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
                    "value": "{\n    \"id\": \"pay_76n67eK9Fq4137\",\n    \"amount\": \"20000\",\n    \"currency\": \"IDR\",\n    \"status\": \"completed\",\n    \"order_id\": \"ord_B14sdfwAdmmSDF24a\",\n    \"payment_ref_id\": \"txn2314\",\n    \"created_at\": 1582628071,\n    \"is_live\": true,\n    \"expiration_date\": \"2021-09-21T05:11:09.574136Z\",\n    \"payment_details_type\": \"ewallet_details\",\n    \"method_id\": \"OVO\",\n    \"created_at\": \"2021-09-20T05:11:09.574138Z\",\n    \"updated_at\": \"2021-09-20T05:11:15.161768Z\",\n    \"metadata\": {},\n    \"retry_count\": 0,\n    \"discount\": \"\",\n    \"paid_amount\": \"\",\n    \"provider_id\": \"\",\n    \"total_fee\": \"\",\n    \"promo_id\": \"\",\n    \"shipping_fee\": \"\",\n    \"ds_error_metadata\": null,\n    \"CustomerID\": \"cus_iT1g1t74655079\",\n    \"CustomerName\": \"test\",\n    \"CustomerEmail\": \"\",\n    \"OrderRefID\": \"\",\n    \"Currency\": \"IDR\",\n    \"failure_reason\": {}\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "pay_76n67eK9Fq4137"
                    },
                    "amount": {
                      "type": "string",
                      "example": "20000"
                    },
                    "currency": {
                      "type": "string",
                      "example": "IDR"
                    },
                    "status": {
                      "type": "string",
                      "example": "completed"
                    },
                    "order_id": {
                      "type": "string",
                      "example": "ord_B14sdfwAdmmSDF24a"
                    },
                    "payment_ref_id": {
                      "type": "string",
                      "example": "txn2314"
                    },
                    "created_at": {
                      "type": "string",
                      "example": "2021-09-20T05:11:09.574138Z"
                    },
                    "is_live": {
                      "type": "boolean",
                      "example": true,
                      "default": true
                    },
                    "expiration_date": {
                      "type": "string",
                      "example": "2021-09-21T05:11:09.574136Z"
                    },
                    "payment_details_type": {
                      "type": "string",
                      "example": "ewallet_details"
                    },
                    "method_id": {
                      "type": "string",
                      "example": "OVO"
                    },
                    "updated_at": {
                      "type": "string",
                      "example": "2021-09-20T05:11:15.161768Z"
                    },
                    "metadata": {
                      "type": "object",
                      "properties": {}
                    },
                    "retry_count": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "discount": {
                      "type": "string",
                      "example": ""
                    },
                    "paid_amount": {
                      "type": "string",
                      "example": ""
                    },
                    "provider_id": {
                      "type": "string",
                      "example": ""
                    },
                    "total_fee": {
                      "type": "string",
                      "example": ""
                    },
                    "promo_id": {
                      "type": "string",
                      "example": ""
                    },
                    "shipping_fee": {
                      "type": "string",
                      "example": ""
                    },
                    "ds_error_metadata": {},
                    "CustomerID": {
                      "type": "string",
                      "example": "cus_iT1g1t74655079"
                    },
                    "CustomerName": {
                      "type": "string",
                      "example": "test"
                    },
                    "CustomerEmail": {
                      "type": "string",
                      "example": ""
                    },
                    "OrderRefID": {
                      "type": "string",
                      "example": ""
                    },
                    "Currency": {
                      "type": "string",
                      "example": "IDR"
                    },
                    "failure_reason": {
                      "type": "object",
                      "properties": {}
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
                    "value": "{\n    \"error\": \"error getting payment\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error getting payment"
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