from pyspark.sql import SparkSession
import os
import pickle
from enum import Enum
import pandas as pd

class DataHolderType(Enum):
    PANDAS = "pandas"
    SPARK = "spark"
    HADOOP = "hadoop"
    

class DataHolder:
    def load_data(self, data):
        raise NotImplementedError("load_data method must be implemented in subclasses")


class PandaDataHolder(DataHolder):
 def load_data(self, data):
        if isinstance(data, pd.DataFrame):
            return data  # If data is already a DataFrame, return it directly
        elif os.path.exists(data):
            # If data is a string, assume it's a file path and read it into a DataFrame
            return pd.read_csv(data)  # You can adjust this based on the file format
        elif isinstance(data, list):
            # If data is a list, assume it's a list of dictionaries and convert it to a DataFrame
            return pd.DataFrame(data)
        elif isinstance(data, dict):
            # If data is a dictionary, assume it's a hash and convert it to a DataFrame
            return pd.DataFrame.from_dict(data)
        else:
            raise ValueError("Unsupported data type")


class SparkDataHolder(DataHolder):
    _spark = None  
    # Class-level variable to hold the Spark session    
    def load_data(self, data):
        if SparkDataHolder._spark is None:
            SparkDataHolder._spark = SparkSession.builder \
                .appName("SparkLoader") \
                .getOrCreate()

        if isinstance(data, pd.DataFrame):
            # If data is already a DataFrame, convert it to a Spark DataFrame
            return SparkDataHolder._spark.createDataFrame(data)
        elif isinstance(data, str):
            # If data is a string, assume it's a file path and read it into a Spark DataFrame
            return SparkDataHolder._spark.read.format("csv").load(data)  # Adjust based on the file format
        else:
            raise ValueError("Unsupported data type")


class HadoopDataHolder(DataHolder):
    def load_data(self, ticker: str, start: str, end: str):
        pass


class DataHolderFactory:
    def get_DataHolderType(self, data_holder_type: DataHolderType) -> DataHolder:
        if data_holder_type == DataHolderType.PANDAS:
            return PandaDataHolder()
        if data_holder_type == DataHolderType.SPARK:
          return SparkDataHolder()
        else:
            raise ValueError(f"Unknown DataHolder={data_holder_type}, expected{DataHolderType.PANDAS.value} or {DataHolderType.SPARK.value}")
        

# # Register loaders
# DataDownLoaderMethodFactory.register_loader(DataDownLoaderType.PANDAS, PandasLoader)
# DataDownLoaderMethodFactory.register_loader(DataDownLoaderType.SPARK, SparkLoader)
# DataDownLoaderMethodFactory.register_loader(DataDownLoaderType.HADOOP, HadoopLoader)

