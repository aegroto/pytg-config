import yaml

from modules.pytg.Manager import Manager
from modules.pytg.ModulesLoader import ModulesLoader

class ConfigManager(Manager):
    @staticmethod
    def initialize():
        ConfigManager.__instance = ConfigManager()

        return

    @staticmethod
    def load():
        return ConfigManager.__instance

    def load_settings_file(self, file_name="settings"):
        module_folder = ModulesLoader.get_module_content_folder("config")

        return yaml.safe_load(open("{}/{}.yaml".format(module_folder, file_name)))

    def save_settings_file(self, settings, file_name="settings"):
        module_folder = ModulesLoader.get_module_content_folder("config")

        yaml.safe_dump(settings, open("{}/{}.yaml".format(module_folder, file_name), "w"))