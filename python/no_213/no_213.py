from typing import List


class Solution:
    # ugly
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_chain(arr: List[int]) -> int:
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr[0], arr[1])

            dp = [0 for i in range(n)]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            # print(dp)
            return max(dp)

        return max(nums[0] + rob_chain(nums[2:len(nums) - 1]), rob_chain(nums[1:]))