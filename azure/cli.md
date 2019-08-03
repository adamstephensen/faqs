

### Extra special warning
All my guides are to be used at your own risk.
The commands on this page are extra risky.
Please assume that they are wrong and likely to ruin your life....
... but check them out anyway.

## CLI Doco
Here is the reference to all the CLI doco
https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest



## Common Commands

```
# login
az login

# list all subscriptions
az account list

# show current subscriptoin
az account show


```



## How can I run the cli from a docker container

Source: https://docs.microsoft.com/en-us/cli/azure/run-azure-cli-docker?view=azure-cli-latest

```bash
# download the docker image and run it interactively
docker run -it mcr.microsoft.com/azure-cli

# run the cli
az login

# update the docker image
docker pull mcr.microsoft.com/azure-cli

```



## Where do I find out about the Azure CLI ?
You can find out about it here
https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest

## How do I delete a resource group

```
az group delete -n MyResourceGroup --no-wait
```


