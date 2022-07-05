package no_4

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test4(t *testing.T) {
	require.Equal(t, 2.0, findMedianSortedArrays([]int{1, 3}, []int{2}))
	require.Equal(t, 2.0, findMedianSortedArrays([]int{2}, []int{1,3}))
	require.Equal(t, 2.0, findMedianSortedArrays([]int{1}, []int{3}))
	require.Equal(t, 2.0, findMedianSortedArrays([]int{3}, []int{1}))
	require.Equal(t, 2.5, findMedianSortedArrays([]int{1, 2}, []int{3, 4}))
	require.Equal(t, 2.5, findMedianSortedArrays([]int{3, 4}, []int{1, 2}))
}
