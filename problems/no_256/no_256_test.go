package no_256

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test256(t *testing.T) {
	require.Equal(t, 10, minCost([][]int{[]int{17, 2, 17}, []int{16, 16, 5}, []int{14, 3, 19}}))
	require.Equal(t, 2, minCost([][]int{[]int{7, 6, 2}}))
	require.Equal(t, 7, minCost([][]int{[]int{7, 7, 7}}))
	require.Equal(t, 0, minCost([][]int{[]int{0, 7, 0}}))
}
