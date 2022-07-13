package no_20

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test20(t *testing.T) {
	require.True(t, isValid(""))
	require.True(t, isValid("(())"))
	require.True(t, isValid("()[]{}"))
	require.True(t, isValid("([]){([[]])}"))

	require.False(t, isValid("([)]"))
	require.False(t, isValid("("))
	require.False(t, isValid("(]"))
	require.False(t, isValid("())"))
	require.False(t, isValid("())!"))
}