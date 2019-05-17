

# 1. Develop for cloud storage

## Develop solutions that use file storage

- implement quotas for file shares in storage account
	- https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share
- move items in file shares between containers asynchronously
	- https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10
	- https://docs.microsoft.com/en-us/azure/storage/common/storage-use-data-movement-library
- set file storage container properties in metadata
	- https://docs.microsoft.com/en-us/azure/storage/blobs/storage-properties-metadata

## Develop solutions that use a relational database

- create, read, update, and delete database tables by using code
	- https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/multi-container-microservice-net-applications/data-driven-crud-microservice
- implement dynamic data masking
	- https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dynamic-data-masking-get-started
	- https://docs.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking?view=sql-server-2017

# 2. Create Platform as a Service (PaaS) Solutions

## Create an app service Logic App

- create a custom connector for Logic Apps, a custom template for a Logic App
	- https://docs.microsoft.com/en-us/connectors/custom-connectors/create-logic-apps-connector
	- https://docs.microsoft.com/en-us/connectors/custom-connectors/define-openapi-definition
	- https://docs.microsoft.com/en-us/connectors/custom-connectors/define-postman-collection
- create a Logic App
	- https://docs.microsoft.com/en-us/azure/logic-apps/quickstart-create-first-logic-app-workflow
- package an Azure App Service Logic App
	- ??? ARM Template ?? 
	- https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-create-deploy-template

## Create app or service that runs on Service Fabric

- develop a stateful Reliable Service and a stateless Reliable Service
- develop an actor-based Reliable Service
- write code to consume Reliable Collections in your service
	
  
## Schedule bulk operations

- define the batch output and conditions by using Batch Service API
- write code to run a batch job
- run a batch job by using Azure CLI, Azure Portal, and other tools

## Design and develop applications that run in containers

- configure diagnostic settings on resources
- create a container image by using a Docker file
    - [Tutorial: Create a container image for deployment to Azure Container Instances](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app)
    - [Push your first image to a private Docker container registry using the Docker CLI](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli)
    - [Difference between ```Run``` and ```cmd``` in a dockerfile](http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/)
- create an Azure Container Service (ACS/AKS) cluster by using the Azure CLI and Azure Portal
- publish an image to the Azure Container Registry
- implement an application that runs on an Azure Container Instance
- implement container instances by using Azure Container Service (ACS/AKS), Azure Service Fabric, and other tools
manage container settings by using code


# 3. Secure cloud solutions

## Implement access control

- implement Claims-Based Access Control (CBAC) and Role-Based Access Control (RBAC) authorization


# 4. Develop for an Azure cloud model
	
## Develop for asynchronous processing

- implement parallelism, multit-hreading, processing, durable functions, Azure logic apps, interfaces with storage, interfaces to data access, and appropriate asynchronous compute models

## Develop for auto-scaling

