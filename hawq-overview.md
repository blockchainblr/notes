HAWQ is designed as a MPP SQL processing engine.

Breaks complex queries into small tasks and distributes them to MPP Query processing units for execution.

Designed to support highest level of performance and scalibility.
  
## Components of HAWQ System.

* HAWQ Master
* HAWQ Segment
* HAWQ Storage
* HAWQ Interconnect

### Points to note

- Basic unit of parallelism is the segment instance.
- Mulitple segment instances on commodity servers work together to form a single parallel query processing system.
- Each query submitted in hawq is optimized, broken into smaller components, and dispatched to segments that work together to deliver a sigle result set.
- Relational queries are executed in paralled across segments. i.e table scans, joins, aggregations, and sorts are executed in parallel.
- Data is transferred between components through a scalable User Datagram Protocol (UDP) interconnect in a dynamic pipeline.
- No single point of failure and supports full online recovery.

### HAWQ Master
- Entry point to the system.
- This is a database process that accepts client connections and processes the SQL commands issued.
- End users/client programs always interacts/connects through master.
- `global system catalog` resides in the master where the set of system tables that contain metadata about HAWQ system itself resides.
- Responsible for authenticating client connections, processing incoming SQL commands, distributes workload among segments, corordinates the results returned by each segment and presents the final results to the client program.

    ### Master Mirroring (redundancy and failover)
    - Backup or mirror of the master instance on a seperate host from the master node can be deployed.
    - This host serves as a *warm standby*
    - standby master is kept up to date by a *transaction log replication process*

### HAWQ Segment
- `segments` are units which process the individual data modules simultaneously.
- These are stateless.
- Gets the SQL resuest to along with the related metadata information to process from master.
- The metadata contains the HDFS url for the required table.
- Segments access the corresponding data using the HDFS url from metadata.

    ### Segment Failover
    - The segments are stateless. This ensures fast recovery and better availability.
    - Existing sessions during failover are automatically resigned to the remaining segments. 
    - Segments state is always verified by Fault Tolerance service.
    - All the sessions are automatically reconfigured to use the full computing power.
  
### HAWQ Storage
- Stores all table data, except the system tables, in HDFS.
- The metadata for each user table is stored on the master's local file system and table content in HDFS.

### HAWQ Interconnect
- `interconnect` is the networking layer of HAWQ.
- `interconnect` refers to inter-process communication between the segments, as well as network infrastructure on which this communication relies.
- Uses UDP to send messages over the network.
- Additional packet verification is done by HAWQ platform, which equivalents the reliability of TCP but the performance and scalability exceeds that of TCP.
    
    ### Interconnect Redundancy
    - By deploying dual Gigabit Ethernet switches on the network.
    - By deploying redundant Gigabit connection to hte HAWQ host(master and segment) servers.
