package no_408

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test408(t *testing.T) {
	require.Equal(t, true, validWordAbbreviation("substitution", "s10n"))
	require.Equal(t, true, validWordAbbreviation("substitution", "sub4u4"))
	require.Equal(t, true, validWordAbbreviation("substitution", "12"))
	require.Equal(t, true, validWordAbbreviation("substitution", "su3i1u2on"))
	require.Equal(t, true, validWordAbbreviation("substitution", "substitution"))

	require.Equal(t, false, validWordAbbreviation("substitution", "s55n"))
	require.Equal(t, false, validWordAbbreviation("substitution", "s010n"))
	require.Equal(t, false, validWordAbbreviation("substitution", "s0ubstitution"))

	require.Equal(t, false, validWordAbbreviation("a", "2"))
	require.Equal(t, false, validWordAbbreviation("hi", "1"))
	require.Equal(t, false, validWordAbbreviation("hi", "2i"))
}
