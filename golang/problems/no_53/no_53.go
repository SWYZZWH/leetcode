package no_53

import "math"

// 53. Maximum Subarray

// maxSubArray 2D dp, but over time
//
//	func maxSubArray(nums []int) int {
//		ret := math.MinInt
//		dp := make([]int, len(nums))
//		for i := 0; i < len(nums); i++ {
//			dp[i] = nums[i]
//			ret = max(nums[i], ret)
//		}
//		for i := 1; i < len(nums); i++ {
//			for j := len(nums) - 1; j >= i; j-- {
//				dp[j] = dp[j] + nums[j - i]
//				ret = max(dp[j], ret)
//			}
//		}
//
//		return ret
//	}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxSubArray(nums []int) int {
	ret := math.MinInt
	curSum := 0
	for _, num := range nums {
		ret = max(ret, num)
		if curSum+num > 0 {
			curSum += num
			ret = max(ret, curSum)
		} else {
			curSum = 0
		}
	}
	return ret
}
