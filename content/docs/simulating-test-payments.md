---
updatedAt: 2025-06-17T23:23:21.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Simulating Test Payments

## Introduction

When your account is created in Durianpay, you will immediately gain access to the sandbox feature. This feature will allow you to play around with Durianpay's products without having real consequences in the production environment. The sandbox environment is accessible with different API Keys than the LIVE ones, and there will be a different section in Durianpay's Dashboard for sandbox data.

## Getting your Sandbox API Keys

Your sandbox API Keys will be shown in your Durianpay dashboard's API Keys page alongside your LIVE API Keys.

![](https://files.readme.io/9a95d2d2d41d4f0df07e525293f613037d2da491c55ea0f9a32fb290c55a73d5-image.png)

## Simulating a payment

To simulate a payment status in sandbox mode, the steps will be as follows:

<br />

### Step 1: Create a payment in sandbox mode

Creating a sandbox payment can be done by both API and Dashboard, the same with **LIVE** mode. Specifically for payment creation with API, the difference between the ones in LIVE will only be the API Keys. Where you will have to send a proper request body (i.e., the same with LIVE mode) and to the same API endpoints.

<br />

### Step 2: Simulating the Payment Status

Payment status can be simulated by using the "**Simulator**" feature in Durianpay dashboard. To access this feature, you must:

1. Login to your Durianpay Dashboard account
2. Change your Durianpay Dashboard's mode to `Sandbox`
3. Access the **Simulator** page in Durianpay dashboard

On this page, there will be a function to manually mark a sandbox transaction with a specific status, as shown below:

![](https://files.readme.io/7a3342500c1e966f1d3c724e774fb8e231a2ed9407e524b050924afbff6dfb51-image.png)

Afterwards, if you have configured your payment webhook in the sandbox environment, corresponding webhook will be sent towards the URL (i.e., your server) that you have specified.

> 🚧 Callback configuration in Sandbox environment is exclusive with the one in LIVE environment. When you are going LIVE, please ensure the webhook is also configured in LIVE environment.