---
updatedAt: 2026-07-08T11:24:52.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Charge Subscription

The following endpoint activates a subscription with its first charge, or retry a payment for past due subscription.

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
    "/v1/subscriptions/{id}/charge": {
      "post": {
        "operationId": "chargeSubscription",
        "summary": "Charge Subscription",
        "tags": [
          "Subscriptions"
        ],
        "description": "The following endpoint activates a subscription with its first charge, or retry a payment for past due subscription.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "example": "sub_xyz123",
            "description": "Durianpay's subscription identifier. ID that you received on Create Subscription API Response"
          },
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
                  "payment_method_unique_id"
                ],
                "properties": {
                  "payment_method_unique_id": {
                    "type": "string",
                    "example": "GOPAY",
                    "description": "Binding reference for the customer's bound payment method.",
                    "enum": [
                      "SHOPEEPAY"
                    ]
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Charge executed, or payment method updated (no charge).",
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
                      "type": "object"
                    }
                  }
                },
                "examples": {
                  "chargeExecuted": {
                    "summary": "Charge executed",
                    "value": {
                      "status": "success",
                      "data": {
                        "subscription_id": "sub_xyz123",
                        "charge_id": "chg_88GtL22k",
                        "payment_id": "pay_abc456",
                        "order_id": "ord_192837A",
                        "amount": 99000,
                        "currency": "IDR",
                        "billing_cycle": 1,
                        "status": "success"
                      }
                    }
                  },
                  "paymentMethodUpdated": {
                    "summary": "Payment method updated (no charge)",
                    "value": {
                      "status": "success",
                      "data": {
                        "subscription_id": "sub_xyz123",
                        "payment_method_unique_id": "binding_new456",
                        "message": "Payment method updated. Next charge will use the new method on 2026-04-01T10:05:00Z.",
                        "next_billing_date": "2026-04-01T10:05:00Z"
                      }
                    }
                  }
                }
              }
            }
          },
          "402": {
            "description": "The auto-debit charge was declined by the payment provider.",
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
                  "CHARGE_FAILED": {
                    "summary": "CHARGE_FAILED",
                    "value": {
                      "status": "error",
                      "code": "CHARGE_FAILED",
                      "message": "Auto-debit charge was declined by the payment provider."
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "No subscription with the given id exists for this merchant.",
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
                  "SUBSCRIPTION_NOT_FOUND": {
                    "summary": "SUBSCRIPTION_NOT_FOUND",
                    "value": {
                      "status": "error",
                      "code": "SUBSCRIPTION_NOT_FOUND",
                      "message": "No subscription found with id 'sub_xyz123' for this merchant."
                    }
                  }
                }
              }
            }
          },
          "409": {
            "description": "The current billing cycle has already been charged with this payment method.",
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
                  "ALREADY_CHARGED": {
                    "summary": "ALREADY_CHARGED",
                    "value": {
                      "status": "error",
                      "code": "ALREADY_CHARGED",
                      "message": "Subscription has already been charged for the current billing cycle with this payment method."
                    }
                  }
                }
              }
            }
          },
          "422": {
            "description": "The subscription is in a state that cannot be charged.",
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
                  "INVALID_SUBSCRIPTION_STATE": {
                    "summary": "INVALID_SUBSCRIPTION_STATE",
                    "value": {
                      "status": "error",
                      "code": "INVALID_SUBSCRIPTION_STATE",
                      "message": "Cannot charge a cancelled subscription."
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