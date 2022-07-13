package no_11

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test11(t *testing.T) {
	require.Equal(t, 49, maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
	require.Equal(t, 1, maxArea([]int{1, 1}))
}
