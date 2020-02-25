### This file will be checking the values from IBM values.yaml that I found online
# Will be referencing the yaml file in TestCharts/IBM-example/values.yaml


import json

### Testing the values against the policies
def checkIBMValues(IBM_values, policy_Rules):
    #### traverse through the policy_Rules
    for k, v in policy_Rules.items():
        checkPortNumber(k, v)


### Simple check port number
def checkPortNumber(policy_key, policy_value):
    ### Test Port number
    if(policy_value == IBM_values_sample.get(policy_key, 0)):
        print("Port passes policy")
    else:
        print("The values port does not match the intended policy")

### Main method
def main():
    checkIBMValues(IBM_values_sample, policy_Rules_sample)


#### Giving sample input for now
policy_Rules_sample = {"port" : 80}
IBM_values_sample = {"port" : 120}
main()
