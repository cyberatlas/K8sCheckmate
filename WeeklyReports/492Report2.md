# SE 492 – sdmay20-58
# K8s Checkmate
# Week 1 Report (1/13 – 1/27)
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


#### 13 Jan - 19 Jan
- Alex (13 Jan) - Researched locations of values, merged branches, cleaned up the POC, discussed issues/possible ways to move forward, and tried to improve our organization/communication
- Jacob (13 Jan) - Researched ways to better parse values, raised concerns with John and Alex, discussed ways to improve our organization/communication
- John (13 Jan) - Worked on organizing team meetings, collected availabilities, and met with Jacob and Alex to discuss issues and possible solutions to improve organization/communication


#### 20 Jan - 26 Jan
- John and Jacob (20 Jan) Talked about having a set of the overall basic struct for our security checker. We’re still working out the issues on how to make our struct more generic
- Sean researched different golang open-source libraries that provided YAML and JSON support for different loading, parsing, and storing functionality. Additionally researched the implementation specifics in other languages.
- Daniel Brink (20 Jan) Worked on keeping our group up to date with the team meetings with the Progress Update



| Name  | Bi-weekly Hours | Total Hours  |
|---|---|---|
| Alex Stevenson  | 12  | 12  |
| Daniel Brink  | 4  | 4  |
| Jacob Cram  | 8  |  8 |
| Sean Sailer  | 4  | 4  |
| John Young  | 8  | 8 |






### Plans for Coming Week
---
- [] Explore saving the values directly to a map or to our data structure `map[string][]string{}`
- [] Explore extracting everything using structs that contain every possible value, after which the fields without values are automatically left out.
- [] Explore what Helm and Kubernetes use to get the values and store them
We will need to weigh the pros and cons of each method and decide which to use moving forward. 
Once this is done we will need to:


- [] Figure out if the values must be saved to `values.yaml` or if they can be defined where they are used in the charts. If the latter is true, we will need to find a way to check all of the possible places they can be
- [] Find a way to parse the values from any sub-charts
- [] Figure out how templates play into this. Do we rerun the check on the templates? Do we have a list of allowed templates? How should go about dealing with them in a way that allows maximum flexibility to the end-user?
- [] Explore how we can utilize templates
- [] Parse a `policy.yaml` file and store the values
- [] Write methods to check the values from the policy against the chart
- [] Alert on any misconfigurations
- [] Figure out what to put in the policy files
- [] Figure out where users on the pods are defined


- Alex Stevenson is going to talk to Workiva about potentially including some python into this project
- John will work on setting up a Kubernetes cluster
- Jacob will continue to work on getting our JSON object to represent a map
- Sean will continue looking at libraries and looking at other languages and writing tests for our charts to ensure we are properly parsing and storing as they should be.
- Daniel will continue to manage how much progress our team has made
