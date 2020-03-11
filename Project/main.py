from Modules.Parser import parser as P
from Modules.ValueVerifier import value_verifier as V
from Modules.OutputHandler import output_handler as O
from Modules.ErrorHandler import error_handler as E
from Modules.ConfigHandler import config_handler as C

def main():
    # Check File Exists
        # Throw error
    config = C.get_config_file()

    print(config)
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