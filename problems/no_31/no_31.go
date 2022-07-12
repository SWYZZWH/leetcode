package no_31

//A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
//
//For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
//The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
//
//For example, the next permutation of arr = [1,2,3] is [1,3,2].
//Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
//While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
//Given an array of integers nums, find the next permutation of nums.
//
//The replacement must be in place and use only constant extra memory.

//1 <= nums.length <= 100
//0 <= nums[i] <= 100

func nextPermutation(nums []int) {
	if len(nums) == 0 {
		return
	}
	i := len(nums) - 1
	for ; i > 0; i-- {
		if nums[i-1] < nums[i] {
			for j := len(nums) - 1; j >= i; j-- {
				if nums[j] > nums[i-1] {
					nums[i-1], nums[j] = nums[j], nums[i-1]
					flipOver(i, len(nums), nums)
					return
				}
			}
		}
	}
	flipOver(0, len(nums), nums)

}

func flipOver(start, end int, total []int) {
	if len(total) == 0 || start >= end {
		return
	}

	nums := total[start:end]

	for i := 0; i < len(nums)/2; i++ {
		nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
	}
}
