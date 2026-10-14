---
updatedAt: 2025-06-17T23:25:23.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Create Order API

The following endpoint creates an Order

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
      "post": {
        "summary": "Create Order API",
        "description": "The following endpoint creates an Order",
        "operationId": "create-order",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "amount",
                  "currency",
                  "customer"
                ],
                "properties": {
                  "amount": {
                    "type": "string",
                    "description": "The amount for which the Order was created. Example: \"10000\" or \"10000.23\" for amount with decimal value",
                    "default": "1000"
                  },
                  "currency": {
                    "type": "string",
                    "description": "The currency associated with the Order's amount. Example: \"IDR\"",
                    "default": "IDR"
                  },
                  "customer": {
                    "type": "object",
                    "description": "The customer fields including id, email, mobile, first_name, given_name, address json object, customer_ref_id. One of id, mobile, email is mandatory field whereas others are optional.  address is mandatory to use BNPL payment method.",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "The customer ID from Durianpay"
                      },
                      "email": {
                        "type": "string",
                        "description": "The customer's email address. Should of the format jane.doe@gmail.com and should not contain any invalid special characters (¢,£,§,©,etc)",
                        "default": "testing@testing.com"
                      },
                      "mobile": {
                        "type": "string",
                        "description": "The customer's mobile number. Please ensure that the number follows Indonesia's phone number format : +62xxxxxxxxxx or 08xxxxxxxxxx."
                      },
                      "customer_ref_id": {
                        "type": "string",
                        "description": "A unique reference ID from the merchant to identify the customer",
                        "default": "test_123"
                      },
                      "given_name": {
                        "type": "string",
                        "description": "The customer's given name"
                      },
                      "middle_name": {
                        "type": "string",
                        "description": "The customer's middle name"
                      },
                      "sur_name": {
                        "type": "string",
                        "description": "The customer's surname"
                      },
                      "address": {
                        "type": "object",
                        "description": "The address fields includes receiver_name, receiver_phone, label, address_line, city, region, postal_code, landmark",
                        "properties": {
                          "receiver_name": {
                            "type": "string"
                          },
                          "label": {
                            "type": "string"
                          },
                          "address_line": {
                            "type": "string"
                          },
                          "city": {
                            "type": "string"
                          },
                          "region": {
                            "type": "string"
                          },
                          "postal_code": {
                            "type": "string"
                          },
                          "landmark": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  },
                  "payment_option": {
                    "type": "string",
                    "description": "The type of payment option with which order was created. Possible values: \"full_payment\" or \"installment\"",
                    "default": "full_payment"
                  },
                  "order_ref_id": {
                    "type": "string",
                    "description": "The unique identifier of Order from the merchant. Example: \"INV/1/2021\"",
                    "default": "INV/1/2021"
                  },
                  "items": {
                    "type": "array",
                    "description": "Array of objects with each object including name, brand, category, sku, price, qty, total_price. mandatory to use BNPL and LINKAJA payment method",
                    "items": {
                      "properties": {
                        "name": {
                          "type": "string",
                          "description": "The item's name"
                        },
                        "qty": {
                          "type": "integer",
                          "description": "The quantity of the item"
                        },
                        "price": {
                          "type": "string",
                          "description": "The price for a single item"
                        },
                        "logo": {
                          "type": "string",
                          "description": "The URL for the logo of the item"
                        },
                        "brand": {
                          "type": "string",
                          "description": "The brand of the item"
                        },
                        "category": {
                          "type": "string",
                          "description": "The category of the item"
                        },
                        "sku": {
                          "type": "string",
                          "description": "The SKU (Stock Keeping Unit) of the item"
                        },
                        "total_price": {
                          "type": "string",
                          "description": "The total price of the item"
                        },
                        "metadata": {
                          "type": "string",
                          "description": "The metadata of the item"
                        }
                      },
                      "required": [
                        "name",
                        "qty",
                        "price"
                      ],
                      "type": "object"
                    }
                  },
                  "description": {
                    "type": "string",
                    "description": "String to store description of the order. Example: \"This order is delicate. Handle with Care!\"",
                    "default": "This order is delicate handle with care"
                  },
                  "admin_fee_method": {
                    "type": "string",
                    "description": "Used to specify if the transactional charges are to be included and paid by the merchant or customer. Possible Values:  \"included\" - Transaction Fee is paid by merchant \"excluded\" - Transaction Fee is paid by customer",
                    "default": "excluded"
                  },
                  "metadata": {
                    "type": "string",
                    "description": "Key-Value pair that can be used to store additional information about the entity."
                  },
                  "expiry_date": {
                    "type": "string",
                    "description": "The time stamp at which the order will expire. Please ensure that the value is in RFC3339 format and the timezone is in GMT+7. Example: \"2022-03-29T10:00:00.000Z\"",
                    "default": "2026-09-29T10:00:00.000Z"
                  },
                  "is_payment_link": {
                    "type": "boolean",
                    "description": "Whether Payment Link is to be generated. Example: true or false",
                    "default": ""
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
                    "value": "{\n    \"data\": {\n        \"id\": \"ord_0dIWbuDJQ84078\",\n        \"customer_id\": \"cus_ViPeX4iBYp2233\",\n        \"order_ref_id\": \"order_ref_001\",\n        \"order_ds_ref_id\": \"\",\n        \"amount\": \"10001.00\",\n        \"payment_option\": \"full_payment\",\n        \"currency\": \"IDR\",\n        \"status\": \"started\",\n        \"created_at\": \"2021-04-01T14:39:37.860426Z\",\n        \"updated_at\": \"2021-04-01T14:39:37.860426Z\",\n        \"expiry_date\": \"2022-03-29T10:00:00Z\",\n        \"metadata\": {\n            \"my-meta-key\": \"my-meta-value\",\n            \"SettlementGroup\": \"BranchName\"\n        },\n        \"items\": [\n            {\n                \"name\": \"LED Television\",\n                \"qty\": 1,\n                \"price\": \"10001.00\",\n                \"logo\": \"https://merchant.com/tv_image.jpg\"\n            }\n        ],\n        \"access_token\": \"adsyoi12sdASd123ASX@qqsda231\",\n        \"expire_time\": \"2022-09-15T13:40:17.064478772Z\",\n        \"is_live\": true,\n        \"fees\": null,\n        \"shipping_fee\": \"\",\n        \"admin_fee_method\": \"included\"\n    }\n}"
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
                          "example": "ord_0dIWbuDJQ84078"
                        },
                        "customer_id": {
                          "type": "string",
                          "example": "cus_ViPeX4iBYp2233"
                        },
                        "order_ref_id": {
                          "type": "string",
                          "example": "order_ref_001"
                        },
                        "order_ds_ref_id": {
                          "type": "string",
                          "example": ""
                        },
                        "amount": {
                          "type": "string",
                          "example": "10001.00"
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
                        "created_at": {
                          "type": "string",
                          "example": "2021-04-01T14:39:37.860426Z"
                        },
                        "updated_at": {
                          "type": "string",
                          "example": "2021-04-01T14:39:37.860426Z"
                        },
                        "expiry_date": {
                          "type": "string",
                          "example": "2022-03-29T10:00:00Z"
                        },
                        "metadata": {
                          "type": "object",
                          "properties": {
                            "my-meta-key": {
                              "type": "string",
                              "example": "my-meta-value"
                            },
                            "SettlementGroup": {
                              "type": "string",
                              "example": "BranchName"
                            }
                          }
                        },
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": "string",
                                "example": "LED Television"
                              },
                              "qty": {
                                "type": "integer",
                                "example": 1,
                                "default": 0
                              },
                              "price": {
                                "type": "string",
                                "example": "10001.00"
                              },
                              "logo": {
                                "type": "string",
                                "example": "https://merchant.com/tv_image.jpg"
                              }
                            }
                          }
                        },
                        "access_token": {
                          "type": "string",
                          "example": "adsyoi12sdASd123ASX@qqsda231"
                        },
                        "expire_time": {
                          "type": "string",
                          "example": "2022-09-15T13:40:17.064478772Z"
                        },
                        "is_live": {
                          "type": "boolean",
                          "example": true,
                          "default": true
                        },
                        "fees": {},
                        "shipping_fee": {
                          "type": "string",
                          "example": ""
                        },
                        "admin_fee_method": {
                          "type": "string",
                          "example": "included"
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
                    "value": "{\n    \"data\": {\n    \"error\": \"required fields missing\",\n    \"error_code\": \"DPAY_INVALID_REQUEST\",\n    \"request_id\": \"not-set\",\n    \"errors\": [\n        {\n            \"field\": \"amount=\"amount invalid\"\n\",\n            \"message\": \"Please provide valid order data\"\n        }\n    ]\n}\n"
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
                    "value": "{\n    \"error\": \"invalid Authorization header in request\",\n    \"error_code\": \"DPAY_UNAUTHORIZED_ACCESS\",\n    \"request_id\": \"not-set\"\n}\n"
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
                    },
                    "request_id": {
                      "type": "string",
                      "example": "not-set"
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