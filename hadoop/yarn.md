## YARN Terminology
Resource Manager
> Master daemon that is responsible for controlling YARN submission authorization, resource limits, and application master assignment.

Node Manager
> Worker daemon that is responsible for executing application masters, as well as application tasks.

Container
> Bucket of resources that a unit of work(task) will be all allocated for execution. Container resources are CPU cores and memory
Vcore
> Virtual CPU core, which is a logical unit of processing power. Typically equivalent to a physical CPU core or HyperThreaded virtual CPU core.

Application Master
> Responsible for co-ordinating all resource requirements for a given YARN application. The ApplicationMaster is executed on a different NodeManager for every application. ApplicationMasters are responsible for requesting container allocations from the ResourceManager for application tasks to run.