# 2405. Optimal Partition of String

# greedy
class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        ret = 1
        for i in range(len(s)):
            if s[i] in d:
                ret += 1
                d = set(s[i])
            else:
                d.add(s[i])

        return ret
