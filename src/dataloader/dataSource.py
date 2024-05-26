
from abc import ABC, abstractmethod
import yfinance as yf
from datetime import datetime as dt
from jugaad_data.nse import bhavcopy_save
from enum import Enum


class DataSourceType(Enum):
    YAHOO = 'yahoo'
    GOOGLE = 'google'
    JUGAAD = 'jugaad'

class DataSource(ABC):
    @abstractmethod
    def get_data(self, *args):
        pass
    

class YahooFinanceDataSource(DataSource):
    def get_data(self,func, *args):
        return func(*args)


class GoogleFinanceDataSource(DataSource):
    def get_data(self, func , *args):
        return func(*args)


class JugaadDataSource(DataSource):
    def get_data(self, *args):
        return bhavcopy_save(*args)
      
class DataSourceFactory:
    def get_DataSource(self, source: str) -> DataSource:
        if source == DataSourceType.YAHOO:
            return YahooFinanceDataSource()
        elif source == DataSourceType.GOOGLE:
            return GoogleFinanceDataSource()
        elif source == DataSourceType.JUGAAD:
            return JugaadDataSource()
        else:
            raise ValueError(f"Unknown data source={source}, expected {DataSourceType.YAHOO}, {DataSourceType.GOOGLE} or {DataSourceType.JUGAAD}")
        

