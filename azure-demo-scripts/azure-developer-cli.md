1. Import the Calculator wsdl
```
http://www.dneonline.com/calculator.asmx?wsdl
```
Don't forget to select the products.

2. Test 'Add method'



# Setup

## Ensure the Azure Developer CLI is configured
[Get started using Azure Developer CLI (azd) ](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/get-started)

## Open the following documents
[What is the Azure Developer CLI (azd) ?](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/overview?tabs=nodejs) (lists the available templates)

[GitHub Repo for the NodeJS Azure Container Apps Sample](https://github.com/azure-samples/todo-nodejs-mongo-aca)


# Demo Script

## Deploy and setup the developer workflow

1. Download the template and deploy it to Azure

```
azd up --template todo-nodejs-mongo-aca
```

2. Create the service principle and configure the Github Action
```
azd pipeline config
```

3. Commit code changes and automatically deploy to app running on Azure

```
//update automatically
git push

//monitor the application
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