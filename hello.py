from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("oci-test-dataflow").getOrCreate()

data = [("hello", "world"), ("oci", "dataflow")]
df = spark.createDataFrame(data, ["key", "value"])
df.show()

spark.stop()