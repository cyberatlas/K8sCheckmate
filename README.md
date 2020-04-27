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
```$ pip install K8sCheckmate``

# Demo
In K8sCheckmate directory you can run the project by using
Mac:
```$ python Project/main.py```
Windows (in powershell):
```$ python .\Project\main.py | Out-Host ```


# Testing:
To run the all tests run 


- [] Add the instructions for pyenv - **Alex**
- [] Make a requirements.txt

# Things to work on/Timeline

### Phase 1
> Parse Helm charts
- [] Finish code and dictionary - **Jacob**
- [] Test - **Sean**

### Phase 2
> Parse and save policy templates
- [] Parse and store policies - **Alex**
- [] Test - **Sean**

### Phase 3
> Check and alert on misconfigurations 
- [] Implement logic for checking - **Daniel and John**
- [] Test 
- [] Reorganize for robustness (optimize)

# Tracking Work 

In `thingsWeveDone.md` write your name, date, number of hours spent, and what you did.
This is essentially a worklog.
This greatly simplifies the creation of biweekly reports, tracking progress, and tracking what each person did.

# Ideas For Policies

- Max Number Of Ports: #
- Banned Ports: #, #, #
- Allowed Ports: #, #, #
- No Root: True/False
- Check Outside Images: True/False
- Banned Images: image, image, image
- Allowed Images: image, image, image

# Other TODOs
- [x] Clean up the Git repo - **Alex**
- [] Talk to WK about getting charts to test with - **Alex**
- [] Research Python OOP best practices - **Sean**
- [] Research Python testing modules (including mock and codecov) - **Sean**
