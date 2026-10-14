---
updatedAt: 2025-06-17T23:24:14.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Dynamic Routing

Dynamic Routing is a payment recovery service that is used when the primary processor fails and the payment is routed to a backup processor.

There are scenarios where a payment may fail or decline with one processor but be authorized with another, such as when the first processor has technical issues. By setting up fallbacks to route the payment to a second processor under certain conditions, you increase the chance of a successful payment.

## How to setup dynamic routing?

It is setup **automatically** for dynamic QRIS and dynamic closed virtual accounts. This way, we ensure that your payments gets the best success rate in the market.

<Gambar />

## When is dynamic routing triggered?

Dynamic routing is triggered when there is a decrease in the performance of the payment processor selected for a specific payment method. If the performance of the chosen processor declines, any new transaction created will automatically be routed to an alternative payment processor with the best available performance at that time. It’s important to note that this change only applies to new transactions; any transaction that has already been created will continue with the originally selected payment processor.

## Benefits of dynamic routing for your business

The following are the benefits that you will receive with dynamic routing:

1. **Improved Payment Reliability**: Ensures each transaction is processed through the best-performing provider to minimize failed payments.
2. **Increased Revenue**: Maximizes successful transactions, helping you capture more sales without manual intervention.
3. **Operational Efficiency**: Minimizes back-and-forth troubleshooting by automatically choosing the best provider, ensuring smooth payment operations.