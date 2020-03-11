from ..ErrorHandler import file_not_found, config_not_found
from ...Models import FileType
from pathlib import Path
import json

# TODO
def get_config_file():
    # Check to see if the config file exists
    if not verify_file_exists("config.json"):
        config_not_found()

    with open('config.json') as f:
        config_file = json.load(f)

    # Check to see if chart path exists
    if not verify_file_exists(config_file['chartPath']):
        file_not_found(FileType.Chart)

    # Check to see if policy paths exist
    for file_path in config_file['policyPaths']:
        if not verify_file_exists(file_path):
            file_not_found(FileType.Policy)

    # Check to see if out path exists
    if not verify_file_exists(config_file['outputPath']):
        file_not_found(FileType.Output)

    return config_file


# TODO
def verify_file_exists(path):
    return Path(path).is_file()

# TODO -- more methods wherever necessary

def main():
    print('Config Handler')

if __name__ == '__main__':
    main()
