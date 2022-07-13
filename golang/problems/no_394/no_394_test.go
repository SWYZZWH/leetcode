package no_394

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test394(t *testing.T) {
	require.Equal(t, "a", decodeString("a"))
	require.Equal(t, "", decodeString(""))
	require.Equal(t, "ab", decodeString("[ab]"))
	require.Equal(t, "ababab", decodeString("3[ab]"))
	require.Equal(t, "bb", decodeString("1[2[b]]"))
	require.Equal(t, "aaabcbc", decodeString("3[a]2[bc]"))
	require.Equal(t, "accaccacc", decodeString("3[a2[c]]"))
	require.Equal(t, "abcabccdcdcdef", decodeString("2[abc]3[cd]ef"))
}
