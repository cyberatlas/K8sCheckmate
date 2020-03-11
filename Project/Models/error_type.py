from enum import Enum

#Definition of Errors for the WrongDict in value_verifier to use
#Key is Enum, Value is more info regarding error as desribed in comments below
class ErrorType(Enum):
    MAX_OPEN_PORTS = 0,     #Number of ports over limit
    BANNED_PORTS = 1,       #List of ports used that are banned
    ALLOWED_PORTS = 2,      #List of ports used that are not allowed
    NO_ROOT = 3,        #None, key existing is enough
    BANNED_IMAGES = 5,      #List of images used that are not allowed
    ALLOWED_IMAGES = 4      #List of images used that are banned