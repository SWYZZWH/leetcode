# 1047. Remove All Adjacent Duplicates In String
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.s

# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    # the point is: the rest letters keeps their relative orders as before
    # so we can feel free about the removal order
    # def removeDuplicates(self, s: str) -> str:
    #     n = len(s)
    #     removed = [False] * n
    #     i = 0
    #     while i < n:
    #         j, k = i, i + 1
    #         while j >= 0 and k < n and s[j] == s[k] and not removed[j]:
    #             removed[j], removed[k] = True, True
    #             while j >= 0 and removed[j]:
    #                 j -= 1
    #             if j < 0:
    #                 break
    #             k += 1
    #         i = k
    #
    #     ret = ""
    #     for i in range(n):
    #         if not removed[i]:
    #             ret += s[i]
    #     return ret

    # should use stack!
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        stk = []
        for i in range(n):
            if len(stk) != 0 and stk[-1] == s[i]:
                stk.pop()
            else:
                stk.append(s[i])
        return "".join(stk)
