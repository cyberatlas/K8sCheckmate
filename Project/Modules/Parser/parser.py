import yaml

class Parser():

    def __init__(self):
        self.__chart_dict = None
        self.__policy_dict = None
        

    def load_chart(self, path):
        with open(path) as json_file:
            self.__chart_dict = yaml.load(json_file, yaml.SafeLoader)

    def load_policy(self, path):
        with open(path) as json_file:
            self.__policy_dict = yaml.load(json_file, yaml.SafeLoader)

    def get_chart_dict(self):
        return self.__chart_dict

    def get_policy_dict(self):
        return self.__policy_dict



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
