# Docker 101 - From Docker Getting Started

## Part 1 Docker Orientation
> based on https://docs.docker.com/get-started/

```
## List Docker CLI commands

# docker system prune # use with caution


docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world
docker run -it ubuntu bash
> cat /etc/os-release
> exit

## List Docker images
docker image ls


## List Docker containers (running, all, all in quiet mode - used to be 'docker ps')
docker container ls
docker container ls --all
docker container ls -aq

## pull and push images from container registry
docker pull
docker push

```

## Part 2 - Containers

Source: https://docs.docker.com/get-started/part2/

### Define a container with Dockerfile

#### Short Demo

```
docker build -t myhello .        # Create image using this directory's Dockerfile
docker run -p 4000:80 myhello    # Run "friendlyhello" mapping port 4000 to 80
docker run -d -p 4000:80 myhello         # Same thing, but in detached mode
docker login                           # Log in this CLI session using your Docker credentials
docker tag myhello adamstephensen/myhellot001:v1.0.0  # Tag <image> for upload to registry
docker push adamstephensen/myhellot001:v1.0.0            # Upload tagged image to registry
docker run adamstephensen/myhellot001:v1.0.0                   # Run image from a registry
```


#### Longer Demo

```
docker build -t friendlyhello .        # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello    # Run "friendlyhello" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker container ls                                # List all running containers
docker container ls -a                 # List all containers, even those not running
docker container stop <hash>           # Gracefully stop the specified container
docker container kill <hash>           # Force shutdown of the specified container
docker container rm <hash>             # Remove specified container from this machine
docker container rm $(docker container ls -a -q)         # Remove all containers
docker image ls -a                             # List all images on this machine
docker image rm <image id>             # Remove specified image from this machine
docker image rm $(docker image ls -a -q)   # Remove all images from this machine
docker login                           # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```