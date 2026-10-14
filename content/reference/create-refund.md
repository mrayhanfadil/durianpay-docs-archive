---
updatedAt: 2025-06-17T23:26:01.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Create Refund

The following endpoint creates an Refund.

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
      "post": {
        "summary": "Create Refund",
        "description": "The following endpoint creates an Refund.",
        "operationId": "create-refund",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "ref_id",
                  "payment_id",
                  "amount"
                ],
                "properties": {
                  "ref_id": {
                    "type": "string",
                    "description": "Merchant refund reference id. Example: \"ref_reference_123\"",
                    "default": "abc"
                  },
                  "payment_id": {
                    "type": "string",
                    "description": "Durianpay payment id used to create refund. Example: \"pay_ttqs62k99s\"",
                    "default": "pay_IsL5nOCW4M2790"
                  },
                  "amount": {
                    "type": "string",
                    "description": "The refund amount requested. Example: \"10000\" or \"10000.23\" for amount with decimal value",
                    "default": "10000"
                  },
                  "notes": {
                    "type": "string",
                    "description": "The refund note. Example: \"rejected product\"",
                    "default": "rejected product"
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
                    "value": "{\n  \"data\": {\n    \"id\": \"rfn_qfrsL0tlnT0308\",\n    \"ref_id\": \"reference_1\",\n    \"amount\": \"20000.00\",\n    \"refund_type\": \"partial\",\n    \"status\": \"approved\",\n    \"created_at\": \"2021-07-20T10:43:42.201587Z\",\n    \"updated_at\": \"2021-07-20T10:43:42.401256Z\",\n    \"approved_at\": \"2021-07-20T10:43:42.401256Z\",\n    \"source\": \"api\",\n    \"customer_name\": \"joe\",\n    \"customer_email\": \"jade@sfs.com\",\n    \"customer_phone\": \"\"\n  }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "rfn_qfrsL0tlnT0308"
                        },
                        "ref_id": {
                          "type": "string",
                          "example": "reference_1"
                        },
                        "amount": {
                          "type": "string",
                          "example": "20000.00"
                        },
                        "refund_type": {
                          "type": "string",
                          "example": "partial"
                        },
                        "status": {
                          "type": "string",
                          "example": "approved"
                        },
                        "created_at": {
                          "type": "string",
                          "example": "2021-07-20T10:43:42.201587Z"
                        },
                        "updated_at": {
                          "type": "string",
                          "example": "2021-07-20T10:43:42.401256Z"
                        },
                        "approved_at": {
                          "type": "string",
                          "example": "2021-07-20T10:43:42.401256Z"
                        },
                        "source": {
                          "type": "string",
                          "example": "api"
                        },
                        "customer_name": {
                          "type": "string",
                          "example": "joe"
                        },
                        "customer_email": {
                          "type": "string",
                          "example": "jade@sfs.com"
                        },
                        "customer_phone": {
                          "type": "string",
                          "example": ""
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
                    "value": "{\n    \"error\": \"error reading request body\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\",\n}\n"
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
          "403": {
            "description": "403",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": \"refund amount exceed\",\n    \"error_code\": \"DPAY_REFUND_AMOUNT_EXCEEDED\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "refund amount exceed"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_REFUND_AMOUNT_EXCEEDED"
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
                    "value": "{\n    \"error\": \"error creating refund\",\n    \"error_code\": \"DPAY_INTERNAL_ERROR\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "error creating refund"
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