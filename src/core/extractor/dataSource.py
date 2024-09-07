from abc import ABC, abstractmethod
from enum import Enum

from jugaad_data.nse import bhavcopy_save

from src.core.utils.config_manager import get_config_manager_singleton


class DataSourceType(Enum):
    YAHOO = 'yahoo'
    GOOGLE = 'google'
    JUGAAD = 'jugaad'


class DataSource(ABC):
    @abstractmethod
    def get_data(self, test_mode: bool = False, *args):
        pass


class YahooFinanceDataSource(DataSource):
    def get_data(self, test_mode: bool = False, *args):
        pass


class GoogleFinanceDataSource(DataSource):
    def get_data(self, test_mode: bool = False, *args):
        pass


class JugaadDataSource(DataSource):
    def get_data(self, test_mode: bool = False, *args):
        pass
        data_dir = get_config_manager_singleton().project.test_data_dir if test_mode else get_config_manager_singleton().project.data_dir
        bhavcopy_save(*args, data_dir)
        # full_bhavcopy_save(source_date, directory)
        # bhavcopy_fo_save(source_date, directory)
        # bhavcopy_index_save(source_date, directory)


class DataSourceFactory:
    @staticmethod
    def get_data_source(source: DataSourceType) -> DataSource:
        if type(source) is not DataSourceType:
            raise ValueError(
                f"Unknown data source={source}, expected {DataSourceType.YAHOO}, {DataSourceType.GOOGLE} "
                f"or {DataSourceType.JUGAAD}")
        elif source.value == DataSourceType.YAHOO.value:
            return YahooFinanceDataSource()
        elif source.value == DataSourceType.GOOGLE.value:
            return GoogleFinanceDataSource()
        elif source.value == DataSourceType.JUGAAD.value:
            return JugaadDataSource()
        else:
            raise ValueError(
                f"Unknown data source={source}, expected {DataSourceType.YAHOO}, {DataSourceType.GOOGLE} "
                f"or {DataSourceType.JUGAAD}")
