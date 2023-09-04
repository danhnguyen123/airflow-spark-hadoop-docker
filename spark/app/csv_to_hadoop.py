import sys
import pyspark
from pyspark.sql import SparkSession
from modules import moduleExample

spark = SparkSession.\
        builder.\
        config("spark.executor.memory", "512m").\
        config("spark.eventLog.enabled", "true").\
        config("spark.eventLog.dir", "hdfs://namenode/shared/spark-logs").\
        config("spark.history.fs.logDirectory", "hdfs://namenode/shared/spark-logs").\
        getOrCreate()

#Create PySpark DataFrame from Pandas
csv_file = sys.argv[1]

df=spark.read.format("csv").option("header","true").load(csv_file)

df_csv_sample = moduleExample.pysparkFunctions.sample_df(df, 0.1)

# Applying the python function. We don't need to create UDF in spark since spark version 3.1
df_csv_sample = df_csv_sample.withColumn("uuid", moduleExample.pythonFunctions.generate_uuid())

df_csv_sample.show()

df_csv_sample.write.option("header",True) \
        .partitionBy("success_ekyc") \
        .mode("overwrite") \
        .parquet("hdfs://namenode/sales")

print("Dataframe stored in Hadoop.")
        # config("spark.driver.host", "localhost").\
        # config("spark.eventLog.enabled", "true").\
        # config("spark.eventLog.dir", "hdfs://namenode/shared/spark-logs").\
        # config("spark.history.fs.logDirectory", "hdfs://namenode/shared/spark-logs").\

        # config("spark.executor.memory", "512m").\
        # config("spark.eventLog.enabled", "true").\
        # config("spark.eventLog.dir", "hdfs://namenode/shared/spark-logs").\
        # config("spark.history.fs.logDirectory", "hdfs://namenode/shared/spark-logs").\