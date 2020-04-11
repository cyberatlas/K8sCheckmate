from Project.Modules.ConfigHandler.config_handler import ConfigHandler
from Project.Modules.Parser.parser import Parser


def main():
    # Get config
    config_handler = ConfigHandler()
    parser = Parser()

    config = config_handler.get_config()
    print(config)

    chart_dict = parser.get_chart_dict(config)
    policy_dict = parser.get_policy_dict(config)
    values_dict = parser.get_values_dict(config)

    # Verify the values
    print(chart_dict)
    print(policy_dict)
    print(values_dict)


if __name__ == "__main__":
    main()
