class ErrorHandler():

    # Constructor
    def __init__(self):
        print("constructor")

    # Throws error message if file does not exist
    def file_not_found(self, path):
        print(path, " file could not be found")
        exit(-1)

    def path_not_found(self, parameter):
        print("Please provide a path for ", parameter)

    # Throws error if the file type is incorrect
    """def incorrect_format(expectedFileType):
        if expectedFileType is FileType.Policy:
            # handle policy file
            print("The policy file has an incorrect format")

        elif expectedFileType is FileType.Chart:
            # handle chart file
            print("The chart file has an incorrect format")

        elif expectedFileType is FileType.Output:
            # handle ouput file
            print("The output file has an incorrect format")

        elif expectedFileType is FileType.Config:
            print("The config file has an incorrect format")

        else:
            # handle generic
            print("Generic file has incorrect format")"""
