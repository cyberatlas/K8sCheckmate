from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from Project.Modules.ConfigHandler.config_handler import ConfigHandler
from Project.Modules.OutputHandler.output_handler import OutputHandler
from Project.Modules.Parser.parser import Parser
from Project.Modules.ValueVerifier.value_verifier import ValueVerifier
import time



def main():
    start = time.time()

    # Get config
    config_handler = ConfigHandler()
    parser = Parser()
    value_verifier = ValueVerifier()
    output_handler = OutputHandler()

    config = config_handler.get_config()
    print(config)

    chart_dict = parser.get_chart_dict(config)
    policy_dict = parser.get_policy_dict(config)
    values_dict = parser.get_values_dict(config)

    for idx, val in enumerate(values_dict):
        verify_dict = value_verifier.check(val, policy_dict)

        # Do some logging
        end = time.time()
        output_handler.output_to_terminal(policy_dict, verify_dict, end - start, config['valuesPath'][idx])
        if config['outputPath'] != '':
            output_handler.set_output_directory(config['outputPath'])
            output_handler.log_to_file(policy_dict, verify_dict, end - start, config['valuesPath'][idx])

if __name__ == "__main__":
    main()
