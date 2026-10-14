---
updatedAt: 2026-07-08T11:24:52.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Cancel Subscription

This endpoint permanently cancels a subscription

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
    "/v1/subscriptions/{id}/cancel": {
      "post": {
        "operationId": "cancelSubscription",
        "summary": "Cancel Subscription",
        "tags": [
          "Subscriptions"
        ],
        "description": "This endpoint permanently cancels a subscription",
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
        "responses": {
          "200": {
            "description": "Subscription cancelled.",
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
                        "status": {
                          "type": "string",
                          "example": "cancelled"
                        },
                        "cancelled_at": {
                          "type": "string",
                          "format": "date-time",
                          "example": "2026-03-06T10:00:00Z"
                        }
                      }
                    }
                  }
                },
                "examples": {
                  "Cancelled": {
                    "summary": "Cancelled",
                    "value": {
                      "status": "success",
                      "data": {
                        "id": "sub_xyz123",
                        "status": "cancelled",
                        "cancelled_at": "2026-03-06T10:00:00Z"
                      }
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "The subscription belongs to a different merchant.",
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
                  "FORBIDDEN": {
                    "summary": "FORBIDDEN",
                    "value": {
                      "status": "error",
                      "code": "FORBIDDEN",
                      "message": "You do not have access to this subscription."
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "No subscription with the given id exists.",
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
                      "message": "No subscription found with id 'sub_xyz123'."
                    }
                  }
                }
              }
            }
          },
          "422": {
            "description": "The subscription is already cancelled.",
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
                  "ALREADY_CANCELLED": {
                    "summary": "ALREADY_CANCELLED",
                    "value": {
                      "status": "error",
                      "code": "ALREADY_CANCELLED",
                      "message": "This subscription is already inactive."
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