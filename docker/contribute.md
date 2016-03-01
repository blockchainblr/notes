Setup for Engine Development
----------------------------

Required software
* Git
* make
* docker

Steps:
======
1. Fork and clone the Docker code
>
```
$ cd repos
$ git clone https://github.com/davinashreddy/docker.git docker-fork
$ cd docker-fork
```

2. Setup upstreame remote
>
```
$ git remote add upstream https://github.com/docker/docker.git
$ git remote -v
```

3. Create and push a branch
>
```
    $ cd docker-fork
    $ git checkout -b dry-run-test
    $ git branch
After making changes
    $ git add <changed files>
    $ git commit -s -m "Commit message"
Push changes to github
    $ git push --set-upstream origin dry-run-test
```

4. Working with docker development container
>
```
Remove unnessary artifacts by verifying using
    $ docker ps
Verify that host has no dangling images
    $ docker images
Remove dangling images if exists using
    $ docker rmi -f $(docker images -q -a -f)
    
```


