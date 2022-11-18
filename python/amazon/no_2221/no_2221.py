from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # (x + y) ^ 4  -> 1 4 6 4 1 -> ith coff = 4Ck
        n = len(nums) - 1
        if n == 0:
            return nums[0]
        coff = 1
        res = 0
        for i, num in enumerate(nums):
            res += coff * num
            coff *= n - i
            coff //= i + 1
        return res % 10
