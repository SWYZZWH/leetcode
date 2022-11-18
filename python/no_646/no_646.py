class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: -x[0])
        dp = [1 for i in range(len(pairs))]
        for i in range(len(dp)):
            for j in range(i):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)