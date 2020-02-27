# SE 492 – sdmay20-58
# K8s Checkmate
# Week 2 Report (1/27 – 2/13)
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



#### 21 Feb - 27 Feb
- Daniel (23 Feb) [5 hours] - Updated valueCheck to fit the format of testpolicies.yaml, and expanded the checking function and testing it.
- Daniel (24 Feb) [4 hours] - Set up the outline of the Peer Review document and began filling it out.


| Name  | Bi-weekly Hours | Total Hours  |
|---|---|---|
| Alex Stevenson  | -  | 24  |
| Daniel Brink  | 12  | 24  |
| Jacob Cram  | -  |  17 |
| Sean Sailer  | -  | 10  |
| John Young  | -  | 19 |


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
- John 
- Jacob 
- Sean 
- Daniel will continue working on value checking, keeping it updated such that it works when integrated into the greater program, as well as testing it sufficiently.  In addition, will spend time working on the Peer Review presentation.
