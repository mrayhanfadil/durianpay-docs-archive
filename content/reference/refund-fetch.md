---
updatedAt: 2025-06-17T23:26:01.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Refund Fetch

The following endpoint retrieves list of all Refunds created

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
    "/refunds": {
      "get": {
        "summary": "Refund Fetch",
        "description": "The following endpoint retrieves list of all Refunds created",
        "operationId": "refund-fetch",
        "parameters": [
          {
            "name": "from",
            "in": "query",
            "description": "Timestamp (in YYYY-MM-DD format) from when the refunds should be fetched",
            "schema": {
              "type": "string",
              "default": "20204-09-01"
            }
          },
          {
            "name": "to",
            "in": "query",
            "description": "Timestamp (in YYYY-MM-DD format) up till when refunds are to be fetched",
            "schema": {
              "type": "string",
              "default": "2024-09-10"
            }
          },
          {
            "name": "skip",
            "in": "query",
            "description": "The number of refunds to be skipped. The default value is 0. This can be used for pagination, in combination with count",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of refunds to be fetched. Default value is 25. This can be used for pagination, in combination with the skip parameter",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 1
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
                    "value": "{\n  \"data\": {\n    \"refund\": [\n      {\n        \"id\": \"rfn_lCs4X0M9gB0135\",\n        \"merchant_id\": \"mer_MsCtIPhqRc8045\",\n        \"status\": \"approved\",\n        \"disbursement_id\": null,\n        \"total_amount\": \"10000.00\",\n        \"created_at\": \"2021-06-29T15:43:49.998179Z\",\n        \"updated_at\": \"2021-06-29T15:43:54.634024Z\",\n        \"approved_at\": \"2021-06-29T15:43:54.634024Z\",\n        \"payment_id\": \"pay_jkQXIs4Zhw7801\",\n        \"refund_ref_id\": null,\n        \"is_live\": false,\n        \"type\": \"instant\",\n        \"order_id\": \"\",\n        \"customer_id\": \"cus_0lyb30V7O16812\",\n        \"refund_partial\": \"partial\",\n        \"refund_notes\": \"\",\n        \"payment_paid_amount\": \"\",\n        \"payment_details_type\": \"\",\n        \"payment_method_id\": \"\",\n        \"customer_name\": \"Ar\",\n        \"customer_email\": \"arifiseng@gmail.com\",\n        \"customer_phone\": \"8572281712\",\n        \"destination\": null,\n        \"ewallet_name\": null,\n        \"account_name\": null,\n        \"account_number\": null,\n        \"created_by\": 50,\n        \"created_by_name\": \"Arif Bud\",\n        \"updated_by\": 50,\n        \"updated_by_name\": \"Arif Bud\",\n        \"history\": null,\n        \"source\": \"\",\n        \"allow_retrigger\": false\n      },\n      {\n        \"id\": \"rfn_10rCPdp09a3775\",\n        \"merchant_id\": \"mer_MsCtIPhqRc8045\",\n        \"status\": \"approved\",\n        \"disbursement_id\": null,\n        \"total_amount\": \"10000.00\",\n        \"created_at\": \"2021-06-29T14:47:41.204717Z\",\n        \"updated_at\": \"2021-06-29T14:47:46.704391Z\",\n        \"approved_at\": \"2021-06-29T14:47:46.704391Z\",\n        \"payment_id\": \"pay_jkQXIs4Zhw7801\",\n        \"refund_ref_id\": null,\n        \"is_live\": false,\n        \"type\": \"instant\",\n        \"order_id\": \"\",\n        \"customer_id\": \"cus_0lyb30V7O16812\",\n        \"refund_partial\": \"partial\",\n        \"refund_notes\": \"\",\n        \"payment_paid_amount\": \"\",\n        \"payment_details_type\": \"\",\n        \"payment_method_id\": \"\",\n        \"customer_name\": \"Ar\",\n        \"customer_email\": \"arifiseng@gmail.com\",\n        \"customer_phone\": \"8572281712\",\n        \"destination\": null,\n        \"ewallet_name\": null,\n        \"account_name\": null,\n        \"account_number\": null,\n        \"created_by\": 50,\n        \"created_by_name\": \"Arif Bud\",\n        \"updated_by\": 50,\n        \"updated_by_name\": \"Arif Bud\",\n        \"history\": null,\n        \"source\": \"\",\n        \"allow_retrigger\": false\n      }\n    ],\n    \"total_data\": 2\n  }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "refund": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "example": "rfn_lCs4X0M9gB0135"
                              },
                              "merchant_id": {
                                "type": "string",
                                "example": "mer_MsCtIPhqRc8045"
                              },
                              "status": {
                                "type": "string",
                                "example": "approved"
                              },
                              "disbursement_id": {},
                              "total_amount": {
                                "type": "string",
                                "example": "10000.00"
                              },
                              "created_at": {
                                "type": "string",
                                "example": "2021-06-29T15:43:49.998179Z"
                              },
                              "updated_at": {
                                "type": "string",
                                "example": "2021-06-29T15:43:54.634024Z"
                              },
                              "approved_at": {
                                "type": "string",
                                "example": "2021-06-29T15:43:54.634024Z"
                              },
                              "payment_id": {
                                "type": "string",
                                "example": "pay_jkQXIs4Zhw7801"
                              },
                              "refund_ref_id": {},
                              "is_live": {
                                "type": "boolean",
                                "example": false,
                                "default": true
                              },
                              "type": {
                                "type": "string",
                                "example": "instant"
                              },
                              "order_id": {
                                "type": "string",
                                "example": ""
                              },
                              "customer_id": {
                                "type": "string",
                                "example": "cus_0lyb30V7O16812"
                              },
                              "refund_partial": {
                                "type": "string",
                                "example": "partial"
                              },
                              "refund_notes": {
                                "type": "string",
                                "example": ""
                              },
                              "payment_paid_amount": {
                                "type": "string",
                                "example": ""
                              },
                              "payment_details_type": {
                                "type": "string",
                                "example": ""
                              },
                              "payment_method_id": {
                                "type": "string",
                                "example": ""
                              },
                              "customer_name": {
                                "type": "string",
                                "example": "Ar"
                              },
                              "customer_email": {
                                "type": "string",
                                "example": "arifiseng@gmail.com"
                              },
                              "customer_phone": {
                                "type": "string",
                                "example": "8572281712"
                              },
                              "destination": {},
                              "ewallet_name": {},
                              "account_name": {},
                              "account_number": {},
                              "created_by": {
                                "type": "integer",
                                "example": 50,
                                "default": 0
                              },
                              "created_by_name": {
                                "type": "string",
                                "example": "Arif Bud"
                              },
                              "updated_by": {
                                "type": "integer",
                                "example": 50,
                                "default": 0
                              },
                              "updated_by_name": {
                                "type": "string",
                                "example": "Arif Bud"
                              },
                              "history": {},
                              "source": {
                                "type": "string",
                                "example": ""
                              },
                              "allow_retrigger": {
                                "type": "boolean",
                                "example": false,
                                "default": true
                              }
                            }
                          }
                        },
                        "total_data": {
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
                    "value": "{\n    \"error\": \"invalid skip and limit parameter\",\n    \"error_code\": \"DPAY_INVALID_REQUEST\",\n    \"request_id\": \"dp_Ue6hHUM6TB1425\"\n}"
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
                      "example": "dp_Ue6hHUM6TB1425"
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