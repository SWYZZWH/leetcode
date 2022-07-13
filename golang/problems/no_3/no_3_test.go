package no_3

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test3(t *testing.T) {
	//require.Equal(t, 3, lengthOfLongestSubstring("abcabcbb"))
	//require.Equal(t, 1, lengthOfLongestSubstring("bbbbb"))
	//require.Equal(t, 3, lengthOfLongestSubstring("pwwkew"))
	//require.Equal(t, 1, lengthOfLongestSubstring("a"))
	//require.Equal(t, 2, lengthOfLongestSubstring("au"))
	require.Equal(t, 2, lengthOfLongestSubstring("abba"))
	require.Equal(t, 3, lengthOfLongestSubstring("abacc"))
}