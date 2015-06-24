package core.index.build;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import com.google.common.collect.Maps;
import com.google.common.primitives.Ints;

import core.index.MDIndex;
import core.access.spark.SparkUpfrontPartitioner;
import core.index.key.CartilageIndexKey;
import core.index.robusttree.RobustTreeHs;

public class IndexBuilder {

	int bucketSize = 64*1024*1024;

	public void build(MDIndex index, CartilageIndexKey key, String inputFilename, PartitionWriter writer){

		long startTime = System.nanoTime();
		File f = new File(inputFilename);
		long fileSize = f.length();
		index.initBuild((int) (fileSize / bucketSize) + 1);
		InputReader r = new InputReader(index, key);
		r.scan(inputFilename);
		double time1 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Scanning and sampling time = "+time1+" sec");

		startTime = System.nanoTime();
		index.initProbe();
		double time2 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Build Time = "+time2+" sec");

		startTime = System.nanoTime();
		r.scan(inputFilename, writer);
		writer.flush();
		double time3 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Probe Time = "+time3+" sec");

		startTime = System.nanoTime();
		byte[] indexBytes = index.marshall();
		writer.writeToPartition("index", indexBytes, 0, indexBytes.length);
		writer.flush();

		byte[] sampleBytes = ((RobustTreeHs)index).serializeSample();
		writer.writeToPartition("sample", sampleBytes, 0, sampleBytes.length);
		writer.flush();

		double time4 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index+Sample Write Time = "+time4+" sec");

		System.out.println("Total time = "+(time1+time2+time3+time4)+" sec");
	}

	public void buildWithBlockSampling(double samplingRate, MDIndex index, CartilageIndexKey key, String inputFilename, PartitionWriter writer){

		long startTime = System.nanoTime();
		File f = new File(inputFilename);
		long fileSize = f.length();
		index.initBuild((int) (fileSize / bucketSize) + 1);
		InputReader r = new InputReader(index, key);
		r.scanWithBlockSampling(inputFilename, samplingRate);
		double time1 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Scanning and sampling time = "+time1+" sec");

		startTime = System.nanoTime();
		index.initProbe();
		double time2 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Build Time = " + time2 + " sec");

		startTime = System.nanoTime();
		r.scan(inputFilename, writer);
		System.out.println("2nd Scan Time = " + ((System.nanoTime() - startTime) / 1E9) + " sec");
		writer.flush();
		double time3 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Probe Time = "+time3+" sec");

		startTime = System.nanoTime();
		byte[] indexBytes = index.marshall();
		writer.writeToPartition("index", indexBytes, 0, indexBytes.length);
		writer.flush();

		byte[] sampleBytes = ((RobustTreeHs)index).serializeSample();
		writer.writeToPartition("sample", sampleBytes, 0, sampleBytes.length);
		writer.flush();

		double time4 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index+Sample Write Time = "+time4+" sec");

		System.out.println("Total time = "+(time1+time2+time3+time4)+" sec");
	}

	// files to sample are in a directory, rather than just a file
	// takes a precomputed number of buckets (since we don't know how big the files are in advance)
	public void buildWithBlockSamplingDir(double samplingRate, int bucketNum, MDIndex index, CartilageIndexKey key, String inputDirectory) {
		InputReader r = new InputReader(index, key);
		index.initBuild(bucketNum);
		System.out.println(inputDirectory);
		File[] files = new File(inputDirectory).listFiles();

		long startTime = System.nanoTime();
		for (File f : files) {
			r.scanWithBlockSampling(f.getPath(), samplingRate);
			r.firstPass = true;
		}
		double time1 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Scanning and sampling time = "+time1+" sec");

		startTime = System.nanoTime();
		index.initProbe();
		double time2 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Build Time = " + time2 + " sec");
	}

	// Doesn't really work
	public void buildWithSpark(double samplingRate, RobustTreeHs index, CartilageIndexKey key, String inputFilename, PartitionWriter writer, String propertiesFile, String hdfsPath){

		long startTime = System.nanoTime();
		File f = new File(inputFilename);
		long fileSize = f.length();
		index.initBuild((int) (fileSize / bucketSize) + 1);
		InputReader r = new InputReader(index, key);
		r.scanWithBlockSampling(inputFilename, samplingRate);
		double time1 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Scanning and sampling time = "+time1+" sec");

		startTime = System.nanoTime();
		index.initProbe();
		double time2 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Build Time = " + time2 + " sec");

		startTime = System.nanoTime();
		SparkUpfrontPartitioner partitioner = new SparkUpfrontPartitioner(propertiesFile, hdfsPath);
		partitioner.createTextFile(inputFilename, index.getRoot());
		double time3 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Probe Time = "+time3+" sec");

		startTime = System.nanoTime();
		byte[] indexBytes = index.marshall();
		writer.writeToPartition("index", indexBytes, 0, indexBytes.length);
		writer.flush();

		byte[] sampleBytes = index.serializeSample();
		writer.writeToPartition("sample", sampleBytes, 0, sampleBytes.length);
		writer.flush();

		double time4 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index+Sample Write Time = "+time4+" sec");

		System.out.println("Total time = "+(time1+time2+time3+time4)+" sec");
	}

