# if stones are divided into 2 piles, A & B, the only stone left is sum(A) - sum(B)
# so we just want the minimum of diff of the sum
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)

        dp = [False for i in range(total + 1)]
        dp[0] = True
        for i in range(n):
            # print(dp)
            for j in reversed(range(len(dp))):
                if j - stones[i] >= 0:
                    dp[j] = dp[j] or dp[j - stones[i]]

        # print(dp)
        # print(total)

        i, j = total // 2 + 1, total // 2
        # print(i,j, dp[i], dp[j])
        while i <= total and j >= 0:
            if dp[j]:
                return (total - j) - j
            if dp[i]:
                return i - (total - i)
            i += 1
            j -= 1

        return total
