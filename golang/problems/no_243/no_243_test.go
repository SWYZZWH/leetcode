package no_243

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test243(t *testing.T) {
	require.Equal(t, 1, shortestDistance([]string{"a", "b", "c"}, "a", "b"))
	require.Equal(t, 1, shortestDistance([]string{"a", "b", "a"}, "a", "b"))
	require.Equal(t, 1, shortestDistance([]string{"a", "b", "c", "a"}, "a", "b"))
	require.Equal(t, 1, shortestDistance([]string{"d", "b", "c", "a", "b"}, "a", "b"))
	require.Equal(t, 1, shortestDistance([]string{"a", "a", "b", "a", "b"}, "a", "b"))
	require.Equal(t, 2, shortestDistance([]string{"a", "c", "b", "c", "a"}, "a", "b"))
}
