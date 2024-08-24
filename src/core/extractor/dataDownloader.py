import logging

from src.core.extractor.CacheManager import DataCacheManager
from src.core.extractor.dataHolder import DataHolderType, DataHolderFactory
from src.core.extractor.dataSource import DataSourceType, DataSourceFactory

logging.basicConfig(level=logging.INFO)


class DataDownloader:
    def __init__(self, source: DataSourceType, data_holder: DataHolderType):
        self.data_source = DataSourceFactory().get_data_source(source)
        self.data_holder = DataHolderFactory().get_DataHolderType(data_holder)

    def get_data(self, *args, test_mode=False):
        cache_name = DataCacheManager.generate_cache_name(*args, test_mode=test_mode)
        data = DataCacheManager.load_from_cache(cache_name)
        logging.info(f"cache_name={cache_name}")

        if data is None:
            data = self.data_source.get_data(*args)
            DataCacheManager.save_to_cache(data, cache_name)
        return self.data_holder.load_data(data)
