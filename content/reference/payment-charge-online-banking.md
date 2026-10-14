---
updatedAt: 2025-06-17T23:25:30.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Online Banking

The following endpoint charges the payment for online banking

> 🔗 Jenius Pay Redirect URL
>
> To complete a Jenius Pay payment, prepend the following to the web\_url from the API response:
>
> ```Text URL
> https://links.durianpay.id>
> ```
>
> If web\_url is:
>
> ```Text URL
> /doku_wallet_form?...&transId=pay_7cKEZOnpP79510...
> ```
>
> Then the full redirect URL is:
>
> ```
> https://links.durianpay.id/doku_wallet_form?...&transId=pay_7cKEZOnpP79510>...
> ```
>
> Note: Always use the full URL to redirect the customer to the payment form.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "charge-online-banking",
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
    "/payments/charge": {
      "post": {
        "summary": "Online Banking",
        "description": "The following endpoint charges the payment for online banking",
        "operationId": "payment-charge-online-banking",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type",
                  "request"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "default": "ONLINE_BANKING"
                  },
                  "request": {
                    "type": "object",
                    "description": "The payload object for online banking payment charge",
                    "required": [
                      "id",
                      "type",
                      "name",
                      "mobile"
                    ],
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "The id returned from create order api"
                      },
                      "type": {
                        "type": "string",
                        "description": "Online Banking type. Available value: JENIUSPAY"
                      },
                      "name": {
                        "type": "string",
                        "description": "Name that should appear in the Online Banking's page"
                      },
                      "mobile": {
                        "type": "string",
                        "description": "Customer's mobile number linked to the Jeniuspay account"
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
                    "value": "{\n    \"data\": {\n        \"type\": \"ONLINE_BANKING\",\n        \"response\": {\n            \"payment_id\": \"pay_7cKA5555P79510\",\n            \"order_id\": \"ord_ABd012ZFa01765\",\n            \"mobile\": \"\",\n            \"status\": \"\",\n            \"expiration_time\": \"2025-04-25T00:00:00.000Z\",\n            \"web_url\": \"doku_wallet_form?basket=Jenius Pay,1000.00,0,1000.00&mallid=XXXX&currency=360&amount=1000.00&transId=pay_xxxxxxxxxxxxxx&words=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&datetime=20250424000000&sessionId=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&email=customer@example.com&name=John Doe&addres=&state=&zipcode=&phone=081234567890&url=https://pay.example.com/redirect&paymentChannel=51\",\n            \"unique_id\": \"JENIUSPAY\",\n            \"paid_amount\": \"1000.00\",\n            \"metadata\": {}\n        }\n    }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "example": "ONLINE_BANKING"
                        },
                        "response": {
                          "type": "object",
                          "properties": {
                            "payment_id": {
                              "type": "string",
                              "example": "pay_7cKA5555P79510"
                            },
                            "order_id": {
                              "type": "string",
                              "example": "ord_ABd012ZFa01765"
                            },
                            "mobile": {
                              "type": "string",
                              "example": ""
                            },
                            "status": {
                              "type": "string",
                              "example": ""
                            },
                            "expiration_time": {
                              "type": "string",
                              "example": "2025-04-25T00:00:00.000Z"
                            },
                            "web_url": {
                              "type": "string",
                              "example": "doku_wallet_form?basket=Jenius Pay,1000.00,0,1000.00&mallid=XXXX&currency=360&amount=1000.00&transId=pay_xxxxxxxxxxxxxx&words=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&datetime=20250424000000&sessionId=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&email=customer@example.com&name=John Doe&addres=&state=&zipcode=&phone=081234567890&url=https://pay.example.com/redirect&paymentChannel=51"
                            },
                            "unique_id": {
                              "type": "string",
                              "example": "JENIUSPAY"
                            },
                            "paid_amount": {
                              "type": "string",
                              "example": "1000.00"
                            },
                            "metadata": {
                              "type": "object",
                              "properties": {}
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
                    "value": "{\n  \"error\": \"invalid Authorization header in request\",\n  \"error_code\": \"DPAY_UNAUTHORIZED_ACCESS\"\n}"
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