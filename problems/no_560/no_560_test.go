package no_560

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test560(t *testing.T) {
	require.Equal(t, 2, subarraySum([]int{1, 1, 1}, 2))
	require.Equal(t, 2, subarraySum([]int{1, 2, 3}, 3))
	require.Equal(t, 0, subarraySum([]int{1, 2, 3}, -1))
	require.Equal(t, 1, subarraySum([]int{1}, 1))
	require.Equal(t, 0, subarraySum([]int{2}, 1))
	require.Equal(t, 6, subarraySum([]int{1, -1, 1, -1, 1}, 0))
}
