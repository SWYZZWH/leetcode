package no_1293

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test1293(t *testing.T) {
	require.Equal(t, 6, shortestPath([][]int{{0, 0, 0}, {1, 1, 0}, {0, 0, 0}, {0, 1, 1}, {0, 0, 0}, {1, 1, 0}}, 1))
	//require.Equal(t, 6, shortestPath([][]int{{0, 0, 0}, {1, 1, 0}, {0, 0, 0}, {0, 1, 1}, {0, 0, 0}}, 1))
	//require.Equal(t, -1, shortestPath([][]int{{0, 1, 1}, {1, 1, 1}, {1, 0, 0}}, 1))
}
