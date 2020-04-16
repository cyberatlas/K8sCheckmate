import datetime
from os import path, makedirs

from Project.Modules.ErrorHandler.error_handler import ErrorHandler


class OutputHandler():

    def __init__(self):
        self.__output_directory = None
        self.__passing = '\033[92m'
        self.__failing = '\033[91m'
        self.__bold = '\033[1m'
        self.__italic = '\033[3m'
        self.__end = '\033[0m'
        self.__errorHandler = ErrorHandler()

    def set_output_directory(self, out_dir):
        if path.exists(out_dir):
            self.__output_directory = out_dir
        else:
            makedirs(out_dir)
            # Check with Sean if this is right
            self.__errorHandler.path_does_not_exist("Output directory")

    def output_to_terminal(self, policy_dict, verify_dict, elapsed_time):
        print('Finished parsing security policy in {0} seconds'.format(elapsed_time))
        for k, v in policy_dict.items():
            if verify_dict.get(k):
                #failed
                if "BANNED" in k:
                    print('Policy \"{0}\" '.format(k) +
                          self.__failing + 'FAILED' +
                          self.__end + self.__italic +
                          '\n\tFound Banned Artifact: {0}\n\tBanned List: {1}'.format(verify_dict[k], v) +
                          self.__end)
                else:
                    print('Policy \"{0}\" '.format(k) +
                          self.__failing + 'FAILED' +
                          self.__end + self.__italic +
                          '\n\tExpected: {0}\n\tWas: {1}'.format(v, verify_dict[k]) +
                          self.__end)

            else:
                #passed
                print('Policy \"{0}\" '.format(k) +
                      self.__passing +
                      'PASSED' +
                      self.__end)


    def log_to_file(self, policy_dict, verify_dict, elapsed_time):
        if self.__output_directory is None:
            # Handle error
            self.__errorHandler.path_does_not_exist("Output Directory")
            pass

        timestamp = str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '_')
        file_name = path.join(self.__output_directory, 'k8scheckmate_{0}.txt'.format(timestamp))
        file = open(file_name, 'a+')
        file.write('Finished parsing security policy in {0} seconds\n'.format(elapsed_time))
        for k,v in policy_dict.items():
            if verify_dict.get(k):
                #failed
                file.write('Policy \"{0}\" FAILED\n\tExpected:{1}\n\tWas:{2}\n'.format(k, v, verify_dict[k]))

            else:
                #passed
                file.write('Policy \"{0}\" PASSED\n'.format(k))
        file.close()
        print('Successfully wrote output to file: {0}'.format(file_name))
