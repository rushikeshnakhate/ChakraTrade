from omegaconf import DictConfig
from hydra.core.global_hydra import GlobalHydra
from hydra import initialize, compose
import os
import sys
from hydra.errors import HydraException


src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))
sys.path.append(src_dir)

class ConfigManager:
    _instance = None
    _cfg = None

    def __new__(cls):
        """Implements the singleton pattern using the __new__ method to ensure only one instance of the class is created."""
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._initialize_config()
        return cls._instance

    @classmethod
    def _initialize_config(cls):
        try:
            """ Initializes the Hydra configuration system."""
            if not GlobalHydra().is_initialized():
                initialize(config_path=("../../config"), job_name="app")
            cls._cfg = compose(config_name="config")
        except HydraException as e:
            print(f"Error loading Hydra config: {e}")
            # Handle the error gracefully or raise it further if needed
    @property
    def config(self) -> DictConfig:
        """Returns the Hydra configuration object."""
        return self._cfg

def get_config_manager_singleton():
    """Returns a singleton instance of the ConfigManager class."""
    config_manager = ConfigManager()
    cfg = config_manager.config
    return cfg

