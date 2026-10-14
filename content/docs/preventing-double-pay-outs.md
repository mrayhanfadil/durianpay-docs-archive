---
updatedAt: 2025-06-17T23:24:46.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Preventing Double Pay Outs on API transactions

Handling payout transactions effectively is essential to ensuring a seamless experience for both the business and the recipient. Occasionally, a transaction may timed-out or fail, requiring a retry to complete the payout. To avoid any risk of duplicate payouts, we recommend the following best practices:

SNAP API:

1. Implement inquiry status properly to check status of a disbursement before retrying transaction.
2. Handling X-External-ID , as this field is treated as idempotency-key within a day.
3. Handling partnerReferenceNo to be unique for a particular transaction during retry.

Legacy API:

1. Implement inquiry status properly to check status of a disbursement before retrying transaction (can be done using your idempotency key or our disbursement id).
2. Implement idempotency-key properly and trying to hit with the same idempotency-key during retry to avoid creating double disbursement.