import os
import unittest
from datetime import date

from src.core.extractor.dataSource import DataSourceFactory, DataSourceType, YahooFinanceDataSource, \
    GoogleFinanceDataSource, JugaadDataSource
from src.core.utils.config_manager import get_config_manager_singleton


class TestDataSourceFactory(unittest.TestCase):

    def setUp(self):
        self.global_config = get_config_manager_singleton(config_path="../../../config", config_name="config")
        self.test_data_dir = self.global_config.project.test_data_dir

    def TearDown(self):
        pass

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
        generated_csv_filename = data_source.get_data(start_date, self.test_data_dir)
        self.assertTrue(os.path.exists(generated_csv_filename))
        os.remove(generated_csv_filename)

    #
    def test_invalid_data_source(self):
        factory = DataSourceFactory()
        with self.assertRaises(ValueError):
            factory.get_data_source("invalid_source")


if __name__ == '__main__':
    unittest.main()
