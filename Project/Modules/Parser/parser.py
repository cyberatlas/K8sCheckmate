import yaml

class Parser():

    def __init__(self):
        self.__chart_dict = None
        self.__policy_dict = None
        self.__values_dict = None
        

    def load_chart(self, path):

        with open(path) as yaml_file:
            self.__chart_dict = yaml.load(yaml_file, yaml.SafeLoader)

    def load_policy(self, path):
        with open(path) as yaml_file:
            self.__policy_dict = yaml.load(yaml_file, yaml.SafeLoader)

    def load_values(self, path):
        with open(path) as yaml_file:
            self.__values_dict = yaml.load(yaml_file, yaml.SafeLoader)

    def get_chart_dict(self, config):
        if config['chartPath'] != '':
            self.load_chart(config['chartPath'])
            return self.__chart_dict
        else:
            # handle error
            print('Err')

    def get_policy_dict(self, config):
        if config['policyPath'] != '':
            self.load_policy(config['policyPath'])
            return self.__policy_dict
        else:
            # handle error
            print('Err')

    def get_values_dict(self, config):
        if config['valuesPath'] != '':
            self.load_values(config['valuesPath'])
            return self.__values_dict
        else:
            # handle error
            print('Err')

# def dictIterate(d, level):
#     tabs = ''.join('\t' for i in range(0, level))
#     for key, value in d.items():
#         if isinstance(value, dict):
#             # print("{0}{1}: ").format(tabs, key)
#             print(f"{tabs}{key}: ")
#             level += 1
#             dictIterate(value, level)
#         else:
#             # print("{0}{1}: {2}".format(tabs, key, value))
#             print(f"{tabs}{key}: {value}")

# dictionary = {'cats': 'whiskers', 'dogs': { 'corgi': 'winston'}, 'KEY': 'walue', 'dict': { 'dict2': { 'special': 'times' }}, 'one': 'two'}

# dictIterate(dictionary, 0)
