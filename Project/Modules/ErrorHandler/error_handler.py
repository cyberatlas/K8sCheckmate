from Models import file_type as FileType

# TODO
def file_not_found(expectedFileType):
    if expectedFileType is FileType.Config:
        this.config_not_found()
    elif expectedFileType is FileType.Policy:
        # handle policy file
        print("")
    elif expectedFileType is FileType.Chart:
        # handle chart file
        print("")
    else:
        # handle generic
        print("")

    exit(-1)

# TODO
def config_not_found():
    print('TODO')

# TODO -- more moethods

def main():
    print('Error Handler')

if __name__ == '__main__':
    main()
