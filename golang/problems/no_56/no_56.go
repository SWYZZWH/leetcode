package no_56

import "sort"

// 排序 + 判断
// 找连通分量，每个 interval 视为一个节点，两个节点属于同一连通分量当且仅当他们有重合部分，或同时与第三个节点有重合部分 O(n^2) 共扫描 n 次，每层产生的新节点再扫描一次
// sort the intervals by left border
// then simply visit once
func merge(intervals [][]int) [][]int {
	if intervals == nil || len(intervals) == 0 {
		return nil
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	ret := [][]int{}
	left, right := intervals[0][0], intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		l, r := intervals[i][0], intervals[i][1]
		if l > right {
			ret = append(ret, []int{left, right})
			left, right = l, r
		} else {
			right = max(r, right)
		}
	}
	ret = append(ret, []int{left, right})
	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
