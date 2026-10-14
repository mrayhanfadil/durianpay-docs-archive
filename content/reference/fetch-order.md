---
updatedAt: 2025-06-17T23:25:24.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Order Fetch API

The following endpoint retrieves the details of all Orders created

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
    "/orders": {
      "get": {
        "summary": "Order Fetch API",
        "description": "The following endpoint retrieves the details of all Orders created",
        "operationId": "fetch-order",
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
            "description": "The number of orders to be skipped. The default value is 0. This can be used for pagination, in combination with count",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of orders to be fetched. Default value is 25. This can be used for pagination, in combination with the skip parameter",
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
                    "value": "{\n  \"orders\": [{\n    \"id\": \"ord_A31sd3AwAgItmmXdp\",\n    \"customer_id\": \"cus_p46hhyWq988496\",\n    \"amount\": \"20000\",\n    \"payment_option\": \"full_payment\",\n    \"currency\": \"IDR\",\n    \"status\": \"started\",\n    \"order_ref_id\": \"order2314\",\n    \"order_ds_ref_id\": \"\",\n    \"created_at\": 1582628071,\n    \"updated_at\": 1582899071,\n    \"expiry_date_\": 1592628071,\n    \"is_live\": true,\n    \"given_name\": \"John\",\n    \"sur_name\": \"Doe\",\n    \"email\": \"jude_casper@koss.info\",\n    \"mobile\": \"+6285722173217\",\n    \"payment_id\": \"pay_KEQQaXqazp2892\",\n    \"payment_details_type\": \"bnpl_details\",\n    \"payment_method_id\": \"ZZZZZZ\",\n    \"payment_status\": \"completed\",\n    \"payment_date\": \"2025-01-01T01:11:11.111111Z\",\n    \"description\": \"this order is fetched\",\n    \"payment_link_url\": \"zzzzzz\",\n    \"is_notification_enabled\": false,\n    \"email_subject\": \"This is email subject\",\n    \"email_content\": \"This is email body\"\n  }, {\n    \"id\": \"ord_A54sd3AwAgItmmXdp\",\n    \"customer_id\": \"cus_p96hhyWq988496\",\n    \"amount\": \"20000\",\n    \"payment_option\": \"full_payment\",\n    \"currency\": \"IDR\",\n    \"status\": \"started\",\n    \"order_ref_id\": \"order2314\",\n    \"order_ds_ref_id\": \"\",\n    \"created_at\": 1582628072,\n    \"updated_at\": 1582899072,\n    \"expiry_date_\": 1592628072,\n    \"is_live\": true,\n    \"given_name\": \"Jane\",\n    \"sur_name\": \"Doe\",\n    \"email\": \"jane_doe@koss.info\",\n    \"mobile\": \"+6285722223217\",\n    \"payment_id\": \"pay_loQQaXqazp2892\",\n    \"payment_details_type\": \"bnpl_details\",\n    \"payment_method_id\": \"ZZZZZZ\",\n    \"payment_status\": \"completed\",\n    \"payment_date\": \"2025-01-01T01:11:11.111111Z\",\n    \"description\": \"this order is fetched\",\n    \"payment_link_url\": \"zzzzzz\",\n    \"is_notification_enabled\": false,\n    \"email_subject\": \"This is email subject\",\n    \"email_content\": \"This is email body\"\n  }],\n  \"count\": 2\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "orders": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "example": "ord_A31sd3AwAgItmmXdp"
                          },
                          "customer_id": {
                            "type": "string",
                            "example": "cus_p46hhyWq988496"
                          },
                          "amount": {
                            "type": "string",
                            "example": "20000"
                          },
                          "payment_option": {
                            "type": "string",
                            "example": "full_payment"
                          },
                          "currency": {
                            "type": "string",
                            "example": "IDR"
                          },
                          "status": {
                            "type": "string",
                            "example": "started"
                          },
                          "order_ref_id": {
                            "type": "string",
                            "example": "order2314"
                          },
                          "order_ds_ref_id": {
                            "type": "string",
                            "example": ""
                          },
                          "created_at": {
                            "type": "integer",
                            "example": 1582628071,
                            "default": 0
                          },
                          "updated_at": {
                            "type": "integer",
                            "example": 1582899071,
                            "default": 0
                          },
                          "expiry_date_": {
                            "type": "integer",
                            "example": 1592628071,
                            "default": 0
                          },
                          "is_live": {
                            "type": "boolean",
                            "example": true,
                            "default": true
                          },
                          "given_name": {
                            "type": "string",
                            "example": "John"
                          },
                          "sur_name": {
                            "type": "string",
                            "example": "Doe"
                          },
                          "email": {
                            "type": "string",
                            "example": "jude_casper@koss.info"
                          },
                          "mobile": {
                            "type": "string",
                            "example": "+6285722173217"
                          },
                          "payment_id": {
                            "type": "string",
                            "example": "pay_KEQQaXqazp2892"
                          },
                          "payment_details_type": {
                            "type": "string",
                            "example": "bnpl_details"
                          },
                          "payment_method_id": {
                            "type": "string",
                            "example": "ZZZZZZ"
                          },
                          "payment_status": {
                            "type": "string",
                            "example": "completed"
                          },
                          "payment_date": {
                            "type": "string",
                            "example": "2025-01-01T01:11:11.111111Z"
                          },
                          "description": {
                            "type": "string",
                            "example": "this order is fetched"
                          },
                          "payment_link_url": {
                            "type": "string",
                            "example": "zzzzzz"
                          },
                          "is_notification_enabled": {
                            "type": "boolean",
                            "example": false,
                            "default": true
                          },
                          "email_subject": {
                            "type": "string",
                            "example": "This is email subject"
                          },
                          "email_content": {
                            "type": "string",
                            "example": "This is email body"
                          }
                        }
                      }
                    },
                    "count": {
                      "type": "integer",
                      "example": 2,
                      "default": 0
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
                    "value": "{\n    \"error\": \"invalid skip and limit parameter\",\n    \"error_code\": \"DPAY_INVALID_REQUEST\",\n    \"request_id\": \"dp_1lRGmHZClt3882\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "invalid skip and limit parameter"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INVALID_REQUEST"
                    },
                    "request_id": {
                      "type": "string",
                      "example": "dp_1lRGmHZClt3882"
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
                    "value": "{\n    \"error\": \"error getting orders\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}"
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