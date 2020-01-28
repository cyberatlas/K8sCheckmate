import yaml
import argparse

def get_yaml(values_file) -> values_dict:
    """get_yaml

    :param values_file:
    :rtype: values_dict
    """

    with open(values_file) as f:
        data = yaml.safe_load(f)
        print(f'{data} \n \n')
        print(yaml.dump(data))

        print(type(data))
        print(data.get("image"))
        print(type(data.get("image")))

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


