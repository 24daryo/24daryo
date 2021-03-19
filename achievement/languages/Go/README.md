# Learning History

## Install

I recommend you to see the below website (Japanese)

https://qiita.com/koralle/items/7a16772ad1d2e2e34682

1. Refer to the official website below and follow the steps to install

https://golang.org/doc/install

```
$ echo 'export PATH="$GOROOT/bin/$PATH"' >> ~/.zshenv
$ echo 'export PATH="$PATH:$GOPATH/bin"' >> ~/.zshenv
```

2. Setup Goenv(Optional)

```
git clone https://github.com/syndbg/goenv.git ~/.goenv
```

```
$ echo 'export GOENV_ROOT="$HOME/.goenv"' >> ~/.bash_profile
$ echo 'export PATH="$GOENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(goenv init -)"' >> ~/.bash_profile
```

Check after restarting the shell

```
$ goenv -v
goenv 2.0.0beta11
```

3. Allow Go project development outside of $ GOPATH

```
go env -w GO111MODULE=on
$ go env GO111MODULE
on
```

## Hello World

1. Initialize

```
go mod init example.com/hello
```

2. Create hello.golang

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

3. Run

```
go run .
```

### Tips

how to add module

```
go get github.com/gin-gonic/gin
```

The recommended development location is the location where the project is created in go / src of the local environment.

## Build a web server
