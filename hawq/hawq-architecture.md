Pivotal HD Architecture comprises of 
* Apache opensource Components
* Pivotal Ad-on components - HAWQ(Advanced Database services), PXF, GemFire XD(Real-time database services), Command Center and ICM, GraphLab and Hamster
*   * Command Center - Command line and web-based tool for installing, managing and monitoring the Pivotal HD cluster
*   * Hamster - Framework that enables users runnng MPI programs on Apache Hadoop YARN platform.
*   * HAWQ - Parallel SQL database and query engine on Hadoop
*   * PXF - Extension framework for external tables support to access external data formats includeing HDFS, HBase and Hive
*   * GraphLab - Graph-based, high performance, distributed computation framework for designing and implementing parallel algorithms in machine learning.
*   


## HAWQ Architecture

* HAWQ Master
*   * No user data
*   * Contains Global System Catalog
*     - System tables that contain HAWQ metadata
*   * Authenticates client connections, process SQL, distributes work between segments, co-ordinates results returned by segments, presents final results.
*       --  Parser
*       -- Query Optimizer
*       -- Local TM
*       -- Dispatch
*       -- Query Executor
*       -- Catalog
*       -- Local Storage
*       

* HAWQ Segments
*   - Segment is a unit of parallelism
*   - Segments are stateless, i.e does not store database and table metadata.
*   - Segments communicate with NameNode to obtain block lists where data is located.
*   - Segments access data stored in HDFS.
*   


* HAWQ Parser -- enforces the sql syntax, and converts the SQL into a parse tree structure descrbing the query.
* Query Optimizer -- Converts the SQL into physical execution plan.
* A cost optimizer considers multiple plans and looks for the most efficient plan.
* The physical plan contains all the query operations like sort, agg. scan, etc
* This global planning avois sub-optimal SQL pushing to segments and directly inserts motion nodes for intersegment communiction and efficient non local join processing
* 
HAWQ Master dispatches the query to executior plan to query executor along with a plugable meta-data.

A query executor or worker process is responsible for code cleaning its portion on work and communicating its results to other worker processes.

For each slice in the query plan, there is atleast one worker process assigned. It works on its signed portion of the query pla independently.

During query execution each segmetn will have a number of worker processes working in parallel. 

Related worker process across segments that are working on the same portion the qyuer plan is referred to as a gain.

HAWQ interconnect provides inter-process-communication between hawq segments. It is ethernet that uses UDP.

(Add udp details)

## HAWQ dynamic pipelining

* is a core execution fw that enables parallel data flow. No intermediate materialization is performed. 
* 
Upstream to downsteream data transfer.






* HAWQ Standby Master
* NameNode
* DataNode
