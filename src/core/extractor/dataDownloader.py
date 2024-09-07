import logging

from src.core.extractor.CacheManager import DataCacheManager
from src.core.extractor.dataHolder import DataHolderType, DataHolderFactory
from src.core.extractor.dataSource import DataSourceType, DataSourceFactory
from src.core.extractor.envType import EnvType

logging.basicConfig(level=logging.INFO)


class DataDownloader:
    def __init__(self, env_type: EnvType, data_name: str, source: DataSourceType, data_holder: DataHolderType):
        self.data_source = DataSourceFactory().get_data_source(source)
        self.data_holder = DataHolderFactory().get_DataHolderType(data_holder)
        self.data_name = data_name
        self.test_mode: bool = (env_type.value == EnvType.Test.value)

    def get_data(self, *args):
        cache_name = DataCacheManager.generate_cache_name(*args, test_mode=self.test_mode)
        data = DataCacheManager.load_from_cache(cache_name)
        if data is None:
            data = self.data_source.get_data(test_mode=self.test_mode, *args)
            DataCacheManager.save_to_cache(data, cache_name)
        return self.data_holder.load_data(data)
