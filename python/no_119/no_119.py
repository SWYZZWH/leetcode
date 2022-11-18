from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [0 for i in range(rowIndex + 1)]
        dp[0] = 1

        for i in range(rowIndex + 1):
            for j in reversed(range(i + 1)):
                if j > 0:
                    dp[j] += dp[j - 1]
        return dp