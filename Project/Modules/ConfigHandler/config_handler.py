import json
from os import path

class ConfigHandler():

    def __init__(self):
        self.__config = None
        self.__CONFIG_PATH = 'C:\\Users\\Sean\\Desktop\\config.json'


    def load_config(self):
        if not path.exists(self.__CONFIG_PATH):
            print('config.json not found')
            # handle error

        with open(self.__CONFIG_PATH) as json_file:
            self.__config = json.load(json_file)


    def get_config(self):
        if self.__config is None:
            self.load_config()

        return self.__config


