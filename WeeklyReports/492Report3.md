# SE 492 – sdmay20-58
# K8s Checkmate
# Week 3 Report (2/14 – 2/27)
###### Client: Workiva
###### Faculty Advisor: Julie Rursch
###### Team Members:
- Daniel Brink - Delivery Manager
- Jacob Cram - Test Engineer
- Sean Sailer - Software Developer/Tester
- Alexander Stevenson - Project Manager/Team Lead
- John Young - Software Developer/Meeting Facilitator


## Past Week Accomplishments
---
#### Individual Contributions
Team Member Contribution Weekly


#### 14 Feb - 20 Feb
- Daniel (16 Feb) [3 hours] - Continued looking at examples of Helm charts.
- John (17 Feb) [4 hours ] - Looking at IBM example with their values
- Sean (18 Feb) [2 hours] - Familiarized myself with PyUnit tesitng framework by writing example test code.
- John (19 Feb) [4 hours ] - Setting up architecture for testing IBM example values.yaml with a Policy file
- Sean (19 Feb) [1 hour] - Worked on dictionary iteration
- Alex (27 Jan) [5 hours] - Was having an issue saving YAML files in a map so explored the idea of how to do it in Python. Made a new branch for that as it's only to see if that will be able to be used just in case it's needed. Currently it loads the yaml file, saves it to a map, then prints out the map.





#### 21 Feb - 27 Feb
- Daniel (23 Feb) [5 hours] - Updated valueCheck to fit the format of testpolicies.yaml, and expanded the checking function and testing it.
- Daniel (24 Feb) [4 hours] - Set up the outline of the Peer Review document and began filling it out.
- Sean (22 Feb) [3 hours] - Worked on finding robust test configurations and writing test code using hte test files
- Sean (27 Feb) [2 hours] - Talked with Alex about recursive roadblock, helped implement a solution that recursively iterates nested dictionaries
- John (24 Feb) [4 hours ] - Testing in Python for IBM policies and planning out architecture with Alex and Jacob for utulizing dictionaries from the parsing
- Alex (24 Feb) [2.5 hours] - Worked on testing values in the chart, changed helmparse to be a module so it can be imported, looked a bit into how to search the key in nested dictionary. Going to look into recursively searching.
- Alex (27 Feb) [3 hours] - Merged branches, made necessary modules. Code runs in pycharm but not the terminal, debugging the issue. Says project is not a module, but I have made it one, tried to run as a module and add to the python path, but it did not like that. Got a hacky MVP create in StevensonTesting.py that works on max open ports and banned ports. Went to meeting with advisor.



| Name  | Bi-weekly Hours | Total Hours  |
|---|---|---|
| Alex Stevenson  | 10.5  | 34.5  |
| Daniel Brink  | 12  | 24  |
| Jacob Cram  | -  |  17 |
| Sean Sailer  | 8  | 18  |
| John Young  | 12  | 31 |


### Plans for Coming Week
---
- [] Figure out if the values must be saved to `values.yaml` or if they can be defined where they are used in the charts. If the latter is true, we will need to find a way to check all of the possible places they can be
- [] Find a way to parse the values from any sub-charts
- [] Figure out how templates play into this. Do we rerun the check on the templates? Do we have a list of allowed templates? How should go about dealing with them in a way that allows maximum flexibility to the end-user?
- [] Explore how we can utilize templates
- [] Parse a `policy.yaml` file and store the values
- [] Write methods to check the values from the policy against the chart
- [] Alert on any misconfigurations
- [] Figure out what to put in the policy files
- [] Figure out where users on the pods are defined

### Tasks 

- Alex Stevenson 
- John Meet with our group to force out the final architecture and get every phase to work together
- Jacob 
- Sean is going to help finish phase 1 and 2, and implement robust test code using the configured charts and YAML recently added to the repository. Additionally, will work with others on Saturday to get a fleshed-out POC to be tested by end-users next week 
- Daniel will continue working on value checking, keeping it updated such that it works when integrated into the greater program, as well as testing it sufficiently.  In addition, will spend time working on the Peer Review presentation.
