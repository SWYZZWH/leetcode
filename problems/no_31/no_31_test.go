package no_31

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test31(t *testing.T) {
	nums := []int{1, 2, 3}
	nextPermutation(nums)
	require.Equal(t, []int{1, 3, 2}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{2, 1, 3}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{2, 3, 1}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{3, 1, 2}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{3, 2, 1}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{1, 2, 3}, nums)

	nums = []int{1, 1, 5}
	nextPermutation(nums)
	require.Equal(t, []int{1, 5, 1}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{5, 1, 1}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{1, 1, 5}, nums)

	nums = []int{1, 1}
	nextPermutation(nums)
	require.Equal(t, []int{1, 1}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{1, 1}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{1, 1}, nums)

	nums = []int{0}
	nextPermutation(nums)
	require.Equal(t, []int{0}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{0}, nums)
	nextPermutation(nums)
	require.Equal(t, []int{0}, nums)

	nums = []int{5, 4, 7, 5, 3, 2}
	nextPermutation(nums)
	require.Equal(t, []int{5, 5, 2, 3, 4, 7}, nums)

	nums = []int{4, 2, 0, 2, 3, 2, 0}
	nextPermutation(nums)
	require.Equal(t, []int{4, 2, 0, 3, 0, 2, 2}, nums)
}
