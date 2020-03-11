from Models import FileType

# TODO -- more methods
def parse_file(fileType):
    if fileType is FileType.JSON:
        parse_json()
    elif fileType is FileType.YAML:
        parse_yaml()
    else:
        # Error handler
        print("Error handler")


def parse_json(file):
    # Parse the json file
    return json.load(file)


def parse_yaml():
    print ("fix")


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

def main():
    print('Parser')

if __name__ == '__main__':
    main()
