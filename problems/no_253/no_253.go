package no_253

import (
	"container/heap"
	"sort"
)

// 253. Meeting Rooms II
// Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

// the interesting part is :
// [0, 3] [1, 4] equals to [0,4] [1,3]
// so we keep recording the right borders in ascending order [righti1, righti2, ...], if we find a left > righti1, then righti1 can be removed
// min meeting rooms equals to len of right borders we keep

// right borders will be saved in a priority queue

type borders []int

func (b borders) Less(i, j int) bool {
	return b[i] < b[j]
}

func (b borders) Len() int {
	return len(b)
}

func (b borders) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}

func (b *borders) Pop() interface{} {
	ret := (*b)[len(*b)-1]
	*b = (*b)[:len(*b)-1]
	return ret
}

func (b *borders) Push(x any) {
	*b = append(*b, x.(int))
}

func (b *borders) Top() int {
	return (*b)[0]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minMeetingRooms(intervals [][]int) int {
	if len(intervals) == 0 {
		return 0
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	ends := &borders{}
	heap.Init(ends)
	heap.Push(ends, intervals[0][1])
	ret, rightMin := 1, intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		for len(*ends) != 0 && intervals[i][0] >= (*ends).Top() {
			rightMin = heap.Pop(ends).(int)
		}
		rightMin = min(rightMin, intervals[i][1])
		heap.Push(ends, intervals[i][1])
		ret = max(len(*ends), ret)
	}
	return ret
}

// a simpler way is sort starts and ends separately
