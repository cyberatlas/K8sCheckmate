import yaml
import argparse
# from Project.HelmParse import helmparse
from Project.HelmParse import helmparse
from Project.PolicyParse import policyparse
from Project.ValueCheck import valueCheck

def main():
    vals = helmparse.get_yaml("../TestCharts/hello-world/values.yaml")
    policies = policyparse.get_policies_dict("../PolicyParse/testpolicies.yaml")
    valueCheck.check(vals, policies)

    # TODO this should work in theory but it's not getign the banned port that is used in the nested dict


if __name__ == '__main__':
    main()