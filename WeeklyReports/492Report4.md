SE 492 – sdmay20-58
===
# K8s Checkmate
# Week 4 Report (2/28 – 3/12)
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


#### 28 Feb - 5 Mar
- All (29 Feb) [3 hours] - Group meeting, discussed future development.
- Daniel (1 Mar) [3 hours] - Experimented with a new Parsing method.
- Alex (3 Mar) [3 hours] - Fruitlessly worked on fixing module errors and recursion issues.
- Jacob (4 Mar) [2 hours] - Ran tests with our current version. Found it had issues, solved by Sean's next major push.
- Sean (5 Mar) [1 hour] - Theorized new architecture plan




#### 6 Mar - 12 Mar
- All (5 Mar) [3 hours] - Group meeting, discussed changing the architecture of the project.
- Daniel (9 Mar) [3 hours] - Attempting to modify existing code to conform to and work with new architecture.
- Alex (9 Mar) [2 hours] - Worked on slides for the presentation.
- Daniel (11 Mar) [2 hours] - More effort regarding the value verification function.
- John, Jacob, Sean (6 Mar) [2 hours] - Looked over Sean's new stucture for utulizing every phase of our mvp.
- John, Sean (11 Mar) [6 hours] - Worked on testing the file's existence and format type 
- Jacob (11 Mar) [2 hours] - Compared to make sure that the change in structure provided by Sean was still up to our spec.



| Name  | Bi-weekly Hours | Total Hours  |
|---|---|---|
| Alex Stevenson  | 11  | 45.5  |
| Daniel Brink  | 14  | 38  |
| Jacob Cram  | 12 |  29 |
| Sean Sailer  | 12  | 30  |
| John Young  | 14  | 45 |


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

- Alex  
- John Continue to work on finalizing our mvp with the structure. Also start implementing colors in our terminal for output.
- Jacob Keep updated regarding future schedule changes. Get potential beta version ready to show with above plans finished.
- Sean Continue pair programming with team members to ensure we are following best practices, and making it easier to work as a team. Additionally, drive development to ensure we have MVP delivered for client to test.
- Daniel will stay up-to-date on changes in 492's schedule due to circumstances and keep the team aware of them as well.  In addition, will also modify the verification code to work as the rest of the project is produced.
