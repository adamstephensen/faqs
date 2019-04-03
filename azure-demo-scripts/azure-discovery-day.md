
## Azure Portal Demo

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

