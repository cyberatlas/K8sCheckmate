import yaml
import argparse


def get_yaml(values_file):
    with open(values_file) as f:
        data = yaml.safe_load(f)
        print(f'{data} \n \n')
        print(yaml.dump(data))

        print(type(data))



def main():
    parser = argparse.ArgumentParser(description = "Testing python implementation for a POC")
    parser.add_argument('valuesYaml', help = "The values.yaml file to pass in")
    args = parser.parse_args()
    values_file = args.valuesYaml

    get_yaml(values_file)

"""
    # TODO implement checking for file types, args, etc
    with open(values_file) as f:
        data = yaml.safe_load(f)
        print(f'{data} \n \n')
        print(yaml.dump(data))
"""

main()
