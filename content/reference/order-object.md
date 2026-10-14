---
updatedAt: 2025-06-17T23:25:23.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Order Object

The `Order` captures the details of a customer’s purchase intent. It contains information about the items being purchased, the total amount, and other relevant metadata.

> 📘 We recommend creating `Order` as soon as amount is known, such as when customer begins the checkout process, to help track your sales funnel. If the amount changes, you can create a new `Order`

<br />

## Order Lifecycle

| Status         | Definition                                                                                                                                                                                                                                             |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Started**    | When you create an order, it is in started state. It stays in this state till any payment is attempted against it                                                                                                                                      |
| **Processing** | An order moves to processing state when a payment is created/attempted on it. It remains in this state till one payment associated with this order (at least) is completed                                                                             |
| **Completed**  | After the payment is completed, the order moves to the completed state. No further payment requests are permitted once the order moves to the completed state. The order stays in this state even if the payment associated with the order is refunded |