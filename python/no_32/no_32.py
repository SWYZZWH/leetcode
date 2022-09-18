class Solution:
    # if sub string [a, b] is a valid parentheses and we got s[a - 1] == "("
    # s[b + 1] == ")", then substring [a - 1, b + 1] is also a valid parentheses
    # so the state transmission equation is like:
    #   dp[i][j] = {dp[i]dp[i + k] and dp[i + k][j]} or {dp[i + 1][j - 1] and s[i] == "(" and s[j] == ")"} but this will TLE

    # dp[i] means the longest parentheses ending at i
    # s[i] must be ")"
    # if s[i - 1] == "(", dp[i] = dp[i - 2] + 2
    # if s[i - 1] == ")", dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2] if s[i - dp[i - 1] - 2] == "("
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n)]
        for i in range(n):
            if s[i] == "(" or i == 0:
                continue
            if s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
            else:
                if i - dp[i - 1] - 1 < 0 or s[i - dp[i - 1] - 1] == ")":
                    continue
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2
        return max(dp) if dp else 0
