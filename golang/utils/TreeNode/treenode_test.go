package TreeNode

import "testing"

func TestFromList(t *testing.T) {
	FromList([]int{3, 9, 20, -1, -1, 15, 7}).printTree()
	println()
	FromList([]int{3, 9, 8, 4, 0, 1, 7}).printTree()
	println()
	FromList([]int{3, 9, 8, 4, 0, 1, 7, -1, -1, -1, 2, 5}).printTree()
	println()
}
