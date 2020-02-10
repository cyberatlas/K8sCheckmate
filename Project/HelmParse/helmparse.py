import yaml
import argparse


def get_yaml(values_file):
    """
    Gets the values from the given yaml file and saves them as a dictionary

    :param values_file: The yaml file that the user passed in as commandline arg
    :returns: A dictionary with the data from the values file
    """

    with open(values_file) as f:
        data = yaml.safe_load(f)

    return data

def main():
    """
    The main function of the program

    This program takes 1 commandline argument, the filepath of the file to read in

    For more information or help on the command line arguments do the following:
        python helmparse.py -h or python helmparse.py --help
    """

    # The command line help description of the file
    parser = argparse.ArgumentParser(description = "Testing python implementation for a POC")
    # Adds the values file to read as an argument and provides help for it
    parser.add_argument('valuesYaml', \
            help = "The path to (relative or abssolute) the values.yaml file to pass in")
    args = parser.parse_args()
    values_file = args.valuesYaml

    values_dict = get_yaml(values_file)

    # The following is just used for testing
    # print(f'{values_dict} \n \n')
    print(f'Dump the dict:\n\n{yaml.dump(values_dict)}')

    print(f'\nType: {type(values_dict)}')
    print(f'\nImage: {values_dict.get("image")}')
    print(f'\nImage type in dict: {type(values_dict.get("image"))}')

    """
    # TODO implement checking for file types, args, etc
    with open(values_file) as f:
        data = yaml.safe_load(f)
        print(f'{data} \n \n')
        print(yaml.dump(data))
    """

main()


##To run from main project directory use ~ python Project/HelmParse/helmparse.py Project/TestCharts/hello-world/values.yaml
