---
updatedAt: 2025-06-17T23:23:20.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Idempotent Request Implementation Guide

> 📘 The current API version is equipped with idempotency support on both request and object level. This allows merchant to safely retry requests without accidentally performing the same operation twice.

## What is idempotency key on request level (X-Idempotency-Key)?

X-Idempotency-Key is a unique token that is submitted alongside each API request made to Durianpay and will be assigned as identifier of that request. This key should be attached on the header of each API request.

<br />

## Why implementing X-Idempotency-Key on request level is mandatory?

**To avoid accidental request to perform same operation twice in case of network or system issue.**

This is especially important for disbursement transaction as it may incur double transaction for merchant if merchant is retrying transaction without proper idempotency-key.

For example, if disbursement creation fails due to network issue, ideally merchant will retry the disbursement. Unique X-Idempotency-Key will ensure that only one transaction is created upon retry.

<br />

## How to implement X-Idempotency-Key?

**When creating new transaction**\
Provide X-Idempotency-Key on the header of each of your request. We recommend merchants to use UUID format. Remember, the idempotency key should be unique and hasn't been used for successful transaction before.

**When retrying transaction request that receives error response**\
Please retry request using the same X-Idempotency-Key. Else, it will be counted as a different request. For further explanation on the cases please review the next questions.

<br />

## What is the difference between X-Idempotency-Key (request level) and idempotency\_key (batch level)?

Both have the same purpose, to prevent accidentally processing unintended identical disbursement transaction.

However, they have different purposes and implementation.

### X-idempotency-Key

`X-Idempotency-Key` is assigned to each request made to different API even if the requests are related to the same object

### Idempotency Key

`idempotency_key` is assigned to the disbursement batch itself where merchants can align it with internal reference IDs created from merchant's side and is only implemented to submit disbursement API.

![](https://files.readme.io/3f7d06320ab1e17bec0cfecf7f5c1ada26b4f30cb4258020dbfd5d3d145e408d-image.png)

<br />

## Possible Combination of X-Idempotency-Key and Idempotency\_Key

Below are the possible responses of using combination of X-Idempotency-Key and idempotency\_key when sending request:

a. Original request has been successfully processed and received final status (failed/success) from submit disbursement API. Hitting the API with different X-Idempotency-Key but same idempotency\_key will result in 403.

![](https://files.readme.io/e6f09cc23dd884684f248a933c7c5f10fa59b949f9f32fd763d604ca06d2951f-image.png)

b. Original request has been successfully processed and received final status (failed/success) from submit disbursement API. Hitting the API with the same X-Idempotency-Key but different idempotency\_key will return response that was sent to original request.

![](https://files.readme.io/8b0531b8edacfd90d85bf98787feee3f6ef54aca544f11c72b06a477a1f2c7fc-image.png)

<br />

### How does the X-Idempotency-Key work on various scenario?

In short, when a transaction request is successfully processed, X-Idempotency-Key will be stored in relation to the related transaction request. If the transaction request is failed to be processed, the X-Idempotency-Key will not be stored and you can use the same X-Idempotency-Key to retry the request.

Below are the list of cases when merchant submit request with the same X-Idempotency-Key as previous request (we will use the term 'original request' here):