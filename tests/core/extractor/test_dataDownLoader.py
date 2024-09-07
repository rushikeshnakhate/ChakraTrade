import unittest
from datetime import date
from pathlib import Path

import pandas as pd

from src.core.extractor.dataSource import DataSourceType
from src.core.extractor.envType import EnvType
from src.core.utils.config_manager import get_config_manager_singleton
from src.core.extractor.dataDownloader import DataDownloader
from src.core.extractor.dataHolder import DataHolderType


class TestJugaadDataSource(unittest.TestCase):
    def setUp(self):
        self.global_config = get_config_manager_singleton(config_path="../../../config", config_name="config")
        self.test_data_dir = self.global_config.project.test_data_dir
        data_name = "bhav_data"
        self.data_downloader = DataDownloader(env_type=EnvType.Test, data_name=data_name, source=DataSourceType.JUGAAD,
                                              data_holder=DataHolderType.PANDAS)

    def test_get_data_returns_dataframe(self):
        start_date = date(2020, 1, 1)

        result = self.data_downloader.get_data(start_date)

        # Assert that the result is not None
        self.assertIsNotNone(result)

        # Assert that the result is of the expected data type
        self.assertIsInstance(result, pd.DataFrame)

        # Assert that the result has the expected number of rows
        self.assertEqual(len(result), 1910)

        # Assert that the result contains the expected columns
        expected_columns = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY',
                            'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'Unnamed: 13']
        self.assertListEqual(list(result.columns), expected_columns)

    def test_get_data_caches_result_from_cache(self):
        # Create a DataDownloader instance
        # Set the start date and download path
        start_date = date(2020, 1, 2)
        # Call the get_data method twice
        result1 = self.data_downloader.get_data(start_date)
        # Set the start date and download path
        start_date = date(2020, 1, 2)
        # Call the get_data method twice
        result2 = self.data_downloader.get_data(start_date)
        # Compare the two results and print which rows are different
        self.assertTrue(result1.equals(result2))


if __name__ == "__main__":
    unittest.main()
