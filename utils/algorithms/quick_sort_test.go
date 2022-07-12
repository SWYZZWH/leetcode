package algorithms

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestQuickSort(t *testing.T) {
	require.Equal(t, []int{1, 2, 3, 4, 5}, quickSort([]int{2, 3, 1, 4, 5}))
	require.Equal(t, []int{1}, quickSort([]int{1}))
	require.Equal(t, []int{1, 1, 1}, quickSort([]int{1, 1, 1}))
	require.Equal(t, []int{1, 1, 2, 2, 3, 3}, quickSort([]int{1, 1, 2, 2, 3, 3}))
	require.Equal(t, []int{1, 1, 2, 2, 3, 3}, quickSort([]int{3, 3, 1, 1, 2, 2}))
}
