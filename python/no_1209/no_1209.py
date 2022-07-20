# 1209. Remove All Adjacent Duplicates in String II

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
#
# Constraints:
#
# 1 <= s.length <= 105
# 2 <= k <= 104
# s only contains lower case English letters.

class Solution:
    # def removeDuplicates(self, s: str, k: int) -> str:
    #     if k == 1:
    #         return ""
    #     n = len(s)
    #     stk = []
    #     charMap = {}
    #     for i in range(n):
    #         if len(stk) == 0 or stk[-1] != s[i]:
    #             if s[i] not in charMap or len(charMap[s[i]]) == 0:
    #                 charMap[s[i]] = [1]
    #             else:
    #                 charMap[s[i]].append(1)
    #             stk.append(s[i])
    #             continue
    #
    #         if charMap[s[i]][-1] == k - 1:
    #             for j in range(1, k):
    #                 stk.pop()
    #             charMap[s[i]].pop()
    #             continue
    #
    #         charMap[s[i]][-1] += 1
    #         stk.append(s[i])
    #     return "".join(stk)
    #

    # simplify the solution above
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for i in range(len(s)):
            if len(stk) == 0 or s[i] != stk[-1][0]:
                stk.append([s[i], 1])
            else:
                stk[-1][1] += 1
                # if stk[-1][1] == k:
                #     stk.pop()
        ret = ""
        for i in range(len(stk)):
            ret += stk[i][0] * (stk[i][1] % k)
        return ret

