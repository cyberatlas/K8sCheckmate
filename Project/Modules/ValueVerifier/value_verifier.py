from Models import error_type as ErrorType




def main():
    print('Value Verifier');

if __name__ == '__main__':
    main()


#Several assumptions that may very well be wrong:
#	Values and Policies are passed as dictionaries
#	Values and Policies dicts are parsed in a not-stupid way and actually holds Ints and the like and not just strings
#	Ports have the key "port"

def check(values_dict, policy_dict):
	
	#Dictionarly of Errors
	WrongDict = {}

	#Get a list of used ports
	portList = port_search(values_dict)
	
	#Do the same for Images?
	imageList = image_search(values_dict)
	
	#Iterate through policies we want to check
	for key in policy_dict:
		
		#Compare between values and policy
		#Depends on policy
		
		#Maximum Number of Ports - int
		if key == "max_open_ports":			
			
			if len(portList) > policy_dict[key]:
			
				WrongDict[ErrorType.MAX_OPEN_PORTS] = len(portList) - policy_dict[key]
				
#				print("Bad - Too many ports")
#			else:
#				print("Good - Not too many ports")
		
		
		#Banned Ports - list of ints
		elif key == "banned_ports":
			for port in policy_dict[key]:
				if port in portList:
				
					if ErrorType.BANNED_PORTS not in WrongDict:
						WrongDict[ErrorType.BANNED_PORTS] = []
						
					WrongDict[ErrorType.BANNED_PORTS].append(port)
					
#					print("Bad - Using banned port " + str(port))
#				else:
#					print("Good - Not using banned port")
		
		
		#Allowed Ports - list of ints
		elif key == "allowed_ports":
			for port in portList:
				if port not in policy_dict[key]:
				
					if ErrorType.ALLOWED_PORTS not in WrongDict:
						WrongDict[ErrorType.ALLOWED_PORTS] = []
						
					WrongDict[ErrorType.ALLOWED_PORTS].append(port)
					
#					print("Bad - Using non-allowed port " + str(port))
#				else:
#					print("Good - Using allowed port")
		
		
		#No Root - Boolean
		elif key == "NO_ROOT":
		#TODO:  Figure out exactly how this works
			if "securityContext" in values_dict:
				if "runAsNonRoot" in values_dict["securityContext"]:
					if values_dict["securityContext"]["runAsNonRoot"] != policy_dict[key]:
				
						WrongDict[ErrorType.NO_ROOT] = 1
				
#						print("Bad - No Root is not " + str(policy_dict[key]))
#					else:
#						print("Good - No Root matches policy")
				
		
		#Check Outside Images - Boolean
		
		
		#Banned Images - list of Images
		elif key == "banned_images":
			for image in imageList:
				if image in policy_dict[key]:
				
					if ErrorType.BANNED_IMAGES not in WrongDict:
						WrongDict[ErrorType.BANNED_IMAGES] = []
						
					WrongDict[ErrorType.BANNED_IMAGES].append(image)
					
#					print("Bad - Using banned image " + str(port))
#				else:
#					print("Good - Using allowed image")
		
		#Allowed Images - list of Images
		elif key == "allowed_images":
			for image in imageList:
				if image not in policy_dict[key]:
				
					if ErrorType.ALLOWED_IMAGES not in WrongDict:
						WrongDict[ErrorType.ALLOWED_IMAGES] = []
						
					WrongDict[ErrorType.ALLOWED_IMAGES].append(image)
					
#					print("Bad - Using banned image " + str(port))
#				else:
#					print("Good - Using allowed image")
		
		
	return WrongDict


#The thing is, ideally the Values should be parsed in such a way that these functions are unnecessary, but just in case:

#Returns a list of ints representing ports used
def port_search(values_dict):
	
	ports = []
	
	for key in values_dict:
		if isinstance(values_dict[key], dict):
			ports.extend(port_search(values_dict[key]))
		else:
			if key == "port":
				ports.append(values_dict[key])
	
	return ports

#Returns a list of strings representing images used
def image_search(values_dict):
	
	images = []
	
	for key in values_dict:
		if isinstance(values_dict[key], dict): 
			images.extend(port_search(values_dict[key]))
		else:
#TODO: Figure out how Images are labeled
			if key == "image": 
				images.append(values_dict[key])
	
	return images