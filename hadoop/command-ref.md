### HDFS commands
#### put & get
``put`` and ``get`` are used to insert and retrieve data to/from HDFS
```
    $ hdfs dfs -put <src> <dst>
    $ hdfs dfs -get <src> <dst>
```

#### ls
Lists the directories under specified location
```
    $hdfs dfs -ls <path>
```

#### tail
Prints the contents of last ``n`` lines on console
```
$ hdfs dfs -tail [n] <filename>
```


#### HDFS Set Quota
```
$ hdfs dfsadmin -setSpaceQuota <N>  <filename>

N is in bytes
```


#### HDFS Get Quota
```
$ hadoop fs -count -q /path/to/directory
  QUOTA  REMAINING_QUOTA     SPACE_QUOTA  REMAINING_SPACE_QUOTA    DIR_COUNT  FILE_COUNT      CONTENT_SIZE FILE_NAME
   none              inf  54975581388800          5277747062870   
```


## Submitting a job to specific pools in MR2
#####Map Reduce
``` 
Property: mapreduce.job.queuename=<pool-name>
Usage: yarn jar <jar-location> <classname> -Dmapreduce.job.queuename=<pool-name> <input> <output>
```
#####Hive
```
Prpoerty: mapred.job.queue.name=<pool-name>
Usage: beeline> SET mapred.job.queue.name=<poolname>;
       beeline> ## Hive statement
```
#####Spark
```
Property: mapreduce.job.queuename=<pool-name>
Usage: spark-submit --class <class-name> --master yarn-cluster --queue <queue-name> <jar> <input> <output>
```

#####Impala
```
Property: REQUEST_POOL=<pool-name>
Usage: impala-shell> SET REQUEST_POOL=<poolname>;
impala-shell> ## Impala statement
```


## Kerberos
#####Creating Keytabs using username and password - works in windows machine
```
$ ktab -a <principal@relm> [<password>] -k <keytab-location>
```
