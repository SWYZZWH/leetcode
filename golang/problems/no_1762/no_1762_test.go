package no_1762

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test1762(t *testing.T) {
	require.Equal(t, []int{0, 2, 3}, findBuildings([]int{4, 2, 3, 1}))
	require.Equal(t, []int{0, 1, 2, 3}, findBuildings([]int{4, 3, 2, 1}))
	require.Equal(t, []int{3}, findBuildings([]int{1, 3, 2, 4}))
	require.Equal(t, []int{0}, findBuildings([]int{1}))
	require.Equal(t, []int{2}, findBuildings([]int{1,1,1}))
}
