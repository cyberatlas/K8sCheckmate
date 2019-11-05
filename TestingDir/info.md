This is a directory that is being used for testing

Right now, we just want to figure out how to parse the YAML files and see if we can extract values. 

The `parse.bak` file is an old version that might be useful to have.
It is very similar but it uses `go-yaml` whereas in the new version `kubernetes-sigs/yaml` is being pulled in 

hello-world is an intro Helm chart used we are using for testing

## To Get the dependencies:
- `go get`
- `go build parse.go`
> You may get an error in one of these steps. 
> While still only in dev, don't need to worry about it being in the GOPATH yet. 

## To Compile and Run
- `go build parse.go`
- `./parse hello-world/values.yaml`


