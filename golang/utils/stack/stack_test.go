package stack

import "testing"
import "github.com/stretchr/testify/require"

func TestStack(t *testing.T) {
	stack := Stack{}
	_, ok := stack.Pop()
	require.False(t, ok)
	stack.Push(1)
	stack.Push(2)
	val1, ok := stack.Pop()
	require.Equal(t,2, val1)
	require.True(t, ok)
	val2, ok := stack.Pop()
	require.Equal(t, 1, val2)
	require.True(t, ok)
}