package no_224

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test224(t *testing.T) {
	require.Equal(t, 1, calculate("1"))
	require.Equal(t, -1, calculate("-1"))
	require.Equal(t, -193284, calculate("-193284"))
	require.Equal(t, 0, calculate("-0"))
	require.Equal(t, 0, calculate("0"))
	require.Equal(t, 3, calculate("1 + 2"))
	require.Equal(t, -1, calculate("1 - 2"))
	require.Equal(t, -2, calculate("(1 - 2) - 1"))
	require.Equal(t, -2, calculate("-1 + 1 + (1 - 2) - 1"))
	require.Equal(t, -2, calculate("((-1 + 1 + (1 - 2) - 1))"))
	require.Equal(t, 1, calculate("-1 + 1 + (1 - 2 + (3 + (  1 + (-1))) ) - 1"))
	require.Equal(t, 3, calculate(" 2-1 + 2 "))
}
