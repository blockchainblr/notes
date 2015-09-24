## PXF - Pivotal Extension Framework

* Fast, extensible framework that allows HAWQ to query external system data.
* Supported sources are `HDFS, HBase, Hive and GemFire`
* API to enable custom connector development for any data source is available.
* Can write data to HDFS
  - Supported formats are `delimited text, csv, Sequence`
  - Various compression codecs and options.

### PXF Components
* Fragmenter
  * Present on the Namenode
  * Metadata of data source(blocks and location) is passed back to hte HAWQ Master by the Fragmenter
* Accessor
  * Responsible for reading specific data fragments and passing them to the resolver
* Resolver
  * De-serializes the records and serializes them into list of one field objects.
  * One field objects converted into GPDBWritable that can be read by HAWQ
* Analyzer
  * Responsible for collecting statistics on external table data that can be used by HAWQ optimizer.

### PXF Differentiators
* Utilizes HAWQ fast parallel optimizer
* Applies data locality optimizations to reduce resources and network traffic.
* Extensible framework
* Support ANALYZE for gathering HDFS file statistics and having it available for the query planner at runtime

### Usecases
* Using SQL query functionality from HAWQ on HDFS, HBase, or Hive data without materialization into HAWQ
* Join dimensions stored tables stored in HAWQ with HBase fact tables.
* Fast ingest of high value processed data from HDFS, HIVE or HBase data into HAWQ.


### Syntax
` CREATE EXTERNAL TABLE foo ()
LOCATION ('pxf://<host:port>/<data source>?<plugin options>')
FORMAT '<type>'(<params>)`


### Examples
#### HDFS
-- Table is created

#### HBase

`CREATE EXTERNAL TABLE hbase_sales (
  recordkey bytea,
  "cf1:saleid" int,
  "cf3:comments" varchar
) LOCATION ('pxf://uri:port/sales?profile=HBase')
FORMAT 'custom' (formatter='gpxfwritable_import')`

#### Unloading data from HAWQ to HDFS (EXPORT)
`CREATE WRITABLE EXTERNAL TABLE ...
LOCATION ('pxf://<host:port>/sales?profile=HdfsTextSimple&COMPRESSION_CODEC=org.apache.hadoop.io.compress.GzipCodec')
FORMAT 'text'(delimiter ',');`
