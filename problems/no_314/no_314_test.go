package no_314

import (
	TreeNode2 "awesomeProject/utils/TreeNode"
	"github.com/stretchr/testify/require"
	"testing"
)

func Test314(t *testing.T) {
	require.Equal(t, [][]int{{3}}, verticalOrder(TreeNode2.FromList([]int{3})))
	require.Equal(t, [][]int(nil), verticalOrder(TreeNode2.FromList([]int{-1})))
	require.Equal(t, [][]int{{3}, {1}}, verticalOrder(TreeNode2.FromList([]int{3, -1, 1})))
	require.Equal(t, [][]int{{9}, {3, 15}, {20}, {7}}, verticalOrder(TreeNode2.FromList([]int{3, 9, 20, -1, -1, 15, 7})))
	require.Equal(t, [][]int{{4}, {9}, {3, 0, 1}, {8}, {7}}, verticalOrder(TreeNode2.FromList([]int{3, 9, 8, 4, 0, 1, 7})))
	require.Equal(t, [][]int{{4}, {9, 5}, {3, 0, 1}, {8, 2}, {7}}, verticalOrder(TreeNode2.FromList([]int{3, 9, 8, 4, 0, 1, 7, -1, -1, -1, 2, 5})))
}
