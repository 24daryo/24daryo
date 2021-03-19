package main

import (
    "fmt"
    "os"
    "1.hello_world/add"
    "strconv"
)

func main() {
	fmt.Println("Hello World")
    a, _ := strconv.Atoi(os.Args[1])
    b, _ := strconv.Atoi(os.Args[2])
    fmt.Println(add.Add(a, b))
}