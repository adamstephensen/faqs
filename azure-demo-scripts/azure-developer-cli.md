# Setup

## Ensure the Azure Developer CLI and GitHub CLI are configured

[Get started using Azure Developer CLI (azd) ](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/get-started)

[GitHub - GitHub CLI](https://github.com/cli/cli)

## Open the following documents
[What is the Azure Developer CLI (azd) ?](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/overview?tabs=nodejs) (lists the available templates)

[GitHub Repo for the NodeJS Azure Container Apps Sample](https://github.com/azure-samples/todo-nodejs-mongo-aca)


# Demo Script

## Deploy and setup the developer workflow

1. Execute ONE of the following commands to download the template and deploy it to Azure. [The full list of available templates](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/overview?tabs=python#azure-developer-cli-templates) are in the docs.

```
// using Azure Container Apps (ReactJS web app + NodeJs APIs)
azd up --template todo-nodejs-mongo-aca

// using ReactJS web app on Azure Static Web App + NodeJs Azure Function APIs)
azd up --template todo-nodejs-mongo-swa-func

// using ReactJS web app on Azure Static Web App + Python Azure Function APIs)
azd up --template todo-python-mongo-swa-func

```


This may take a while to complete as it executes three commands: azd init (initializes environment), azd provision (provisions Azure resources), and azd deploy (deploys application code). 

** Inspect the Solution
* /scr folder - all the application code
* /infra folder - Infrastructure as code
* /azure.yaml - Azure developer Configuration ties the source code to the azure services defined in /infra
* /.vscode folder - VS Code configuration to run and debug the application
* /.github/workflows - Github actions


2. Setup a pipeline using ```azd pipeline```

```
azd pipeline config
```

This creates a Service Principal stored in a GitHub secret named ```AZURE_CREDENTIALS```.
It then executes the GitHub action from the workflows folder and pushes from the private git repo to a new repo on GitHub


3. Commit code changes and automatically deploy to app running on Azure

```
//update automatically
git push

```

4. Monitor the application

```

//opens the "overview" dashboard
azd monitor --overview

//opens the Live Metrics dashboard
azd monitor --live

//opens the logs dashboard
azd monitor --logs  

```

## Clean up resources so you don't continue to get charged

```
azd down
```

# trouble shooting 

### docker isn't running in wsl 

```
service docker status
sudo service docker start
sudo docker run hello-world
```

alternatively .... to enable docker to run without needing sudo [follow the steps in the docs](https://docs.docker.com/engine/install/linux-postinstall/)

```
sudo groupadd docker
sudo usermod -aG docker $USER
```

### can't open default browser in wsl

```warning: failed to open default browser: could not open resource: exec: "xdg-open": executable file not found in $PATH```

