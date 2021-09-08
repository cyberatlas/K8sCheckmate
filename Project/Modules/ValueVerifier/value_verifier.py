from Project.Models.error_type import ErrorType


class ValueVerifier():
    def __init__(self):
        self.__failing_dict = {}

    # Several assumptions that may very well be wrong:
    #	Values and Policies are passed as dictionaries
    #	Values and Policies dicts are parsed in a not-stupid way and actually holds Ints and the like and not just strings
    #	Ports have the key "port"
    def check(self, values_dict, policy_dict):
        self.__failing_dict = {}
        # Get a list of used ports
        portList = self.port_search(values_dict)

        # Do the same for Images?
        imageList = self.image_search(values_dict)

        # Iterate through policies we want to check
        for key in policy_dict:
            # Compare between values and policy
            # Depends on policy
            # Maximum Number of Ports - int
            if key == ErrorType.MAX_OPEN_PORTS.name:
                if len(portList) > policy_dict[key]:
                    self.add_issue(key, len(portList))

            # Banned Ports - list of ints
            elif key == ErrorType.BANNED_PORTS.name:
                for port in policy_dict[key]:
                    if port in portList:
                        self.add_issue(key, port)

            # No Root - Boolean
            elif key == ErrorType.NO_ROOT.name:
                if 'securityContext' in values_dict:
                    if 'runAsNonRoot' in values_dict['securityContext']:
                        if values_dict['securityContext']['runAsNonRoot'] != policy_dict[key]:
                            self.add_issue(key, values_dict['securityContext']['runAsNonRoot'])

            elif key == ErrorType.BANNED_USERS.name:
                if 'securityContext' in values_dict:
                    if 'runAsUser' in values_dict['securityContext']:
                        if values_dict['securityContext']['runAsUser'] in policy_dict[key]:
                            self.add_issue(key, values_dict['securityContext']['runAsUser'])

            # Check Outside Images - Boolean
            # Banned Images - list of Images
            elif key == ErrorType.BANNED_IMAGES.name:
                for image in imageList:
                    self.add_issue(key, image)

            # Check Outside Images - Boolean
            # Banned Images - list of Images
            elif key == ErrorType.ALLOWED_IMAGES.name:
                for image in imageList:
                    # print(f'image : {image} imglist:{imageList} policylist: {policy_dict[key]} \n')
                    # TODO Check the condition for when there is no allowed registries configured - commented line does not work in that cas'
                    # if image['repository'] not in policy_dict[key] and image['Registry'] not in policy_dict['ALLOWED_REGISTRIES']:
                    # if image['repository'] not in policy_dict[key]:
                    if image['repo'] not in policy_dict[key]:
                            self.add_issue(key, image)

                    if 'ALLOWED_REGISTRIES' in policy_dict:
                        if 'registry' not in image or image['registry'] not in policy_dict['ALLOWED_REGISTRIES']:
                            self.add_issue('ALLOWED_REGISTRIES', image)

            # This is the main feature that we are after - checks that repo is in the correct registry
            elif key == ErrorType.ALLOWED_REGISTRY_REPO.name:
                # If the image does not contain a registry nor repo it auto fails the check
                for image in imageList:
                    # if 'registry' not in image or 'repo' not in image:
                    if 'registry' not in image or 'repo' not in image:
                        # TODO perhaps clean up the image? like a list? maybe make this more descriptive
                        self.add_issue(key, image)
                        # self.__failing_dict[key].append(image)

                    elif [image['registry'], image['repo']] in policy_dict[key]:
                        continue
                    else:
                        self.add_issue(key, image)

        return self.__failing_dict

    # Adds the failing checks to the failing dict
    def add_issue(self, key, val):
        # Add the policy to the dict of failed checks if not in there already
        if key not in self.__failing_dict:
            self.__failing_dict[key] = []
        self.__failing_dict[key].append(val)

    # The thing is, ideally the Values should be parsed in such a way that these functions are unnecessary, but just in case:
    # Returns a list of ints representing ports used
    def port_search(self, values_dict):
        ports = []
        for key in values_dict:
            if isinstance(values_dict[key], dict):
                ports.extend(self.port_search(values_dict[key]))
            else:
                if key == 'port':
                    ports.append(values_dict[key])

        return ports

    # Returns a list of strings representing images used
    def image_search(self, values_dict):
        images = []
        for key in values_dict:
            if key == 'image':
                # images.append(values_dict[key]['repository'])
                images.append(values_dict[key])
            elif isinstance(values_dict[key], dict):
                images.extend(self.image_search(values_dict[key]))

        return images
