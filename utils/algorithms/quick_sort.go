package algorithms

import "math/rand"

// quick select find kth element
// sort nums[:k], nums[k+1:] separately

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
	return less
}

func quickSort(nums []int) []int {
	if nums == nil || len(nums) == 0 {
		return nil
	}

	k := quickSelect(0, len(nums), nums)
	quickSort(nums[:k])
	quickSort(nums[k+1:])
	return nums
}
