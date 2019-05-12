

# 1. Develop for cloud storage

## Develop solutions that use file storage
- implement quotas for file shares in storage account
- move items in file shares between containers asynchronously
- set file storage container properties in metadata

## Develop solutions that use a relational database
- create, read, update, and delete database tables by using code
- implement dynamic data masking


# 2. Create Platform as a Service (PaaS) Solutions

## Create an app service Logic App
- create a custom connector for Logic Apps, a custom template for a Logic App
- create a Logic App
- package an Azure App Service Logic App


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
- implement parallelism, multithreading, processing, durable functions, Azure logic apps, interfaces with storage, interfaces to data access, and appropriate asynchronous compute models

## Develop for autoscaling
- implement autoscaling rules and patterns (schedule, operational/system metrics, code that addresses singleton application instances, and code that addresses transient state

## Implement distributed transactions
- identify tools to implement distributed transactions (e.g., ADO.NET, elastic transactions, multi-database transactions)
- manage transaction scope
- manage transactions across multiple databases and servers


#5 Imlement cloud integration solutions
## Configure a message-based integration architecture
configure an app or service to send emails, Event Grid, and the Azure Relay Service  
create and configure a Notification Hub, an Event Hub, and a Service Bus  
configure queries across multiple products  
configure an app or service with Microsoft Graph  
## Develop an application message model
create a message schema and a message exchange  
create an event model  
create topics and subscriptions  

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
- configure Azure Disk Encryption for VMs

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
- create an Azure App Service background task by using WebJobs
- enable diagnostics logging

## Create Azure App Service mobile apps
- add push notifications for mobile apps
- enable offline sync for mobile app
- implement a remote instrumentation strategy for mobile devices

## Create Azure App Service API apps
- create an Azure App Service API app
- create documentation for the API by using open source and other tools

## Implement Azure functions
- implement input and output bindings for a function
- implement function triggers by using data operations, timers, and webhooks
- implement Azure Durable Functions
- create Azure Function apps by using Visual Studio


# 9. Develop for Azure storage

## Develop solutions that use storage tables
- design and implement policies for tables
- query table storage by using code
- implement partitioning schemes

## Develop solutions that use Cosmos DB storage
- create, read, update, and delete data by using appropriate APIs
- implement partitioning schemes
- set the appropriate consistency level for operations

## Develop solutions that use a relational database
- provision and configure relational databases
- configure elastic pools for Azure SQL Database
- create, read, update, and delete data tables by using code

## Develop solutions that use blob storage
- move items in blob storage between storage accounts or containers
- set and retrieve properties and metadata
- implement blob leasing
- implement data archiving and retention


# 10. Implement Azure security

## Implement authentication
- implement authentication by using certificates, forms-based authentication, or tokens
- implement multi-factor or Windows authentication by using Azure AD
- implement OAuth2 authentication
- implement Managed Service Identity (MSI)/Service Principal authentication

## Implement access control
- implement CBAC (Claims-Based Access Control) authorization
- implement RBAC (Role-Based Access Control) authorization
- create shared access signatures

## Implement secure data solutions
- encrypt and decrypt data at rest and in transit
- create, read, update, and delete keys, secrets, and certificates by using the KeyVault API

# 11. Monitor, troubleshoot, and optimize solutions

## Develop code to support scalability of apps and services
- implement autoscaling rules and patterns (schedule, operational/system metrics, singleton applications)
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
