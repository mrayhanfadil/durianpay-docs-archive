---
updatedAt: 2026-09-24T08:09:31.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Generate Access Token (B2B) API

The following endpoint generate access token for SNAP transaction APIs

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "durianpay-snap-api-access-token",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://api.durianpay.id/v1.0"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "Content-Type",
        "x-default": "application/json"
      },
      "sec1": {
        "type": "apiKey",
        "in": "header",
        "name": "X-TIMESTAMP",
        "x-default": "2024-05-14T18:54:57+07:00"
      },
      "sec2": {
        "type": "apiKey",
        "in": "header",
        "name": "X-SIGNATURE",
        "x-default": ""
      },
      "sec3": {
        "type": "apiKey",
        "in": "header",
        "name": "X-CLIENT-KEY",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": [],
      "sec1": [],
      "sec2": [],
      "sec3": []
    }
  ],
  "paths": {
    "/access-token/b2b": {
      "post": {
        "summary": "Generate Access Token (B2B) API",
        "description": "The following endpoint generate access token for SNAP transaction APIs",
        "operationId": "access-token-b2b",
        "parameters": [
          {
            "name": "Content-Type",
            "in": "header",
            "description": "Indicates the media type of the resource. value: application/json",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-TIMESTAMP",
            "in": "header",
            "description": "Timestamp in ISO8601 format, Example: 2024-05-14T18:54:57+07:00",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-SIGNATURE",
            "in": "header",
            "description": "Asymmetric signature (SHA256withRSA, Base64-encoded) of the string Client ID & Timestamp, signed with your private key.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "X-CLIENT-KEY",
            "in": "header",
            "description": "Client Key given by Durianpay upon completing registration.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "grantType"
                ],
                "properties": {
                  "grantType": {
                    "type": "string",
                    "description": "Value: AUTHORIZATION_CODE"
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
                  "OK": {
                    "value": "{\n    \"responseCode\": \"2007300\",\n    \"responseMessage\": \"Successful\",\n    \"accessToken\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTAwNTYsImlhdCI6MTcxNTU4OTE1NiwibWVyY2\",\n    \"tokenType\": \"BearerToken\",\n    \"expiresIn\": \"2024-05-13 08:47:36.452492159 +0000 UTC\"\n  }"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "responseCode": {
                      "type": "string",
                      "example": "2007300"
                    },
                    "responseMessage": {
                      "type": "string",
                      "example": "Successful"
                    },
                    "accessToken": {
                      "type": "string",
                      "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEdXJpYW4gTW9uZXkiLCJleHAiOjE3MTU1OTAwNTYsImlhdCI6MTcxNTU4OTE1NiwibWVyY2"
                    },
                    "tokenType": {
                      "type": "string",
                      "example": "BearerToken"
                    },
                    "expiresIn": {
                      "type": "string",
                      "example": "2024-05-13 08:47:36.452492159 +0000 UTC"
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
                  "Unauthorized - Missing Client Key Header": {
                    "value": "{\n    \"responseCode\": \"4017300\",\n    \"responseMessage\": \"missing client-key header in request\",\n  }"
                  },
                  "Unauthorized - Invalid Signature": {
                    "value": "{\n    \"responseCode\": \"4017300\",\n    \"responseMessage\": \"missing client-key header in request\",\n  }"
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
                  "Internal Server Error": {
                    "value": "{\n    \"responseCode\": \"5001600\",\n    \"responseMessage\": \"General Error\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "responseCode": {
                      "type": "string",
                      "example": "5001600"
                    },
                    "responseMessage": {
                      "type": "string",
                      "example": "General Error"
                    }
                  }
                }
              }
            }
          },
          "504": {
            "description": "504",
            "content": {
              "application/json": {
                "examples": {
                  "Gateway Timeout": {
                    "value": "{\n    \"responseCode\": \"5041600\",\n    \"responseMessage\": \"Timeout\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "responseCode": {
                      "type": "string",
                      "example": "5041600"
                    },
                    "responseMessage": {
                      "type": "string",
                      "example": "Timeout"
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl --location 'https://api.durianpay.id/v1.0/access-token/b2b' \\\n--header 'X-TIMESTAMP: 2024-05-13T15:32:36.422+07:00' \\\n--header 'X-SIGNATURE: KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=' \\\n--header 'X-CLIENT-KEY: client_id' \\\n--header 'Content-Type: application/json' \\\n--data '{\n    \"grantType\": \"AUTHORIZATION_CODE\"\n}'"
            },
            {
              "language": "python",
              "code": "import requests\n\nurl = 'https://api.durianpay.id/v1.0/access-token/b2b'\nheaders = {\n    'X-TIMESTAMP': '2024-05-13T15:32:36.422+07:00',\n    'X-SIGNATURE': 'KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=',\n    'X-CLIENT-KEY': 'client_id',\n    'Content-Type': 'application/json'\n}\ndata = {\n    \"grantType\": \"AUTHORIZATION_CODE\"\n}\n\nresponse = requests.post(url, headers=headers, json=data)\n\nprint(response.text)"
            },
            {
              "language": "java",
              "code": "OkHttpClient client = new OkHttpClient();\n\nString url = \"https://api.durianpay.id/v1.0/access-token/b2b\";\nString timestamp = \"2024-05-13T15:32:36.422+07:00\";\nString signature = \"KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=\";\nString clientKey = \"client_id\";\nString contentType = \"application/json\";\n\nGson gson = new Gson();\nString jsonBody = gson.toJson(Map.of(\"grantType\", \"AUTHORIZATION_CODE\"));\n\nRequestBody requestBody = RequestBody.create(MediaType.parse(contentType), jsonBody);\n\nRequest request = new Request.Builder()\n    .url(url)\n    .addHeader(\"X-TIMESTAMP\", timestamp)\n    .addHeader(\"X-SIGNATURE\", signature)\n    .addHeader(\"X-CLIENT-KEY\", clientKey)\n    .addHeader(\"Content-Type\", contentType)\n    .post(requestBody)\n    .build();\nResponse response = client.newCall(request).execute();"
            },
            {
              "language": "javascript",
              "code": "const request = require('request');\n\nconst url = 'https://api.durianpay.id/v1.0/access-token/b2b';\nconst headers = {\n    'X-TIMESTAMP': '2024-05-13T15:32:36.422+07:00',\n    'X-SIGNATURE': 'KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=',\n    'X-CLIENT-KEY': 'client_id',\n    'Content-Type': 'application/json'\n};\nconst data = {\n    \"grantType\": \"AUTHORIZATION_CODE\"\n};\n\nrequest.post({\n    url: url,\n    headers: headers,\n    json: data\n}, (error, response, body) => {\n    if (error) {\n        console.error('Request error:', error);\n    } else {\n        console.log('Response status code:', response.statusCode);\n        console.log('Response body:', body);\n    }\n});"
            },
            {
              "language": "ruby",
              "code": "require 'net/http'\nrequire 'uri'\nrequire 'json'\n\nurl = URI.parse('https://api.durianpay.id/v1.0/access-token/b2b')\nheaders = {\n  'X-TIMESTAMP' => '2024-05-13T15:32:36.422+07:00',\n  'X-SIGNATURE' => 'KLJ9KthaIiZSzPqHUMuJRsKOZtYCqqWd5DhfWqYC7OjZ2Qlu0PvQ2wRQF5vfDWsz/qFYEexOXb47+oQBjMhAz4XRNhXBBfwoWxrGTG8iU8EYSDVfChW0NqAWjWIQolhB4UcHn5SybPFRON3rvAOIQTzuEshUA1PNAln8jOKaRmY=',\n  'X-CLIENT-KEY' => 'client_id',\n  'Content-Type' => 'application/json'\n}\ndata = { 'grantType' => 'AUTHORIZATION_CODE' }\n\nhttp = Net::HTTP.new(url.host, url.port)\nhttp.use_ssl = true\n\nrequest = Net::HTTP::Post.new(url.request_uri, headers)\nrequest.body = data.to_json\n\nresponse = http.request(request)\nputs \"Response code: #{response.code}\"\nputs \"Response body: #{response.body}\"\n"
            }
          ],
          "samples-languages": [
            "curl",
            "python",
            "java",
            "javascript",
            "ruby"
          ]
        }
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