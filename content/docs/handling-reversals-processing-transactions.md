---
updatedAt: 2026-08-19T09:21:03.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Handling Pay Out Reversals

Most pay outs reach a final status (success or failed) and need no further action. In two cases, extra handling is required after submission: a disbursement that already succeeded can later be **reversed**, or a transaction can stay **in processing** for longer than expected.

What you receive for a reversal depends on which API you use and whether you have registered the reversal webhook. Find your setup below.

| Your setup                                    | What you receive on a reversal                                                              | Where to read                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| SNAP API, reversal webhook registered         | A dedicated `transfer.bank.reversal` event with `latestTransactionStatus`:`04` / `Refunded` | [SNAP API with the reversal webhook](#snap-api-with-the-reversal-webhook-recommended) |
| SNAP API, reversal webhook **not** registered | The existing `transfer-bank.notify` event with `06` / `failed`                              | [SNAP API without the reversal webhook](#snap-api-without-the-reversal-webhook)       |
| Legacy (non-SNAP) Disbursement API            | No dedicated reversal event. A webhook is re-sent with the item status changed to `failed`  | [Legacy Disbursement API](#legacy-non-snap-disbursement-api)                          |

## Handling Reversals

A reversal happens when a disbursement that was previously marked successful is later returned and reversed. Reversals are initiated from the provider or bank side and are rare in practice, well under 0.03% of transactions.

A reversal can occur up to **9 working days** after the original success, though in most cases it is detected and processed on **D+1**. The most common causes are a wrong or invalid beneficiary account, or a compliance or fraud review.

### What happens during a reversal

Regardless of your integration type:

* **The disbursement status becomes&#x20;**`failed`**.** This is the transaction's own status, shown on the Dashboard and returned by status inquiry.
* The full reversed amount, including the disbursement fee, is credited back to your Durianpay balance.

<Callout icon="❗️" theme="error">
  ### Important: a reversal is reported at two levels

  The **disbursement status** becomes `failed`, while the `latestTransactionStatus` in the reversal webhook is `04` / `Refunded`.

  These are not contradictory. The disbursement did not ultimately deliver funds, so its status is `failed`. The `04` / `Refunded` value tells you _why_ it failed: it was reversed after previously succeeding, rather than failing outright.

  Use `latestTransactionStatus` `04` to identify a reversal. Do not expect the disbursement status itself to read `Refunded`.
</Callout>

<Callout icon="❗️" theme="error">
  ### A reversal cannot be undone

  Once a transaction is reversed, it stays reversed. If the funds still need to reach the beneficiary, create a new disbursement.
</Callout>

What differs between integration types is **how you are notified**, covered in the options below.

***

### 1. SNAP API with the reversal webhook (recommended)

This applies only if you use the SNAP Disbursement API **and** have registered the reversal webhook event.

This is the only setup where a reversal is clearly distinguishable from a normal failed transfer.

#### Reversal webhook event

| Event Name               | Description                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `transfer.bank.reversal` | Triggered when a previously successful SNAP disbursement is reversed. Delivered to your registered reversal URL. |

#### Status handling

| latestTransactionStatus | transactionStatusDesc | Disbursement status | Description                                                                  |
| ----------------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------- |
| 00                      | done                  | success             | The transaction is successfully completed.                                   |
| 03                      | Pending               | processing          | The transaction is still being processed and has not reached a final status. |
| 04                      | Refunded              | failed              | The transaction was previously successful and is now reversed.               |
| 06                      | failed                | failed              | The transaction has failed.                                                  |

#### Webhook sample

`transfer.bank.reversal`

```json
{
  "originalPartnerReferenceNo": "1000-1000-1000-1180",
  "originalReferenceNo": "dis_item_Jl2HIglkQN4340",
  "latestTransactionStatus": "04",
  "transactionStatusDesc": "Refunded",
  "amount": {
    "value": "10000.00",
    "currency": "IDR"
  },
  "beneficiaryAccountNo": "3370018285",
  "beneficiaryAccountName": "John Doe",
  "beneficiaryBankCode": "014",
  "additionalInfo": {
    "failureReason": "Reversal Transaction"
  }
}
```

#### How to handle it

1. Validate the digital signature and headers using the same SNAP scheme as `transfer-bank.notify`. See [Handling Webhooks](https://docs.durianpay.id/docs/handling-webhooks) for the verification steps.
2. Look up the original transaction using `originalReferenceNo` or `originalPartnerReferenceNo`.
3. Mark that transaction as reversed, treating it as a failed disbursement with a reversal reason, and adjust your settlement, ledger, or finance records accordingly.
4. Make the handling idempotent. The event may be retried, so guard against processing the same reversal twice.
5. Return an HTTP `200 OK` response so Durianpay does not retry the delivery.

#### Registering the reversal webhook

Register the event the same way as any other Pay Out webhook: go to **Settings > Webhooks > Create New**, select the reversal event, and set your callback URL. See [Handling Webhooks](https://docs.durianpay.id/docs/handling-webhooks) for the full setup walkthrough.

***

### 2. SNAP API without the reversal webhook

This applies if you use the SNAP Disbursement API but have **not** registered the reversal webhook event.

Your integration continues to work with no change. Reversals are still delivered, but through the existing `transfer-bank.notify` flow:

| latestTransactionStatus | transactionStatusDesc | What it means in this setup                                                                                          |
| ----------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 06                      | failed                | Either a genuine failed transfer **or** a reversal of a previously successful transfer. These are indistinguishable. |

<Callout icon="🚧" theme="warn">
  ### Reversals look identical to normal failures

  Because both cases arrive as `06` / `failed`, your system cannot tell whether the transfer never succeeded or succeeded and was later reversed. If your reconciliation depends on that distinction, register the reversal webhook.
</Callout>

#### What to watch out for

* A transaction you previously recorded as successful may later arrive as `failed`. Your handler must be able to move a transaction from a success state to a failed state, not only from pending to failed.
* Reconciling a reversal against your ledger may require manual confirmation, since no reversal reason is provided.
* Check the Dashboard, or contact support with the disbursement ID (`dis_item_xx`), if you need to confirm whether a specific `failed` transaction was a reversal.

#### Recommended next step

Register the `transfer.bank.reversal` webhook so reversals arrive as a distinct event carrying `04` / `Refunded` and a reversal reason. This removes the ambiguity and the manual follow-up. See [SNAP API with the reversal webhook](#snap-api-with-the-reversal-webhook-recommended).

***

### 3. Legacy (non-SNAP) Disbursement API

This applies if you use the Legacy Disbursement API (`disbursement.completed` and `disbursement.validation.completed`) rather than the SNAP API.

The dedicated reversal webhook is a SNAP-only feature, so there is no distinct reversal event on the Legacy Disbursement API.

You are still notified. When a reversal occurs, Durianpay re-sends the webhook for that transaction with **the item status changed from&#x20;**`done`**&#x20;to&#x20;**`failed`. The full amount, including the fee, is credited back to your Durianpay balance.

<Callout icon="🚧" theme="warn">
  ### A reversal arrives as an ordinary failure

  Because the item simply becomes `failed`, a reversal is indistinguishable from a transaction that failed outright. No reversal reason is provided.

  The signal that a reversal occurred is the **transition**: an item you previously received as `done` is now reported as `failed`.
</Callout>

#### How to handle it

1. Look up the transaction by disbursement item ID (`dis_item_xx`).
2. If your records show that item was previously `done`, treat the change to `failed` as a reversal.
3. Mark the transaction as failed and adjust your settlement, ledger, or finance records. The amount has been credited back to your balance.
4. Make the handling idempotent, so a repeated webhook does not adjust your ledger twice.
5. Return an HTTP `200 OK` response so Durianpay does not retry the delivery.

#### What to watch out for

* **Your system must accept a&#x20;**`done`**&#x20;item later becoming&#x20;**`failed`**.** This is the most common integration gap. If your handler ignores webhooks for transactions already recorded as successful, or treats `done` as final and never re-reads it, you will miss reversals entirely and your balance will drift from your ledger.
* Do not treat a successful disbursement as final for reconciliation purposes until 9 working days have passed.
* To confirm whether a specific `failed` transaction was a reversal, check the Dashboard or contact support with the disbursement ID.

<Callout icon="📘" theme="info">
  ### Moving to SNAP

  If you need reversals to be identifiable as reversals, rather than inferred from a `done` to `failed` transition, we recommend migrating to the SNAP Disbursement API and registering the reversal webhook. See [Integration Steps for SNAP](https://docs.durianpay.id/docs/snap-disbursement-api-implementation).
</Callout>

***

<Callout icon="📘" theme="info">
  ### Reducing reversals (all integration types)

  Because reversals are provider-driven, they cannot be fully prevented, but you can reduce them by validating the beneficiary before you disburse (see [Verifying Recipients](https://docs.durianpay.id/docs/checking-recipients)), double-checking the account number, name, and bank code, and keeping compliance and KYC clean.
</Callout>