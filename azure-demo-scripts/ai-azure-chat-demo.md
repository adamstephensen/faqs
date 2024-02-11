### Resources: 
Official Repo: https://github.com/microsoft/azurechat
Thivy's new version: https://github.com/thivy/azurechat-2/tree/main

## setup - tooling requirements
install node LTS from https://nodejs.org/
select to include that additional tools, this will include chocolatey


## upgrade Powershell
I got this error: "'pwsh' is not recognized as an internal or external command, operable program or batch file"

solution: 
dotnet tool update --global PowerShell


### initiate the repo using azd
note: prefix must start with a letter and be 7 or less characters

azd auth login
azd init -t microsoft/azurechat
azd up

# if you are wanting to see logs run with debug flag
azd up --debug

note: to tear it down and delete resources use ```azd down```

### Prep - starting with your own resource group
Start with the subscriptoin and resource group settings

Example Subscription ID: ```zzzzzz-09fa-40ab-a0cd-d3d7d055fc7a```

### Create the resource group

```az group create --name <ResourceGroupName> --location <Location>```

example: 

```
az group create --name zz0205a --location australiaeast
```


### Fork the repo

### Create a service principal with the Contributor role on the resource group that contains the Azure App Service.
az ad sp create-for-rbac --name <NAME OF THE CREDENTIAL> --role contributor --scopes /subscriptions/<SUBSCRIPTION ID>/resourceGroups/<RESOURCE GROUP> --sdk-auth --output json

for example

az ad sp create-for-rbac --name oaidemocontribsp --role contributor --scopes /subscriptions/<SUBSCRIPTION ID>/resourceGroups/<RESOURCE GROUP> --sdk-auth --output json


### Create the secret in GitHub for the RBAC Credential

In the Repo, go to Settings, Secrets and Variables, Actions, New Secret

Enter AZURE_CREDENTIALS as the name and paste the contents of the JSON output as the value.

#### Create the web app name
secrets: create AZURE_APP_SERVICE_NAME with a value of the app service name. "zz-adams-azurechat-web'
