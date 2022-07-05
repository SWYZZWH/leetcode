package no_560

// 560. Subarray Sum Equals K
// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
// A subarray is a contiguous non-empty sequence of elements within an array.

// can't sort
//func subarraySum(nums []int, k int) int {
//	//sort.Ints(nums)
//	ret := 0
//	curSum := 0
//	left, right := 0, 0
//	for i := 0; i < len(nums); i++ {
//		curSum += nums[i]
//		if curSum == k {
//			ret += 1
//			right++
//		} else if curSum < k {
//			right++
//			continue
//		} else if curSum > k {
//			for left < right && curSum > k {
//				curSum -= nums[left]
//				left++
//				if curSum == k {
//					ret += 1
//				}
//			}
//		}
//	}
//}

// brute force can do, the optimized time complexity is O(n^2) and the optimized space complexity is O(1)
// however, use sum frequency map and a simple equation: sum(i) - sum(j) = k will achieve O(n)
func subarraySum(nums []int, k int) int {
	if nums == nil || len(nums) == 0 {
		return 0
	}
	freq := map[int]int{0: 1}
	curSum, ret := 0, 0
	for i := 0; i < len(nums); i++ {
		curSum += nums[i]
		if val, ok := freq[curSum-k]; ok {
			ret += val
		}
		freq[curSum] += 1
	}
	return ret
}
