package no_121

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test121(t *testing.T) {
	require.Equal(t, 5, maxProfit([]int{7, 1, 5, 3, 6, 4}))
	require.Equal(t, 0, maxProfit([]int{7, 6, 4, 3, 1}))
}