	// given an index that has already been constructed, and a directory of files to partition,
	// writes out the appropriate partition files
	public void buildDistributedFromIndex(MDIndex index, CartilageIndexKey key, String inputDirectory, PartitionWriter writer){

		InputReader r = new InputReader(index, key);
		r.firstPass = false;
		File[] files = new File(inputDirectory).listFiles();

		long startTime = System.nanoTime();
		for (File f : files) {
			r.scan(f.getPath(), writer);
			writer.flush();
		}
		writer.flush();
		double time3 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Probe Time = " + time3 + " sec");
	}

	// Builds replicas with block sampling
	public void build(double samplingRate, int numBuckets, MDIndex[] indexes, CartilageIndexKey[] keys, String inputDirectory, PartitionWriter[] writers){

		long startTime = System.nanoTime();
		for(MDIndex index: indexes)
			index.initBuild(numBuckets);
		ReplicatedInputReader r = new ReplicatedInputReader(indexes, keys);

		File[] files = new File(inputDirectory).listFiles();
		for (File f : files) {
			r.firstPass = true;
			r.scanWithBlockSampling(f.getPath(), samplingRate);
		}
		double time1 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Scanning and sampling time = " + time1 + " sec");

		startTime = System.nanoTime();
		for(MDIndex index: indexes)
			index.initProbe();
		double time2 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Build Time = "+time2+" sec");

		startTime = System.nanoTime();
		for (File f : files) {
			r.scan(f.getPath(), writers);
		}
		for(PartitionWriter writer: writers)
			writer.flush();
		double time3 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index Probe Time = " + time3 + " sec");

		startTime = System.nanoTime();
		for (int i = 0; i < indexes.length; i++) {
			PartitionWriter writer = writers[i];
			RobustTreeHs index = (RobustTreeHs)indexes[i];
			byte[] indexBytes = index.marshall();
			writer.writeToPartition("index", indexBytes, 0, indexBytes.length);
			byte[] sampleBytes = index.serializeSample();
			writer.writeToPartition("sample", sampleBytes, 0, sampleBytes.length);
			byte[] infoBytes = keys[i].toString().getBytes();
			writer.writeToPartition("info", infoBytes, 0, infoBytes.length);
			writer.flush();
		}
		double time4 = (System.nanoTime()-startTime)/1E9;
		System.out.println("Index+Sample Write Time = "+time4+" sec");

		System.out.println("Total time = " + (time1 + time2 + time3 + time4) + " sec");
	}

	public void build(double samplingRate, int numBuckets, MDIndex index, CartilageIndexKey key, String inputFilename, PartitionWriter writer, int attributes, int replication) {
		int attrPerReplica = attributes / replication;

		Map<Integer, List<Integer>> replicaAttrs = Maps.newHashMap();
		for (int j = 0; j < attributes; j++) {
			int r = j / attrPerReplica >= replication ? replication - 1 : j / attrPerReplica;
			if (!replicaAttrs.containsKey(r))
				replicaAttrs.put(r, new ArrayList<Integer>());
			replicaAttrs.get(r).add(j);
		}

		MDIndex[] indexes = new MDIndex[replication];
		CartilageIndexKey[] keys = new CartilageIndexKey[replication];
		PartitionWriter[] writers = new PartitionWriter[replication];

		for (int i = 0; i < replication; i++) {
			try {
				keys[i] = key.clone();
				keys[i].setKeys(Ints.toArray(replicaAttrs.get(i)));
				indexes[i] = index.clone();
				writers[i] = writer.clone();
				writers[i].setPartitionDir(writer.getPartitionDir() + "/" + i);
				writers[i].createPartitionDir();
			} catch (CloneNotSupportedException e) {
				e.printStackTrace();
			}
		}

		build(samplingRate, numBuckets, indexes, keys, inputFilename, writers);
	}

}
