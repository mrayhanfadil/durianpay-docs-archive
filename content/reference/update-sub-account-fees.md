---
updatedAt: 2025-06-17T23:25:57.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Update Sub-Account Fees

This following endpoint allows master accounts to manage fees for subaccounts

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
    "/merchants/subaccount/fee": {
      "post": {
        "summary": "Update Sub-Account Fees",
        "description": "This following endpoint allows master accounts to manage fees for subaccounts",
        "operationId": "update-sub-account-fees",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "id",
                  "disbursement_fees"
                ],
                "properties": {
                  "id": {
                    "type": "string",
                    "description": "Unique identifier of the subaccount, which can be taken from the response of Register subaccount API or Fetch Subaccount API",
                    "default": "mer_x6EzWyIeVX3831"
                  },
                  "payment_fees": {
                    "type": "array",
                    "description": "Details on which payment method will be assigned with the fee, including the fee configuration. Either fixed_fee or percentage_fee is mandatory; you must provide one of them, but providing both is not required, If both fee presents, The fee is calculated by accumulating percentage fee (applied to the total amount before the fee) to the fixed fee.",
                    "items": {
                      "properties": {
                        "payment_method_id": {
                          "type": "string",
                          "description": "Payment method which will be updated with the new fee. Possible values: BCA, BNI For the complete list of the supported payment methods and its payment_method_id (code) please refer here: Supported Payment Method",
                          "default": "BCA"
                        },
                        "fixed_fee": {
                          "type": "string",
                          "description": "Amount of the fixed fee. Example: \"1000\"",
                          "default": "1000"
                        },
                        "percentage_fee": {
                          "type": "string",
                          "description": "Amount of the percentage fee. Example: \"10\"",
                          "default": "10"
                        }
                      },
                      "required": [
                        "payment_method_id"
                      ],
                      "type": "object"
                    }
                  },
                  "disbursement_fees": {
                    "type": "object",
                    "description": "Details on the configuration of disbursement fees.",
                    "required": [
                      "type",
                      "fee"
                    ],
                    "properties": {
                      "type": {
                        "type": "string",
                        "description": "Fee type, possible values: flat, percentage",
                        "default": "flat"
                      },
                      "fee": {
                        "type": "string",
                        "description": "Amount of respective fee type",
                        "default": "25"
                      }
                    }
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
                    "value": {
                      "message": "Merchant Fee has been updated successfully",
                      "data": {
                        "id": "mer_x6EzWyIeVX3831",
                        "payment_fees": [
                          {
                            "payment_method_id": "GOPAY",
                            "fixed_fee": "500",
                            "percentage_fee": "3"
                          },
                          {
                            "payment_method_id": "DANA",
                            "fixed_fee": "1000",
                            "percentage_fee": "3"
                          }
                        ],
                        "disbursement_fees": {
                          "type": "flat",
                          "fee": "25"
                        }
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Merchant Fee has been updated successfully"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "mer_x6EzWyIeVX3831"
                        },
                        "payment_fees": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "payment_method_id": {
                                "type": "string",
                                "example": "GOPAY"
                              },
                              "fixed_fee": {
                                "type": "string",
                                "example": "500"
                              },
                              "percentage_fee": {
                                "type": "string",
                                "example": "3"
                              }
                            }
                          }
                        },
                        "disbursement_fees": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "example": "percentage"
                            },
                            "fee": {
                              "type": "string",
                              "example": "30"
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
                  "Invalid payment method ID": {
                    "value": "{\n    \"data\": {\n    \"error\": \"error found in row 0, cannot setup payment method GRPAY\",\n    \"error_code\": \"DPAY_MERCHANT_SETTINGS_ERROR\"\n}\n"
                  }
                }
              },
              "text/plain": {
                "examples": {
                  "Invalid Disbursement Fee Type": {
                    "value": "{\n    \"error\": \"invalid disbursement fee type\",\n    \"error_code\": \"DPAY_MERCHANT_SETTINGS_ERROR\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "invalid disbursement fee type"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_MERCHANT_SETTINGS_ERROR"
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
                    "value": "{\n    \"error\": \"internal server error\"\n}\n"
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