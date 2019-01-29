## I don't understand Kubuernetes. What can I do ?
Watch this. It is awesome.

https://azure.microsoft.com/en-us/resources/videos/the-illustrated-children-s-guide-to-kubernetes/



## What is the big deal about containers.
"portability and consistency regardless of the platform that it is running on." - Build Keynote

You compile your code, build a container and then know it is going to work in dev / test / prod and even on an IOT device.

Scenario: You test your app using Python 2.7 in development, and then it's going to run on Python 3 in production and something weird will happen. Alternatively - you have an old application that you would like to put on PaaS... but it's on an old unsupported version of Python - but you don't want to have to maintain a virtual machine to host an old version of Python.

Or you rely on the behavior of a certain version of an SSL library and another one will be installed. 
You'll run your tests on Debian and production is on Red Hat and all sorts of weird things happen.

Customers need a way of bundling an entire runtime environment: an application, plus all its dependencies, libraries and other binaries, and configuration files needed to run it so that differences in OS distributions and underlying infrastructure are abstracted away. This way they can spend more  time writing their apps than worry about underlying infrastucture and migration.

 
## I heard there was an awesome book on Containers and Microservices ?  
.NET Microservices - Architecture for Containerized .NET Applications' Guide/eBook
This is the free book on Microservices architecture. It will answer most of your questions about how and why.
 
It is available from here https://www.microsoft.com/net/learn/architecture  (under Microservices & Docker - Architecture e-book)
There is a pdf download, and even better a code repository on GitHub with a sample solution. 

The update notes from just 2 weeks ago are here: https://blogs.msdn.microsoft.com/dotnet/2017/08/02/microservices-and-docker-containers-architecture-patterns-and-development-guidance/

## How do I create a CI/CD pipeline for ACS ?

Creating a CI/CD pipeline on Azure Container Services with Kubernetes and Visual Studio Team Services
https://dgkanatsios.com/2017/05/29/creating-a-cicd-pipeline-on-azure-container-services-with-kubernetes-and-visual-studio-team-services/


## How do I deploy a Docker container using the Azure portal ?
https://docs.microsoft.com/en-gb/azure/container-service/dcos-swarm/container-service-deployment


## Where can I find out stuff about Docker in general ?

https://github.com/dotnet/dotnet-docker-samples/blob/master/dotnetapp-selfcontained/Dockerfile
https://kubernetes.io/docs/home/

## Where can I get an AKS walkthrough ? 

https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough





# Where can I find resources


Check out this video on Kubernetes best practices
["Best Practices with Azure & Kubernetes"](
https://developer.microsoft.com/en-us/events/build/content/best-practices-with-azure-kubernetes) from Build 2018

Also here was a list of great resources everyone provided for learning Kubernetes:

### Books: (Available On aka.ms/safari)
- Designing Distributed Systems — Brendan Burns
- Kubernetes In Action — Marko Luksa
- Managing Kubernetes — Brendan Burns and Craig Tracey
- Kubernetes Cookbook — Sebastien Goasäuen
- Kubernetes For Developers — Joseph Hack
- Prometheus Up and Running — Brian Barazil
- Istio In Action (MEAP) — Christian E. Post

### Videos and YouTube Channels:
- Lachlan Evenson (aka Crocodile Dundee Of Kubernetes) https://www.youtube.com/channel/UCC5NsnXM2lE6kKfJKdQgsRQ
- TGI Kubernetes by Heptio - https://www.youtube.com/channel/UCjQU5ZI2mHswy7OOsii_URg/videos
- Linux Foundation CKA (Must Register With MSFT For Free Access) https://lms.quickstart.com

### Hands-On:
- Kubernetes BootCamp - https://kubernetesbootcamp.github.io/kubernetes-bootcamp/index.html
- Katacoda Labs - Kubernetes https://katacoda.com/courses/kubernetes
- Katacoda Labs - Docker https://katacoda.com/courses/docker
- Azure Citadel - https://azurecitadel.github.io/
- GBB Azure Kubernetes Hackfest – 

### Large curated list of resources:
- https://github.com/ramitsurana/awesome-kubernetes




# Unsorted links on ACS AKS and Containers

Understand the future of software development in the cloud with the Azure Application Platform
https://channel9.msdn.com/events/Ignite/2016/BRK2085-TS?term=understand%20the%20future%20of

Azure Microservices presentation
https://azure.microsoft.com/en-us/solutions/microservice-applications/

Azure functions on Linux Containers
https://blogs.msdn.microsoft.com/appserviceteam/2017/11/15/functions-on-linux-preview/

https://github.com/Azure/aci-connector-k8s
https://hub.docker.com/r/microsoft/aci-connector-k8s/
https://azure.microsoft.com/en-au/pricing/details/container-instances/
https://azure.microsoft.com/en-au/resources/videos/using-kubernetes-with-azure-container-instances/


Github repo https://github.com/dotnet-architecture/eShopOnContainers
Online version of book https://aka.ms/microservices-guide-online-msft-docs

The App Service Web Application Reference Architecture (for scalability)

Here is a the Microsoft guidance on a scalable web app. https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/scalable-web-app 


## k8s failure stories
https://srcco.de/posts/kubernetes-failure-stories.html *todo*
