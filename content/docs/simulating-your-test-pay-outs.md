---
updatedAt: 2025-12-21T15:50:24.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Simulating Test Pay Outs

## Introduction

After your Durianpay account is created, you will immediately have access to the sandbox feature. This feature will allow you to play around with Durianpay's products without having real consequences in the production environment. The Sandbox environment is accessible with different API Keys and URL from the ones in production.

## Getting your Sandbox API Keys

You can access your Sandbox API Keys from your Durianpay dashboard:

1. Log in to <https://dashboard.durianpay.id/#/login>.
2. From the menu options, click **Settings**.
3. Click on the **API Keys** tab,
   1. For **SNAP API**, please use SNAP API Keys
   2. For **Legacy API**, please use Legacy API Keys

<Image border={false} src="https://files.readme.io/8c52905061d2b5f589c3e0eb57d8d3954eb6eef01b38d96824dfea08967be0f6-image.png" />

## Simulating a Pay Out

To simulate a Pay Out status in Sandbox mode, the steps are as follows:

### Step 1: Create a Sandbox Disbursement

Creating a sandbox disbursement can be done via API or through your Durianpay dashboard - this is the same in the **LIVE** environment.

Specifically for submitting a disbursement via API, there are differences to note between the Live and Sandbox environment:

1. API keys
2. base URL
   1. Sandbox: [https://api-sandbox.durianpay.id](https://api-sandbox.durianpay.id/)
   2. Live: [https://api.durianpay.id](https://api.durianpay.id/)

Regardless of environment, a proper request body will be required.

#### 1.1 Simulating Bank Account Validation & E-Wallet Account Validation API

To simulate success case and failed case on bank account validation & e-wallet account validation you can use following rules:

| Case            | How to simulate                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------ |
| Valid account   | Use even number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation) |
| Invalid account | Use odd number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation)  |

#### 1.2 Simulating Bank Account Transfer & E-Wallet Account Transfer API

To simulate success case or failed case, you can use following rules. The callback or inquiry status will be affected with the status of the transaction you simulate with.

| Case                              | How to Simulate                                                                                    |
| :-------------------------------- | :------------------------------------------------------------------------------------------------- |
| Accepted Transaction - Processing | Use even number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation)  |
| Failed transaction                | Use odd number in beneficiaryAccountNo (Bank Validation) or customerNumber (E-Wallet Validation)   |
| Success transaction               | Simulate in `Sandbox Mode` using `Simulator` Menu `Disbursements` tab then click `Mark as success` |

We provide a Simulator feature in `Sandbox Mode` to simulate real success/failed transaction via dashboard. To access this feature:

1. Log in to <https://dashboard.durianpay.id/#/login>.
2. Change your Durianpay Dashboard mode to `Sandbox`.
3. Access the **Simulator** page in Durianpay dashboard.
4. Navigate towards **Disbursements** section in **Simulator** page.

<Image border={false} src="https://files.readme.io/dd500821e242b8db8393f2fa67d8d1173013012f368f9868d5a947e0cdb610d6-image.png" />

### Step 2: Handling final status : Inquiry status & Callback handling

After creating a transaction and simulating either a success or failed status, Durianpay will send a callback to the webhook URL you configured, based on the simulation status you selected. The inquiry status will also reflect the current status recorded in sandbox mode.

> 🚧 Callback configuration in Sandbox environment is exclusive to the one in LIVE environment. When you are going LIVE, please ensure the webhook is also configured in LIVE environment.