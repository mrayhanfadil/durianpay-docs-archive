---
updatedAt: 2025-06-17T23:25:37.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Patch Virtual Accounts By ID

The following endpoint is used to override Expiry Time of a single Virtual Account.

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
      "patch": {
        "summary": "Patch Virtual Accounts By ID",
        "description": "The following endpoint is used to override Expiry Time of a single Virtual Account.",
        "operationId": "virtual-accounts-patch-by-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Unique identifier of the Virtual Account to be retrieved",
            "schema": {
              "type": "string",
              "default": "va_1234"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "expiry_minutes": {
                    "type": "integer",
                    "description": "Number of minutes left till expiry from now. Set to 0 to expire VA Example: 10000",
                    "default": 0,
                    "format": "int32"
                  },
                  "min_amount": {
                    "type": "integer",
                    "description": "Modify minimum amount which can be paid to an open VA. Example: 10000",
                    "default": 10000,
                    "format": "int32"
                  },
                  "max_amount": {
                    "type": "integer",
                    "description": "Modify maximum amount which can be paid to an open VA. Example: 10000",
                    "default": 100000,
                    "format": "int32"
                  },
                  "amount": {
                    "type": "integer",
                    "description": "Modify maximum amount which can be paid to a closed VA. Example: 10000",
                    "default": 10000,
                    "format": "int32"
                  },
                  "is_disabled": {
                    "type": "boolean",
                    "description": "Modify enabling/disabling payments to a VA while still reserving it. Example: true",
                    "default": false
                  },
                  "va_ref_id": {
                    "type": "string",
                    "description": "Modify a reference ID which the merchant wants to use for a specific VA. Example: \"VA_XYZ_1234\"",
                    "default": "va_123"
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
                  "Result": {
                    "value": "{\n    \"data\": {\n        \"virtual_account\": {\n            \"id\": \"va_sample_EwCm3LrPqE5184\",\n            \"bank_code\": \"PERMATA\",\n            \"account_number\": \"88565004532522\",\n            \"name\": \"Ardi Hanan Durian\",\n            \"is_closed\": true,\n            \"amount\": 123456,\n            \"currency\": \"IDR\",\n            \"customer_id\": \"cus_akA2FwrR5B2217\",\n            \"is_sandbox\": true,\n            \"created_at\": \"2022-06-27T02:52:30.236901Z\",\n            \"expiry_at\": \"2022-06-29T05:40:59.795448Z\",\n            \"metadata\": {},\n            \"is_disabled\": true,\n            \"is_paid\": false,\n            \"is_reusable\": true,\n            \"min_amount\": 50000,\n            \"max_amount\": null,\n            \"va_ref_id\": \"1234412\",\n            \"auto_disable_after_payment\": false\n        },\n        \"virtual_account_status\": \"VirtualAccountSuccess\",\n        \"customer\": {\n            \"id\": \"cus_akA2FwrR5B2217\",\n            \"customer_ref_id\": \"\",\n            \"given_name\": \"\",\n            \"middle_name\": \"\",\n            \"sur_name\": \"\",\n            \"email\": \"p.ardi.h@gmail.com\",\n            \"mobile\": \"+628978678578\"\n        }\n    }\n}\n"
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
                              "example": "va_sample_EwCm3LrPqE5184"
                            },
                            "bank_code": {
                              "type": "string",
                              "example": "PERMATA"
                            },
                            "account_number": {
                              "type": "string",
                              "example": "88565004532522"
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
                              "example": 123456,
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
                              "example": "2022-06-27T02:52:30.236901Z"
                            },
                            "expiry_at": {
                              "type": "string",
                              "example": "2022-06-29T05:40:59.795448Z"
                            },
                            "metadata": {
                              "type": "object",
                              "properties": {}
                            },
                            "is_disabled": {
                              "type": "boolean",
                              "example": true,
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
                              "example": "1234412"
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
                          "example": "VirtualAccountSuccess"
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
                    "value": "{\n    \"error_code\": \"DPAY_INVALID_REQUEST\",\n    \"request_id\": \"dp_Dzc8hMzkQU4826\",\n    \"errors\": [\n        {\n            \"field\": \"expiry_minutes\",\n            \"message\": \"can't be less than 0\"\n        }\n    ]\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INVALID_REQUEST"
                    },
                    "request_id": {
                      "type": "string",
                      "example": "dp_Dzc8hMzkQU4826"
                    },
                    "errors": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "field": {
                            "type": "string",
                            "example": "expiry_minutes"
                          },
                          "message": {
                            "type": "string",
                            "example": "can't be less than 0"
                          }
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