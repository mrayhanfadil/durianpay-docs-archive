---
updatedAt: 2026-07-08T11:24:52.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Fetch Subscriptions

The following endpoint fetch existing subscriptions

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
      "get": {
        "operationId": "listSubscriptions",
        "summary": "Fetch Subscriptions",
        "tags": [
          "Subscriptions"
        ],
        "description": "The following endpoint fetch existing subscriptions",
        "parameters": [
          {
            "in": "query",
            "name": "status",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                "pending",
                "active",
                "past_due",
                "paused",
                "cancelled"
              ]
            },
            "description": "Filter by subscription status."
          },
          {
            "in": "query",
            "name": "customer_id",
            "required": false,
            "schema": {
              "type": "string"
            },
            "description": "Filter by customer."
          },
          {
            "in": "query",
            "name": "from",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Include subscriptions with created_at >= from."
          },
          {
            "in": "query",
            "name": "to",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Include subscriptions with created_at <= to."
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
            "description": "Paginated list of subscriptions.",
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
                            "example": "sub_xyz123"
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
                          "customer_id": {
                            "type": "string",
                            "example": "cust_abc"
                          },
                          "subscription_ref_id": {
                            "type": "string",
                            "nullable": true,
                            "example": "sub-ref-0001"
                          },
                          "amount": {
                            "type": "integer",
                            "example": 99000,
                            "description": "Amount in the smallest currency unit. 99000 = Rp 99,000."
                          },
                          "currency": {
                            "type": "string",
                            "example": "IDR"
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
                          "next_billing_date": {
                            "type": "string",
                            "format": "date-time",
                            "nullable": true,
                            "example": "2026-04-14T10:00:00Z"
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
                          "id": "sub_xyz123",
                          "status": "active",
                          "customer_id": "cust_abc",
                          "subscription_ref_id": "sub-ref-0001",
                          "amount": 99000,
                          "currency": "IDR",
                          "interval": "monthly",
                          "interval_count": 1,
                          "next_billing_date": "2026-04-14T10:00:00Z",
                          "created_at": "2026-03-14T10:00:00Z"
                        }
                      ],
                      "pagination": {
                        "page": 1,
                        "per_page": 20,
                        "total": 142
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
}
```