package queue

import (
	"testing"
)
import "github.com/stretchr/testify/require"

func TestQueue(t *testing.T) {
	q := Queue{}
	_, ok := q.Dequeue()
	require.False(t, ok)
	q.Enqueue(1)
	q.Enqueue(2)
	val1, ok := q.Dequeue()
	require.Equal(t,1, val1)
	require.True(t, ok)
	val2, ok := q.Dequeue()
	require.Equal(t, 2, val2)
	require.True(t, ok)
}