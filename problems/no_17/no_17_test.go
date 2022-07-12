package no_17

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test17(t *testing.T) {
	require.Equal(t, 0, len(letterCombinations("")))
	require.Equal(t, 3, len(letterCombinations("2")))
	require.Equal(t, 9, len(letterCombinations("22")))
	require.Equal(t, 36, len(letterCombinations("229")))
	require.Nil(t, letterCombinations("29"))
}
