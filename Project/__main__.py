from Project.Modules.ConfigHandler.config_handler import ConfigHandler
from Project.Modules.Parser.parser import Parser

def main():
    # Get config
    config_handler = ConfigHandler()
    parser = Parser()

    config = config_handler.get_config()
    print(config)

    if config['policyPath'] != '':
        parser.load_policy(config['policyPath'])
    else:
        # handle error
        print('Err')

    if config['chartPath'] != '':
        parser.load_chart(config['chartPath'])
    else:
        # handle error
        print('Err')

    chart_dict = parser.get_chart_dict()
    policy_dict = parser.get_policy_dict()

    # Verify the values
    print(chart_dict)
    print(policy_dict)



if __name__ == "__main__":
    main()