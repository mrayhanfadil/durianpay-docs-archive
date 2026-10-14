---
updatedAt: 2025-06-17T23:22:19.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Payment Flow

Understand how payment flow through Durianpay

## Relation Between Orders and Payments

In Durianpay, Order and Payment function as two distinct but interconnected entities that facilitate a seamless transaction process.

### Order Entity: Capturing Customer's Purchase Intent

The `Order` captures the details of a customer’s purchase intent. It contains information about the items being purchased, the total amount, and other relevant metadata.

### Payment Entity: Facilitating the Transaction

The `Payment` entity represents a specific attempt to complete the financial transaction, connected to a particular payment method (credit card, bank transfer, etc.).

<br />

## Transaction Lifecycle

The transaction lifecycle highlights the dynamic interaction between Order and Payment entities, from initiation to completion, with mechanisms for handling failures and expiries.

### 1. Order Initiation

The merchant creates an `Order`, which indicates purchase intent.

* **Order Expiry**: An expiry time is set for completing the transaction. If the order reaches its expiry without a successful payment, all associated payments are canceled, and no further attempts are allowed.

### 2. Payment Attempt

Merchant creates a `Payment`, which tied to a payment method, that associated with the `Order`.

* **Payment Expiry**: Each payment attempt has an expiry time based on the method used. `Payment` expiry cannot exceed the `Order` expiry. The `Order` itself remains open for new payment attempts until it expires.
* **Multiple Payment Attempts**: Each `Order` can have several associated payment attempts. If a payment fails, the `Order` remains active, allowing the customer to attempt payment again using a different or the same payment method.

### 3. Payment Processing

* **Successful Payment**: Once the customer paid the transaction, then the `Payment` status will be marked as completed which automatically will change the `Order` status to completed—ending the lifecycle.
* **Failed Payment**: If the `Payment` creation fails, the `Order` will remain active, allowing the customer to start another `Payment` until the order expiry is reached.