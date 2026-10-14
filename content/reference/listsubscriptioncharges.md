---
updatedAt: 2026-07-08T11:24:52.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch Subscription Charges

The following endpoint fetch all payments on a single subscription

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
    "/v1/subscriptions/{id}/charges": {
      "get": {
        "operationId": "listSubscriptionCharges",
        "summary": "Fetch Subscription Charges",
        "tags": [
          "Subscriptions"
        ],
        "description": "The following endpoint fetch all payments on a single subscription",
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
            "in": "query",
            "name": "status",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                "processing",
                "success",
                "failed"
              ]
            },
            "description": "Filter by charge status."
          },
          {
            "in": "query",
            "name": "page",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 1,
              "minimum": 1
            },
            "description": "Page number."
          },
          {
            "in": "query",
            "name": "per_page",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 20,
              "minimum": 1,
              "maximum": 100
            },
            "description": "Items per page."
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
            "description": "Paginated charge history.",
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
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "example": "chr_abc001"
                          },
                          "subscription_id": {
                            "type": "string",
                            "example": "sub_xyz123"
                          },
                          "order_id": {
                            "type": "string",
                            "example": "ord_001"
                          },
                          "billing_cycle": {
                            "type": "integer",
                            "example": 3
                          },
                          "charge_type": {
                            "type": "string",
                            "enum": [
                              "automatic",
                              "manual"
                            ],
                            "example": "automatic"
                          },
                          "status": {
                            "type": "string",
                            "enum": [
                              "processing",
                              "success",
                              "failed"
                            ],
                            "example": "success"
                          },
                          "created_at": {
                            "type": "string",
                            "format": "date-time",
                            "example": "2026-03-14T10:00:00Z"
                          }
                        }
                      }
                    },
                    "pagination": {
                      "type": "object",
                      "properties": {
                        "page": {
                          "type": "integer",
                          "example": 1
                        },
                        "per_page": {
                          "type": "integer",
                          "example": 20
                        },
                        "total": {
                          "type": "integer",
                          "example": 142,
                          "description": "Total records matching the query, across all pages."
                        }
                      }
                    }
                  }
                },
                "examples": {
                  "OK": {
                    "summary": "OK",
                    "value": {
                      "status": "success",
                      "data": [
                        {
                          "id": "chr_abc001",
                          "subscription_id": "sub_xyz123",
                          "order_id": "ord_001",
                          "billing_cycle": 3,
                          "charge_type": "automatic",
                          "status": "success",
                          "created_at": "2026-03-14T10:00:00Z"
                        },
                        {
                          "id": "chr_abc000",
                          "subscription_id": "sub_xyz123",
                          "order_id": "ord_000",
                          "billing_cycle": 2,
                          "charge_type": "automatic",
                          "status": "failed",
                          "created_at": "2026-02-14T10:00:00Z"
                        }
                      ],
                      "pagination": {
                        "page": 1,
                        "per_page": 20,
                        "total": 3
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
          }
        }
      }
    }
  }
}
```