## How do I backup VSTS ? 

From my experiences 95% of customers do not back up SaaS applications like DropBox, SalesForce and Visual Studio Team Services… they rely on their built in mechanisms and the fact that loss of data would be catastrophic for their reputation.

Here is the white paper on VSTS Data Protection
http://aka.ms/vsts-security.


There is also a User Voice request to provide in-built backs here

It contains the following comment from the VSTS Team
VSTS Team (Product group, Microsoft Visual Studio) commented  ·   
Thanks for your feedback. We understand the importance of ensuring that your data is safe and secure. Providing the ability to use backups to recover from errors and corruption is an essential element of our data protection practices. The full description of these practices can be found at http://aka.ms/vsts-security.
We do not currently support self-service restoration of VSTS accounts from backups. However, we do support related scenarios.
1. Many operations within VSTS are reversible. For instance, Account deletion (https://docs.microsoft.com/vsts/accounts/delete-your-vsts-account#restore-your-vsts-account) and Work item deletion (https://docs.microsoft.com/vsts/work/backlogs/remove-delete-work-items) perform “soft” deletes, which can be recovered without requiring a backup. Also, all changes to source files under version control are logged so that you can revert to a previous version as needed.
2. For those operations which are not reversible or in the case of corruption, accounts can be manually restored from backups by our support team. Reach out to support at https://www.visualstudio.com/team-services/support/. Note that there is no magic – just like restoring TFS databases from backups in the on-premises world, you will lose any changes made since the time of the backup.
Longer term, we plan to make more delete operations “soft” and make recovery self-service. The hope is that this reduces the need for self-service restoration from backup to the point where it is no longer needed except in extreme situations.

Beyond that
-	Backing up Git Repositories from VSTS is very easy. You have a script that recurringly pulls all the branches of the Git repo locally, and backs up that folder.
This guarantees you never loose your code… but does not back up artefacts like your work items and build pipeline configuration
-	 There are open source / third party tools you can use to backup the other components of VSTS

