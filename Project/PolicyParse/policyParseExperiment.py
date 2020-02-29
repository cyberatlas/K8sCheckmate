import yaml

#Takes the filepath of the policy file as input,
#Returns a one-level dictionary with one value or list of values per key
def pol_parse(policy_filepath):
	
	#Get raw dictionary
	with open(policy_filepath) as policy_file:
		policies_dict = yaml.safe_load(policy_file)
		
	#Edit Dictionary to hold useful values instead of just strings
	
	#max_open_ports, int to int
	try:
		key = "max_open_ports"
		if key in policies_dict:
			policies_dict[key] = int(policies_dict[key])
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1
		
	#banned_ports, comma-separated string to int[]
	try:
		key = "banned_ports"
		if key in policies_dict:
			policies_dict[key] = policies_dict[key].replace(" ","")
			policies_dict[key] = policies_dict[key].split(',')
			for q in range(len(policies_dict[key])):
				policies_dict[key][q] = int(policies_dict[key][q])
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1
		
	#allowed_ports, comma-separated string to int[]
	try:
		key = "allowed_ports"
		if key in policies_dict:
			policies_dict[key] = policies_dict[key].replace(" ","")
			policies_dict[key] = policies_dict[key].split(',')
			for q in len(policies_dict[key]):
				policies_dict[key][q] = int(policies_dict[key][q])
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1

	#no_root, bool
	try:
		key = "no_root"
		if key in policies_dict:
			if policies_dict[key].lower() == "true":
				policies_dict[key] = True
			elif policies_dict[key].lower() == "false":
				policies_dict[key] = False
			else:
				raise Exception("Not a Boolean?")
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1
		
	#check_outside_images, bool
	try:
		key = "check_outside_images"
		if key in policies_dict:
			if policies_dict[key].lower() == "true":
				policies_dict[key] = True
			elif policies_dict[key].lower() == "false":
				policies_dict[key] = False
			else:
				raise Exception("Not a Boolean?")
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1

	#banned_images, comma-separated string to string[] (?)
	try:
		key = "banned_images"
		if key in policies_dict:
			policies_dict[key] = policies_dict[key].split(',')
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1
		
	#allowed_images, comma-separated string to string[] (?)
	try:
		key = "allowed_images"
		if key in policies_dict:
			policies_dict[key] = policies_dict[key].split(',')
	except:
		print("Something went wrong with the " + key + " key in the Policies File")
		return -1
		
	#Return complete Policy Dictionary
	return policies_dict