---
updatedAt: 2025-08-14T09:24:12.000Z
agentTools:
  projectIndex: https://docs.durianpay.id/llms.txt
---

# Disbursement Status Definition

The `Disbursement` entity represents an action initiated by the sender to send fund to the beneficiary.

## Disbursement Item Lifecycle

| Pay Out Status       | Description                                                                     |
| :------------------- | :------------------------------------------------------------------------------ |
| **need\_validation** | Pay out is created in Durianpay side and has not been initiated to the provider |
| **valid**            | Pay out destination is valid after checking with the provider                   |
| **invalid**          | Pay out destination is invalid after checking with the provider                 |
| **processing**       | Pay out transaction is initiated to the provider and currently processing       |
| **failed**           | Pay out transaction is failed                                                   |
| **done / completed** | Pay out transaction is successfully transferred to the beneficiary              |