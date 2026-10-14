---
updatedAt: 2025-06-17T23:25:35.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Create Virtual Account

The following endpoint creates a new virtual account

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
      "post": {
        "summary": "Create Virtual Account",
        "description": "The following endpoint creates a new virtual account",
        "operationId": "create-virtual-account",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "bank_code",
                  "name",
                  "customer"
                ],
                "properties": {
                  "bank_code": {
                    "type": "string",
                    "description": "The bank code for the Virtual Account. Supported Bank Codes: \"BRI\", \"BCA\", \"MANDIRI\", \"PERMATA\", \"CIMB\", \"BNI\", \"NOBU\"",
                    "default": "PERMATA"
                  },
                  "name": {
                    "type": "string",
                    "description": "The name of the virtual account which will appear in ATM/Banking app. Example: \"John's Virtual Account\"",
                    "default": "Dpay Jane Doe"
                  },
                  "is_closed": {
                    "type": "boolean",
                    "description": "Whether account can accept open(any amount) or closed(specific amount). Example: true or false",
                    "default": true
                  },
                  "amount": {
                    "type": "string",
                    "description": "Specify amount to be paid to va when is_closed=true. Example: \"12000.12\"",
                    "default": "20000"
                  },
                  "customer": {
                    "type": "object",
                    "description": "Object containing fields (id, email, mobile, given_name). One of (id, mobile, email) is mandatory field and given_name is mandatory.",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "Durianpay's customer ID"
                      },
                      "given_name": {
                        "type": "string",
                        "description": "Customer's name",
                        "default": "Jane Doe"
                      },
                      "mobile": {
                        "type": "string",
                        "description": "Customer's mobile number in Indonesia's phone number format (+62xxxxxxxxxx or 08xxxxxxxxxx), with a length of 8 to 14 digits.",
                        "default": "+628121343222"
                      },
                      "email": {
                        "type": "string",
                        "description": "Customer's email address in a valid email format (e.g., jane.doe@gmail.com) without invalid special characters (¢, £, §, ©, etc.)",
                        "default": "product@durianpay.id"
                      },
                      "customer_ref_id": {
                        "type": "string",
                        "description": "A unique reference ID from the merchant to identify the customer",
                        "default": "test_123"
                      }
                    }
                  },
                  "expiry_minutes": {
                    "type": "integer",
                    "description": "Number of minutes left till expiry from now. maximum: 15768000 minutes",
                    "default": 100,
                    "format": "int32"
                  },
                  "account_suffix": {
                    "type": "string",
                    "description": "Account suffix for the Virtual Account. If not provided, a random suffix will be automatically generated for the virtual account number.",
                    "default": "123456"
                  },
                  "is_reusable": {
                    "type": "boolean",
                    "description": "Whether multiple payments can be used for a particular VA. Example: true or false",
                    "default": false
                  },
                  "va_ref_id": {
                    "type": "string",
                    "description": "A reference ID which the merchant wants to use for a specific VA. Example: \"VA_XYZ_1234\"",
                    "default": "VA_123"
                  },
                  "auto_disable_after_payment": {
                    "type": "boolean",
                    "description": "Disable a reusable VA temporarily after a payment. Patch API can be used to enable it again after changing some parameters. Example: true or false",
                    "default": false
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
                    "value": "{\n  \"data\": {\n    \"customer_id\": \"cus_abcdefghijklm\",\n    \"virtual_account\": {\n      \"id\": \"va_abcdefghjklmn\",\n      \"bank_code\": \"PERMATA\",\n      \"account_number\": \"1234006781234569\",\n      \"name\": \"Dpay Jane Doe\",\n      \"is_closed\": true,\n      \"amount\": 20000,\n      \"currency\": \"IDR\",\n      \"customer_id\": \"cus_abcdefghijklm\",\n      \"is_sandbox\": false,\n      \"created_at\": \"2025-03-05T02:39:09.738801Z\",\n      \"expiry_at\": \"2025-03-05T12:39:09.744Z\",\n      \"metadata\": {},\n      \"is_disabled\": false,\n      \"is_paid\": false,\n      \"is_reusable\": false,\n      \"min_amount\": null,\n      \"max_amount\": null,\n      \"va_ref_id\": \"VA_123\",\n      \"auto_disable_after_payment\": false\n    }\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "customer_id": {
                          "type": "string",
                          "example": "cus_abcdefghijklm"
                        },
                        "virtual_account": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "example": "va_abcdefghjklmn"
                            },
                            "bank_code": {
                              "type": "string",
                              "example": "PERMATA"
                            },
                            "account_number": {
                              "type": "string",
                              "example": "1234006781234569"
                            },
                            "name": {
                              "type": "string",
                              "example": "Dpay Jane Doe"
                            },
                            "is_closed": {
                              "type": "boolean",
                              "example": true,
                              "default": true
                            },
                            "amount": {
                              "type": "integer",
                              "example": 20000,
                              "default": 0
                            },
                            "currency": {
                              "type": "string",
                              "example": "IDR"
                            },
                            "customer_id": {
                              "type": "string",
                              "example": "cus_abcdefghijklm"
                            },
                            "is_sandbox": {
                              "type": "boolean",
                              "example": false,
                              "default": true
                            },
                            "created_at": {
                              "type": "string",
                              "example": "2025-03-05T02:39:09.738801Z"
                            },
                            "expiry_at": {
                              "type": "string",
                              "example": "2025-03-05T12:39:09.744Z"
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
                              "example": false,
                              "default": true
                            },
                            "min_amount": {},
                            "max_amount": {},
                            "va_ref_id": {
                              "type": "string",
                              "example": "VA_123"
                            },
                            "auto_disable_after_payment": {
                              "type": "boolean",
                              "example": false,
                              "default": true
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
                    "value": "{\n    \"error\": \"pq: VA Already Created\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\",\n    \"request_id\": \"dp_QMPB7IO53p6517\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "pq: VA Already Created"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INTERNAL_ERROR"
                    },
                    "request_id": {
                      "type": "string",
                      "example": "dp_QMPB7IO53p6517"
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