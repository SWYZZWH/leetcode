package no_588

import (
	"sort"
	"strings"
)

//588. Design In-Memory File System
//Design a data structure that simulates an in-memory file system.
//
//Implement the FileSystem class:
//
//FileSystem() Initializes the object of the system.
//List<String> ls(String path)
//If path is a file path, returns a list that only contains this file's name.
//If path is a directory path, returns the list of file and directory names in this directory.
//The answer should in lexicographic order.
//void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
//void addContentToFile(String filePath, String content)
//If filePath does not exist, creates that file containing given content.
//If filePath already exists, appends the given content to original content.
//String readContentFromFile(String filePath) Returns the content in the file at filePath.

// only thing to be noticed is LS filepath

type Node struct {
	nodeType int              // 0 for dir, 1 for regular file
	name     string           // path of itself
	content  string           // if it is a file, may have content
	children map[string]*Node // sub dirs
}

// FileSystem may use cache to accelerate search
// map[string]*Node{"/a": Node1, "/b": Node2}
type FileSystem struct {
	root *Node
}

func Constructor() FileSystem {
	root := Node{
		nodeType: 0,
		name:     "/",
		content:  "",
		children: map[string]*Node{},
	}
	return FileSystem{root: &root}
}

func (this *FileSystem) findNode(path string) *Node {
	if path == "/" {
		return this.root
	}
	paths := strings.Split(path, "/")[1:]
	n := this.root
	for _, p := range paths {
		n = n.children[p]
		if n == nil {
			return n
		}
	}
	return n
}

func (this *FileSystem) findOrCreateNode(path string, node *Node) {
	paths := strings.Split(path, "/")[1:]
	dirs := paths
	if node != nil && node.nodeType == 1 {
		dirs = paths[:len(paths)-1]
	}
	// create dir
	n := this.root
	for _, p := range dirs {
		if child, ok := n.children[p]; !ok {
			newNode := Node{
				nodeType: 0,
				name:     p,
				content:  "",
				children: map[string]*Node{},
			}
			n.children[p] = &newNode
			n = &newNode
		} else {
			n = child
		}
	}
	if node != nil && node.nodeType == 1 {
		n.children[node.name] = node
	}
}

func (this *FileSystem) Ls(path string) []string {
	n := this.findNode(path)
	if n.nodeType == 1 {
		return []string{n.name}
	}
	dirs := make([]string, len(n.children))
	i := 0
	for name, _ := range n.children {
		dirs[i] = name
		i ++
	}
	sort.Strings(dirs)
	return dirs
}

func (this *FileSystem) Mkdir(path string) {
	this.findOrCreateNode(path, nil)
}

func (this *FileSystem) AddContentToFile(filePath string, content string) {
	paths := strings.Split(filePath, "/")[1:]
	n := this.findNode(filePath)
	if n != nil {
		n.content = strings.Join([]string{n.content, content}, "")
	} else {
		this.findOrCreateNode(filePath, &Node{
			nodeType: 1,
			name:     paths[len(paths) - 1],
			content:  content,
			children: map[string]*Node{},
		})
	}
}

func (this *FileSystem) ReadContentFromFile(filePath string) string {
	n := this.findNode(filePath)
	return n.content
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ls(path);
 * obj.Mkdir(path);
 * obj.AddContentToFile(filePath,content);
 * param_4 := obj.ReadContentFromFile(filePath);
 */
