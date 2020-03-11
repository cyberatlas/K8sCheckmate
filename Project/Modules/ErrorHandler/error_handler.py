from Models import file_type as F

# TODO
def file_not_found(expectedFileType):
    if expectedFileType is F.FileType.Policy:
        # handle policy file
        print("")

    elif expectedFileType is F.FileType.Chart:
        # handle chart file
        print("")

    elif expectedFileType is F.FileType.Output:
        # handle ouput file
        print("")
        
    else:
        # handle generic
        print("")

    exit(-1)


# TODO
def config_not_found():
    print('TODO')


# TODO
def incorrect_format(expectedFileType):
    if expectedFileType is F.FileType.Policy:
        # handle policy file
        print("The policy file has an incorrect format")

    elif expectedFileType is F.FileType.Chart:
        # handle chart file
        print("The chart file has an incorrect format")

    elif expectedFileType is F.FileType.Output:
        # handle ouput file
        print("The output file has an incorrect format")

    elif expectedFileType is F.FileType.Config:
        print("The config file has an incorrect format")

    else:
        # handle generic
        print("Generic file has incorrect format")


# TODO -- more moethods

def main():
    print('Error Handler')

if __name__ == '__main__':
    main()