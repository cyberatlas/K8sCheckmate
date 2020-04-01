# To run: go to main directory -> python -m ValueCheck.StevensonTesting
# It also works with just the setup.py. Do `python setup.py install` in root dir

import yaml
import argparse
# from Project.HelmParse import helmparse
# from Project.HelmParse import helmparse
# from HelmParse import helmparse
# import Project.HelmParse
from HelmParse import helmparse
# from Project.PolicyParse import policyparse
from PolicyParse import policyparse
# from Project.ValueCheck import valueCheck
from ValueCheck import valueCheck

foundVals = []

def dictIterate(d, level, searched):
    tabs = ''.join('\t' for i in range(0, level))
    isfound = False
    for key, value in d.items():
        if key == searched:
            print(f'\nFOUND {key}:{value}\n')
            foundVals.append(value)
        if isinstance(value, dict):
            # print("{0}{1}: ").format(tabs, key)
            # print(f"{tabs}{key}: ")
            level += 1
            dictIterate(value, level,searched)
        # else:
        # print("{0}{1}: {2}".format(tabs, key, value))
        # print(f"{tabs}{key}: {value}")
    # print(f'foundvals = {foundVals}')
    return foundVals

# dictionary = {'cats': 'whiskers', 'dogs': { 'corgi': 'winston'}, 'KEY': 'walue', 'dict': { 'dict2': { 'special': 'times' }}, 'one': 'two'}

def checkPorts(policies, foundVals):


    banned_port_list = (policies['banned_ports']).split(',')
    print(f'Banned Ports List: {banned_port_list}')
    for value in foundVals:
        # print(value)
        if str(value) in banned_port_list:
            print(f'found banned port {value}')

    print(f'len foundvals: {len(foundVals)}')
    if len(foundVals) > int(policies["max_open_ports"]):
        print("too many open ports")
    else:
        print(f"Num ports({len(foundVals)}) in acceptable range")



def main():
    # vals = helmparse
    # from HelmParse import helmparse.get_yaml("../TestCharts/hello-world/values.yaml")
    #     vals = helmparse.get_yaml("../TestCharts/hello-world/values.yaml")
    vals = helmparse.get_yaml("TestCharts/hello-world/values.yaml")
    # policies = policyparse.get_policies_dict("../PolicyParse/testpolicies.yaml")
    policies = policyparse.get_policies_dict("PolicyParse/testpolicies.yaml")
    # print(type(policies['banned_ports']))
    valueCheck.check(vals, policies)

    foundVals = dictIterate(vals, 0, 'port')
    checkPorts(policies,foundVals)

    # print(foundVals)
    # print(policies['banned_ports'])
    # banned_port_list = (policies['banned_ports']).split(',')
    # print(banned_port_list)
    # for value in foundVals:
    #     print(value)
    #     if str(value) in banned_port_list:
    #         print(f'found banned port {value}')
    # # TODO this should work in theory but it's not getign the banned port that is used in the nested dict



if __name__ == '__main__':
    main()