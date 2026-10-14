---
updatedAt: 2025-06-17T23:25:26.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Payment Object

The `Payment` entity represents a specific attempt to complete the financial transaction, connected to a particular payment method (credit card, bank transfer, etc.).

## Payment Lifecycle

| Status         | Description                                                                                                                                                                                                                |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Processing** | A payment is created in processing state when a payment request receives a success response from downstream                                                                                                                |
| **Completed**  | The completed status indicates that the customer has successfully paid for the transaction. The funds will be settled to the merchant's account according to the agreed settlement schedule of the selected payment method |
| **Failed**     | The Failed status means the payment could not be created due to an issue on Durianpay's or its provider's side. You can safely retry the payment with the same method for the same order                                   |
| **Expired**    | The Expired status indicates that the payment was not completed by the customer before the payment expiry date. As a result, the transaction is no longer valid                                                            |
| **Cancelled**  | The Cancelled status indicates that the merchant has deliberately canceled the transaction by calling Durianpay's Cancel Payment API. No payment will be processed, and the transaction is considered void                 |