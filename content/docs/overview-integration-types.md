---
updatedAt: 2026-09-11T06:59:08.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Available Integration Types

## No Code Solution

In addition to integration options, Durianpay provides a No Code Solution called Payment Link to help you start accepting payments instantly. The Payment Link is a shareable URL that embeds Durian Checkout, allowing your customers to make secure payments through Durianpay without any technical setup required. Simply generate and share the Payment Link with your customers, making it easy for them to complete their payments seamlessly.

<br />

## Payment Integration Types

<HTMLBlock>{`
<table style="width:100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th colspan="6" style="border: 1px solid #000; text-align: center;">Integration Methods</th>
    </tr>
    <tr>
      <th rowspan="3" style="border: 1px solid #000;"></th>
      <th colspan="4" style="border: 1px solid #000; text-align: center;">Durian Checkout</th>
      <th rowspan="3" style="border: 1px solid #000; text-align: center;">Payment APIs</th>
    </tr>
    <tr>
      <th rowspan="2" style="border: 1px solid #000; text-align: center;">JavaScript</th>
      <th rowspan="2" style="border: 1px solid #000; text-align: center;">Plugins</th>
      <th colspan="2" style="border: 1px solid #000; text-align: center;">Payment Link</th>
    </tr>
    <tr>
      <th style="border: 1px solid #000;">Dashboard</th>
      <th style="border: 1px solid #000;">API</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000;">Development effort required</td>
      <td style="border: 1px solid #000;">~5 day<br>(1 Engineer)</td>
      <td style="border: 1px solid #000;">~1 day<br>(1 Engineer)</td>
      <td style="border: 1px solid #000;">None<br>(no code)</td>
      <td style="border: 1px solid #000;">~2 days<br>(1 Engineer)</td>
      <td style="border: 1px solid #000;">~10 days<br>(2 Engineers)</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000;">Integration flow</td>
      <td style="border: 1px solid #000;">Create Order API, then open the checkout modal with the JavaScript snippet</td>
      <td style="border: 1px solid #000;">Install and configure the plugin</td>
      <td style="border: 1px solid #000;">Fill in the Create New form in the Dashboard, then share the link</td>
      <td style="border: 1px solid #000;">Create Order API with <code>is_payment_link</code> set to <code>true</code>, then send the customer to the payment link URL returned in the response</td>
      <td style="border: 1px solid #000;">Call the payment method APIs directly</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000;">Customization</td>
      <td style="border: 1px solid #000;">Themes, Button Colors, Business Logo</td>
      <td style="border: 1px solid #000;">Themes, Button Colors, Business Logo</td>
      <td style="border: 1px solid #000;">Themes, Button Colors, Business Logo</td>
      <td style="border: 1px solid #000;">Themes, Button Colors, Business Logo</td>
      <td style="border: 1px solid #000;">Payment flow, User Interface</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000;">Pre-selected payment method availability</td>
      <td style="border: 1px solid #000;">Supported. Enable the customer to directly land on a payment method page, for example QRIS or Virtual Account</td>
      <td style="border: 1px solid #000;">No. The customer always starts on the payment method list</td>
      <td style="border: 1px solid #000;">No. The customer always starts on the payment method list</td>
      <td style="border: 1px solid #000;">No. The customer always starts on the payment method list</td>
      <td style="border: 1px solid #000;">You build the flow, so you control which method is shown</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000;">Payment Page</td>
      <td style="border: 1px solid #000;">Provided by Durianpay<br>(modal inside your page)</td>
      <td style="border: 1px solid #000;">Provided by Durianpay</td>
      <td style="border: 1px solid #000;">Provided by Durianpay<br>(hosted at links.durianpay.id)</td>
      <td style="border: 1px solid #000;">Provided by Durianpay<br>(hosted at links.durianpay.id)</td>
      <td style="border: 1px solid #000;">Provided by Merchant</td>
    </tr>
    <tr>
      <td style="border: 1px solid #000;">Use Case</td>
      <td style="border: 1px solid #000;">Native Support for your Websites</td>
      <td style="border: 1px solid #000;">Native support for WooCommerce</td>
      <td style="border: 1px solid #000;">Collect payments with no website and no engineering work. Create a link per order and share it over WhatsApp, email, or social media</td>
      <td style="border: 1px solid #000;">Recommended for mobile apps, where you open the URL instead of embedding JavaScript. Also lets your own system generate links automatically</td>
      <td style="border: 1px solid #000;">Fully Customizable Payment Experience</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>