from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = []

        def reverse_arr(nums: List[int], i: int, j: int):
            return nums[:i] + list(reversed(nums[i: j + 1])) + nums[j + 1:]

        def next_permutation(nums: List[int]) -> List[int]:
            for i in reversed(range(n)):
                if i == 0:
                    return None
                if nums[i] > nums[i - 1]:
                    j = i
                    while j < n:
                        if nums[j] <= nums[i - 1]:
                            break
                        j += 1
                    nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                    nums = reverse_arr(nums, i, n)
                    return nums

        while nums:
            ret.append(nums.copy())
            nums = next_permutation(nums)

        return ret
