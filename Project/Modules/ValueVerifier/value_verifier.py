from Project.Models.error_type import ErrorType


class ValueVerifier():

	def __init__(self):
		self.__failing_dict = {}

	#Several assumptions that may very well be wrong:
	#	Values and Policies are passed as dictionaries
	#	Values and Policies dicts are parsed in a not-stupid way and actually holds Ints and the like and not just strings
	#	Ports have the key "port"

	def check(self, values_dict, policy_dict):
		#Get a list of used ports
		portList = self.port_search(values_dict)

		#Do the same for Images?
		imageList = self.image_search(values_dict)

		#Iterate through policies we want to check
		for key in policy_dict:

			#Compare between values and policy
			#Depends on policy

			#Maximum Number of Ports - int
			if key == "max_open_ports":

				if len(portList) > policy_dict[key]:

					self.__failing_dict["max_open_ports"] = len(portList) - policy_dict[key]

	#				print("Bad - Too many ports")
	#			else:
	#				print("Good - Not too many ports")


			#Banned Ports - list of ints
			elif key == "banned_ports":
				for port in policy_dict[key]:
					if port in portList:

						if "banned_ports" not in self.__failing_dict:
							self.__failing_dict["banned_ports"] = []

						self.__failing_dict["banned_ports"].append(port)

	#					print("Bad - Using banned port " + str(port))
	#				else:
	#					print("Good - Not using banned port")


			#Allowed Ports - list of ints
			elif key == "allowed_ports":
				for port in portList:
					if port not in policy_dict[key]:

						if ErrorType.ALLOWED_PORTS not in self.__failing_dict:
							self.__failing_dict[ErrorType.ALLOWED_PORTS] = []

						self.__failing_dict[ErrorType.ALLOWED_PORTS].append(port)

	#					print("Bad - Using non-allowed port " + str(port))
	#				else:
	#					print("Good - Using allowed port")


			#No Root - Boolean
			elif key == "NO_ROOT":
			#TODO:  Figure out exactly how this works
				if "securityContext" in values_dict:
					if "runAsNonRoot" in values_dict["securityContext"]:
						if values_dict["securityContext"]["runAsNonRoot"] != policy_dict[key]:
							self.__failing_dict[ErrorType.NO_ROOT] = 1

	#						print("Bad - No Root is not " + str(policy_dict[key]))
	#					else:
	#						print("Good - No Root matches policy")


			#Check Outside Images - Boolean


			#Banned Images - list of Images
			elif key == "banned_images":
				for image in imageList:
					if image in policy_dict[key]:

						if ErrorType.BANNED_IMAGES not in self.__failing_dict:
							self.__failing_dict[ErrorType.BANNED_IMAGES] = []

						self.__failing_dict[ErrorType.BANNED_IMAGES].append(image)

	#					print("Bad - Using banned image " + str(port))
	#				else:
	#					print("Good - Using allowed image")

			#Allowed Images - list of Images
			elif key == "allowed_images":
				for image in imageList:
					if image not in policy_dict[key]:

						if ErrorType.ALLOWED_IMAGES not in self.__failing_dict:
							self.__failing_dict[ErrorType.ALLOWED_IMAGES] = []

						self.__failing_dict[ErrorType.ALLOWED_IMAGES].append(image)

	#					print("Bad - Using banned image " + str(port))
	#				else:
	#					print("Good - Using allowed image")


		return self.__failing_dict


	#The thing is, ideally the Values should be parsed in such a way that these functions are unnecessary, but just in case:

	#Returns a list of ints representing ports used
	def port_search(self, values_dict):

		ports = []

		for key in values_dict:
			if isinstance(values_dict[key], dict):
				ports.extend(self.port_search(values_dict[key]))
			else:
				if key == "port":
					ports.append(values_dict[key])

		return ports

	#Returns a list of strings representing images used
	def image_search(self, values_dict):

		images = []

		for key in values_dict:
			if isinstance(values_dict[key], dict):
				images.extend(self.port_search(values_dict[key]))
			else:
	#TODO: Figure out how Images are labeled
				if key == "image":
					images.append(values_dict[key])

		return images
