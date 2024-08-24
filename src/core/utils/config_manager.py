from pprint import pprint

from hydra import initialize, compose
from hydra.core import singleton
from hydra.core.global_hydra import GlobalHydra
from hydra.core.singleton import Singleton
from hydra.errors import HydraException
from omegaconf import DictConfig


class ConfigManager(metaclass=Singleton):
    _cfg = None

    def __init__(self, config_path=None, config_name="config"):
        if config_path:
            self._initialize_config(config_path, config_name)

    @classmethod
    def _initialize_config(cls, config_path, config_name):
        try:
            if not GlobalHydra().is_initialized():
                initialize(config_path=config_path, job_name="app", version_base=None)
            cls._cfg = compose(config_name=config_name)
        except HydraException as e:
            print(f"Error loading Hydra config: {e}")

    @property
    def config(self) -> DictConfig:
        """Returns the Hydra configuration object."""
        return self._cfg


def get_config_manager_singleton(config_path=None, config_name="config"):
    """Returns a singleton instance of the ConfigManager class."""
    config_manager = ConfigManager(config_path, config_name)
    cfg = config_manager.config
    return cfg
#
#
# def get_config_manager_singleton():
#     """Returns a singleton instance of the ConfigManager class."""
#     config_manager = ConfigManager()
#     # pprint(config_manager.config)  # This will ensure the config is initialized
#     cfg = config_manager.config
#     return cfg
