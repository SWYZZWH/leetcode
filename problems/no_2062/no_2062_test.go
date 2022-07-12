package no_2062

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test2062(t *testing.T) {
	require.Equal(t, 0, countVowelSubstrings("a"))
	require.Equal(t, 0, countVowelSubstrings("s"))
	require.Equal(t, 1, countVowelSubstrings("aeiou"))
	require.Equal(t, 0, countVowelSubstrings("aesious"))
	require.Equal(t, 1, countVowelSubstrings("aesiousaeiou"))
	require.Equal(t, 4, countVowelSubstrings("aaeeiioouu"))
	require.Equal(t, 2, countVowelSubstrings("aeiouu"))
	require.Equal(t, 0, countVowelSubstrings("unicornarihan"))
	require.Equal(t, 7, countVowelSubstrings("cuaieuouac"))
}
