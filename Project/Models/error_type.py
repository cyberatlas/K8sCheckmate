from enum import Enum

#Definition of Errors for the WrongDict in value_verifier to use
#Key is Enum, Value is more info regarding error as described in comments below
class ErrorType(Enum):
    MAX_OPEN_PORTS = "MAX_OPEN_PORTS",     # Number of ports over limit
    BANNED_PORTS = "BANNED_PORTS",       # List of ports used that are banned
    NO_ROOT = "NO_ROOT",        # None, key existing is enough
    BANNED_IMAGES = "BANNED_IMAGES",   # List of images used that are not allowed
    BANNED_USERS = "BANNED_USERS",  # List of users who are banned
    BANNED_APIS = "BANNED_APIS",  # List of banned APIs
    BANNED_SERVICES = "BANNED SERVICES",  # List of banned services
    PORT_NUMBER = "PORT_NUMBER",  # If user only wants one port, then this is specified
    RBAC = "RBAC",  # Checks to see if Role Based Access Control is enabled or not
    TLS = "TLS",  # Checks to see if transport layer security is used
    REPLICA_COUNT = "REPLICA_COUNT",  # Number of replica counts
    PULL_POLICY = "PULL_POLICY"  # If the pull policy is present or not
    ALLOWED_IMAGES = "ALLOWED_IMAGES"
    ALLOWED_REGISTRY_REPO = "ALLOWED_REGISTRY_REPO"
