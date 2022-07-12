package no_2262

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test2262(t *testing.T) {
	require.Equal(t, 1, appealSum("a"))
	require.Equal(t, 4, appealSum("ab"))
	require.Equal(t, 10, appealSum("abc"))
	require.Equal(t, 20, appealSum("abcd"))
	require.Equal(t, 3, appealSum("aa"))
	require.Equal(t, 8, appealSum("aab"))
	require.Equal(t, 9, appealSum("aba"))
	require.Equal(t, 28, appealSum("abbca"))
	require.Equal(t, 23, appealSum("aabba"))
	require.Equal(t, 6, appealSum("aaa"))
	require.Equal(t, 30, appealSum("aaabbb"))
}
