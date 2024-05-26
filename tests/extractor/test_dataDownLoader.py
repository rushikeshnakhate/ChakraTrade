import unittest
import os
import sys
from datetime import date
import pandas as pd
from pathlib import Path

# Ensure the src directory is in the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from extractor.dataDownloader import DataDownloader
from extractor.dataDownloader import DataSourceType
from extractor.dataHolder import DataHolderType
from utils.config_manager import get_config_manager_singleton

class TestJugaadDataSource(unittest.TestCase):
    def test_get_data_returns_dataframe(self):
        # Create a DataDownloader instance
        data_downloader = DataDownloader(source=DataSourceType.JUGAAD, data_holder=DataHolderType.PANDAS)
        
        # Set the start date and download path
        start_date = date(2020, 1, 1)
        data_dir = get_config_manager_singleton().project.data_dir    

        # Call the get_data method
        result = data_downloader.get_data(start_date, Path(data_dir))
                

        # Assert that the result is not None
        self.assertIsNotNone(result)
        
        # Assert that the result is of the expected data type
        self.assertIsInstance(result, pd.DataFrame)
        
        # Assert that the result has the expected number of rows
        self.assertEqual(len(result), 1910)
        
        # Assert that the result contains the expected columns
        expected_columns = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP', 'TOTALTRADES', 'ISIN', 'Unnamed: 13']
        self.assertListEqual(list(result.columns), expected_columns)

if __name__ == "__main__":
    unittest.main()