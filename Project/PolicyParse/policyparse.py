import yaml
import argparse
from Project.HelmParse import helmparse

# I think it might be prudent down the line to  these in seperate files grouped by utility - but that's for the future

def get_max_open_ports(policies_dict):
    max_num_ports = policies_dict.get("max_open_ports")
    if max_num_ports is None:
        print('The value max_open_ports was not found in the policies_dict')
        return -1
    
    return max_num_ports

def get_policies_dict(policy_filepath):
    """
    Reads policy files and stores it in a dict
    :param policy_filepath:
    :return: policies dict
    """
    try: 
        with open(policy_filepath) as policy_file:
            policies_dict = yaml.safe_load(policy_file)
    except FileNotFoundError as err:
        raise err

    return policies_dict


def main():
    arg_parser = argparse.ArgumentParser(description="The portion of the application that parses and stores the security policy")
    arg_parser.add_argument('PolicyYaml', \
                            help= "The filepath of the policy definitions file")
    args = arg_parser.parse_args()
    policy_filepath = args.PolicyYaml
    policies_dict = get_policies_dict(policy_filepath)

    print(f'Dump policies: \n{yaml.dump(policies_dict)}')

    check_max_open_ports(policies_dict)

    # TODO fix this, just for testing

    vals = helmparse.get_yaml("../TestCharts/hello-world/values.yaml")
    print(f'values: {vals}')
    # print(f'values {vals["port"]}')
    print(vals.get('port'))
    # TODO find out how to loop thorugh the nested dict looking ofr a key.
    # TODO could try making a recursive function for this
    # TODO could also try to flatten the nested dicts

if __name__ == '__main__':
    main()
