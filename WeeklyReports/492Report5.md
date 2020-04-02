SE 492 – sdmay20-58
===
# K8s Checkmate
# Week 5 Report (3/13 – 4/2)
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


#### 13 Mar - 19 Mar
- Jacob (16 Mar) [3 hours] - Made/recorded slides, put together the slides and recordings for the team and turned it in.
- Alex (16 Mar) [3 hours] - Made slides, recorded slides, and did stuff to help with presentation. I am guessing the date, was sometime that week.
- John (17 Mar) [6 hours] - Tried to incorporate intelisense into our project
- Sean (17 Mar) [3 hours] - Worked with John to try and get the python dev environment set up and compatible with our project
- Jacob (17 Mar) [2 hours] - Worked to figure out why intelisense was working on my laptop but not John or Seans.

#### 20 Mar - 26 Mar
- Sean (20 Mar) [3 hours] - Worked with outputting parsed values to the terminal in a user-friendly way, as well as logging them for auditing purposes
- Daniel (22 Mar) [2 hours] - Installed and set up necessary software to support working remotely
- John (22 Mar) [3 hours] - Met with advisor/looked in our git to pull a previous push in order to set up a demo
- Jacob (22 Mar) [1 hour] - Met with advisor and talked to team about demo for advisor.
- Alex (26 Mar) [1 hour] - Meeting with our advisor. Discussed progress and stuff.
- Alex (27 Mar) [1 hour] - Worked on the peer review stuff.
- Alex (28 Mar) [1 hour] - Worked on the peer review reply stuff.
- Jacob (28 Mar) [2 hours] - Worked on peer review with team, put together and selected the best of our teams questions to post for the other teams.

#### 27 Mar - 2 April

- Daniel (28 Mar) [4 hours] - Attempted to add informative terminal output to value_verifier
- Alex (1 April) [3 hours] - Cleaned up and added to MVP commit, looked at current project refactor, assessing next steps. 
- John (28 Mar) [3 hours] - Talked with Alex and talked about how we can get a previous commit to show our mvp/discuss our layout
- Sean (27 Mar) [3 hours] - More work on outputting and logging of results

| Name  | Bi-weekly Hours | Total Hours  |
|---|---|---|
| Alex Stevenson  | 9 | 54.5  |
| Daniel Brink  | 6 | 44  |
| Jacob Cram  | 8 | 37 |
| Sean Sailer  | 9 | 39  |
| John Young  | 12 | 57 |


### Plans for Coming Week
---
- [] Have client test MVP and provide feedback
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
- Daniel will continue to stay up-to-date on changes in 492's schedule due to circumstances and keep the team aware of them as well.  In addition, will also modify the verification code to work as the rest of the project is produced, and work towards the final presentation and poster.

