---
updatedAt: 2025-06-17T23:25:20.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Introduction

Welcome to Durianpay's API Documentation! Our APIs empower businesses to integrate seamless payment solutions into their applications. Built on RESTful architecture, our APIs are reliable, scalable, and easy to use, enabling developers to deliver exceptional payment experiences.

## REST API

REST API (Representational State Transfer) is a web architecture that facilitates communication over HTTP using methods like GET, POST, PUT, and DELETE. It employs JSON for efficient and straightforward data exchange.

## Sandbox & Live Mode

Durianpay supports two modes: Sandbox and Live. Sandbox Mode is a testing environment that replicates real-world API behavior without processing actual transactions, ideal for integration testing. Live Mode is designed for production and handles real transactions securely.

By default, you are provided with Sandbox Mode to test your integration. Live Mode is activated upon successful KYB and onboarding verification. Once enabled, you can seamlessly switch between modes via the toggle in the top-left corner of your dashboard.

<Image alt="Dashboard - Sandbox Mode" align="center" border={true} src="https://files.readme.io/2454ecd8ae3141e103d924dd09097fc26feab11d58888104f064f468182f602d-image.png">
  Dashboard - Sandbox Mode
</Image>

Below are the details for the Sandbox and Live URLs in Durianpay:

* Sandbox Base URL : <https://api-sandbox.durianpay.id>
* Live Base URL: <https://api.durianpay.id>
* Full Live URL: \{base\_url}/\{version}/\{api-name} , Example:
  * Normal API: <https://api.durianpay.id/v1/payments/charge>
  * SNAP API: <https://api.durianpay.id/v1.0/access-token/b2b>

To interact with the API, ensure you use the correct credentials and URL according to the mode:

* Sandbox Mode: Use the sandbox credentials and sandbox URL.
* Live Mode: Use the live credentials and live URL.

You can access this credentials information via Menu Settings - API Keys in respective mode.

<Image alt="Settings API Key" align="center" width="400px" src="https://files.readme.io/59cb4d32b30c6acc27bcf2144785b13a3300db19c4811df0878715c5d28709b1-image.png">
  Settings API Key
</Image>

<br />

## SNAP Postman Collection

To simplify testing on SNAP endpoint, we've prepared a Postman collection that you can use with the credentials above. [SNAP Postman Collection](https://app.getpostman.com/run-collection/21542481-05002fcd-c2a2-495f-9d89-d00956f6ea23?action=collection%2Ffork\&collection-url=entityId%3D21542481-05002fcd-c2a2-495f-9d89-d00956f6ea23%26entityType%3Dcollection%26workspaceId%3D621679ab-309b-4e70-9aca-aa32d1c2cbab#?env%5BDurianpay%5D=W3sia2V5IjoiYmFzZV91cmwiLCJ2YWx1ZSI6Imh0dHBzOi8vYXBpLmR1cmlhbnBheS5pZC92MSIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiaHR0cHM6Ly9hcGkuZHVyaWFucGF5LmlkL3YxIiwic2Vzc2lvbkluZGV4IjowfSx7ImtleSI6InNlcnZlcl9rZXkiLCJ2YWx1ZSI6ImRwX1hYWFgiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCIsInNlc3Npb25WYWx1ZSI6ImRwX2xpdmVfbnZURFlKcE11cXdaSmFTMSIsInNlc3Npb25JbmRleCI6MX1d)

How to install postman and set up the environment can be seen on [Postman Installation](https://docs.durianpay.id/reference/postman-installation)

## API Overview

<HTMLBlock>{`
<head>
  <style>
    .api-container {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 10px;
    }

    .api-card {
      background-color: #ffffff;
      border-radius: 15px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      padding: 10px;
      width: 300px;
      text-align: left; /* Align text to the left */
      text-decoration: none; /* Remove underline for links */
      color: #767676; /* Inherit text color */
      transition: transform 0.2s, background-color 0.2s;
    }

    .api-card:hover {
      transform: scale(1.05);
      background-color: lightgray;
      
    }

    .api-title {
      font-size: 1.25rem;
      font-weight: bold;
      margin-bottom: 5px;
      color: #767676;
      text-decoration: none; /* Remove underline for links */
    }

    .api-description {
      font-size: 1rem;
      color: #767676;
      text-decoration: none; /* Remove underline for links */
    }
  </style>
</head>
<body>
<p>Explore our suite of APIs designed to streamline your payment processes.</p>

<div class="api-container">
  <a href=order-apis-1 class="api-card">
    <div class="api-title">Payments API</div>
    <div class="api-description">Accept customer payment</div>
  </a>
 
  <a href=snap-disbursement-apis class="api-card">
    <div class="api-title">Pay Outs API</div>
    <div class="api-description">Send fund to to the beneficiary</div>
  </a>
  
  <a href=refund-apis-1 class="api-card">
    <div class="api-title">Refund APIs</div>
    <div class="api-description">Refund customer payments</div>
  </a>

  <a href=static-va-apis-1 class="api-card">
    <div class="api-title">Custom VA APIs</div>
    <div class="api-description">Advanced Virtual Accounts usage</div>
  </a>

  <a href=sub-accounts-apis class="api-card">
    <div class="api-title">Platform APIs</div>
    <div class="api-description">Manage sub organizations or branches</div>
  </a>


</div>

</body>
`}</HTMLBlock>