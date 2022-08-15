class Solution:
    # prefix-sum
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        s = 0
        ret = 0
        for i, num in enumerate(nums):
            s += num
            if s == k:
                ret = max(i + 1, ret)
            if s - k in d:
                ret = max(i - d[s - k], ret)
            if s in d:
                continue
            d[s] = i
        return ret
