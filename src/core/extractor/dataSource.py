from abc import ABC, abstractmethod
from enum import Enum
from pprint import pprint

from jugaad_data.nse import bhavcopy_save


class DataSourceType(Enum):
    YAHOO = 'yahoo'
    GOOGLE = 'google'
    JUGAAD = 'jugaad'


class DataSource(ABC):
    @abstractmethod
    def get_data(self, *args):
        pass


class YahooFinanceDataSource(DataSource):
    def get_data(self, func, *args):
        pprint(f"YahooFinanceDataSource.get_data({func}, {args})")
        return func(*args)


class GoogleFinanceDataSource(DataSource):
    def get_data(self, func, *args):
        return func(*args)


class JugaadDataSource(DataSource):
    def get_data(self, *args):
        return bhavcopy_save(*args)


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
