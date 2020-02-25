import yaml
import argparse
from Project.HelmParse import helmparse

# I think it might be prudent down the line to  these in seperate files grouped by utility - but that's for the future

def check_max_open_ports(policies_dict):
   max_num_ports = policies_dict.get("max_open_ports")
   print(f'max_open_ports {max_num_ports}')
   return

def main():
    arg_parser = argparse.ArgumentParser(description="The portion of the application that parses and stores the security policy")
    arg_parser.add_argument('PolicyYaml', \
                            help= "The filepath of the policy definitions file")
    args = arg_parser.parse_args()
    policy_filepath = args.PolicyYaml

    with open(policy_filepath) as policy_file:
        # Dictionary of the policies from the file
        policies_dict = yaml.safe_load(policy_file)

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
