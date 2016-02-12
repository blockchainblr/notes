#Docker
Docker is a platform for developing, shipping and running applications using container virtualization technology.

More information regarding containers can be found at XXXX location

### Terminology
Image
> Image is the filesystem snapshot or tarball.

Container
> Container is an image when it is run.

Host Management
> Process of setting up(provisioning) a physical server or virtual machine so that it's ready to run docker container

Orchestration
> Orchestration is the controller process that decides where containers should run and how to let the cluster know about the available services.

Scheduling
> Deciding which containers can run on which hosts given resource constraints like CPU, memory, and IO.

Discovery
> The process of how a container exposes a service to the cluster and discovers how to find and communicate with other services.

#### When is docker best utilized?

* Best utilized only when application code is pre-packaged into a Docker image. i.e., The image contains all the application code as well as runtime dependencies and system requirements.
* Configuration files containing database credentials and other secrets are often added to the image at runtime rather than being built into the image.


### Docker Stack
* Docker Engine
* Docker Swarm
* Docker Compose
* Docker Hub
* Docker Trusted Registery
* Docker Cloud
* Docker Machine
* Docker Toolbox
* Docker Registry
* Docker Notary

These docker components will address the following concerns:
* Build system
* Image repository
* Host Management
* Configuraion management
* Deployment
* Orchestration
* Logging
* Monitoring