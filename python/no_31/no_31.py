from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # from back to front
        # find the first idx i, let nums[i] > nums[i - 1],  if can't find any, simply rotate the nums
        # find the smallest element in nums[i:] which is greater than nums[i - 1], index of which is k
        # swap(num[i - 1], nums[k])
        # rotate nums[i:]

        def rotate(i: int, j: int):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        for i in reversed(range(len(nums))):
            if i == 0:
                rotate(0, len(nums) - 1)
                return
            if nums[i] > nums[i - 1]:
                j = len(nums) - 1
                while nums[j] <= nums[i - 1]:
                    j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                rotate(i, len(nums) - 1)
                return
