package no_71

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test71(t *testing.T) {
	require.Equal(t, "/home", simplifyPath("/home/"))
	require.Equal(t, "/", simplifyPath("/../"))
	require.Equal(t, "/home/foo", simplifyPath("/home//.//foo"))
	require.Equal(t, "/home", simplifyPath("./../home///"))
	require.Equal(t, "/", simplifyPath(""))
	require.Equal(t, "/...", simplifyPath("/..."))
	require.Equal(t, "/..hidden", simplifyPath("/..hidden"))
}
