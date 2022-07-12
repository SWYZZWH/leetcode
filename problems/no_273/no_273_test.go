package no_273

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test273(t *testing.T) {
	require.Equal(t, "Zero", numberToWords(0))
	require.Equal(t, "Nine", numberToWords(9))
	require.Equal(t, "Thirteen", numberToWords(13))
	require.Equal(t, "Twenty", numberToWords(20))
	require.Equal(t, "Thirty One", numberToWords(31))
	require.Equal(t, "One Hundred Thirty One", numberToWords(131))
	require.Equal(t, "One Hundred", numberToWords(100))
	require.Equal(t, "One Thousand", numberToWords(1000))
	require.Equal(t, "One Thousand One Hundred Twelve", numberToWords(1112))
	require.Equal(t, "One Thousand Thirty One", numberToWords(1031))
	require.Equal(t, "Twelve Thousand", numberToWords(12000))
	require.Equal(t, "One Million Twelve Thousand Two", numberToWords(1012002))
	require.Equal(t, "One Billion One Million Twelve Thousand Two", numberToWords(1001012002))
}
