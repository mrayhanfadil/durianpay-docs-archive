---
updatedAt: 2025-06-17T23:23:55.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Payment Flow

The following is the payment flow for E-wallet:

1. Merchant creates order through Durianpay dashboard/calling Create Orders API
2. Customer opens Durianpay checkout page/payment link
3. Customer chooses which e-wallet to use for payment
4. E-wallet service provider processes the payment
5. E-wallet service provider’s system notifies Durianpay system once payment is successful
6. Durianpay proceeds the payment status notification to merchant
7. Merchant receives the payment upon settlement date