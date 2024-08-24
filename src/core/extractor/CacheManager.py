import os
import pickle
from pathlib import Path

from src.core.utils.config_manager import get_config_manager_singleton


class DataCacheManager:
    @staticmethod
    def load_from_cache(cache_name: str):
        cache_file = f"{cache_name}.pkl"
        if os.path.exists(cache_file):
            with open(cache_file, "rb") as f:
                return pickle.load(f)
        else:
            return None

    @staticmethod
    def save_to_cache(data, cache_name: str):
        cache_file = f"{cache_name}.pkl"
        with open(cache_file, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def generate_cache_name(*args, test_mode=False):
        cache_file_name = "_".join(str(arg) for arg in args if not isinstance(arg, Path))
        cache_file_name += ".pkl"
        data_dir = get_config_manager_singleton().project.test_data_dir if test_mode else get_config_manager_singleton().project.data_dir
        return os.path.join(data_dir, cache_file_name)
