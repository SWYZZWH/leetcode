package no_252

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test252(t *testing.T) {
	require.Equal(t, false, canAttendMeetings([][]int{{0, 30}, {5, 10}, {15, 20}}))
	require.Equal(t, true, canAttendMeetings([][]int{{0, 10}, {10, 15}}))
	require.Equal(t, true, canAttendMeetings([][]int{{30, 40}, {20, 10}, {20, 30}}))
}
