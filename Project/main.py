from Modules.Parser import parser as P
from Modules.ValueVerifier import value_verifier as V
from Modules.OutputHandler import output_handler as O
from Modules.ErrorHandler import error_handler as E
from Modules.ConfigHandler import config_handler as C
from pathlib import Path
import sys

def main():
    # Check File Exists
        # Throw error
    if(len(sys.argv) < 2):
        print("Error. Please give a file for the command argument")
        sys.exit()
    else:
        file_path = sys.argv[1]
        if(Path(file_path).is_file()):
            print("File exists")
        else:
            print("Argument for file is present, but the file path does not exist")
            sys.exit()
    # End of file existence

    P.main()
    V.main()
    O.main()
    E.main()
    C.main()
    
    # Parse <file> w/ Helm Parser

    # Parse <Policy> w/ Policy Parser

    # Check outputs w/ Value Check
    
    # Red/Green terminal While Parsing

    # Log When done (Errors @ top)

    print("Hello World")

main()