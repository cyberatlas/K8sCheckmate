import policyParseExperiment

test_policies_file_1 = "testpolicies.yaml"
#Contents:
#max_open_ports: 5
#banned_ports: 21,23,80
#allowed_ports: 69, 420, 80085
#no_root: false
#check_outside_images: True
#banned_images: This, That, Other
#allowed_images: The other one, also this one

test_policy_dict_1 = {
	"max_open_ports": 5,
	"banned_ports": [21,23,80],
	"allowed_ports": [69,420,80085],
	"no_root": False,
	"check_outside_images": True,
	"banned_images": ["This"," That"," Other"],
	"allowed_images": ["The other one"," also this one"]
}

test_policies_file_2 = "testpoliciesWrong.yaml"
#Contents:
#max_open_ports: Five
#banned_ports: 21, Twenty-Three, Ten Eights


test_policy_dict_2 = {
	"max_open_ports": 5,
	"banned_ports": [21,23,80]
}

def test_1():
	assert policyParseExperiment.pol_parse(test_policies_file_1) == test_policy_dict_1
	
def test_2():
	assert policyParseExperiment.pol_parse(test_policies_file_2) == -1