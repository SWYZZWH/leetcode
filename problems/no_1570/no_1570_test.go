package no_1570

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test1570(t *testing.T) {
	v1, v2 := Constructor([]int{1, 0, 0, 2, 3}), Constructor([]int{0, 3, 0, 4, 0})
	require.Equal(t, 8, (&v1).dotProduct(v2))

	v1, v2 = Constructor([]int{1}), Constructor([]int{100})
	require.Equal(t, 100, (&v1).dotProduct(v2))

	v1, v2 = Constructor([]int{0}), Constructor([]int{1})
	require.Equal(t, 0, (&v1).dotProduct(v2))

	v1, v2 = Constructor([]int{0, 1, 0, 0, 0}), Constructor([]int{0, 0, 0, 0, 2})
	require.Equal(t, 0, (&v1).dotProduct(v2))
}
