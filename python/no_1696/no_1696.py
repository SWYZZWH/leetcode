import collections
from typing import List


class Solution:
    # simple 2d dp will TLE
    # monotonic queue
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [num for num in nums]

        q = collections.deque([(nums[0], 0)])

        for i in range(1, len(nums)):
            if q[0][1] + k < i:
                q.popleft()
            dp[i] = q[0][0] + nums[i]
            while q and q[-1][0] < dp[i]:
                q.pop()
            q.append((dp[i], i))

        return dp[-1]
