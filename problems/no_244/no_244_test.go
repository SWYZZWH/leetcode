package no_244

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test244(t *testing.T) {
	wd := Constructor([]string{"d", "b", "c", "a", "b", "c", "a"})
	require.Equal(t, 1, wd.Shortest("a", "b"))
	require.Equal(t, 1, wd.Shortest("d", "b"))
	require.Equal(t, 3, wd.Shortest("a", "d"))
}
