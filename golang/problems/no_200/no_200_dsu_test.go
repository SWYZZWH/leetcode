package no_200

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test200Dsu(t *testing.T) {
	grid1 := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	}
	require.Equal(t, 1, numIslandsDsu(grid1))

	grid2 := [][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '1', '0', '0'},
		{'0', '0', '0', '1', '1'},
	}
	require.Equal(t, 3, numIslandsDsu(grid2))

	grid3 := [][]byte{
		{'1', '1', '0', '1', '0'},
	}
	require.Equal(t, 2, numIslandsDsu(grid3))

	grid4 := [][]byte{
		{'1'},
	}
	require.Equal(t, 1, numIslandsDsu(grid4))

	grid5 := [][]byte{
		{'0'},
	}
	require.Equal(t, 0, numIslandsDsu(grid5))
}