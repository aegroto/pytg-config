import yaml

from pytg.Manager import Manager
from pytg.load import get_module_content_folder

class ConfigManager(Manager):
    def load_settings(self, module="config", file_name="settings"):
        module_folder = get_module_content_folder(module)

        return yaml.safe_load(open("{}/config/{}.yaml".format(module_folder, file_name)))

    def save_settings(self, settings, module="config", file_name="settings"):
        module_folder = get_module_content_folder(module)

        yaml.safe_dump(settings, open("{}/config/{}.yaml".format(module_folder, file_name), "w"))