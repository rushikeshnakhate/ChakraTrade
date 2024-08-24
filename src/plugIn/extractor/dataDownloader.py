import logging
import os
import pickle
from pathlib import Path

from src.plugIn.extractor.dataHolder import DataHolderFactory, DataHolderType
from src.plugIn.extractor.dataSource import DataSourceType, DataSourceFactory
from src.core.utils.config_manager import get_config_manager_singleton

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
        cache_file_name = "_".join(str(arg) for arg in args if not isinstance(arg, Path))
        data_dir = get_config_manager_singleton().project.data_dir
        return os.path.join(data_dir, cache_file_name)


class DataDownloader:
    def __init__(self, source: DataSourceType, data_holder: DataHolderType):
        self.data_source = DataSourceFactory().get_data_source(source)
        self.data_holder = DataHolderFactory().get_DataHolderType(data_holder)

    def get_data(self, *args):
        cache_name = DataCacheManager.generate_cache_name(*args)
        data = DataCacheManager.load_from_cache(cache_name)
        logging.info(f"cache_name={cache_name}")

        if data is None:
            data = self.data_source.get_data(*args)
            DataCacheManager.save_to_cache(data, cache_name)
        return self.data_holder.load_data(data)