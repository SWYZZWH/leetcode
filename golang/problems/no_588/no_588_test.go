package no_588

import (
	"fmt"
	"testing"
)

func Test588(t *testing.T) {
	fs := Constructor()
	fmt.Printf("%v\n", fs.Ls("/"))
	fs.Mkdir("/a/b/c")
	fs.Mkdir("/a2")
	fs.Mkdir("/a1")
	fs.AddContentToFile("/a/b/c/d", "hello")
	fmt.Printf("%v\n", fs.Ls("/"))
	fmt.Printf("%v\n", fs.Ls("/a/b/c/d"))
	fmt.Printf("%v\n",fs.ReadContentFromFile("/a/b/c/d"))
	fs.AddContentToFile("/a/b/c/d", " world")
	fmt.Printf("%v\n", fs.Ls("/"))
	println(fs.ReadContentFromFile("/a/b/c/d"))
}
