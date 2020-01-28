# K8sCheckmate

# Getting started:
Need to install:
- go
- helm 
- tiller
- minkube / kubernetes
- Virtualbox (to run minikube if needed)
- Docker

# Things to work on 

Right now, we have three options to explore. 
Currently we have 2 POCs, one using `yaml v2` another one using `k8s yaml` which uses `yaml v2` under the hood. 

This is what things look like stored in the map

```
map[affinity:map[] fullnameOverride: image:map[pullPolicy:IfNotPresent repository:nginx tag:stable] imagePullSecrets:[] ingress:map[annotations:map[] enabled:false hosts:[map[host:chart-example.local paths:[]]] tls:[]] nameOverride: nodeSelector:map[] podSecurityContext:map[] replicaCount:1 resources:map[] securityContext:map[] service:map[port:80 type:ClusterIP] serviceAccount:map[create:true name:<nil>] tolerations:[]]
```
This is what it looks like when cleaned up. 

```
k: image v: map[pullPolicy:IfNotPresent repository:nginx tag:stable]
k: imagePullSecrets v: []
k: fullnameOverride v: 
k: tolerations v: []
k: nameOverride v: 
k: podSecurityContext v: map[]
k: nodeSelector v: map[]
k: resources v: map[]
k: replicaCount v: 1
k: serviceAccount v: map[create:true name:<nil>]
k: ingress v: map[annotations:map[] enabled:false hosts:[map[host:chart-example.local paths:[]]] tls:[]]
k: securityContext v: map[]
k: service v: map[port:80 type:ClusterIP]
k: affinity v: map[]
```

We have 3 options to explore in regards to how we are getting the values 

- [] We can do the method of recursively converting it to JSON and storing it in a map.
- [] Explore saving the values directly to a map or to our data structure map[string][]string{}
- [] Explore extracting everything using structs that contain every possible value, after which the fields without values are automatically left out.
- [] Explore what Helm and Kubernetes use to get the values and store them 

We will need to weigh the pros and cons of each method and decide which to use moving forward. 
Once this is done we will need to:

- [] Figure out if the values must be saved to `values.yaml` or if they can be defined where they are used in the charts. If the latter is true, we will need to find a way to check all of the possible places they can be
- [] Find a way to parse the values from any subcharts
- [] Figure out how templates play into this. Do we rerun the check on the templates? Do we have a list of allowed templates? How should go about dealing with them in a way that allows maximum flexibility to the end user?
- [] Explore how we can utilize templates
- [] Parse a `policy.yaml` file and store the values
- [] Write methods to check the values from the policy against the chart
- [] Alert on any misconfigurations
- [] Figure out what to put in the policy files
- [] Figure out where users on the pods are defined

# Tracking Work 

In `thingsWeveDone.md` write your name, date, and what you did. 
This greatly simplifies the creation of biweekly reports, tracking progress, and tracking what each person did.


# Ideas For Policy File

- Ensure that things aren't being run as root by default
- Allow a max number of open ports on the cluster
- Ban certain ports from being used

