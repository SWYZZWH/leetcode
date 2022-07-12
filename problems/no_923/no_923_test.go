package no_923

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test923(t *testing.T) {
	require.Equal(t, 20, threeSumMulti([]int{1, 1, 2, 2, 3, 3, 4, 4, 5, 5}, 8))
	require.Equal(t, 12, threeSumMulti([]int{1, 1, 2, 2, 2, 2}, 5))
	require.Equal(t, 1, threeSumMulti([]int{2, 1, 3}, 6))
	require.Equal(t, 4, threeSumMulti([]int{2, 2, 2, 1, 3}, 6))
	require.Equal(t, 2, threeSumMulti([]int{1, 2, 0, 3, 2}, 4))
}
