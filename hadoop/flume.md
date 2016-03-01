Flume
-----

* Event based ingestion tool
* Components: 
	1. source(s)	- defines how data is to be read from the upsteram provider
	2. sink(s)		- defines how data should be written downstream
	3. channel(s)	- defines how data is stored between the source and sink.
		- Channel types: 
			Memory 
		and File based -- this implements a write-ahead log that is persisted to stable storage as each event is put into the channel.(calcultes checksum and stores along with the event)

** Flume agent contains the code for sources, sinks and channels.
** Flume agents can be connected to each other. i.e sink of one agent connects to source of other agent
** Flume agents are Java processes that transfer events
 - event is the smallest unit of data that flows through flume.

** Source can either pull events from the external source or it can have events pushed to it by the external sources.

** Data integrity
** Availability - failure handline, load balancing.


================================================================
Reporting / Monitoring / Security / Load Balancing is supported
================================================================


Security / Confidentiality
--------------------------

Unauthorized access to data as it transits the network, Flume supports enabling SSL encryption on Sink.

** Can setup trusted policies to ensure that a sink is only sending data to a trusted source.

i.e Flume is configured with SSL certificates


** In addition to protecting data over the wire, we need to ensure that data is encrypted on the drives where Flume writes events as they transit a channel.

Flume offers the ability to encrypt the logfiles used by the file channel. (Current implementation supports AES encryption).
*** Called on-disk encryption




Reference: https://www.safaribooksonline.com/library/view/Hadoop+Security/9781491900970/ch10.html#securing_data_ingest






Source types
-------------
Avro 
	listenes on Avro port and receives events from external Avro client streams
Thrift
	Listenes on Thrift port and receives events from external Thrift client streams
Exec Source 
	Runs a given Unix command on start-up and expects that process to continuously produce data on standart out.
JMS Source
	Reads messages from a JMS destination such as a queue or topic.
Spooling Directory Source 
	Lets ingest data by placinf files to be ingested into a "spooling" directory on disk.
Kafka Source 
	Kafka consumer that reads messages from a Kafka topic.
NetCat Source 
	Listenes on a given port and turns each line of text into an event
Sequence Generator Source
	Continuously generates events with a counter that starts from 0 and increments by 1
Syslog Source
Syslog TCP Source
Multi-port Syslog TCP Source
Syslog UPD Source
HTTP Source 
	Accepts Flume events by HTTP POST and GET. HTTP requests are converted into flume events by a pluggable "handler" which must implement the HTTPSourceHandler interface.

Stress Source
Legacy Source
Avro Legacy Source
Thrift Legacy Source


Custom Source
	Own implementation of the Source interface. The custom source's class and its dependencies must be included in the agent's class path when starting the Flume agent.

Scribe Source


Sink Types
---------
HDFS Sink
	- Supports Creating Text and Sequence files only
	- Compression allowed in both file types
	- Files can be rolled periodically
	- Buckets/partitions data

HIVE Sink
	- Streams events directly into a Hive table or partition
	- Event are written using Hive transactions

Logger Sink
Avro Sink
Thrift Sink
IRC Sink
File Roll Sink
Null Sink
HBase Sink
MorphlineSolr Sink
Kafka Sink
Custom Sink
etc


Channels
----------
Memory Channel
JDBC Channel (Support only Derby)
Kafka Channel
File Channel
Spillable Memory Channel
Custom Channel

Channel Selectors
-----------------
Replicating Channel Selector
Multiplexing Channel Selector
Custom Channel Selector

Sink Processors
---------------------
Default Sink Processor
Failover Sink Processor
Load balancing Sink processor
Custom Sink processor


Event Serializers
------------------
Body Text Serializer
Avro Event serializer


Interceptor
-----------
Timestamp Interceptor
Host Interceptor
Static Interceptor
UUID Interceptor
Morphline Interceptor
Search and Replace Interceptor
Regex Filtering Interceptor
Regex Extractor Interceptor