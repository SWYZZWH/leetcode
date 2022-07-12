package no_5

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test5(t *testing.T) {
	require.Equal(t, "bab", longestPalindrome("babad"))
	require.Equal(t, "bb", longestPalindrome("cbbd"))
	require.Equal(t, "", longestPalindrome(""))
	require.Equal(t, "a", longestPalindrome("a"))
	require.Equal(t, "a", longestPalindrome("abcdefg"))
	require.Equal(t, "aabaa", longestPalindrome("aabaadefg"))
	require.Equal(t, "aabaa", longestPalindrome("aabaaccd"))
	require.Equal(t, "aca", longestPalindrome("aacabdkacaa"))
}
