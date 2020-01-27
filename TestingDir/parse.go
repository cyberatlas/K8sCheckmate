package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"

	"sigs.k8s.io/yaml"
	//"gopkg.in/yaml.v2"
	//	"sigs.k8s.io/yaml"
)

// Struct used for testing
/*
type Config struct {
    Foo string
    Bar []string
}
*/
/**
type Config struct {
	Service struct {
		Type string
		Port int
	}
	Image struct {
		Tag string
	}
}**/

func convert(i interface{}) interface{} {
	switch x := i.(type) {
	case map[interface{}]interface{}:
		m2 := map[string]interface{}{}
		for k, v := range x {
			m2[k.(string)] = convert(v)
		}
		return m2
	case []interface{}:
		for i, v := range x {
			x[i] = convert(v)
		}
	}
	return i
}

func main() {
	filename := os.Args[1]
	//var config Config

	source, err := ioutil.ReadFile(filename)

	fmt.Printf("Input: %s\n", source)
	var body interface{}

	if err != nil {
		panic(err)
	}

	if err := yaml.Unmarshal(source, &body); err != nil {
		panic(err)
	}

	body = convert(body)

	if b, err := json.Marshal(body); err != nil {
		panic(err)
	} else {
		//fmt.Printf("Output: %s\n", b)
		fmt.Printf("Output: %s\n", b)
	}

	if err != nil {
		panic(err)
	}

	/**
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
	**/

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

/**func (c *Config) Parse(data []byte) error {
	if err := yaml.Unmarshal(data, c); err != nil {
		return err
	}
	if c.Service.Type == "" {
		return errors.New("Kitchen config: invalid `hostname`")
	}
	// ... same check for Username, SSHKey, and Port ...
	return nil
}**/
