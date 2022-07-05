package DSU

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestDSU(t *testing.T) {
	dsu := NewDSU(5)
	require.Equal(t, 1, dsu.Find(1))
	require.Equal(t, 0, dsu.Find(0))
	require.True(t, dsu.Find(0) != dsu.Find(1))

	dsu.Union(0, 1)
	require.True(t, dsu.Find(1) == 1 || dsu.Find(1) == 0)
	require.True(t, dsu.Find(0) == 1 || dsu.Find(0) == 0)
	require.True(t, dsu.Find(0) == dsu.Find(1))

	dsu.Union(2, 3)
	dsu.Union(2, 4)
	dsu.Union(0, 4)
	require.True(t, dsu.Find(0) == dsu.Find(1))
	require.True(t, dsu.Find(1) == dsu.Find(2))
	require.True(t, dsu.Find(2) == dsu.Find(3))
	require.True(t, dsu.Find(3) == dsu.Find(4))

	require.True(t, dsu.Find(5) == -1)
}

func TestDSUCompressed(t *testing.T) {
	dsu := NewDSU(5)
	dsu.Union(0, 1)
	dsu.Union(1, 2)
	dsu.Union(2, 3)
	dsu.Union(3, 4)
	require.Equal(t, []int{1, 2, 3, 4, 4}, dsu.parents)
	dsu.Find(2)
	require.Equal(t, []int{1, 2, 4, 4, 4}, dsu.parents)
	dsu.Find(0)
	require.Equal(t, []int{4, 4, 4, 4, 4}, dsu.parents)
}


func TestDisjointSetUnion_Size(t *testing.T) {
	dsu := NewDSU(7)
	dsu.Union(0, 1)
	dsu.Show()
	dsu.Union(2, 3)
	dsu.Show()
	dsu.Union(4, 5)
	dsu.Show()
	dsu.Union(5, 6)
	dsu.Show()
	dsu.Union(0, 4)
	dsu.Show()
	dsu.Union(2, 0)
	dsu.Show()
}