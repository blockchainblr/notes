Docker Command Reference
-------------------------
##### Version
Command to check docker engine and client versions.
```
$ docker version
```

> 
```
Example: 
```

#####Images
```
$ docker images
```
```
Options: 
```

> 
```
Example:
```

#### Docker Run
```
$ docker run [options] [image] [command] [args]
```

#### PS 
Command to list containers
```
$ docker run ps
```

#### Commit
Saves changes in a container as a new image
```
$ docker commit [container-id] [name]
```

#### Delete Containers
```
$ docker rm [container-id]
```

#### Delete local images
```
$ docker rmi [image-id]
```

#### Push
```
$ docker push [repo:tag]
```

#### tag
```
$ docker tag [image-id] [repo:tag]
```
