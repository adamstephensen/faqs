
## Create an AKS Cluster
```
GROUP_NAME=<aks-resource-group-name>
AKS_NAME=<aks-resource-name>
az group create -n $GROUP_NAME -l <azure-region>
az aks create -n $AKS_NAME -g $GROUP_NAME -k 1.11.6 --generate-ssh-keys 
az aks get-credentials -n $AKS_NAME -g $GROUP_NAME
kubectl get nodes
```

## delete the resource group
```
az group delete -n <aks-resource-group-name>
```


## Quickstart: Deploy an Azure Kubernetes Service (AKS) cluster using the Azure CLI
based on https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough
build the app tutorial: https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-app?WT.mc_id=none-github-nepeters
srouce code for the app: https://github.com/Azure-Samples/azure-voting-app-redis


```
docker run -it mcr.microsoft.com/azure-cli

az login
clear
az account list
az account show

# If required set the correct account
# az account set --subscription <subscription_id> 

RESOURCEGROUP="adams-k8s-demo1"
echo $RESOURCEGROUP
az group create --name $RESOURCEGROUP --location australiaeast

### Create the AKS Cluster  ###
#   ith Azure Montiro for containers enabled
az aks create \
    --resource-group $RESOURCEGROUP \
    --name myAKSCluster \
    --node-count 1 \
    --enable-addons monitoring \
    --generate-ssh-keys

### Connect to the cluster ###

# install Kubectl locally
az aks install-cli

# configure kubectl to connect to the cluster -> downloads creds and configures kube CLI to use them
az aks get-credentials --resource-group $RESOURCEGROUP --name myAKSCluster

# confirm connection by returning a list of nodes
kubectl get nodes

### Run the application ###

# download the K8s manifest file. it defines the desired state for the cluster.
# this manifest includes 2 K8s deployments -> one for the sample python apps, and one for a Redis instance.
# two K8s services are also created - internal service for Redis, external service to Azure Vote app 

wget -O azure-vote.yaml bit.ly/k8s-azure-vote-yaml
cat azure-vote.yaml

# deploy the appy
kubectl apply -f azure-vote.yaml

kubectl get service azure-vote-front --watch

# navigate to the external ip address when it appears

# monitor health and logs
# In the portal, open the cluster and choose 'Monitoring', 'Insights'
# Choose '+ Add Filter', 'Namespace' and '<all but kube-system>'
# choose to view Containers'
# Choose 'View in analytics', 'View Container Logs'

# tidy up
az group delete --name $RESOURCEGROUP --yes --no-wait
# delete the created AAD service principal separately as per [considerations](https://docs.microsoft.com/en-us/azure/aks/kubernetes-service-principal#additional-considerations)
az ad sp delete --id $(az aks show -g $RESOURCEGROUP -n myAKSCluster --query servicePrincipalProfile.clientId -o tsv)

```
