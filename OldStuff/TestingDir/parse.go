package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sigs.k8s.io/yaml"
    //"gopkg.in/yaml.v2"

	"github.com/pkg/errors"
//	"sigs.k8s.io/yaml"
)

// Struct used for testing
/*
type Config struct {
    Foo string
    Bar []string
}
*/

type Config struct {
	Service struct {
		Type string
		Port int
	}
	Image struct {
		Tag string
	}
}


func checkNumPorts(){



}


func main() {
	filename := os.Args[1]
	var config Config
	source, err := ioutil.ReadFile(filename)

	if err != nil {
		panic(err)
	}

	// Unmarshal converts the yaml into an obj
	err = yaml.Unmarshal(source, &config)

	if err := config.Parse(source); err != nil {
		panic(err)
	}
	fmt.Printf("%+v\n", config)

	// Grabs all of the values from the yaml file
	var config2 map[string]interface{}
	err = yaml.Unmarshal(source, &config2)

	if err != nil {
		panic(err)
	}

	// fmt.Printf("Value: %#v\n", config.Bar[0])
	// Printing the values we greabbed
	fmt.Println("service : port : image")
	fmt.Println(config.Service.Type, config.Service.Port, config.Image.Tag)

	fmt.Println(config)
	fmt.Printf("%+v\n", config)

	// This is to print when we grab everything from the map
	/*
		   for v1, v2 := range(config2){

		        fmt.Printf("%s: %s \n\n", v1, v2)
			}
	*/

    /**
    //This only works with yaml v2 for some reason

    // Trying another method
     m := make(map[interface{}]interface{})
        err = yaml.Unmarshal([]byte(source), &m)
        if err != nil {
                // log.Fatalf("error: %v", err)
                fmt.Printf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)
        for k, v := range m {
            fmt.Println("k:", k, "v:", v)
        }

        **/
}
func (c *Config) Parse(data []byte) error {
	if err := yaml.Unmarshal(data, c); err != nil {
		return err
	}
	if c.Service.Type == "" {
		return errors.New("Kitchen config: invalid `hostname`")
	}
	// ... same check for Username, SSHKey, and Port ...
	return nil
}