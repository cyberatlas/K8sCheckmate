from Modules.ErrorHandler import error_handler as _error_handler
from Models import file_type as F
from Modules.Parser import parser as P
from pathlib import Path
import json

# TODO
def get_config_file():
    # Check to see if the config file exists
    if not verify_file_exists("config.json"):
        _error_handler.config_not_found()

    # Check to see if json is valid
    with open('config.json') as f:
        try:
            config_file = parser.parse_json(f)
        except:
            _error_handler.file_not_found(F.FileType.Config)     

    # Check to see if chart path exists
    if not verify_file_exists(config_file['chartPath']):
        _error_handler.file_not_found(F.FileType.Chart)

    # Check to see if policy paths exist
    for file_path in config_file['policyPaths']:
        if not verify_file_exists(file_path):
            _error_handler.file_not_found(F.FileType.Policy)

    # Check to see if out path exists
    if not verify_file_exists(config_file['outputPath']):
        _error_handler.file_not_found(F.FileType.Output)

    return config_file


# TODO
def verify_file_exists(path):
    return Path(path).is_file()

# TODO -- more methods wherever necessary

def main():
    print('Config Handler')

if __name__ == '__main__':
    main()
