---
updatedAt: 2025-06-17T23:24:59.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Preparation & Configuration

## What do you need to use our No Code Pay Outs?

You only need Live Durianpay account (An account which has passed KYB - Know Your Business verification and be enabled for pay outs).

## Manage User for Pay Outs

Once your live account is ready, you will be given an admin access to the account. We recommend you to to create at least 1 maker and 1 approver for your operational needs. Here's the overview of user roles for pay outs:

| Role     | View Pay Outs | Create Pay Outs | Approve Pay Outs |
| :------- | :------------ | :-------------- | :--------------- |
| Admin    | Yes           | Yes             | Yes              |
| Maker    | Yes           | Yes             | No               |
| Approver | Yes           | No              | Yes              |

<br />

### Create New User for Pay Outs

* Go to the` User` Menu and click `Invite New User` button
* Invite maker or approver role into Durianpay dashboard in your organization

  ![](https://files.readme.io/c92118ba784a876dd2285dd7a2ef70c96e6c30119c26545188c988efc77436ba-image.png)
* Once user is invited, email & password will be sent to the invited email destination.
* New user can login through Durianpay dashboard login page (<https://dashboard.durianpay.id/>)
* We **strongly** recommend the invited user to directly change the password using menu of Account Settings on the top right corner of the dashboard

  <Image alt="Account Settings option" align="center" src="https://files.readme.io/abb11a07d556b68790d1a7498cc28f5477e768ea9a19ac99c64f327a0f32ecd7-image.png">
    Account Settings option
  </Image>

  <Image alt="Change password button in account settings" align="center" src="https://files.readme.io/32aea2e85d8cc28ba4a1a8fd2f3ca188b8660ce839e4770c5cc80a7b1ff0bc53-image.png">
    Change password button in account settings
  </Image>
* In addition to password change, we also **strongly** recommend to activate 2-Step Verification to protect your account and add security for your pay out process.

<br />

## Configure Notification for Disbursement

* Go to the `Settings` menu and click `Notification` header
* In the page, you can set disbursement notification to customer using email or WhatsApp. This will be sent to the email/phone number specified at transaction level.

  ![](https://files.readme.io/b4ed1fe9f5103325ba1e0df35ebc311f68ff45c65e04e951f3250b90a30c68b7-image.png)
* Customer will receive notifications as following via Email/ WhatsApp
  > Congratulations \<Beneficiary Name>,
  >
  > \<Amount> has been transferred to your \<Bank Name> \<Account Number> account by \<Merchant Name>\
  > Total Amount: \<Amount>\
  > Notes: \<Notes>\
  > Disbursement ID: \<Durianpay Disbursement ID>
  >
  > Thanks,\
  > Durianpay Team