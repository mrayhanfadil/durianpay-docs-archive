---
updatedAt: 2026-05-21T09:25:03.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Feature and Use Cases

<HTMLBlock>{`
<table style="width:100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="padding: 10px; text-align: left;">VA TYPE</th>
            <th style="padding: 10px; text-align: left;">DESCRIPTION</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" style="padding: 10px; font-weight: bold;">VA Number</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Static VA</td>
            <td style="padding: 10px;">Each customer will be assigned a fixed VA number that can be used multiple times as long as the VA is active — ideal for repeating payments</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Dynamic VA</td>
            <td style="padding: 10px;">For each customer payment, a randomly generated VA number will be created. New VA number will be generated every time a customer transacts — ideal for one-time transactions</td>
        </tr>
        <tr>
            <td colspan="2" style="padding: 10px; font-weight: bold;">Payment Amount</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Open-amount</td>
            <td style="padding: 10px;">Allow customers to input payment amount</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Closed-amount</td>
            <td style="padding: 10px;">Can only be paid with the nominal set during the VA creation</td>
        </tr>
        <tr>
            <td colspan="2" style="padding: 10px; font-weight: bold;">Usage</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Single</td>
            <td style="padding: 10px;">Can only receive payment once and then expired</td>
        </tr>
        <tr>
            <td style="padding: 10px;">Multiple</td>
            <td style="padding: 10px;">Can receive payment multiple times, will be expired once it has passed the predetermined expiration date</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

> 📘 Dynamic VA will always be close amount and available for single use.

> 🚧 If you do not set the type when creating Static VA, the default type will be open amount and available for multiple uses.