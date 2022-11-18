from typing import List


# it turns out top-down dp solution it is the fastest
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ones = [s.count("1") for s in strs]
        zeroes = [s.count("0") for s in strs]

        if m >= sum(zeroes) and n >= sum(ones):
            return len(strs)

        @functools.cache
        def dfs(idx: int, mm: int, nn: int, cnt: int) -> int:
            if idx == len(strs):
                return cnt

            ret = 0
            if mm - zeroes[idx] >= 0 and nn - ones[idx] >= 0:
                ret = max(ret, dfs(idx + 1, mm - zeroes[idx], nn - ones[idx], cnt + 1))
            ret = max(ret, dfs(idx + 1, mm, nn, cnt))

            return ret

        return dfs(0, m, n, 0)

# bottom-up solution takes longer time ...
# however, we can use a hash map and try to optimize
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         ones = [s.count("1") for s in strs]
#         zeroes = [s.count("0") for s in strs]
#
#         if m >= sum(zeroes) and n >= sum(ones):
#             return len(strs)
#
#         ret = 0
#         dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
#         for i in range(len(strs)):
#             for j in range(m, zeroes[i] - 1, -1):
#                 for k in range(n, ones[i] - 1, -1):
#                     dp[j][k] = max(dp[j][k], dp[j - zeroes[i]][k - ones[i]] + 1)
#                     ret = max(ret, dp[j][k])
#
#         return ret

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ones = [s.count("1") for s in strs]
        zeroes = [s.count("0") for s in strs]

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for l in range(len(strs)):
            for i in reversed(range(m + 1)):
                for j in reversed(range(n + 1)):
                    if i < zeroes[l] or j < ones[l]:
                        continue
                    dp[i][j] = max(dp[i - zeroes[l]][j - ones[l]] + 1, dp[i][j])

        return dp[-1][-1]