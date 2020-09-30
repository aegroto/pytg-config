import yaml

from modules.pytg.Manager import Manager
from modules.pytg.load import get_module_content_folder

class ConfigManager(Manager):
    @staticmethod
    def initialize():
        ConfigManager.__instance = ConfigManager()

        return

    @staticmethod
    def load():
        return ConfigManager.__instance

    def load_settings(self, module="config", file_name="settings"):
        module_folder = get_module_content_folder(module)

        return yaml.safe_load(open("{}/config/{}.yaml".format(module_folder, file_name)))

    def save_settings(self, settings, module="config", file_name="settings"):
        module_folder = get_module_content_folder(module)

        yaml.safe_dump(settings, open("{}/config/{}.yaml".format(module_folder, file_name), "w"))