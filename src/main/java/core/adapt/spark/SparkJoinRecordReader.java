package core.adapt.spark;


import java.io.IOException;

import com.google.common.collect.ArrayListMultimap;
import core.common.globals.Globals;
import org.apache.curator.framework.CuratorFramework;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.TaskAttemptContext;

import core.adapt.HDFSPartition;
import core.adapt.iterator.IteratorRecord;
import core.adapt.iterator.PartitionIterator;
import core.adapt.spark.SparkJoinInputFormat.SparkFileSplit;
import core.utils.CuratorUtils;

/**
 * Created by ylu on 12/2/15.
 */


public class SparkJoinRecordReader extends
        RecordReader<LongWritable, IteratorRecord> {

    protected Configuration conf;

    protected SparkFileSplit sparkSplit;
    int currentFile;

    protected PartitionIterator iterator;

    ArrayListMultimap<Long, byte[]> hashTable;

    LongWritable key;
    long recordId;
    boolean hasNext;

    CuratorFramework client;

    @Override
    public void initialize(InputSplit split, TaskAttemptContext context)
            throws IOException, InterruptedException {
        conf = context.getConfiguration();
        client = CuratorUtils.createAndStartClient(conf
                .get(SparkQueryConf.ZOOKEEPER_HOSTS));

        sparkSplit = (SparkFileSplit) split;
        Path[] paths = sparkSplit.getPaths();

        System.out.println(">>> build hashtable from the following files: ");

        for(Path p : paths){
            System.out.println(p);
        }

        String joinCond = conf.get("JOIN_CONDITION");
        String tokens[] = joinCond.split("=");
        int join_attr1 = Integer.parseInt(tokens[0]);
        int join_attr2  = Integer.parseInt(tokens[1]);

        hashTable = ArrayListMultimap.create();

        iterator = sparkSplit.getIterator();



        currentFile = 0;
        hasNext = initializeNext();
        key = new LongWritable();
        recordId = 0;

        System.out.println("In SparkJoinRecordReader:" + Globals.schema);

        int count = 0;

        while(nextKeyValue()){
            IteratorRecord r = getCurrentValue();
            hashTable.put(r.getLongAttribute(join_attr1), r.getBytes());
            count ++;
        }

        System.out.println("There are " + count + " records!");

        if(true){
            throw new RuntimeException("");
        }
    }

    protected boolean initializeNext() throws IOException {
//		if (currentFile > 0)
//			System.out.println("Records read = " + recordId);

        if (currentFile >= sparkSplit.getStartOffsets().length)
            return false;
        else {
            Path filePath = sparkSplit.getPath(currentFile);
            final FileSystem fs = filePath.getFileSystem(conf);
            HDFSPartition partition = new HDFSPartition(fs, filePath.toString(),
                    Short.parseShort(conf.get(SparkQueryConf.HDFS_REPLICATION_FACTOR)),
                    client);
            System.out.println("INFO: Loading path: " + filePath.toString());
            try {
                partition.loadNext();
                iterator.setPartition(partition);
                currentFile++;
                return true;
            } catch (java.lang.OutOfMemoryError e) {
                System.out.println("ERR: Failed to load " + filePath.toString());
                System.out.println(e.getMessage());
                e.printStackTrace();
                return false;
            }
        }
    }

    @Override
    public boolean nextKeyValue() throws IOException, InterruptedException {
        while (hasNext) {
            if (iterator.hasNext()) {
                recordId++;
                return true;
            }
            hasNext = initializeNext();
        }
        /*
		 * do{ if(iterator.hasNext()){ recordId++; return true; } }
		 * while(initializeNext());
		 */

        // System.out.println("Record read = "+recordId);
        return false;
    }

    @Override
    public LongWritable getCurrentKey() throws IOException,
            InterruptedException {
        key.set(recordId);
        return key;
    }

    @Override
    public IteratorRecord getCurrentValue() throws IOException,
            InterruptedException {
        return iterator.next();
    }

    @Override
    public float getProgress() throws IOException, InterruptedException {
        return (float) currentFile / sparkSplit.getStartOffsets().length;
    }

    @Override
    public void close() throws IOException {
        iterator.finish(); // this method could even be called earlier in case
        // the entire split does not fit in main-memory
        // counter.close();
        // locker.cleanup();
    }
}
