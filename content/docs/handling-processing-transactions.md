---
updatedAt: 2026-08-19T09:21:18.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Handling Processing Disbursements

This section applies to **all** integration types, SNAP and legacy.

A transaction is **in process** when it has been accepted and is being processed by the bank or provider, but has not yet reached a final status. This is a normal interim state. It can last longer than usual around bank cut-off times, provider maintenance, or intermittent provider delays.

### What to do

* **Do not resubmit the same pay out.** Retrying risks a double disbursement. See [Preventing Double Pay Outs on API transactions](https://docs.durianpay.id/docs/preventing-double-pay-outs).
* **Wait for the final status webhook.** Durianpay delivers the terminal status when it is confirmed, and retries at 2, 5, 10, 90, and 210 minutes if the webhook is not acknowledged with `200 OK`. SNAP merchants receive `transfer-bank.notify`; legacy merchants receive `disbursement.completed`.
* **Poll the status API** if you need to check before the webhook arrives. SNAP merchants can use the Status Inquiry API; legacy merchants can use the disbursement status endpoint.
* **Treat in-process as pending, not failed.** Do not mark the transaction failed, refund the end user, or re-disburse until you receive a terminal status.
* **If it stays in process beyond the expected window,** use Dashboard **Sync Status** or **Retrigger Webhook** on the transaction, or contact support with the disbursement ID (`dis_item_xx`).

<Callout icon="🚧" theme="warn">
  ### Never assume a stuck transaction has failed

  An in-process transaction may still complete successfully. Marking it as failed before a terminal status is received can lead to double payments or incorrect reconciliation.
</Callout>

### Where to get help

If a transaction remains stuck after the steps above, reach out through your usual support channel with the disbursement ID, or check the [Durianpay Status Page](https://status.durianpay.id/) for any ongoing incidents.