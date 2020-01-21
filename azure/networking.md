
## App Service VNet Integration
This is THE document https://docs.microsoft.com/en-us/azure/app-service/web-sites-integrate-with-vnet


## Load balancing options

https://docs.microsoft.com/en-au/azure/frontdoor/front-door-lb-with-azure-app-delivery-suite *todo*

## What are service endpoints ? 

Virtual Network (VNet) service endpoints extend your virtual network private address space and the identity of your VNet to the Azure services, over a direct connection. Endpoints allow you to secure your critical Azure service resources to only your virtual networks. Traffic from your VNet to the Azure service always remains on the Microsoft Azure backbone network.

This feature is available for the following Azure services and regions:

- Azure Storage: Generally Available in all Azure regions
- Azure SQL Database: Generally Available in all Azure regions
- Azure Cosmos DB: Generally Available in all Azure public cloud regions
- Azure SQL Data Warehouse: Preview in all Azure public cloud regions
- Azure database services for PostgreSQL and MySQL: Preview in Azure regions where database service is available.

Source: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview

## What is Azure Frontdoor ?

Azure Frontdoor is a global web application acceleration platform.

It makes your application
- more scalable
- increases availablity
- increases reliability
- boosts performance
- increases application layer security
- global http & https load balancing
- instant global multi-region failover

Resources
- [Azure Frondoor - on Azure Fridays](https://www.youtube.com/watch?v=3Di9H1V0zuc)
- [Azure Frontdoor - Homepage](https://azure.microsoft.com/en-au/services/frontdoor/)

## DNS Tools

- https://www.whois.com.au/whois/dns.html
- https://www.ultratools.com/tools/dnsLookupResult


## Private link

- [Azure Blog - Private link announcement](https://azure.microsoft.com/en-au/blog/announcing-azure-private-link/)
- [Private link overview video](https://www.youtube.com/watch?v=--ri7oy0Cgw&feature=youtu.be)



## Connecting Web App to SQL Server

https://stackoverflow.com/questions/50483132/how-to-secure-access-from-app-service-to-azure-sql-database-using-virtual-networ/50483574

## Todo - clarification required

This is not to be confused with service endpoints TO your app. That is the recently released capability to lock traffic to your app down to selected VNet/subnets.

https://stackoverflow.com/questions/50483132/how-to-secure-access-from-app-service-to-azure-sql-database-using-virtual-networ/50483574

## network size cheater

``` text
/24 - 256 addresses (2^8)
/25 - 128 addresses (2^7)
/26 - 64 addresses (2^6)
/27 - 32 addresses (2^5)
/28 - 16 addresses (2^4)
```

## connecting to on-prem resources

https://social.msdn.microsoft.com/Forums/sqlserver/en-US/a2df13c0-a87d-4e05-82aa-621bd7566b7a/mssql-server-on-premise-connection-from-azure?forum=servbus

To reach on-premises resource from Azure, there are multiple ways to achieve this.

Below are the approaches you can consider :

#### 1) Hybrid Connection . It is a feature in Azure App Service

It provides a convenient way to connect the Apps in Azure App Service to on-premises resources behind your firewall. 

https://docs.microsoft.com/en-us/azure/biztalk-services/integration-hybrid-connection-overview

https://docs.microsoft.com/en-us/azure/app-service/app-service-hybrid-connections



 #### 2) By Logic App : Connect to on-premises data sources from Azure Logic Apps

In this you need to create an on-premises data gateway resource in the Azure portal and then logic apps can use the on-premises connector .

https://docs.microsoft.com/bs-latn-ba/azure/logic-apps/logic-apps-gateway-connection

#### 3) Configuring a site-to-site VPN Gateway between Azure and On-Premise

The article shows you how to use the Azure portal to create a Site-to-Site VPN gateway connection from your on-premises network to the VNet.

https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal.md


## Connect to on-prem SQL 

- [Sync on prem database to Azure SQL](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-get-started-sql-data-sync)
- [Refresh PowerBI from On-Prem SQL via Data Gateway](https://docs.microsoft.com/en-us/power-bi/service-gateway-sql-tutorial)
- [Logic Apps SQL Server connector](https://docs.microsoft.com/en-us/azure/connectors/connectors-create-api-sqlazure)
