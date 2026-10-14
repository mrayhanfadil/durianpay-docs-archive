---
updatedAt: 2025-06-17T23:25:36.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch Virtual Account by ID

The following endpoint retrieves the details of a single Virtual Account

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
    "/payments/va/{id}": {
      "get": {
        "summary": "Fetch Virtual Account by ID",
        "description": "The following endpoint retrieves the details of a single Virtual Account",
        "operationId": "fetch-virtual-account-by-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Virtual Account to be retrieved",
            "schema": {
              "type": "string",
              "default": "va_12345"
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
                    "value": "{\n    \"data\": {\n        \"virtual_account\": {\n            \"id\": \"va_sample_6YBBiGRAPa0943\",\n            \"bank_code\": \"PERMATA\",\n            \"account_number\": \"8856500451311212\",\n            \"name\": \"Ardi Hanan Durian\",\n            \"is_closed\": false,\n            \"amount\": 0,\n            \"currency\": \"IDR\",\n            \"customer_id\": \"cus_akA2FwrR5B2217\",\n            \"is_sandbox\": true,\n            \"created_at\": \"2022-06-27T02:42:28.753671Z\",\n            \"expiry_at\": \"2022-06-27T13:54:27.333786Z\",\n            \"metadata\": {},\n            \"is_disabled\": false,\n            \"is_paid\": false,\n            \"is_reusable\": true,\n            \"min_amount\": 50000,\n            \"max_amount\": null,\n            \"va_ref_id\": \"\",\n            \"auto_disable_after_payment\": false\n        },\n        \"virtual_account_status\": \"VirtualAccountExpired\",\n        \"customer\": {\n            \"id\": \"cus_akA2FwrR5B2217\",\n            \"customer_ref_id\": \"\",\n            \"given_name\": \"\",\n            \"middle_name\": \"\",\n            \"sur_name\": \"\",\n            \"email\": \"p.ardi.h@gmail.com\",\n            \"mobile\": \"+628978678578\"\n        },\n        \"payments\": [\n            {\n                \"id\": \"pay_D3yQ1WWSu12492\",\n                \"order_id\": \"ord_5mVIixYOlL6710\",\n                \"payment_ref_id\": \"1234\",\n                \"settlement_id\": \"\",\n                \"payment_ds_ref_id\": \"62340733-c1ce-4fd3-9090-ab89a6\",\n                \"amount\": \"10000.00\",\n                \"status\": \"completed\",\n                \"is_live\": true,\n                \"expiration_date\": \"2022-12-08T09:28:33.756474Z\",\n                \"payment_details_type\": \"va_details\",\n                \"method_id\": \"BNI\",\n                \"created_at\": \"2022-12-08T09:28:33.756474Z\",\n                \"updated_at\": \"2022-12-08T09:28:33.756474Z\",\n                \"metadata\": null,\n                \"retry_count\": 0,\n                \"discount\": \"\",\n                \"paid_amount\": \"10000.00\",\n                \"provider_id\": \"MCPAYMENT\",\n                \"total_fee\": \"\",\n                \"promo_id\": \"\",\n                \"shipping_fee\": \"\",\n                \"ds_error_metadata\": null,\n                \"failure_reason\": {},\n                \"settlement_status\": \"\"\n            }\n        ],\n        \"total_payment\": 1,\n        \"total_page\": 1,\n        \"current_page\": 1\n    }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "virtual_account": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "example": "va_sample_6YBBiGRAPa0943"
                            },
                            "bank_code": {
                              "type": "string",
                              "example": "PERMATA"
                            },
                            "account_number": {
                              "type": "string",
                              "example": "8856500451311212"
                            },
                            "name": {
                              "type": "string",
                              "example": "Ardi Hanan Durian"
                            },
                            "is_closed": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            },
                            "amount": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            },
                            "currency": {
                              "type": "string",
                              "example": "IDR"
                            },
                            "customer_id": {
                              "type": "string",
                              "example": "cus_akA2FwrR5B2217"
                            },
                            "is_sandbox": {
                              "type": "boolean",
                              "example": true,
                              "default": true
                            },
                            "created_at": {
                              "type": "string",
                              "example": "2022-06-27T02:42:28.753671Z"
                            },
                            "expiry_at": {
                              "type": "string",
                              "example": "2022-06-27T13:54:27.333786Z"
                            },
                            "metadata": {
                              "type": "object",
                              "properties": {}
                            },
                            "is_disabled": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            },
                            "is_paid": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            },
                            "is_reusable": {
                              "type": "boolean",
                              "example": true,
                              "default": true
                            },
                            "min_amount": {
                              "type": "integer",
                              "example": 50000,
                              "default": 0
                            },
                            "max_amount": {},
                            "va_ref_id": {
                              "type": "string",
                              "example": ""
                            },
                            "auto_disable_after_payment": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            }
                          }
                        },
                        "virtual_account_status": {
                          "type": "string",
                          "example": "VirtualAccountExpired"
                        },
                        "customer": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "example": "cus_akA2FwrR5B2217"
                            },
                            "customer_ref_id": {
                              "type": "string",
                              "example": ""
                            },
                            "given_name": {
                              "type": "string",
                              "example": ""
                            },
                            "middle_name": {
                              "type": "string",
                              "example": ""
                            },
                            "sur_name": {
                              "type": "string",
                              "example": ""
                            },
                            "email": {
                              "type": "string",
                              "example": "p.ardi.h@gmail.com"
                            },
                            "mobile": {
                              "type": "string",
                              "example": "+628978678578"
                            }
                          }
                        },
                        "payments": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "example": "pay_D3yQ1WWSu12492"
                              },
                              "order_id": {
                                "type": "string",
                                "example": "ord_5mVIixYOlL6710"
                              },
                              "payment_ref_id": {
                                "type": "string",
                                "example": "1234"
                              },
                              "settlement_id": {
                                "type": "string",
                                "example": ""
                              },
                              "payment_ds_ref_id": {
                                "type": "string",
                                "example": "62340733-c1ce-4fd3-9090-ab89a6"
                              },
                              "amount": {
                                "type": "string",
                                "example": "10000.00"
                              },
                              "status": {
                                "type": "string",
                                "example": "completed"
                              },
                              "is_live": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "expiration_date": {
                                "type": "string",
                                "example": "2022-12-08T09:28:33.756474Z"
                              },
                              "payment_details_type": {
                                "type": "string",
                                "example": "va_details"
                              },
                              "method_id": {
                                "type": "string",
                                "example": "BNI"
                              },
                              "created_at": {
                                "type": "string",
                                "example": "2022-12-08T09:28:33.756474Z"
                              },
                              "updated_at": {
                                "type": "string",
                                "example": "2022-12-08T09:28:33.756474Z"
                              },
                              "metadata": {},
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
                                "example": "10000.00"
                              },
                              "provider_id": {
                                "type": "string",
                                "example": "MCPAYMENT"
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
                              "failure_reason": {
                                "type": "object",
                                "properties": {}
                              },
                              "settlement_status": {
                                "type": "string",
                                "example": ""
                              }
                            }
                          }
                        },
                        "total_payment": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "total_page": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "current_page": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        }
                      }
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
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"sql: no rows in result set\",\n    \"error_code\": \"DPAY_VA_NOT_FOUND\",\n    \"request_id\": \"dp_d3HX9S5W0r4989\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "sql: no rows in result set"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_VA_NOT_FOUND"
                    },
                    "request_id": {
                      "type": "string",
                      "example": "dp_d3HX9S5W0r4989"
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