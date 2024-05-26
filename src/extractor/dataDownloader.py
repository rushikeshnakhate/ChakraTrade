import sys
import os

# Ensure the project root directory is in sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from extractor.dataSource import DataSourceFactory
from extractor.dataSource import DataSourceType
from extractor.dataHolder import DataHolder , DataHolderFactory
from utils.config_manager import get_config_manager_singleton

import pickle
import os
from datetime import date
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


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
        cache_file_name =  "_".join(str(arg) for arg in args if not isinstance(arg, Path))
        data_dir = get_config_manager_singleton().project.data_dir
        return os.path.join(data_dir, cache_file_name)
    

class DataDownloader:
    def __init__(self, source: DataSourceType, data_holder : DataHolder):
        self.data_source = DataSourceFactory().get_DataSource(source)
        self.data_holder = DataHolderFactory().get_DataHolderType(data_holder)

    def get_data(self, *args ):
        cache_name = DataCacheManager.generate_cache_name(*args)
        data = DataCacheManager.load_from_cache(cache_name)
        logging.info(f"cache_name={cache_name}") 

        if data is None:      
            data = self.data_source.get_data(*args)
            DataCacheManager.save_to_cache(data, cache_name)
        return self.data_holder.load_data(data)
        
        
