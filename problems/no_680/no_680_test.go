package no_680

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test680(t *testing.T) {
	require.Equal(t, true, validPalindrome("aba"))
	require.Equal(t, true, validPalindrome("abca"))
	require.Equal(t, false, validPalindrome("abc"))
	require.Equal(t, true, validPalindrome("a"))
	require.Equal(t, true, validPalindrome("ab"))
	require.Equal(t, true, validPalindrome("ababa"))
	require.Equal(t, false, validPalindrome("eeccccbebaeeabebccceea"))
}