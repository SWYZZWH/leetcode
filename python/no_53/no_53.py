class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = max(nums)
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > 0:
                ret = max(cur_sum, ret)
            if cur_sum < 0:
                cur_sum = 0

        return ret