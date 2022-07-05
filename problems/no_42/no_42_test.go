package no_42

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test42(t *testing.T) {
	require.Equal(t, 6, trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
	require.Equal(t, 9, trap([]int{4, 2, 0, 3, 2, 5}))
	require.Equal(t, 3, trap([]int{2, 1, 0, 2}))
	require.Equal(t, 0, trap([]int{2, 1}))
	require.Equal(t, 0, trap([]int{2}))
	require.Equal(t, 1, trap([]int{2, 1, 2}))
	require.Equal(t, 3, trap([]int{2, 1, 2, 1, 2, 1, 2}))
}
