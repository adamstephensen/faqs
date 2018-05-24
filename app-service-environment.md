## What is an App Service Environment (ASE) ?

> The main difference between App Service and App Service Environment (ASE) is that App Services run on a pre-built, shared tenant hyper scaled web farm, but ASEs are purpose built (on demand) web farms provisioned directly in your subscription that must be attached to a VNET. Because you can attach your ASE to a VNET, you can then apply Network Security Groups (NSG) to the VNET to prevent/allow traffic to flow to the ASE.
> Here is the page describing how to add the layered security to your ASE once you've built it:
> Layered Security Architecture with App Service Environments
> So with ASE you get the deployment/monitoring/management features of App Services, but with the network layer control of a VM.

> Source: https://stackoverflow.com/questions/39745892/how-can-i-set-up-a-private-web-app-on-azure-using-an-app-service-environment 

More reading: 
https://docs.microsoft.com/en-us/azure/app-service/environment/network-info


## What can I do with an ASE ?

- ASEs enable high-scale app hosting with secure network access. For more information, see the [AzureCon Deep Dive on ASEs](https://azure.microsoft.com/documentation/videos/azurecon-2015-deploying-highly-scalable-and-secure-web-and-mobile-apps/).
- todo: Multiple ASEs can be used to scale horizontally. For more information, see [how to set up a geo-distributed app footprint](https://docs.microsoft.com/en-us/azure/app-service/environment/app-service-app-service-environment-geo-distributed-scale).
- todo: ASEs can be used to configure security architecture, as shown in the AzureCon Deep Dive. To see how the security architecture shown in the AzureCon Deep Dive was configured, see the [article on how to implement a layered security architecture with App Service environments](https://docs.microsoft.com/en-us/azure/app-service/environment/app-service-app-service-environment-layered-security).
- todo: Apps running on ASEs can have their access gated by upstream devices, such as web application firewalls (WAFs). For more information, see [Configure a WAF for App Service environments](https://docs.microsoft.com/en-us/azure/app-service/environment/app-service-app-service-environment-web-application-firewall).

From <https://docs.microsoft.com/en-us/azure/app-service/environment/intro

## Where can I find resources about App Service Environment (ASE) and App Gateway ?

Check out this video from Scott Hanselman
https://azure.microsoft.com/en-us/resources/videos/azure-friday-ilb-ase-and-application-gateway-compy/

## What is 'Best Practice' with regards to ASEs ?
Note: everything on this site is purely my opinion - nothing is official. This is my take on it.

There is deliberately no single best practice for all customers with ASEs.
 
‘Best practice’ often relies on context.
 
‘Very Best Practice’ is to have a separate ASE per environment (e.g. dev+test+prod), but this obviously starts to get expensive.
 
‘Acceptable Best Practice’ for many organisations is to have a single ASE, and manage your environments with separate ASPs.
 
I also often see a ‘Compromise Best Practice’ where there are two ASEs.

- One for production
- One for all non-production environments

Many customers consider this a reasonable balance between cost and independence.

Cons: Different ARM templates for Dev/UAT and Prod.
 
I take several options to customers with a list of pros and cons, and a price comparison and let them decide.
 
