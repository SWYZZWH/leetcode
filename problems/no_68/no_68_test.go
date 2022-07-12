package no_68

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestFullJustify(t *testing.T) {
	require.Equal(t, []string{
		"This    is    an",
		"example  of text",
		"justification.  ",
	}, fullJustify([]string{
		"This", "is", "an", "example", "of", "text", "justification.",
	}, 16))

	require.Equal(t, []string{
		"What   must   be",
		"acknowledgment  ",
		"shall be        ",
	}, fullJustify([]string{
		"What", "must", "be", "acknowledgment", "shall", "be",
	}, 16))

	require.Equal(t, []string{
		"what",
	}, fullJustify([]string{
		"what",
	}, 4))

	require.Equal(t, []string{
		"what is ",
	}, fullJustify([]string{
		"what", "is",
	}, 8))

	require.Equal(t, []string{
		"abcde",
		"ab de",
	}, fullJustify([]string{
		"abcde", "ab", "de",
	}, 5))

	require.Equal(t, []string{
		"Science  is  what we",
		"understand      well",
		"enough to explain to",
		"a  computer.  Art is",
		"everything  else  we",
		"do                  ",
	}, fullJustify([]string{
		"Science", "is", "what", "we", "understand", "well", "enough",
		"to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do",
	}, 20))
}
