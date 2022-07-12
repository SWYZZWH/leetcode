package no_828

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test828(t *testing.T) {
	require.Equal(t, 1, uniqueLetterString("A"))
	require.Equal(t, 4, uniqueLetterString("AB"))
	require.Equal(t, 10, uniqueLetterString("ABC"))
	require.Equal(t, 2, uniqueLetterString("AA"))
	require.Equal(t, 8, uniqueLetterString("ABA"))
	require.Equal(t, 12, uniqueLetterString("ABAB"))
	require.Equal(t, 16, uniqueLetterString("ABABA"))
	require.Equal(t, 3, uniqueLetterString("AAA"))
	require.Equal(t, 6, uniqueLetterString("AAB"))
	require.Equal(t, 20, uniqueLetterString("ABCD"))
	require.Equal(t, 15, uniqueLetterString("AABAA"))
	require.Equal(t, 11, uniqueLetterString("AABA"))
	require.Equal(t, 77, uniqueLetterString("LEETCOEE"))
	require.Equal(t, 11, uniqueLetterString("ABAA"))
	require.Equal(t, 92, uniqueLetterString("LEETCODE"))
}
