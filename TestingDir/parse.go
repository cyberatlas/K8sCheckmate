package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sigs.k8s.io/yaml"
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

func main() {
	filename := os.Args[1]
	var config Config
	source, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	// Unmarshal converts the yaml into an obj
	err = yaml.Unmarshal(source, &config)

	// Grabs all of the values from the yaml file
	//var config2 map[string]interface{}
	//err = yaml.Unmarshal(source, &config2)

	if err != nil {
		panic(err)
	}

	// fmt.Printf("Value: %#v\n", config.Bar[0])
	// Printing the values we greabbed
	fmt.Println(config.Service.Port, config.Service.Type, config.Image.Tag)

	//    fmt.Print( config2)

	// This is to print when we grab everything from the map
	/*
	   for v1, v2 := range(config2){

	        fmt.Printf("%s: %s \n\n", v1, v2)
	    }
	*/

}
