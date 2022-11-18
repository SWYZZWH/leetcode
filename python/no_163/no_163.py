from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def format_range(l: int, r: int) -> str:
            if l == r:
                return "{}".format(l)
            return "{}->{}".format(l, r)

        res = []
        nums = [lower - 1] + nums + [upper + 1]
        l = r = lower
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i] + 1:
                res.append(format_range(nums[i] + 1, nums[i + 1] - 1))

        return res
