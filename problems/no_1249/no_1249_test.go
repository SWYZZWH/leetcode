package no_1249

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestRemovePar(t *testing.T) {
	require.Equal(t,"()()", minRemoveToMakeValid("())()"))
	require.Equal(t,"lee(t(c)o)de", minRemoveToMakeValid("lee(t(c)o)de)"))
	require.Equal(t,"ab(c)d", minRemoveToMakeValid("a)b(c)d"))
	require.Equal(t,"", minRemoveToMakeValid("))(("))
}
