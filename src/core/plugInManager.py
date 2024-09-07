import importlib.util
import os


class PluginManager:
    def __init__(self, global_config):
        self.plugin_directory = global_config.project.plugins_dir
        self.plugins = []
        self.global_config = global_config

    def load_plugins(self):
        """Loads all plugins in the plugin_directory."""
        for root, dirs, files in os.walk(self.plugin_directory):

            for file in files:
                if file.endswith(".py") and file == "process.py":
                    plugin_path = os.path.join(root, file)
                    plugin_name = os.path.basename(root)  # Use directory name as plugin name
                    self._load_plugin(plugin_name, plugin_path)

    def _load_plugin(self, plugin_name, plugin_path):
        """Loads an individual plugin."""
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.plugins.append(module)

    def run_plugins(self):
        """Runs all loaded plugins."""
        for plugin in self.plugins:
            plugin.run(self.global_config)  # Pass the global config to the plugin
