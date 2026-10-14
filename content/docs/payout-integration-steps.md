---
updatedAt: 2025-08-08T06:36:19.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Sending Pay Outs

> 📘 For Pay Outs API we currently have 2 API scheme: SNAP and Legacy API. We recommend you to implement **SNAP** as Legacy API will be deprecated by Q2 2025
>
> Meanwhile there's transition between SNAP and Legacy API, there will be 2 different authentication process between SNAP and Legacy API. We will streamline this process by Q2 2025.

# SNAP vs Legacy API

## What is SNAP?

SNAP (Standar Nasional Open API Pembayaran) is National Standard of Payment API established by Central Bank of Indonesia to build a healthy, competitive and innovative payment industry market; encourage integration, interconnection and interoperability also security and advanced payment infrastructure; and improve an efficient and reasonable market practice in payment activity over Indonesia.

## Why SNAP?

* Standardized security and API format across provider in Indonesia
* Easy interconnection & interoperability to apply other financial service API in Indonesia
* Compliant to Financial Regulation in Indonesia to avoid any future implications in Indonesia (BI require all merchants in Indonesia to use SNAP standard by End of June 2025)

## What is Legacy API?

Before proceeding with SNAP standard for Pay Outs API, Durianpay provide our own API standard and we call this legacy API. It is designed to empower your pay out needs with a strong flexibility to support normal and advanced use case.

## Comparison of SNAP and Legacy API

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Comparison Criteria
      </th>

      <th>
        SNAP
      </th>

      <th>
        Legacy API
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authentication & Security
      </td>

      <td>
        Incorporate Public/Private Key Scheme, B2B Token Access
      </td>

      <td>
        Live Key
      </td>
    </tr>

    <tr>
      <td>
        Interoperability
      </td>

      <td>
        Across Financial Industry in Indonesia
      </td>

      <td>
        Specific for Durianpay
      </td>
    </tr>

    <tr>
      <td>
        Support
      </td>

      <td>
        Will serve as the primary API for the Indonesian market.
      </td>

      <td>
        Will be Deprecated by Q2 2025
      </td>
    </tr>

    <tr>
      <td>
        Granularity of transaction
      </td>

      <td>
        Support item transaction level only for now
      </td>

      <td>
        Support Batch transaction which can contain several item transaction.
      </td>
    </tr>

    <tr>
      <td>
        List of API supported
      </td>

      <td>
        Balance Inquiry, Bank Account Validation, Bank Transfer,  Bank Transfer Inquiry Status, E-Wallet Account Validation, E-Wallet Transfer, E-Wallet Transfer Inquiry Status
      </td>

      <td>
        Submit Disbursement, Approve Disbursement,
        Validate Disbursement,
        Fetch Disbursement Status API,
        Top-up Amount API ,
        Fetch Top-up Detail by ID,
        Fetch Durianpay Balance API, Fetch Disbursement Items by ID , Fetch Disbursement by ID ,
        Delete Disbursement, Get Banks
      </td>
    </tr>
  </tbody>
</Table>

<br />

# FAQ

1. **Can I just implement Legacy API only?**\
   Yes you still can implement Legacy API. However you will be required to migrate to SNAP in the future time (by Q2 2025) as several Legacy API related to the transaction  will be deprecated.
2. **If I implement SNAP, can I use Legacy API?**\
   Yes you can, however the authentication between SNAP and Legacy API will be different. There are some useful API that's only supported in legacy API as of now, such as Topup API, Fetch Topup API and Bank List API. We recommend to strictly use the SNAP API.