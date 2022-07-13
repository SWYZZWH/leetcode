package no_215

import "math/rand"

// 215. Kth Largest Element in an Array
// Given an integer array nums and an integer k, return the kth largest element in the array.
//
// Note that it is the kth largest element in the sorted order, not the kth distinct element.

// S1: sort array and return nums[k]
//func findKthLargest(nums []int, k int) int {
//	sort.Slice(nums, func(i, j int) bool {
//		return i > j
//	})
//	return nums[k]
//}

// S2: use a heap size k
// complexity O(nlogK)

// S3: quick sort

//type hp []int
//
//func (h *hp) Less(i, j int) bool {
//	return (*h)[i] < (*h)[j]
//}
//
//func (h *hp) Swap(i, j int) {
//	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
//}
//
//func (h *hp) Len() int {
//	return len(*h)
//}
//
//func (h *hp) Push(x interface{}) {
//	*h = append(*h, x.(int))
//}
//
//// Pop less one pop first
//func (h *hp) Pop() interface{} {
//	val := (*h)[len(*h)-1]
//	*h = (*h)[:len(*h)-1]
//	return val
//}
//
//func (h *hp) Top() interface{} {
//	return (*h)[0]
//}
//
//func findKthLargest(nums []int, k int) int {
//	reverse := false
//	if k > len(nums)/2 {
//		k = len(nums) + 1 - k
//		reverse = true
//	}
//
//	var h hp
//	h = make([]int, 0, k)
//	heap.Init(&h)
//
//	for i := 0; i < len(nums); i++ {
//		if reverse {
//			nums[i] = -nums[i]
//		}
//		if len(h) < k {
//			heap.Push(&h, nums[i])
//		} else if nums[i] > h.Top().(int) {
//			heap.Pop(&h)
//			heap.Push(&h, nums[i])
//		}
//	}
//	if reverse {
//		return -(heap.Pop(&h).(int))
//	} else {
//		return heap.Pop(&h).(int)
//	}
//
//}

func quickSelect(start, end int, total []int) int {
	if start >= end {
		return -1
	}

	if end-start == 1 {
		return start
	}

	nums := total[start:end]

	idx := rand.Intn(len(nums))
	nums[0], nums[idx] = nums[idx], nums[0]
	less := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[0] {
			nums[less], nums[i] = nums[i], nums[less]
			less++
		}
	}
	nums[0], nums[less-1] = nums[less-1], nums[0]
	return less - 1 + start
}

func findKthLargest(nums []int, k int) int {
	k = len(nums) - k
	start, end := 0, len(nums)
	idx := quickSelect(start, end, nums)
	for idx != k {
		if idx < k {
			start = idx + 1
			idx = quickSelect(start, end, nums)
		} else {
			end = idx
			idx = quickSelect(start, end, nums)
		}
	}
	return nums[k]
}
