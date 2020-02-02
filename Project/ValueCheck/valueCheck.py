import json

#Several assumptions:
#	Values are passed as a dictionary
#	Policies are passed as a JSON string

def check(values_dict, policy_json):
	
	#Mainly for testing
	numWrong = 0
	
	#Convert from JSON string to Dictionary
	policy_dict = json.loads(policy_json)
	
	#Iterate through policies we want to check
	for key in policy_dict:
		
		#Check for missing value
		if key not in values_dict:
		
			numWrong++
			
			print("Bad - " + key + " Is missing")
		
		#If value not missing, compare between values and policy
		#Depends on policy
#MUST UPDATE AS POLICIES ARE ADDED/KNOWN
		
		#Maximum Number of Ports - int
		else if key == "MAX_PORTS":
			if values_dict[key] > policy_dict[key]:
			
				numWrong++
				
				print("Bad - Too many ports")
			else:
				print("Good - Not too many ports")
		
		
		#Banned Ports - list of ints
		else if key == "BANNED_PORTS":
			for port in policy_dict[key]:
				if port in values_dict[key]:
				
					numWrong++
					
					print("Bad - Using banned port " + port)
				else:
					print("Good - Not using banned port")
		
		
		#Allowed Ports - list of ints
		else if key == "ALLOWED_PORTS":
			for port in values_dict[key]:
				if port not in policy_dict[key]:
				
					numWrong++
					
					print("Bad - Using non-allowed port " + port)
				else:
					print("Good - Using allowed port")
		
		
		#No Root - Boolean
		else if key == "NO_ROOT":
			if values_dict[key] != policy_dict[key]:
				
				numWrong++
				
				print("Bad - No Root is not " + policy_dict[key])
			else:
				print("Good - No Root matches policy")
		
		
		#Check Outside Images - Boolean
		else if key == "CHECK_OUTSIDE_IMAGES":
			if values_dict[key] != policy_dict[key]:
				
				numWrong++
				
				print("Bad - Check Outside Images is not " + policy_dict[key])
			else:
				print("Good - Check Outside Images matches policy")
		
		#