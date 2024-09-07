from datetime import date
from pprint import pprint

from src.core.extractor.dataDownloader import DataDownloader
from src.core.extractor.dataHolder import DataHolderType
from src.core.extractor.dataSource import DataSourceType


def run(config):
    print(f"Plugin banacleSheet is running with config: {config}")
    # data_downloader = DataDownloader(source=DataSourceType.JUGAAD, data_holder=DataHolderType.PANDAS)
    # start_date = date(2020, 1, 1)
    # data_dir = config.project.data_dir
    # result = data_downloader.get_data(start_date, data_dir)
    # pprint(result.head())
