import os
import sys

from src.core.plugInManager import PluginManager
from src.core.utils.config_manager import get_config_manager_singleton

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

if __name__ == "__main__":
    # Initialize global configuration
    global_config = get_config_manager_singleton(config_path="../../../config", config_name="config")
    plugin_manager = PluginManager(global_config=global_config)
    plugin_manager.load_plugins()
    plugin_manager.run_plugins()
