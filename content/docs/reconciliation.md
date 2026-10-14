---
updatedAt: 2025-08-14T07:09:20.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Reconcile your transactions

# Export Disbursement Data

Durianpay provide export feature where you can retrieve your pay outs data into excel format. It can be used to reconcile against your system data. Here is the following steps to export pay outs data:

1. Go to`Disbursements` - `Batch Details` page from the dashboard menu

   ![](https://files.readme.io/c127948a8a4fd5a252e46098205773374f5322cb7921cdfd0422043a54f45c53-image.png)
2. Once you click `Export` button, there will be popup to select  date range and type of export you want to get. Click `Export Data` button once you select the details you preferred.

   <Image align="center" width="450px" src="https://files.readme.io/e65bea046230b30656a8d2cc250f7f0fefbf35328a73a959487130dd3748b236-image.png" />
3. You will be redirected to `Export` menu  with the report details. By default, the status will be processing until we finish preparing the report to you.

   ![](https://files.readme.io/d1cedf07abb45c7b8b9a9f195f65ace9587980afc8ae912261292355957ef305-image.png)
4. Once the report is ready you will see `Download` button. Click download button to get the balance history report.

   ![](https://files.readme.io/463aeb431742caca1f67f37b535bbf25a2c963bea8b6067eced02b26b6b71d4d-image.png)

<br />

# Export Disbursement Items Data

1. Go to`Disbursements` - `Item Details` page from the dashboard menu

   ![](https://files.readme.io/768c46dc55456b031ffe621747b6ea6b2731bf0c8b23ae0c99fe419f8cbcb520-image.png)
2. Once you click `Export` button, there will be popup to select  date range and type of export you want to get. Click `Export Data` button once you select the details you preferred.

   <Image align="center" width="400px" src="https://files.readme.io/235d49ee2638977553ad29c3425736545f20465b918e77d6ea848513fb44d36a-image.png" />
3. You will be redirected to `Export` menu  with the report details. By default, the status will be processing until we finish preparing the report to you.
4. <Image align="center" src="https://files.readme.io/8590200f6244a4435d18e10008ef17e10afa2ec9033ecfe1f868f0a81795aba0-image.png" />

   Once the report is ready you will see `Download` button. Click download button to get the balance history report.

   ![](https://files.readme.io/9aedb7848e61548c1ca3e279af62158968107ab1ede011e3c7fa3867dc59ff87-image.png)

<br />

# Balance History

Durianpay provide balance history for you to reconcile the data between Durianpay and your own system. Here's the following step to retrieve balance history:

1. You can access this from the menu of `Balance`. To export the data you can select the date you want to get the balance history data from and click `Export` button

![](https://files.readme.io/b1d0c573c864ee623c971a4f8ff4f5495ac7472620e1b34583133c4447c73e63-image.png)

2. You will be redirected to `Export` menu  with the report details. By default, the status will be processing until we finish preparing the report to you.

   ![](https://files.readme.io/e1e4b1cf3f3543b51f82b608808fd782c3d5f97b6ef6f9c0e604e4a1743d3f56-image.png)
3. Once the report is ready you will see `Download` button. Click download button to get the balance history report.

   ![](https://files.readme.io/1d3dc02e7a7d23734df214904295666a67c9551872cbbcaa861d25101986dd3f-image.png)
4. Example of balance report in excel:

   <Image align="center" src="https://files.readme.io/2e18617bca6bff4de54d6d707ad52cd965ac008b009c8bef1afb99080a746d2b-image.png" />

<br />

# Sync Transaction Status

In order to sync transaction status from your system, you can use our dashboard to re-send notification/webhook information to your webhook url setup in settings.

The sync status button is available in

1. `Disbursement` - `Batch Details`

   1. Click the batch you want to sync against, and you will be redirected to disbursement batch item details.

      ![](https://files.readme.io/d8f4bc647af8d6cb89bb2c4db78942e9ee999fc7eef8892d56b8d079afe80682-image.png)
   2. Click Sync status button. It is available on top right of the page.

      ![](https://files.readme.io/33a14304d7f47338cd5ff3e54c49be734a423013aea6930ef70a0fd6fccde69f-image.png)
2. `Disbursement` - `Item Details`

   1. You can search the item transactions using our search feature to search by disbursement id or by filter of date, bank code and amount

      ![](https://files.readme.io/1da14268c3d98cf54837193aa9a6ef711f4dc2c89fa12fbc42e323793d413600-image.png)
   2. Once you found the pay out transactions you want to sync you can either click the `refresh` button or click three dots and click `Sync Status`.