---
updatedAt: 2025-06-17T23:25:56.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Register Sub-Account

The following endpoint registers a sub account under your master account.

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
    "/merchants/subaccount": {
      "post": {
        "summary": "Register Sub-Account",
        "description": "The following endpoint registers a sub account under your master account.",
        "operationId": "register-sub-account",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "name",
                  "email"
                ],
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the sub account",
                    "default": "Awesome Sub Organization 001"
                  },
                  "email": {
                    "type": "string",
                    "description": "Email of the sub account",
                    "default": "organization_001@masterorg.biz"
                  },
                  "ref_id": {
                    "type": "string",
                    "description": "The unique identifier of Subaccount from the merchant",
                    "default": "mer_123"
                  },
                  "subaccount_ownership": {
                    "type": "string",
                    "default": "owned",
                    "description": "Type of the subaccount, value can be either \"managed\" or \"owned\""
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
                    "value": "{\n  \"data\": {\n      \"id\": \"mer_abc123def456\",\n      \"name\": \"Awesome Sub Organization 001\",\n      \"email\": \"organization_001@masterorg.biz\",\n      \"ref_id\": \"organization_001\"\n  }\n}\n"
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
                          "example": "mer_abc123def456"
                        },
                        "name": {
                          "type": "string",
                          "example": "Awesome Sub Organization 001"
                        },
                        "email": {
                          "type": "string",
                          "example": "organization_001@masterorg.biz"
                        },
                        "ref_id": {
                          "type": "string",
                          "example": "organization_001"
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
                    "value": "{\n    \"error\": \"cannot validate request body for registering sub account\",\n    \"error_code\": \"DPAY_INVALID_REQUEST\",\n    \"errors\": [\n        {\n            \"field\": \"name\",\n            \"message\": \"can't be blank\"\n        }\n    ]\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "cannot validate request body for registering sub account"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "DPAY_INVALID_REQUEST"
                    },
                    "errors": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "field": {
                            "type": "string",
                            "example": "name"
                          },
                          "message": {
                            "type": "string",
                            "example": "can't be blank"
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
                    "value": "{\n    \"error\": \"invalid credentials\",\n    \"error_code\": \"merchant is not registered as a master merchant\",\n    \"request_id\": \"dp_pqHhskeQZf1990\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "invalid credentials"
                    },
                    "error_code": {
                      "type": "string",
                      "example": "merchant is not registered as a master merchant"
                    },
                    "request_id": {
                      "type": "string",
                      "example": "dp_pqHhskeQZf1990"
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
                    "value": "{\n    \"error\": \"internal server error\"\n}"
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