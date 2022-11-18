# 2262. Total Appeal of A String
# strong password
# password strength

class Solution:
    def appealSum(self, s: str) -> int:
        d = {}
        ret = [0 for i in range(len(s) + 1)]
        for i, c in enumerate(s):
            if c not in d:
                ret[i + 1] = i + 1 + ret[i]
            else:
                ret[i + 1] = i - d[c] + ret[i]
            d[c] = i
        return sum(ret)
