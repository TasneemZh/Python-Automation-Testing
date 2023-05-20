from jproperties import Properties

from utils.ManageFiles import ManageFiles


class ConfigureProperties:
    @staticmethod
    def get_properties(properties_file):
        manage_files = ManageFiles()
        config = manage_files.read_from_json("config")
        if config["run_command"]:
            relative_path = "./"
        else:
            relative_path = "../../"
        configs = Properties(properties_file)
        with open(relative_path + properties_file, 'rb') as config_file:
            configs.load(config_file)
        return configs
