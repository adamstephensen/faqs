
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
