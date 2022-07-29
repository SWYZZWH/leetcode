# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
#
#
#  '.' Matches any single character.
#  '*' Matches zero or more of the preceding element.
#
#
#  The matching should cover the entire input string (not partial).
#
#
#  Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
#  Example 2:
#
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
#  Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 20
#  1 <= p.length <= 30
#  s contains only lowercase English letters.
#  p contains only lowercase English letters, '.', and '*'.
#  It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
#
#
#  Related Topics String Dynamic Programming Recursion 👍 8712 👎 1346


# leetcode submit region begin(Prohibit modification and deletion)

# better solution is dp
class Solution:

    def __init__(self):
        self.dp = {}

    def rec(self, s: str, p: str, i: int, j: int) -> bool:
        while i <= len(s) and j < len(p):
            if p[j] != '.':
                if j != len(p) - 1 and p[j + 1] == "*":
                    if self.rec(s, p, i, j + 2):
                        return True
                    if i == len(s):
                        return False
                    if p[j] == s[i]:
                        return self.rec(s, p, i + 1, j)
                if i == len(s) or p[j] != s[i]:
                    return False
                j += 1
                i += 1
                continue
            elif p[j] == '.':
                if j == len(p) - 1 or p[j + 1] != '*':
                    return self.rec(s, p, i + 1, j + 1)
                else:
                    for k in range(i, len(s) + 1):
                        if self.rec(s, p, k, j + 2):
                            return True
                    return False

        return i == len(s) and j == len(p)

    def isMatch(self, s: str, p: str) -> bool:
        return self.rec(s, p, 0, 0)

# leetcode submit region end(Prohibit modification and deletion)
