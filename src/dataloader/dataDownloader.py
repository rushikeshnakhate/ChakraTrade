from .dataSource import DataSource
from .dataSource import DataSourceFactory
from .dataSource import DataSourceType
from .dataHolder import DataHolder , DataHolderFactory
import pickle
import os
from datetime import date
from pathlib import Path

class DataCacheManager:
    @staticmethod
    def load_from_cache(cache_name: str):
        cache_file = f"{cache_name}.pkl"
        if os.path.exists(cache_file):
            with open(cache_file, "rb") as f:
                return pickle.load(f)
        else:
            return None

    @staticmethod
    def save_to_cache(data, cache_name: str):
        cache_file = f"{cache_name}.pkl"
        with open(cache_file, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def generate_cache_name(*args):
        return "_".join(str(arg) for arg in args if not isinstance(arg, Path))
    

class DataDownloader:
    def __init__(self, source: DataSourceType, data_holder : DataHolder):
        self.data_source = DataSourceFactory().get_DataSource(source)
        self.data_holder = DataHolderFactory().get_DataHolderType(data_holder)

    def get_data(self, *args ):
        cache_name = DataCacheManager.generate_cache_name(*args)
        data = DataCacheManager.load_from_cache(cache_name)

        if data is None:      
            data = self.data_source.get_data(*args)
            DataCacheManager.save_to_cache(data, cache_name)
        return self.data_holder.load_data(data)
        
        
