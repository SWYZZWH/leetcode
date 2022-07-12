package no_14

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test14(t *testing.T) {
	require.Equal(t, "fl", longestCommonPrefix([]string{"flower", "flow", "flight"}))
	require.Equal(t, "", longestCommonPrefix([]string{"dog", "racecar", "car"}))
	require.Equal(t, "car", longestCommonPrefix([]string{"car"}))
	require.Equal(t, "", longestCommonPrefix([]string{""}))
	require.Equal(t, "", longestCommonPrefix([]string{"", ""}))
	require.Equal(t, "", longestCommonPrefix([]string{"", "a"}))
	require.Equal(t, "a", longestCommonPrefix([]string{"a", "a"}))
	require.Equal(t, "bb", longestCommonPrefix([]string{"bb", "bb"}))
}
