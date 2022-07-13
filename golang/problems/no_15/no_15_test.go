package no_15

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test15(t *testing.T) {
	require.Equal(t, [][]int{{-1, 0, 1}, {-1, -1, 2}}, threeSum([]int{-1, 0, 1, 2, -1, -4}))
	require.Equal(t, [][]int{}, threeSum([]int{0, 1, 1}))
	require.Equal(t, [][]int{{0, 0, 0}}, threeSum([]int{0, 0, 0}))
	require.Equal(t, [][]int{{0, 0, 0}}, threeSum([]int{0, 0, 0, 0}))
}
