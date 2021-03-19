# Learning History

## 1.Install

I recommend you to see the below website (Japanese)

https://qiita.com/koralle/items/7a16772ad1d2e2e34682

1. Refer to the official website below and follow the steps to install

https://golang.org/doc/install

After completing the settings, enter the following command in order to set up a login shell

```
$ echo 'export PATH="$GOROOT/bin/$PATH"' >> ~/.zshenv
$ echo 'export PATH="$PATH:$GOPATH/bin"' >> ~/.zshenv
```

if you don't know what is zshenv, check the below website(japanese)

https://suwaru.tokyo/zshenv/

2. Setup Goenv(Optional)

```
git clone https://github.com/syndbg/goenv.git ~/.goenv
```

```
$ echo 'export GOENV_ROOT="$HOME/.goenv"' >> ~/.bash_profile
$ echo 'export PATH="$GOENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(goenv init -)"' >> ~/.bash_profile
```

if you don't know .bash_profile, check the below website(japanese)

https://qiita.com/shyamahira/items/260862743e4c9794b5d2

Check after restarting the shell

```
$ goenv -v
goenv 2.0.0beta11
```

3. Allow Go project development outside of $ GOPATH

```
go env -w GO111MODULE=on
go env GO111MODULE
on
```

## 2.Hello World

This time, create a folder hierarchy like the one below

```
sample-proj
├── add
│   ├── add.go
│   └── go.mod
├── go.mod
└── main.go
```

1. Enter the following command to create a folder

```
mkdir 1.hello_world && cd $_
go mod init 1.hello_world
mkdir add && cd $_
go mod init add
```

2. Create a go script

```go main.go
package main

import (
    "fmt"
    "os"
    "sample-proj/add"
    "strconv"
)

func main() {
	fmt.Println("Hello World")
    a, _ := strconv.Atoi(os.Args[1])
    b, _ := strconv.Atoi(os.Args[2])
    fmt.Println(add.Add(a, b))
}
```

```go add.go
package add

// Note that if Add has the same name as add,
//it cannot be referenced from the outside.
func Add(a, b int) int {
    return a + b
}
```

`

3. Change the module so that it can be referenced

```
module 1.hello_world

go 1.15

replace 1.hello_world/add => ./add
```

4. Add module add

```
go get hello_world/add
```

5. Build and run

```
go run main.go 4 5
Hello World
9
```

### Tips

how to add module

````
go get github.com/gin-gonic/gin
```

The recommended development location is the location where the project is created in go / src of the local environment.

## Build a web server
````
