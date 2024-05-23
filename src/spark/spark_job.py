from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
  .appName("Download Data") \
  .getOrCreate()

# # Download data from jugad_data library
# data = spark.read.format("jugad_data") \
#   .option("url", "your_data_url") \
#   .load()

# # Perform operations on the downloaded data
# # ...

# # Stop the SparkSession
# spark.stop()