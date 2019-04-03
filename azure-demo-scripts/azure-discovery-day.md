
## Demo 1- Azure Portal Demo

01 – AZURE PORTAL DEMO

Important: This Demo sets up for later demos by getting long running tasks out of the way early.  Make sure you do the AKS Container setup (Step 9).

1. Open Internet Browser
2. Go to Azure.microsoft.com
3. Click “Portal”
4. Talk through every pane on the screen:  

	a. Dashboard  
	b. Directory / User  
	c. Subscription  
	d. Favorites  
	
> The Azure account is a global unique entity that gets you access to Azure services and your Azure subscriptions. You can create multiple subscriptions in your Azure account to create separation e.g. for billing or management purposes. In your subscription(s) you can manage resources in resources groups. Azure subscription can have a trust relationship with an Azure Active Directory (Azure AD) instance – more here.  	
An Azure subscription has a trust relationship with Azure Active Directory (Azure AD), which means that the subscription trusts Azure AD to authenticate users, services, and devices. Multiple subscriptions can trust the same Azure AD directory, but each subscription can only trust a single directory.
	https://docs.microsoft.com/en-gb/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory

	
5. Look at Resource Groups  
	a. Explain that everything in Azure is a Resource  
	b. Explain that every Resource must live in a Resource Groups  
	c. Explain that Resource Groups live in a Subscription  
	d. Browse and navigate to an existing resource group, and talk about the resources in it  
	e. Create a new Resource Group for today’s Azure Discovery Day  
	
6. Look at Virtual Machines and Classic Virtual Machines  
	a. Explain that ARM VMs end up in Virtual Machines  
	b. Explain that ASM / Classic VMs end up in Classic Virtual Machines  
	c. They are incompatible, and getting them to talk to each other is actually quite difficult.  
7. Provision a Virtual Machine  
	a. Click the “Create a resource” item  
	b. Search the market place for “Linux”  
	c. Fill in each of the fields, while explaining what the field does  
	d. Deploy the VM  
	e. Go to the "Overview" page while it's deploying.  
	f. Use SSH or Putty to connect to the VM IP address  
		a. Login to the VM  
		b. Just do a “LS” or a ”PS AUX” to show we’re connected to a Linux VM.  
	g. Keep this connection open, because we’ll use it again later.  
8. Demonstrate the Azure CLI / Azure PowerShell  
	a. Mention Azure CLI is quicker, but PowerShell is more familiar.  
	b. Use “az group list” to list out all the resource groups  
9. Create the AKS Cluster - Note we will use this later in the containers demo.  
	a. az provider register -n Microsoft.ContainerService  
	b. az group create --name azd-container-demo --location westus  
	c. az aks create --resource-group azd-container-demo --name myK8sCluster --node-count 1 --generate-ssh-keys  
10. Security Center   
	a. Click through and explain the screen  
11. Subscriptions  
	a. Explain this is where your subscription lives  
	b. View each of the various charts  
12. Dashboard & Customization  
	a. Go to Dashboard, show it off  
	b. Create a new Dashboard for today’s session  
	c. Pin some resources to it, I recommend creating a "Billing "Dashboard and pinning some subscription and cost stuff to it.  

## Demo 2 - Resource GroupsCost Management +Billing

02 –ARM Template Demo    
  
Important: This Demo sets up for later demos by getting long running tasks out of the way early.  Make sure you do the VMSS setup (Step 3).  
   
Go to the Azure Portal  
Deploy a simple Windows Server 2016 Datacentre VM  
Click New  
Search for “Windows Server 2016”  
Fill in the options, it doesn’t matter what you use.  Go through deployment until the final step  
View the deployment template  
Explain that this is the what Azure is actually doing when you click deploy on anything inside of Azure.  
Talk through each of the section of the ARM Template and what they are:  
Schema: The version of the ARM Template Schema itself we’re using  
Content Version: The version of the arm template you’re deploying.  If you’ve made a change you could increment this to indicates a newer or older version.  
Parameters: These are inputs to the template.  They can be modified at execution to have different results from your template deployment.  
Variables: These are not inputs to the template.  They can’t be modified, but they can be generated, so that for example you could generate a resource name by concatenating text and inputs from your parameters together.  
Resources: These are the actual resources you will be deploying with your script.  Walk through them, and their dependences.  
Outputs : The output from the template and it’s deployment.  
Azure Quick Start Templates  
Open a browser  
Visit Github Azure Quick Templates at https://github.com/Azure/azure-quickstart-templates  
Look at some of the templates - a good example would be a SharePoint Farm template due to it's complexity.  
Load the 201-vmss-windows-autoscale template at https://github.com/Azure/azure-quickstart-templates/tree/master/201-vmss-windows-autoscale  
Click deployment via the “Deploy to Azure Button” and set this up, because you’ll use it in a demo later.  Make sure it deploys.  
Also try the “Visualize” option to see what it looks like.  
Deploying ARM Templates via PowerShell  
Show an example deployment script – e.g. put the below text into a .ps1 file.  
Explain that "New-AzureRMResourceGroupDeployment" is all you need to know to deploy Azure Resource Manager Templates via PowerShell.  
   
New-AzureRmResourceGroup -Name $demoname -Location "Australia East"  
New-AzureRmResourceGroupDeployment -Name $demoname -ResourceGroupName $demoname -TemplateFile "C:\scripts\azure-quickstart-templates\active-directory-new-domain\azuredeploy.json" -TemplateParameterFile "C:\scripts\azure-quickstart-templates\active-directory-new-domain\azuredeploy.parameters.json" -verbose -dnsPrefix "$demoname-ad"  
New-AzureRmResourceGroupDeployment -Name $demoname -ResourceGroupName $demoname -TemplateFile "C:\scripts\azure-quickstart-templates\201-vm-domain-join\azuredeploy.json" -TemplateParameterFile "C:\scripts\azure-quickstart-templates\201-vm-domain-join\azuredeploy.parameters.json" -verbose -dnslabelprefix "$demoname-adfs"  
New-AzureRmResourceGroupDeployment -Name $demoname -ResourceGroupName $demoname -TemplateFile "C:\scripts\azure-quickstart-templates\201-vm-domain-join\azuredeploy.json" -TemplateParameterFile "C:\scripts\azure-quickstart-templates\201-vm-domain-join\azuredeploy.parameters.json" -verbose -dnslabelprefix "$demoname-proxy"  
New-AzureRmResourceGroupDeployment -Name $demoname -ResourceGroupName $demoname -TemplateFile "C:\scripts\azure-quickstart-templates\201-vm-domain-join\azuredeploy.json" -TemplateParameterFile "C:\scripts\azure-quickstart-templates\201-vm-domain-join\azuredeploy.parameters.json" -verbose -dnslabelprefix "$demoname-sync"  
