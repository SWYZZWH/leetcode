package no_252

import "sort"

// 252. Meeting Rooms
// Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

// s1: brute force O(n ^ 2)
// s2: sort
func canAttendMeetings(intervals [][]int) bool {

	// n log n
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for i := 0; i < len(intervals)-1; i++ {
		if intervals[i][1] > intervals[i+1][0] {
			return false
		}
	}
	return true
}
