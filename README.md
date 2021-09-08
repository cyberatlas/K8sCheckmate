# K8sCheckmate

# Getting started:
Once K8sCheckmate directory is installed, it is recommended to install pyenv if using MacOS or Linux.
- Mac
```brew install pyenv```
- Linux 
```curl https://pyenv.run | bash```

Follow instructions below for pyenv 
https://github.com/pyenv/pyenv/blob/master/README.md#installation

Go to the K8sCheckmate directory
If using pyenv set the current directory to python 3.7 or higher with 
```$ pyenv local 3.8.2```

Now install all other dependencies for all systems.
```$ pip install K8sCheckmate```
If this doesn't work you may need to do 
```$ pip install setuptools```
> You may need to `pip uninstall K8sCheckmate` and reinstall when making changes 

# Demo
In K8sCheckmate directory you can run the project by using
Mac:
```$ python Project/main.py```

Windows (in powershell):
```$ python .\Project\main.py | Out-Host ```


# Testing:
To run the all tests, in K8sCheckmate run
```$ pytest```

# Policies
- `MAX_OPEN_PORTS`
- `BANNED_PORTS`
- `NO_ROOT`
- `BANNED_IMAGES`
- `BANNED_USERS`
- `ALLOWED_IMAGES`
- `ALLOWED_REGISTRIES`
- `ALLOWED_REGISTRY_REPO`
