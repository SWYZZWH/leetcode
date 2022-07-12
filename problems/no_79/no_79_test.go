package no_79

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test79(t *testing.T) {
	require.Equal(t, true, exist([][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'E', 'S'}, {'A', 'D', 'E', 'E'}}, "ABCESEEEFS"))
}
