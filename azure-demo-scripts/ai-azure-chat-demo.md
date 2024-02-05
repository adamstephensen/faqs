### Prep
Start with the subscriptoin and resource group settings

Example Subscription ID: ```zzzzzz-09fa-40ab-a0cd-d3d7d055fc7a```

### Create the resource group

```az group create --name <ResourceGroupName> --location <Location>```

example: 

```az group create --name zz0205a --location australiaeast```


### Fork the repo

### Create a service principal with the Contributor role on the resource group that contains the Azure App Service.
az ad sp create-for-rbac
   --name <NAME OF THE CREDENTIAL> --role contributor --scopes /subscriptions/<SUBSCRIPTION ID>/resourceGroups/<RESOURCE GROUP> --sdk-auth --output json
![image](https://github.com/adamstephensen/faqs/assets/587638/c5a04408-8183-435f-8704-d873c71d989c)


### Create the secret in GitHub for the RBAC Credential

In the Repo, go to Settings, Secrets and Variables, Actions, New Secret

Enter AZURE_CREDENTIALS as the name and paste the contents of the JSON output as the value.
