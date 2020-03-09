from Models import error_type as ErrorType




def main():
    print('Value Verifier');

if __name__ == '__main__':
    main()

#Look, everything is FUCKING PLACEHOLDERS so I have NO FUCKING CLUE how any of this is supposed to work together because apparently throwing away literal months of work and completely changing the architecture while NOT FILLING IN A SINGLE FUNCTION SNIPPET AND LEAVING EVERYTHING BLANK is somehow TOTALLY NOT GOING TO CAUSE A PROBLEM when what he had was working fine and all tests showed perfect results (Before it got messed with and broke, that is), but whatever.  I'm pissed, I'm salty, and I just want this fucking project done.  It's funny, if I had ACTUALLY gotten a proper description and examples of everything that can go in either file like I've been repeatedly asking for since FUCKING OCTOBER, I would have, with no exaggeration, been able to do this entire project in a weekend on my own.  But here we are.  Now, I have no fucking idea WHAT the policy file is supposed to look like or how I'm expected to access it, but that's not my job so am I supposed to just fucking wait until whoever agreed to do it gets off their ass and writes a few goddamn functions?  Sure that sounds like a not completely fucking garbage way to develop.  I can't even write tests because the file already here is full of nonsense.  I suppose the alternative is to just not do anything because it'll just be ignored completely, thrown out, and made invalid in less than a fucking week like the last two times.  Oh wait, it'll take at least a month to get thrown out because we can't have anyone ACTUALLY FUCKING DO ANYTHING MORE THAN FOUR HOURS BEFORE ITS DUE.  Is this even still my job?  It's not like they'd tell me if it wasn't.  

#Fuck it.


#Several assumptions that may very well be wrong:
#	Values and Policies are passed as dictionaries
#	Values and Policies dicts are parsed in a not-stupid way and actually holds Ints and the like and not just strings
#	Ports have the key "port"

def check(values_dict, policy_dict):
	
	#Dictionarly of Errors
	WrongDict = {}

	#Get a list of used ports
	portList = port_search(values_dict)
	
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
		
		
		#Allowed Images - list of Images
		
		
	return WrongDict

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
