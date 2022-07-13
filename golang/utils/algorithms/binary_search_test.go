package algorithms

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestFind(t *testing.T) {
	idx, ok := find([]int{2, 4, 6, 8, 10}, 1)
	require.False(t, ok)
	require.Equal(t, 0, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 2)
	require.True(t, ok)
	require.Equal(t, 0, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 4)
	require.True(t, ok)
	require.Equal(t, 1, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 6)
	require.True(t, ok)
	require.Equal(t, 2, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 7)
	require.False(t, ok)
	require.Equal(t, 3, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 8)
	require.True(t, ok)
	require.Equal(t, 3, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 9)
	require.False(t, ok)
	require.Equal(t, 4, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 10)
	require.True(t, ok)
	require.Equal(t, 4, idx)

	idx, ok = find([]int{2, 4, 6, 8, 10}, 11)
	require.False(t, ok)
	require.Equal(t, 5, idx)
}
