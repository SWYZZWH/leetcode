package no_9

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test9(t *testing.T) {
	require.Equal(t, true, isPalindrome(121))
	require.Equal(t, false, isPalindrome(-121))
	require.Equal(t, true, isPalindrome(1))
	require.Equal(t, true, isPalindrome(1234321))
	require.Equal(t, true, isPalindrome(0))
	require.Equal(t, false, isPalindrome(12))
	require.Equal(t, false, isPalindrome(123331))
}
