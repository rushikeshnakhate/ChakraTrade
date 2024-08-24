import unittest
import os
import sys
from datetime import date
from pprint import pprint

import pandas as pd
from pathlib import Path

from src.core.utils.config_manager import get_config_manager_singleton
from src.plugIn.extractor.dataDownloader import DataDownloader
from src.plugIn.extractor.dataHolder import DataHolderType
from src.plugIn.extractor.dataSource import DataSourceType


class TestJugaadDataSource(unittest.TestCase):
    def setUp(self):
        self.global_config = get_config_manager_singleton(config_path="../../../config", config_name="config")

    def test_get_data_returns_dataframe(self):
        # Create a DataDownloader instance
        data_downloader = DataDownloader(source=DataSourceType.JUGAAD, data_holder=DataHolderType.PANDAS)

        # Set the start date and download path
        start_date = date(2020, 1, 1)
        data_dir = self.global_config.project.data_dir

        # Call the get_data method
        result = data_downloader.get_data(start_date, Path(data_dir))

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

    def test_get_data_caches_result_from_cacahe(self):
        # Create a DataDownloader instance
        data_downloader = DataDownloader(source=DataSourceType.JUGAAD, data_holder=DataHolderType.PANDAS)

        global_config = get_config_manager_singleton(config_path="../../../config", config_name="config")

        # Set the start date and download path
        start_date = date(2020, 1, 1)
        data_dir = global_config.project.data_dir

        # Call the get_data method twice
        result1 = data_downloader.get_data(start_date, Path(data_dir))
        result2 = data_downloader.get_data(start_date, Path(data_dir))

        # Assert that the two results are the same object
        self.assertIs(result1, result2)


if __name__ == "__main__":
    unittest.main()
