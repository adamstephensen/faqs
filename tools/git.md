## how to rebase a commit on top of a fork
https://stackoverflow.com/questions/3611256/forking-vs-branching-in-github


## how to create a git repository from the command line 

    1. install [Hub](https://github.com/github/hub) by Github
    2. Create a new repository with ```hub create```. See [hub manual](https://hub.github.com/hub.1.html) for further information.

to install Hub

On Linux
```
$ brew install hub
$ hub version
git version 1.7.6
hub version 2.2.3
```

On Windows

```cmd
choco install hub
```



## how to keep a fork up to date 
(from https://gist.github.com/CristinaSolana/1885435 )

### 1. Clone your fork:

    git clone git@github.com:YOUR-USERNAME/YOUR-FORKED-REPO.git

### 2. Add remote from original repository in your forked repository: 

    cd into/cloned/fork-repo
    git remote add upstream git://github.com/ORIGINAL-DEV-USERNAME/REPO-YOU-FORKED-FROM.git
    git fetch upstream

### 3. Updating your fork from original repo to keep up with their changes:

    git pull upstream master

