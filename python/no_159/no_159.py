class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        ret = 0
        i, j = 0, 0
        while j != len(s):
            c = s[j]
            if c in d:
                d[c] += 1
            elif c not in d and len(d) < 2:
                d[c] = 1
            else:
                while len(d) >= 2:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        d.pop(s[i])
                    i += 1
                d[c] = 1
            ret = max(ret, j - i + 1)
            j += 1
        return ret
