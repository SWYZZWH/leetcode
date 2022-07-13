package no_227

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test227(t *testing.T) {
	require.Equal(t, 0, calculate("0"))
	require.Equal(t, 123, calculate(" 123   "))
	require.Equal(t, 2, calculate(" 1 * 2"))
	require.Equal(t, 102, calculate(" 1 * 2 + 100"))
	require.Equal(t, 102, calculate("1 /2 + 1 * 2 + 100"))
	require.Equal(t, 99, calculate("1 /2 + 1 - 1 * 2 + 100"))
}
