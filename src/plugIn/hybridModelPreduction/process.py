from datetime import date
from pprint import pprint

from src.core.extractor.dataDownloader import DataDownloader
from src.core.extractor.dataHolder import DataHolderType
from src.core.extractor.dataSource import DataSourceType
from src.core.utils.config_manager import get_config_manager_singleton


class HybridModel:
    def __init__(self, config):
        self.config = config

    def run(self):
        print(f"Plugin hybrid  is running with config: {self.config}")
        global_config = get_config_manager_singleton(config_path="../../../config", config_name="config")
        data_downloader = DataDownloader(source=DataSourceType.JUGAAD, data_holder=DataHolderType.PANDAS)
        start_date = date(2020, 1, 1)
        data_dir = self.config.project.data_dir
        result = data_downloader.get_data(start_date)
        pprint(result.head())


def run(config):
    HybridModel(config).run()
