import policyParseExperiment

test_policies_1 = "testpolicies.yaml"

test_policy_dict_1 = {
	"max_open_ports": 5,
	"banned_ports": [21,23,80]
}

def test_1():
	assert policyParseExperiment.pol_parse(test_policies_1) == test_policy_dict_1
	