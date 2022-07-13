package no_71

import "strings"

//71. Simplify Path

//Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
//
//In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
//
//The canonical path should have the following format:
//
//The path starts with a single slash '/'.
//Any two directories are separated by a single slash '/'.
//The path does not end with a trailing '/'.
//The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
//Return the simplified canonical path.

// only consider valid situation
func simplifyPath(path string) string {
	dirs := []string{}
	for i := 0; i < len(path); i++ {
		// only "." || ".." will be considered reserved, "..." is file name
		if i < len(path)-1 && path[i:i+2] == ".." && (i == len(path)-2 || path[i+2] == '/') {
			if len(dirs) > 0 {
				dirs = dirs[:len(dirs)-1]
			}
		} else if path[i] == '/' || (path[i] == '.' && (i == len(path)-1 || path[i+1] == '/')) {
			continue
		} else {
			start := i
			for i < len(path) && path[i] != '/' {
				i++
			}
			dirs = append(dirs, path[start:i])
		}
	}
	return strings.Join([]string{"/", strings.Join(dirs, "/")}, "")
}
