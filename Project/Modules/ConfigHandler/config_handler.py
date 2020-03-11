from pathlib import Path
import json
from Modules.ErrorHandler import error_handler as E

# TODO
def get_config_file():
    if not verify_file_exists("environment.json"):
        E.config_not_found()
    with open('environment.json') as f:
        return json.load(f)
    
# TODO
def verify_file_exists(path):
    return Path(path).is_file()

# TODO -- more methods wherever necessary

def main():
    print('Config Handler')

if __name__ == '__main__':
    main()
