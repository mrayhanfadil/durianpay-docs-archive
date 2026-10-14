---
updatedAt: 2025-06-17T23:24:49.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Handling errors

## Handling Timeout

* In case of timeout, We recommend you to always call inquiry status API to check the transaction status, before proceeding with changing your internal status.

## Handling 5xx API Response

* 5xx API response means that the server failed to fulfill an apparently valid request.
* We recommend you to always call inquiry status API to check the transaction status, before proceeding with changing your internal status.

## Handling 4xx API Response

* 4xx API response means that client error – the request contains bad syntax or cannot be fulfilled.
* Generally it's safe to mark transaction as failed if you receive 4xx error.