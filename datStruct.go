package main
import "fmt"
func main(){
    // Declare map with string as key, int list as the values
    myMap:= map[string][]int{}
    //Populate
    myMap["a"]=[]int{10,20,30}
    myMap["b"] =[]int{40,50,60}
    // Example of appending
    // Good resource to look at https://openmymind.net/Controlling-Array-Growth-In-Golang/
    myMap["b"]=append(myMap["b"],42)
    // Print
    fmt.Printf("%v \n %v \n", myMap["a"], myMap["b"])
    //fmt.Printf("%v", myMap)
    println(myMap)

    //Let us try a nother menthod
    // make(map[key-type]value-type)
    //map2 := make(map[string]int)
}


