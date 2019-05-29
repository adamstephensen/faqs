### Option 1: Default Optoin - PaaS
- Your default option -> File | new | Web App | PHP

How easy was that!  
If you are running any of this massive list… your migration can be that easy !  

### Option 2: Legacy apps into containers

What about if you have terrible legacy app? I had a government department with an unsupported version of PHP, 
no budget or appetite to modernise as the app is only used internally.  
Solution: Added a Docker file – deployed to Container Web App. Done.

### DevOps Projects - It's not (really) cheating
You don’t know containers ? Not a problem. I’m going to make it easy for you -> File | New | DevOps Project | PHP | Simple PHP | PHP for Containers.  
(Explain while building) Guess what this is doing… Brief description of creating repo | container registry | build and release pipelines.  
Open PHP repo and show the dockerfile. Explain that you put this in any old project and you get a container that will run in Azure  
What about if you have a whole lot of services that you want to move into containers in Azure ?  

### Kubernetes 
2 min Kubernetes exalanationFile | New | DevOps Project | .NET Core | K8s  
Explain that this is spinning up a cluster. Show the app, the build and release pipelines.
Want to reduce operational costs ? accelelerate development with tooling designed for cloud native apps ? -> Serverless
Quick Azure Functions Demo
Note: The official version of this slide has Service Fabric – I deleted it.

While lift and shift to IaaS is a viable path to the cloud for many applications, this route will not unlock all possible cloud benefits.
If you are looking to get the most from the cloud and tap into advanced capabilities like improved resiliency, 
global scale or maximum agility, cloud native applications are built from the ground up and optimized for cloud scale and performance.
They’re based on microservices architectures, use managed services, and take advantage of continuous delivery to achieve reliability and faster time to market.

### Surrounding an existing/legacy application with modern functionality
- e.g. surrounding a legacy app with functions or cog servics


