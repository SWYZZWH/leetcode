package no_923

import (
	"sort"
)

// 923. 3Sum With Multiplicity
// Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
//
// As the answer can be very large, return it modulo 109 + 7.

// sort
// record number frequency map
// unique
// double pointers or hashmap
func threeSumMulti(arr []int, target int) int {
	if arr == nil || len(arr) < 2 {
		return 0
	}
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})
	freq := map[int]int{}
	cur := -1
	unique := make([]int, 0, len(arr))
	for i := 0; i < len(arr); i++ {
		freq[arr[i]]++
		if arr[i] == cur {
			continue
		} else {
			cur = arr[i]
			unique = append(unique, arr[i])
		}
	}

	ret := 0
	for i := 0; i < len(unique); i++ {
		// double pointers
		j := i
		k := len(unique) - 1
		res := target - unique[i]
		if res < unique[j] {
			return ret
		}
		for j <= k {
			if unique[j]+unique[k] == res {
				if unique[i] == unique[j] && unique[i] == unique[k] {
					// ensure 3
					if f, _ := freq[unique[i]]; f >= 3 {
						ret += f * (f - 1) * (f - 2) / 6
						ret %= 1_000_000_007
					}
					break
				} else if unique[i] == unique[j] {
					if f, _ := freq[unique[i]]; f >= 2 {
						freqK := freq[unique[k]]
						ret += freqK * f * (f - 1) / 2
						ret %= 1_000_000_007
					}
				} else if unique[j] == unique[k] {
					if f, _ := freq[unique[j]]; f >= 2 {
						freqI := freq[unique[i]]
						ret += freqI * f * (f - 1) / 2
						ret %= 1_000_000_007
					}
					break
				} else {
					freqI := freq[unique[i]]
					freqJ := freq[unique[j]]
					freqK := freq[unique[k]]
					ret += freqI * freqJ * freqK
					ret %= 1_000_000_007
				}
				k--
			} else if unique[j]+unique[k] < res {
				j++
			} else {
				k--
			}
		}
	}
	return ret
}
