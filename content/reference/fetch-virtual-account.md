---
updatedAt: 2025-06-17T23:25:36.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch Virtual Account

The following endpoint retrieves the details of all Virtual Accounts created

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
    "/payments/va": {
      "get": {
        "summary": "Fetch Virtual Account",
        "description": "The following endpoint retrieves the details of all Virtual Accounts created",
        "operationId": "fetch-virtual-account",
        "parameters": [
          {
            "name": "from",
            "in": "query",
            "description": "Timestamp (in Unix format) from when the virtual accounts should be fetched",
            "schema": {
              "type": "string",
              "default": "2024-09-01"
            }
          },
          {
            "name": "to",
            "in": "query",
            "description": "Timestamp (in Unix format) up till when virtual accounts are to be fetched",
            "schema": {
              "type": "string",
              "default": "2024-09-09"
            }
          },
          {
            "name": "skip",
            "in": "query",
            "description": "The number of virtual accounts to be skipped. The default value is 0. This can be used for pagination, in combination with count",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "The number of virtual accounts to be skipped. The default value is 0. This can be used for pagination, in combination with count",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
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
                    "value": "{\n    \"data\": {\n        \"virtual_accounts\": [\n            {\n                \"id\": \"va_sample_QOIFczRMfG3448\",\n                \"bank_code\": \"PERMATA\",\n                \"account_number\": \"88565004123456\",\n                \"name\": \"Ardi Hanan Durian\",\n                \"is_closed\": true,\n                \"amount\": 12333,\n                \"currency\": \"IDR\",\n                \"customer_id\": \"cus_CtZ8r2GOvq7341\",\n                \"is_sandbox\": true,\n                \"created_at\": \"2022-06-28T10:55:24.578679Z\",\n                \"expiry_at\": \"2022-07-08T05:25:24.580583Z\",\n                \"metadata\": {},\n                \"is_disabled\": false,\n                \"is_paid\": false,\n                \"is_reusable\": true,\n                \"min_amount\": null,\n                \"max_amount\": null,\n                \"va_ref_id\": \"1234\",\n                \"auto_disable_after_payment\": true\n            },\n            {\n                \"id\": \"va_sample_pWM5k3BUI63935\",\n                \"bank_code\": \"PERMATA\",\n                \"account_number\": \"8856500453252122\",\n                \"name\": \"Ardi Hanan Durian\",\n                \"is_closed\": true,\n                \"amount\": 12333,\n                \"currency\": \"IDR\",\n                \"customer_id\": \"cus_CtZ8r2GOvq7341\",\n                \"is_sandbox\": true,\n                \"created_at\": \"2022-06-28T10:38:54.350418Z\",\n                \"expiry_at\": \"2022-07-08T05:08:54.353053Z\",\n                \"metadata\": {},\n                \"is_disabled\": false,\n                \"is_paid\": false,\n                \"is_reusable\": true,\n                \"min_amount\": null,\n                \"max_amount\": null,\n                \"va_ref_id\": \"1234\",\n                \"auto_disable_after_payment\": true\n            }\n        ],\n        \"total\": 10\n    }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "virtual_accounts": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "example": "va_sample_QOIFczRMfG3448"
                              },
                              "bank_code": {
                                "type": "string",
                                "example": "PERMATA"
                              },
                              "account_number": {
                                "type": "string",
                                "example": "88565004123456"
                              },
                              "name": {
                                "type": "string",
                                "example": "Ardi Hanan Durian"
                              },
                              "is_closed": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "amount": {
                                "type": "integer",
                                "example": 12333,
                                "default": 0
                              },
                              "currency": {
                                "type": "string",
                                "example": "IDR"
                              },
                              "customer_id": {
                                "type": "string",
                                "example": "cus_CtZ8r2GOvq7341"
                              },
                              "is_sandbox": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "created_at": {
                                "type": "string",
                                "example": "2022-06-28T10:55:24.578679Z"
                              },
                              "expiry_at": {
                                "type": "string",
                                "example": "2022-07-08T05:25:24.580583Z"
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
                              "min_amount": {},
                              "max_amount": {},
                              "va_ref_id": {
                                "type": "string",
                                "example": "1234"
                              },
                              "auto_disable_after_payment": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              }
                            }
                          }
                        },
                        "total": {
                          "type": "integer",
                          "example": 10,
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
                    "value": "{\n    \"error\": \"invalid skip and limit parameter\"\n}"
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
                    "value": "{\n    \"error\": \"failed to connect to database\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\",\n    \"request_id\": \"dp_d3HX9S5W0r4989\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "failed to connect to database"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INTERNAL_ERROR"
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