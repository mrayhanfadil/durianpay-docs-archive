---
updatedAt: 2025-06-17T23:24:28.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Refund Limitations

> 📘 Currently, Durianpay's Refund only supports E-wallet and QRIS payments

## Refunding Eligibility

To be eligible for a refund, the following criteria must be met:

1. Payment method is either E-wallet or QRIS
2. The refund request is made within the allowed refund period
3. The refund amount is less than or equal to the original payment amount.
4. Refunds on settled payments will use the next available settlement amount from the same payment method and can only proceed when this amount is sufficient for the refund.
5. For QRIS refunds, there may be limitations based on the payor's bank choice when completing the QRIS transaction.
6. The MDR fee charged during settlement will not be refunded when processing a refund on a settled transaction. The refund amount will be deducted from the next available settlement.

## Provider refund capability comparison

The following are the limitation which employed by the provider on refunds:

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th rowspan="2">Limitations</th>
      <th colspan="6">Payment Method</th>
    </tr>
    <tr>
      <th>DANA</th>
      <th>Shopeepay</th>
      <th>OVO</th>
      <th>Gopay</th>
      <th>LinkAja</th>
      <th>QRIS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Refund Window*</td>
      <td>45 days</td>
      <td>365 days</td>
      <td>60 days</td>
      <td>45 days</td>
      <td>Unlimited</td>
      <td>Up to 365 days</td>
    </tr>
    <tr>
      <td>Partial Refund</td>
      <td>No</td>
      <td>Yes</td>
      <td>No</td>
      <td>Yes</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Refund Request Method</td>
      <td>API &amp; Dashboard</td>
      <td>API &amp; Dashboard</td>
      <td>API &amp; Dashboard</td>
      <td>API &amp; Dashboard</td>
      <td>Contact your dedicated account manager</td>
      <td>API &amp; Dashboard</td>
    </tr>
    <tr>
      <td>Refund Processing Time**</td>
      <td>Real-time</td>
      <td>Real-time</td>
      <td>Real-time</td>
      <td>Real-time</td>
      <td>Up tp 5 working days</td>
      <td>Real-time</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

\* Duration after the transaction is paid

\*\* In certain cases, additional process by the provider may extend the refund time.