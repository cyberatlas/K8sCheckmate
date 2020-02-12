# K8sCheckmate

# Getting started:
Install Python 3.7
Install pyenv and virtualenv 

- [] Add the instructions for pyenv - **Alex**
- [x] Make a requirements.txt
> Made this in the main project folder.
This is the standard way to do things for projects like this. 
Alternatively, there is the option of having requirements.txt for each aspect of the project and have the main requirements.txt 

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
