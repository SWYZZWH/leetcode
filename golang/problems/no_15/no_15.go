package no_15

import "sort"

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
//
//Notice that the solution set must not contain duplicate triplets.

// can use 2 pointers
// the time complexity is O(n ^ 2)
func threeSum(nums []int) [][]int {
	// sort nums first
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	ret := make([][]int, 0)
	valueMap := make(map[int]int)
	for i, num := range nums {
		valueMap[num] = i
	}

	resultMap := make(map[int]map[int]int)
	for i := 0; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			idx, ok := valueMap[-nums[i]-nums[j]]
			if !ok || nums[idx] > nums[j] {
				continue
			}
			if nums[idx] == nums[j] && (j == 0 || nums[j] != nums[j-1]) {
				continue
			}
			if _, ok := resultMap[nums[idx]]; ok {
				if _, ok := resultMap[nums[idx]][nums[j]]; ok {
					continue
				} else {
					resultMap[nums[idx]][nums[j]] = nums[i]
				}
			} else {
				resultMap[nums[idx]] = map[int]int{nums[j]: nums[i]}
			}
			ret = append(ret, []int{nums[idx], nums[j], nums[i]})
		}
	}

	return ret
}