- implement auto-scaling rules and patterns (schedule, operational/system metrics, code that addresses singleton application instances, and code that addresses transient state

## Implement distributed transactions

- identify tools to implement distributed transactions (e.g., ADO.NET, elastic transactions, multi-database transactions)
- manage transaction scope
- manage transactions across multiple databases and servers


# 5 Implement cloud integration solutions

## Configure a message-based integration architecture

- configure an app or service to send emails, Event Grid, and the Azure Relay Service  
- create and configure a Notification Hub, an Event Hub, and a Service Bus  
- configure queries across multiple products  
- configure an app or service with Microsoft Graph  

## Develop an application message model

- create a message schema and a message exchange  
- create an event model  
- create topics and subscriptions  


# 6. Develop Azure Cognitive Services, Bot, and IoT solutions

## Integrate Azure Cognitive Services in an application

- develop solutions by using intelligent algorithms that identify items from images and videos
- develop solutions by using intelligent algorithms related to speech, natural language processing, Bing Search, and recommendations and decision making

## Create and integrate bots

- create a bot by using the Bot Framework
- create a natural language conversation flow
- manage bots by using the Azure Portal
- register a bot by using the Bot Framework

## Create and implement IoT solutions

- configure Azure Time Series Insights
- configure Stream Analytics service for inputs and outputs
- establish bidirectional communication with IoT devices by using IoT Hub
- register devices with IoT Hub Device Provisioning Service


# 7. Develop Azure Infrastructure as a Service compute solutions

## Implement solutions that use virtual machines (VM)

- provision VMs
- create ARM templates
    - [Resource manager overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview)
    - [Azure resource providers and types](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-supported-services)
    - [Structure of an ARM template](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authoring-templates)
- configure Azure Disk Encryption for VMs
- [Understand the structure and syntax of Azure Resource Manager templates](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authoring-templates)
- [Create a Windows virtual machine from a Resource Manager template](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/ps-template)

## Implement batch jobs by using Azure Batch Services

- manage batch jobs by using Batch Service API
- run a batch job by using Azure CLI, Azure portal, and other tools
- write code to run an Azure Batch Services batch job

## Create containerized solutions

- create an Azure Managed Kubernetes Service (AKS) cluster
- create container images for solutions
- publish an image to the Azure Container Registry
- run containers by using Azure Container Instance or AKS


# 8. Develop Azure Platform as a Service compute solutions

## Create Azure App Service Web Apps

- create an Azure App Service Web App
    - [az appservice plan](https://docs.microsoft.com/en-us/cli/azure/appservice/plan?view=azure-cli-latest)
    - [az webapp](https://docs.microsoft.com/en-us/cli/azure/webapp?view=azure-cli-latest)
- create an Azure App Service background task by using WebJobs
    - [Getting started with WebJobs](https://docs.microsoft.com/en-us/azure/app-service/webjobs-sdk-get-started)
- enable diagnostics logging
    - [Enable diagnostics logging for apps in Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)

## Create Azure App Service mobile apps

- add push notifications for mobile apps
    - ** https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/windows-push-notification-services--wns--overview
    - ** https://docs.microsoft.com/en-us/azure/notification-hubs/notification-hubs-windows-store-dotnet-get-started-wns-push-notification
    - ** https://docs.microsoft.com/en-us/xamarin/xamarin-forms/data-cloud/push-notifications/azure
- enable offline sync for mobile app
    - ** https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-offline-data-sync
    - ** https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-android-get-started-offline-data
    - ** [How to use the managed client for Azure Mobile Apps](https://docs.microsoft.com/en-us/azure/app-service-mobile/app-service-mobile-dotnet-how-to-use-client-library)
- implement a remote instrumentation strategy for mobile devices

## Create Azure App Service API apps

- create an Azure App Service API app
- create documentation for the API by using open source and other tools

## Implement Azure functions

- implement input and output bindings for a function
    - (Azure Functions triggers and bindings concepts)[https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings]
- implement function triggers by using data operations, timers, and webhooks
- implement Azure Durable Functions
    - ** [Create your first durable function in C#](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-create-first-csharp)
    - [Durable Functions patterns and technical concepts (Azure Functions)](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-concepts)
    - [Durable Functions types and features (Azure Functions)](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-types-features-overview)
    - [Singleton orchestrators in Durable Functions (Azure Functions)](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-singletons)
- create Azure Function apps by using Visual Studio


# 9. Develop for Azure storage

## Develop solutions that use storage tables

- design and implement policies for tables
    - ** https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-a-service-sas
    - ** https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1
    - ** https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage
- query table storage by using code
- implement partitioning schemes

## Develop solutions that use Cosmos DB storage

- create, read, update, and delete data by using appropriate APIs
    - ** [SQL query examples for Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-sql-query)
- implement partitioning schemes
- set the appropriate consistency level for operations
    - ** [Consistency levels in Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/consistency-levels)

## Develop solutions that use a relational database

- provision and configure relational databases
- configure elastic pools for Azure SQL Database
- create, read, update, and delete data tables by using code

## Develop solutions that use blob storage

- move items in blob storage between storage accounts or containers
- set and retrieve properties and metadata
- implement blob leasing
    - ** https://docs.microsoft.com/en-us/rest/api/storageservices/lease-blob
- implement data archiving and retention


# 10. Implement Azure security

## Implement authentication

- implement authentication by using certificates, forms-based authentication, or tokens
- implement multi-factor or Windows authentication by using Azure AD
- implement OAuth2 authentication
- implement Managed Service Identity (MSI)/Service Principal authentication

## Implement Access Control

- implement CBAC (Claims-Based Access Control) authorization
- implement RBAC (Role-Based Access Control) authorization
- create shared access signatures

## Implement secure data solutions

- encrypt and decrypt data at rest and in transit
- create, read, update, and delete keys, secrets, and certificates by using the KeyVault API

# 11. Monitor, troubleshoot, and optimize solutions

## Develop code to support scalability of apps and services

- implement auto-scaling rules and patterns (schedule, operational/system metrics, singleton applications)
- implement code that handles transient faults

## Integrate caching and content delivery within solutions

- store and retrieve data in Azure Redis cache
- develop code to implement CDNs in solutions
- invalidate cache content (CDN or Redis)

## Instrument solutions to support monitoring and logging

- configure instrumentation in an app or service by using Application Insights
- analyze and troubleshoot solutions by using Azure Monitor
- implement Application Insights Web Test and Alerts


# 12. Connect to and consume Azure services and third-party services

## Develop an App Service Logic App

- create a Logic App
- create a custom connector for Logic Apps
- create a custom template for Logic Apps

## Integrate Azure Search within solutions

- create an Azure Search index
- import searchable data
- query the Azure Search index

## Establish API Gateways

- create an APIM instance
- configure authentication for APIs
- define policies for APIs

## Develop event-based solutions

- implement solutions that use Azure Event Grid
- implement solutions that use Azure Notification Hubs
- implement solutions that use Azure Event Hub

## Develop message-based solutions

- implement solutions that use Azure Service Bus
- implement solutions that use Azure Queue Storage queues
