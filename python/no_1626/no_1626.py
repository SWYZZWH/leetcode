from typing import List


class Solution:
    # variants of LIS
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0 for i in range(len(scores))]
        pairs = sorted(zip(ages, scores))
        for i, p in enumerate(pairs):
            dp[i] = p[1]
            for j in range(i):
                if pairs[j][1] <= pairs[i][1]:
                    dp[i] = max(dp[i], dp[j] + p[1])

        return max(dp)
