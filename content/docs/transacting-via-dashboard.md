---
updatedAt: 2025-06-17T23:25:01.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Transacting via Dashboard

# Batch Transaction

Durianpay provides no code pay out transactions via batch upload. It means that you can submit several pay out transactions at once by uploading a file with defined format. The steps to process batch transactions  in Durianpay will be as following:

1. Upload pay outs file by maker
2. Verify pay outs transactions by maker and approver
3. Approve transactions in a batch by approver
4. Durianpay will run all the transactions in the batch  approved.

# Disbursement Batch Status

The following status will be shown when you create a batch transaction in Durianpay:

* `Draft` : The batch of pay outs are created but not submitted by maker
* `Need Approval`: The batch of pay outs is submitted by maker to be approved by approver/admin
* `Rejected`: The batch of pay outs is rejected by approver/ admin.
* `Partially Success`: The batch contain success  and failed pay out transactions
* `Failed`: All pay outs  in a batch are failed
* `Completed`: All pay outs  in a batch are success

Inside a batch, we call the transactions as items. The following status describe item status in Durianpay:

* `Completed or Done`: pay out  item transaction is success.
* `Failed`: pay out item transaction is failed.
* `Processing`: pay out item transaction is currently processing.

# Disbursement Upload - (Maker/Admin Role)

1. Go to `Disbursements` Menu - `Batch Details` and click `Create Disbursement`button

   ![](https://files.readme.io/891c39cf329768350a3f94b4fa993d408694fc6cf2a9cac019c498c6bddcb304-image.png)
2. You can download Excel format / CSV Format directly from the dashboard and fill the bank destinations into the file. Batch Name & Description can also be filled via Excel format. Please fill all the mandatory details (batch name, account\_owner\_name,bank\_code, account\_number,amount) and upload the disbursement file by select file button/ dragging the file to the upload area.

   List of the banks supported can be found in excel file. Excel file also includes sample to fill the file.

   <Image alt="Example of excel data to be filled" align="center" src="https://files.readme.io/74fbbf1335e1b743a252d16b4124e6b0df5e11523e15942628d296bcb835a423-image.png">
     Example of excel data to be filled
   </Image>

   <br />

   <Image alt="Upload file for pay out transactions" align="center" src="https://files.readme.io/178f6b174905c3cb8ad4536cd48b91a2f51a9cba1feab386c3ef5f33bb9eb233-image.png">
     Upload file for pay out transactions
   </Image>
3. After you finish  filling in the details and uploading the file  you can click `Submit File` to proceed

   ![](https://files.readme.io/770e9cbd42d091bba1f082fd771dbb438d8a31c3a44eae4cd68f1294fca3c7d5-image.png)
4. After uploading the file, There will be validation process to the banks/provider. you can check whether the bank account destination is valid or not. Bank stated name will also be shown if the destination is a valid account.

   ![](https://files.readme.io/ab695d8b62eb350196c1ce109898c35802efd1668dd6f08e15c6044d28305680-image.png)
5. When there are transactions with issue, there are several options to process the transactions as following:
   1. Name Mismatch between input name and bank stated name
      1. Submit Anyway - the name will be replaced by the bank stated name to process the transaction. Once replaced the transactions will be in valid transaction section
      2. Delete the transactions row
   2. Invalid Bank Account
      1. By directly editing the field and then tick mark the transactions and click `Revalidate` button. If the record is valid it will move to the valid transaction
      2. Delete the transactions row
   3. Invalid Amount i.e. minimal amount of transactions
      1. By directly editing the incorrect field and then tick mark the transactions and click `Revalidate` button. If the record is valid it will move to the valid transaction
      2. Delete the transactions row
   4. Revalidation Needed (provider disturbance)
      1. Revalidate the transactions by clicking `Revalidate` button. If the record is valid it will move to the valid transaction
      2. Delete the transactions row
6. Click `Submit for approval` once everything is correct to confirm the submission of the disbursement file

![](https://files.readme.io/b4f7168004782d47a6fe85cbf292474cb242a701f4505f720fb612e5d5af2c77-image.png)

7. There will be popup confirmation to summarize the total transactions you are submitting. Click submit once you have confirmed the details.

<Image align="center" width="150px" src="https://files.readme.io/0a95813384910cd2f5cdf72276d4a9f5a9ed3560092a49f9d35a713512101b88-image.png" />

8. You can choose whether to submit new disbursement or go to the disbursement list page.

<Image align="center" width="150px" src="https://files.readme.io/f7872b7fef8e028afd490e9c1132da6290ff7586d6a18f0f81a8175128196b87-image.png" />

9. After Disbursement batch is submitted, the disbursement will be marked with status: ”Need Approval” then maker will need to ask approver/ admin role user to approve the transaction.

   ![](https://files.readme.io/e47676e6a5e554cedb1a537521151caddcfaf4c97710ba12bf3fa980150a015c-image.png)

# Disbursement Approve - (Approver/Admin Role)

1. As an approver/admin, you can click on the transactions with status of need approval (or use the filter to easily search the items). As approver you will also get notification in your email asking for your review whenever maker creates disbursement.

   ![](https://files.readme.io/e2a450db0ccb95c30403f926de3113384da878ca5b9c461ac9762f28129b7345-image.png)
2. As an approver/admin, you will need to check the destination data shown in the disbursement page whether it is correct according to the source of data you use. There are total number of transactions and total transaction amount as well to help checking the transactions. Once everything is fine, you can click Approve and Pay button to proceed with the transactions.

   ![](https://files.readme.io/60569f62c521195334d8dc1a091fd422fd0f56139f36c49150a725fa0719ec18-image.png)
3. Once “Approve and Pay” button is clicked there will be popup to confirm transaction amount and fee charged. Click Approve & Pay to proceed.

   <Image align="center" width="200px" src="https://files.readme.io/1ad64af9445288cb90343d6c84c821d3b8f18d159e1c5214c28b09f600325048-image.png" />
4. If OTP is enabled for your transaction, you will be required to enter 6-digit OTP that will be sent to your email account that's used for login.
5. After transactions is approved the status will be “Approved,” If all items are successfully disbursed the status of transaction will be “success”, "failed",  or “partially success” if some of transactions is success and other is failed.
6. When the transaction is successfully disbursed to the recipient, Durianpay will also send notification via email/WhatsApp if it is set by the merchants\
   Notes: Transaction data can also be received by clicking export button in the disbursement details/ disbursement list page

# Disbursement Reject - (Approver/Admin Role)

1. As an approver/admin, you can click on the transactions with status of need approval (or use the filter to easily search the items).

   ![](https://files.readme.io/e2a450db0ccb95c30403f926de3113384da878ca5b9c461ac9762f28129b7345-image.png)
2. Whenever Approver/Admin sees that the submitted data needs some revision, they can reject the disbursement back to Maker by clicking Reject button.

   ![](https://files.readme.io/60569f62c521195334d8dc1a091fd422fd0f56139f36c49150a725fa0719ec18-image.png)

   <Image align="center" width="200px" src="https://files.readme.io/aadb50532e019232b76da5eb7910328e6704e9b32a00c49ad925a09e768f923e-image.png" />
3. The reason will be shown in the disbursement dashboard to be read by the Maker in the disbursement details

   ![](https://files.readme.io/7800e59a2f4a19e33f9d9f04ccff3c299818ccf6faef4b3b5d909d2c8edefd80-image.png)
4. Once rejected, the disbursement transactions will reach end state, the maker need to fix the error and re-submit the file to transact again.