


#0 Create dotnote core, ruby and / or node app, containerise and deploy
- based on https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-docker-go



#1 Container Web Apps: Create an Azure DevOps Project for .NET Core in Container
- show how much easier it is that #0 and it has full devops. 

#2 Container Web Apps: Open an existing .NET Core app and add the docker file
- don't need to do this one from scratch. just show how eash it is.

#3 ACR Demo

#4 ACI Demo
- [old - hanselman version](https://www.hanselman.com/blog/PennyPinchingInTheCloudDeployingContainersCheaplyToAzure.aspx)
- [demo from docs](https://docs.microsoft.com/en-gb/azure/container-instances/container-instances-quickstart)

```
az group create --name myResourceGroup --location eastus
az container create --resource-group myResourceGroup --name mycontainer --image mcr.microsoft.com/azuredocs/aci-helloworld --dns-name-label aci-demo --ports 80
az container show --resource-group myResourceGroup --name mycontainer --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
az container logs --resource-group myResourceGroup --name mycontainer
az container attach --resource-group myResourceGroup --name mycontainer
az container delete --resource-group myResourceGroup --name mycontainer
az container list --resource-group myResourceGroup --output table
az group delete --name myResourceGroup

```

#5 AKS Demo - Scripted

- Check out the [Simple AKS Demo script](./aks-simple.md) in this folder

#6 AKS Demo - from Azure DevOps Project
- Create an Azure Devops | .NET Core | AKS project
- Inspect the .NET Core App
- Inspect the Build process
- Inspect the release process
