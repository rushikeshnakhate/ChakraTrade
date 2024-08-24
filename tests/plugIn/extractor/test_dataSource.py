import os
import unittest
from datetime import date

from src.core.utils.config_manager import get_config_manager_singleton
from src.plugIn.extractor.dataSource import DataSourceFactory, YahooFinanceDataSource, DataSourceType, \
    GoogleFinanceDataSource, JugaadDataSource


class TestDataSourceFactory(unittest.TestCase):
    def test_get_yahoo_data_source(self):
        factory = DataSourceFactory()
        data_source = factory.get_data_source(DataSourceType.YAHOO)
        self.assertIsInstance(data_source, YahooFinanceDataSource)

    def test_get_google_data_source(self):
        factory = DataSourceFactory()
        data_source = factory.get_data_source(DataSourceType.GOOGLE)
        self.assertIsInstance(data_source, GoogleFinanceDataSource)

    def test_jugad_data(self):
        factory = DataSourceFactory()
        data_source = factory.get_data_source(DataSourceType.JUGAAD)
        self.assertIsInstance(data_source, JugaadDataSource)

        start_date = date(2020, 1, 1)
        data_dir = get_config_manager_singleton().project.data_dir

        generated_csv_filename = data_source.get_data(start_date, data_dir)
        self.assertTrue(os.path.exists(generated_csv_filename))
        os.remove(generated_csv_filename)

    #
    def test_invalid_data_source(self):
        factory = DataSourceFactory()
        with self.assertRaises(ValueError):
            factory.get_data_source("invalid_source")


if __name__ == '__main__':
    unittest.main()
