package no_751

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test751(t *testing.T) {
	require.Equal(t, []string{"255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"}, ipToCIDR("255.0.0.7", 10))
	require.Equal(t, []string{"255.0.0.7/32"}, ipToCIDR("255.0.0.7", 1))
	require.Equal(t, []string{"255.0.0.7/32", "255.0.0.8/31"}, ipToCIDR("255.0.0.7", 3))
	require.Equal(t, []string{"255.0.0.7/32", "255.0.0.8/31", "255.0.0.10/32"}, ipToCIDR("255.0.0.7", 4))
	require.Equal(t, []string{"255.0.0.7/32", "255.0.0.8/32"}, ipToCIDR("255.0.0.7", 2))
}
