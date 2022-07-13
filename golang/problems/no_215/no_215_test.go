package no_215

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test215(t *testing.T) {
	require.Equal(t, 6, findKthLargest([]int{3, 2, 1, 5, 6, 4}, 1))
	require.Equal(t, 5, findKthLargest([]int{3, 2, 1, 5, 6, 4}, 2))
	require.Equal(t, 4, findKthLargest([]int{3, 2, 1, 5, 6, 4}, 3))
	require.Equal(t, 3, findKthLargest([]int{3, 2, 1, 5, 6, 4}, 4))
	require.Equal(t, 2, findKthLargest([]int{3, 2, 1, 5, 6, 4}, 5))
	require.Equal(t, 1, findKthLargest([]int{3, 2, 1, 5, 6, 4}, 6))

	require.Equal(t, 6, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 1))
	require.Equal(t, 5, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 2))
	require.Equal(t, 5, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 3))
	require.Equal(t, 4, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4))
	require.Equal(t, 3, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 5))
	require.Equal(t, 3, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 6))
	require.Equal(t, 2, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 7))
	require.Equal(t, 2, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 8))
	require.Equal(t, 1, findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 9))
}
