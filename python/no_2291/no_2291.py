class Solution:
    # 0 - 1 knap sack
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        p, f = [], []

        for i in range(len(present)):
            if future[i] - present[i] <= 0:
                continue
            p.append(present[i])
            f.append(future[i])

        values = [f[i] - p[i] for i in range(len(p))]

        dp = [[0 for i in range(budget + 1)] for j in range(len(p))]
        ret = 0
        if len(p) > 0 and p[0] <= budget:
            dp[0][p[0]] = values[0]
            ret = max(ret, dp[0][p[0]])
        for i in range(1, len(p)):
            for j in range(0, budget + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= p[i]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - p[i]] + values[i])
                ret = max(ret, dp[i][j])

        return ret
