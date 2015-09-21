## SQL ON HADOOP

#### HIVE
* Developed by Facebook
* HiveQL language is not compatible with ANSI SQL-92


#### IMPALA
* Developed by Cloudera
* Written in C++
* Supports HiveQL and Full ANSI SQL-92 support
* Does not use Map-Reduce
* Requires more memory

#### Stinger
* Hortwonworks initiative to make hive run 100x faster.
* Tez - is the solution by hortonworks. Hive queries are translated to Tez jobs, similar to mapreduce jobs by may use arbitrary topology.
* Optiq - Cost based query optimizer for Hive
* ORCFile - Columnar storage format with adaptive compression and inline indexes.
* Hive-5317 -- Acid and Update/Delete Support.

#### HAWQ
* A product of Pivotal
* Written in C.
* Greenplum MPP DBMS solution is ported to store data in HDFS.
* Supports ANSI SQL-92 and analytic extensions from SQL-2003
* Supports several complex queries with corelated sub-queries, window functions and different joins.

#### VERTICA
* By HP Vertica.
* Supports only MapR distribution.
* Supports ANSI SQL-92, SQL-2003
* Solution is similar to HAWQ as general idea.

#### IBM BigSQL v3
* IBM DB2 is ported to store data in HDFS.
* Federated queries, good query optimizer, etc.
* This solution is similar to HAWQ as general idea.

#### Spark SQL
* Module for working with structured data.
* Integrates SQL quries with Spark programs
* Easy to connect to any data source for Uniform data access.
* Full Hive Compatibility
* Includes cost-based optimizer, columnar storage and code generation to make queries fast.
 
#### Splice Machine
* Provides the Hadoop RDBMS.
* Supports standard ANSI SQL
* Auto-sharding of HBase.
* Real-time updates with Transactional Integrity.
* Distributed Parallelized Query Execution
* High Concurrency
