import json
from os import path

from Project.Modules.ErrorHandler.error_handler import ErrorHandler


class ConfigHandler:

    def __init__(self):
        self.__config = None
        self.__CONFIG_PATH = 'config.json'
        self.__errorHandler = ErrorHandler()

    def load_config(self):
        with open(self.__CONFIG_PATH) as json_file:
            self.__config = json.load(json_file)

    def get_config(self):
        if not path.exists(self.__CONFIG_PATH):
            print('config.json not found')
            # handle error
            self.__errorHandler.path_does_not_exist("Config file")
        else:
            self.load_config()
            return self.__config
