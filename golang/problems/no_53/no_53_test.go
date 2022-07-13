package no_53

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestMaxSubArray(t *testing.T) {
	require.Equal(t, 5, maxSubArray([]int{5}))
	require.Equal(t, -1, maxSubArray([]int{-1}))
	require.Equal(t, 8, maxSubArray([]int{5, -10, 8}))
	require.Equal(t, 14, maxSubArray([]int{5, -10, 8, 2, -2, 6}))
	require.Equal(t, 23, maxSubArray([]int{5, 4, -1, 7, 8}))
	require.Equal(t, 6, maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
