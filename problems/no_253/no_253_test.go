package no_253

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func Test253(t *testing.T) {
	require.Equal(t, 2, minMeetingRooms([][]int{{0, 30}, {5, 10}, {15, 20}}))
	require.Equal(t, 1, minMeetingRooms([][]int{{7, 10}, {2, 4}}))
}
