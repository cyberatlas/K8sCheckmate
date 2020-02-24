13 Jan - 19 Jan
===

- Alex (13 Jan) [6 hours] - Researched locations of values, merged branches, cleaned up the POC, discussed issues/possible ways to move forward, and tried to improve our organization/communication
- Jacob (13 Jan) - Researched ways to better parse values, raised concerns with John and Alex, discussed ways to improve our organization/communication
- John (13 Jan) - Worked on organizing team meetings, collected availabilities, and met with Jacob and Alex to discuss issues and possible solutions to improve organization/communication

20 Jan - 26 Jan
===
- John and Jacob (20 Jan) Talked about having a set of the overall basic struct for our security checker. We working out the issues on how to make our struct more generic

27 Jan - 13 Feb
====
- Alex (27 Jan) [5 hours] - Was having an issue saving YAML files in a map so explored the idea of how to do it in Python. Made a new branch for that as it's only to see if that will be able to be used just in case it's needed. Currently it loads the yaml file, saves it to a map, then prints out the map. 
- Daniel (1 Feb) [2 hours] - Spent time setting up and re-familiarizing self with Python and PyTest.
- Daniel (2 Feb) [3 hours] - Set up a very basic logic checking function.  As of writing, works with test keys and values, but does not work with checking images.  Inital tests show correct behavior.
- Sean (30 Jan) [3 hours] - Researched the different python testing frameworks, and decided on which one best fits our needs and use cases
- Daniel (9 Feb) [3 hours] - Studying and comparing online examples of helm charts to better comprehend what this project would be handling.
- John (27 Jan) [4 hours] - Was looking into a solution that Jacob found that would parse helm charts with GO with having a generic type. I found that this solution would put the helm chart into a JSON file of strings. Worked with this route a little and realized it work, but forcing the code to work because of GO's limitations was causing some issues. Communicated with the team though and we decided that Python would be the better/easier option.
- John (12 Feb) [2 hours] - Looked at some examples of security checking policies online to get a better understanding on what a typical security protocol follows. Talked to Stevenson about whether or not to use online examples or security policies from Workiva's Helm charts.
- John (13 Feb) [5 hours] - Made some tests for checking the security policy based off the research I did.
- Sean (6 Feb) [3 hours] - Began setting up PyUnit test framework in our project allowing for automated testing of logic files. Additionally, began structuring tests for parsing data and storing it correctly

14 Feb - 27 Feb
===
- Daniel (16 Feb) [3 hours] - Continued looking at examples of Helm charts.
- Daniel (23 Feb) [4 hours] - Updated valueCheck to fit the format of testpolicies.yaml, and expanded the checking function and testing it.
- Daniel (24 Feb) [3 hours] - Set up the outline of the Peer Review document and began filling it out.