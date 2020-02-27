#Several assumptions that may very well be wrong:
#	Values and Policies are passed as dictionaries
#	Ports have the key "port"

def check(values_dict, policy_dict):
	
	#Get a list of used ports
	portList = port_search(values_dict)
	
	#Mainly for testing
	numWrong = 0
	
	#Iterate through policies we want to check
	for key in policy_dict:
		
		#Compare between values and policy
		#Depends on policy
		
		#Maximum Number of Ports - int
		if key == "max_open_ports":			
			
			if len(portList) > policy_dict[key]:
			
				numWrong += 1
				
				print("Bad - Too many ports")
			else:
				print("Good - Not too many ports")
		
		
		#Banned Ports - list of ints
		elif key == "banned_ports":
			for port in policy_dict[key]:
				if port in portList:
				
					numWrong += 1
					
					print("Bad - Using banned port " + str(port))
				else:
					print("Good - Not using banned port")
		
		
		#Allowed Ports - list of ints
		elif key == "allowed_ports":
			for port in portList:
				if port not in policy_dict[key]:
				
					numWrong += 1
					
					print("Bad - Using non-allowed port " + str(port))
				else:
					print("Good - Using allowed port")
		
		
		#No Root - Boolean
		elif key == "NO_ROOT":
		#TODO:  Figure out exactly how this works
			if "securityContext" in values_dict:
				if "runAsNonRoot" in values_dict["securityContext"]:
					if values_dict["securityContext"]["runAsNonRoot"] != policy_dict[key]:
				
						numWrong += 1
				
						print("Bad - No Root is not " + str(policy_dict[key]))
					else:
						print("Good - No Root matches policy")
				
		
		#Check Outside Images - Boolean
#		elif key == "CHECK_OUTSIDE_IMAGES":
		#TODO:  Figure out how this works

#			if values_dict[key] != policy_dict[key]:
#				
#				numWrong += 1
#				
#				print("Bad - Check Outside Images is not " + policy_dict[key])
#			else:
#				print("Good - Check Outside Images matches policy")
		
		
		#Banned Images - list of Images
		
		
		#Allowed Images - list of Images
		
		
	return numWrong

#Returns a list of ports used
def port_search(values_dict):
	
	ports = []
	
	for key in values_dict:
		if isinstance(values_dict[key], dict):
			ports.extend(port_search(values_dict[key]))
		else:
			if key == "port":
				ports.append(values_dict[key])
	
	return ports
