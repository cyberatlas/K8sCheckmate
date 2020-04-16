from enum import Enum

#Definition of Errors for the WrongDict in value_verifier to use
#Key is Enum, Value is more info regarding error as described in comments below
class ErrorType(Enum):
    MAX_OPEN_PORTS = "MAX_OPEN_PORTS",     #Number of ports over limit
    BANNED_PORTS = "BANNED_PORTS",       #List of ports used that are banned
    NO_ROOT = "NO_ROOT",        #None, key existing is enough
    BANNED_IMAGES = "BANNED_IMAGES",      #List of images used that are not allowed
    BANNED_USERS = "BANNED_USERS"