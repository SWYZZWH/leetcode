package no_1904

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test1904(t *testing.T) {
	require.Equal(t, 1, numberOfRounds("09:31", "10:14"))
	require.Equal(t, 2, numberOfRounds("09:31", "10:15"))
	require.Equal(t, 12, numberOfRounds("00:00", "03:00"))
	require.Equal(t, 9, numberOfRounds("21:30", "23:59"))
	require.Equal(t, 22, numberOfRounds("21:30", "03:00"))
	require.Equal(t, 1, numberOfRounds("23:45", "00:00"))
	require.Equal(t, 1, numberOfRounds("23:45", "00:01"))
	require.Equal(t, 95, numberOfRounds("00:00", "23:59"))
	require.Equal(t, 0, numberOfRounds("12:00", "12:00"))
	require.Equal(t, 0, numberOfRounds("12:00", "12:01"))
	require.Equal(t, 95, numberOfRounds("12:01", "12:00"))
	require.Equal(t, 0, numberOfRounds("23:46", "00:01"))
}

func TestUpper(t *testing.T) {
	require.Equal(t, 0, upper(0))
	require.Equal(t, 1, upper(1))
	require.Equal(t, 1, upper(15))
	require.Equal(t, 4, upper(59))
	require.Equal(t, 0, lower(0))
	require.Equal(t, 0, lower(1))
	require.Equal(t, 0, lower(14))
	require.Equal(t, 1, lower(15))
}
