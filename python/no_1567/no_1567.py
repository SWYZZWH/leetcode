from typing import List


class Solution:
    # two pointers
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        def getMaxLenSimple(nums: List[int]) -> int:
            n = len(nums)

            if not nums:
                return 0

            negtives = sum([1 for i in range(n) if nums[i] < 0])
            if negtives % 2 == 0:
                return n
            # find the first neg from left
            l = 0
            while nums[l] > 0:
                l += 1

            # find the first neg from right
            r = n - 1
            while nums[r] > 0:
                r -= 1

            return max(n - l - 1, r)

        start = 0
        for i in range(n):
            if nums[i] == 0:
                res = max(res, getMaxLenSimple(nums[start:i]))
                start = i + 1
        res = max(res, getMaxLenSimple(nums[start:]))

        return res
