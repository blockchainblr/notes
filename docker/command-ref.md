Docker Command Reference
-------------------------
##### Version
Command to check docker engine and client versions.
```
$ docker version

Example:
$ docker version
Client:
 Version:      1.9.1
 API version:  1.21
 Go version:   go1.4.3
 Git commit:   a34a1d5
 Built:        Fri Nov 20 17:56:04 UTC 2015
 OS/Arch:      darwin/amd64

Server:
 Version:      1.9.1
 API version:  1.21
 Go version:   go1.4.3
 Git commit:   a34a1d5
 Built:        Fri Nov 20 17:56:04 UTC 2015
 OS/Arch:      linux/amd64
```

#### Docker info
```
$ docker info

Example:
$docker info
ontainers: 0
Images: 0
Storage Driver: devicemapper
 Pool Name: docker-202:64-31811-pool
 Pool Blocksize: 65.54 kB
 Backing Filesystem: extfs
 Data file: /dev/loop0
 Metadata file: /dev/loop1
 Data Space Used: 305.7 MB
 Data Space Total: 107.4 GB
 Data Space Available: 6.455 GB
 Metadata Space Used: 729.1 kB
 Metadata Space Total: 2.147 GB
 Metadata Space Available: 2.147 GB
 Udev Sync Supported: true
 Deferred Removal Enabled: false
 Data loop file: /var/lib/docker/devicemapper/devicemapper/data
 Metadata loop file: /var/lib/docker/devicemapper/devicemapper/metadata
 Library Version: 1.02.95-RHEL6 (2015-09-08)
Execution Driver: native-0.2
Logging Driver: json-file
Kernel Version: 2.6.32-573.12.1.el6.x86_64
Operating System: <unknown>
CPUs: 1
Total Memory: 590.1 MiB
Name: venkateshchensani-gmail-com1.mylabserver.com
ID: OQHY:O4SK:N5UT:HCAH:Y2H6:AEM2:KJOG:EBCT:3JGN:D5HI:KD5N:IY4T
```

#####Images
```
$ docker images

Example:
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
dry-run-test        latest              b8f97cbfce4f        43 seconds ago      2.065 GB
ubuntu              trusty              6cc0fc2a5ee3        3 weeks ago         187.9 MB
```
```
Options: 
```

#### Docker inspect 
```
$ docker inspect [image-name/id]

Example:
$ docker inspect ubuntu
[
{
    "Id": "8693db7e8a0084b8aacba184cfc4ff9891924ed2270c6dec6a9d99bdcff0d1aa",
    "Parent": "a4c5be5b6e596241b4530ade26294afa8d8a4a2b9163c30e36c87f879b0f5073",
    "Comment": "",
    "Created": "2016-01-19T23:31:24.889720757Z",
    "Container": "1351fd9fceb3cee2ceaa8fc342651f91ae84e445bfbb0d93f066dc34a36911c4",
    "ContainerConfig": {
        "Hostname": "dfc2eabdf236",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "PortSpecs": null,
        "ExposedPorts": null,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": null,
        "Cmd": [
            "/bin/sh",
            "-c",
            "#(nop) CMD [\"/bin/bash\"]"
        ],
        "Image": "a4c5be5b6e596241b4530ade26294afa8d8a4a2b9163c30e36c87f879b0f5073",
        "Volumes": null,
        "VolumeDriver": "",
        "WorkingDir": "",
        "Entrypoint": null,
        "NetworkDisabled": false,
        "MacAddress": "",
        "OnBuild": null,
        "Labels": null
    },
    "DockerVersion": "1.8.3",
    "Author": "",
    "Config": {
        "Hostname": "dfc2eabdf236",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "PortSpecs": null,
        "ExposedPorts": null,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": null,
        "Cmd": [
            "/bin/bash"
        ],
        "Image": "a4c5be5b6e596241b4530ade26294afa8d8a4a2b9163c30e36c87f879b0f5073",
        "Volumes": null,
        "VolumeDriver": "",
        "WorkingDir": "",
        "Entrypoint": null,
        "NetworkDisabled": false,
        "MacAddress": "",
        "OnBuild": null,
        "Labels": null
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Size": 0,
    "VirtualSize": 187899635
}
]
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

#### Docker machine status
```
$ docker-machine status <vm name>

Example:
$ docker-machine status default
Running
```

#### Docker environment
```
$docker-machine env <vm name>

Example
$ docker-machine env default
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/avinash/.docker/machine/machines/default"
export DOCKER_MACHINE_NAME="default"
# Run this command to configure your shell: 
# eval "$(docker-machine env default)"
```