package no_236

import (
	TreeNode2 "awesomeProject/utils/TreeNode"
	"github.com/stretchr/testify/require"
	"testing"
)

func Test236(t *testing.T) {
	root := TreeNode2.FromList([]int{3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4})
	require.Equal(t, root, lowestCommonAncestor(root, root.Left, root.Right))
	require.Equal(t, root.Left, lowestCommonAncestor(root, root.Left, root.Left.Right.Right))
}
