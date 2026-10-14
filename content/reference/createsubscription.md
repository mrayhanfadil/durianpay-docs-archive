---
updatedAt: 2026-07-08T11:24:52.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Create Subscription

The following endpoint registers a recurring billing agreement for a customer and returns the subscription in `pending` status. No payment method is collected at this step. The subscription is activated separately by its first payment (hosted checkout, or the Charge Subscription endpoint).

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Subscriptions",
    "version": "1.0.0",
    "description": "Recurring-payment (Subscription) endpoints for Durianpay merchants."
  },
  "servers": [
    {
      "url": "https://api.durianpay.id"
    }
  ],
  "components": {
    "securitySchemes": {
      "serverKey": {
        "type": "http",
        "scheme": "basic",
        "description": "HTTP Basic auth. Use your Durianpay server key as the username with an empty password."
      }
    }
  },
  "security": [
    {
      "serverKey": []
    }
  ],
  "tags": [
    {
      "name": "Subscriptions",
      "description": "Create and manage recurring-payment subscriptions."
    }
  ],
  "paths": {
    "/v1/subscriptions": {
      "post": {
        "operationId": "createSubscription",
        "summary": "Create Subscription",
        "tags": [
          "Subscriptions"
        ],
        "description": "The following endpoint registers a recurring billing agreement for a customer and returns the subscription in `pending` status. No payment method is collected at this step. The subscription is activated separately by its first payment (hosted checkout, or the Charge Subscription endpoint).",
        "parameters": [
          {
            "in": "header",
            "name": "Content-Type",
            "required": true,
            "schema": {
              "type": "string",
              "default": "application/json"
            },
            "description": "Indicates the media type of the resource. value: application/json"
          },
          {
            "in": "header",
            "name": "X-Request-ID",
            "required": false,
            "schema": {
              "type": "string"
            },
            "description": "Optional client-supplied idempotency and tracing ID, echoed back in the response."
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "customer",
                  "amount",
                  "interval",
                  "return_url"
                ],
                "properties": {
                  "customer": {
                    "type": "object",
                    "example": "cus_456",
                    "description": "Object containing fields (id, email, mobile, given_name, customer_ref_id). The customer object must contain at least one of the following fields: id, email, mobile, given_name, or customer_ref_id. Multiple fields may be provided.",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "The customer ID from Durianpay"
                      },
                      "email": {
                        "type": "string",
                        "description": "The customer's email address. Should of the format jane.doe@gmail.com and should not contain any invalid special characters (¢,£,§,©,etc)"
                      },
                      "mobile": {
                        "type": "string",
                        "description": "The customer's mobile number. Please ensure that the number follows Indonesia's phone number format : +62xxxxxxxxxx or 08xxxxxxxxxx."
                      },
                      "given_name": {
                        "type": "string",
                        "description": "The customer's given name"
                      },
                      "customer_ref_id": {
                        "type": "string",
                        "description": "A unique reference ID from the merchant to identify the customer"
                      }
                    }
                  },
                  "amount": {
                    "type": "object",
                    "required": [
                      "currency",
                      "value"
                    ],
                    "description": "",
                    "properties": {
                      "currency": {
                        "type": "string",
                        "example": "IDR",
                        "description": "Currency code. Only supports \"IDR\""
                      },
                      "value": {
                        "type": "string",
                        "example": "10000.00",
                        "description": "Recurring charge amount "
                      }
                    }
                  },
                  "interval": {
                    "type": "string",
                    "enum": [
                      "daily",
                      "weekly",
                      "monthly",
                      "annually"
                    ],
                    "description": "Billing frequency unit."
                  },
                  "interval_count": {
                    "type": "integer",
                    "minimum": 1,
                    "default": 1,
                    "example": 1,
                    "description": "Multiplier for interval (3 + monthly = every 3 months). Defaults to 1."
                  },
                  "return_url": {
                    "type": "string",
                    "format": "uri",
                    "example": "https://merchant.com/subscription/success",
                    "description": "URL the customer is redirected to after hosted checkout."
                  },
                  "subscription_ref_id": {
                    "type": "string",
                    "example": "sub-ref-0001",
                    "description": "Optional. Your own reference for this subscription, returned unchanged for reconciliation."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Subscription created in pending status.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "example": "success"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "sub_xyz123"
                        },
                        "merchant_id": {
                          "type": "string",
                          "example": "mer_123"
                        },
                        "customer_id": {
                          "type": "string",
                          "example": "cus_456"
                        },
                        "amount": {
                          "type": "object",
                          "required": [
                            "currency",
                            "value"
                          ],
                          "description": "Recurring charge amount as a currency and decimal-string value, e.g. {\"currency\":\"IDR\",\"value\":\"10000.00\"}.",
                          "properties": {
                            "currency": {
                              "type": "string",
                              "example": "IDR",
                              "description": "Currency code. IDR only in V1."
                            },
                            "value": {
                              "type": "string",
                              "example": "10000.00",
                              "description": "Decimal string amount."
                            }
                          }
                        },
                        "interval": {
                          "type": "string",
                          "enum": [
                            "daily",
                            "weekly",
                            "monthly",
                            "annually"
                          ],
                          "description": "Billing frequency unit."
                        },
                        "interval_count": {
                          "type": "integer",
                          "example": 1
                        },
                        "status": {
                          "type": "string",
                          "enum": [
                            "pending",
                            "active",
                            "past_due",
                            "paused",
                            "cancelled"
                          ]
                        },
                        "checkout_url": {
                          "type": "string",
                          "example": "https://checkout.durianpay.id/s/sub_xyz123",
                          "description": "Durianpay-hosted activation page for the first payment."
                        },
                        "return_url": {
                          "type": "string",
                          "example": "https://merchant.com/subscription/success"
                        },
                        "subscription_ref_id": {
                          "type": "string",
                          "nullable": true,
                          "example": "sub-ref-0001",
                          "description": "Your own reference, echoed back. Null if not supplied."
                        },
                        "next_billing_date": {
                          "type": "string",
                          "format": "date-time",
                          "nullable": true,
                          "description": "Null until the subscription becomes active."
                        },
                        "payment_method_type": {
                          "type": "string",
                          "nullable": true,
                          "description": "Null until the first payment succeeds."
                        },
                        "cancellation_reason": {
                          "type": "string",
                          "nullable": true,
                          "enum": [
                            "merchant_cancelled",
                            "payment_failed",
                            "expired",
                            "completed"
                          ]
                        },
                        "metadata": {
                          "type": "object",
                          "nullable": true
                        },
                        "created_at": {
                          "type": "string",
                          "format": "date-time",
                          "example": "2026-03-01T10:00:00Z"
                        },
                        "updated_at": {
                          "type": "string",
                          "format": "date-time",
                          "example": "2026-03-01T10:00:00Z"
                        }
                      }
                    }
                  }
                },
                "examples": {
                  "Created": {
                    "summary": "Created",
                    "value": {
                      "status": "success",
                      "data": {
                        "id": "sub_xyz123",
                        "merchant_id": "mer_123",
                        "customer_id": "cus_456",
                        "amount": {
                          "currency": "IDR",
                          "value": "10000.00"
                        },
                        "interval": "monthly",
                        "interval_count": 1,
                        "status": "pending",
                        "checkout_url": "https://checkout.durianpay.id/s/sub_xyz123",
                        "return_url": "https://merchant.com/subscription/success",
                        "subscription_ref_id": "sub-ref-0001",
                        "next_billing_date": null,
                        "payment_method_type": null,
                        "cancellation_reason": null,
                        "metadata": {
                          "internal_plan": "premium"
                        },
                        "created_at": "2026-03-01T10:00:00Z",
                        "updated_at": "2026-03-01T10:00:00Z"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid or missing request fields.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "example": "error"
                    },
                    "code": {
                      "type": "string",
                      "description": "Machine-readable error code."
                    },
                    "message": {
                      "type": "string",
                      "description": "Human-readable explanation."
                    }
                  }
                },
                "examples": {
                  "INVALID_REQUEST": {
                    "summary": "INVALID_REQUEST",
                    "value": {
                      "status": "error",
                      "code": "INVALID_REQUEST",
                      "message": "'quarterly' is not a valid value for 'interval'. Accepted values are: daily, weekly, monthly, annually."
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Subscription feature is not enabled for this merchant.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "example": "error"
                    },
                    "code": {
                      "type": "string",
                      "description": "Machine-readable error code."
                    },
                    "message": {
                      "type": "string",
                      "description": "Human-readable explanation."
                    }
                  }
                },
                "examples": {
                  "FEATURE_NOT_ENABLED": {
                    "summary": "FEATURE_NOT_ENABLED",
                    "value": {
                      "status": "error",
                      "code": "FEATURE_NOT_ENABLED",
                      "message": "Subscription billing is not enabled for your account. Contact your Durianpay account manager to request access."
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "The referenced customer does not exist for this merchant.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "example": "error"
                    },
                    "code": {
                      "type": "string",
                      "description": "Machine-readable error code."
                    },
                    "message": {
                      "type": "string",
                      "description": "Human-readable explanation."
                    }
                  }
                },
                "examples": {
                  "CUSTOMER_NOT_FOUND": {
                    "summary": "CUSTOMER_NOT_FOUND",
                    "value": {
                      "status": "error",
                      "code": "CUSTOMER_NOT_FOUND",
                      "message": "Customer 'cus_456' was not found."
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```