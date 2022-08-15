class Solution:
    # same as 159
    # sliding window
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        d = {}
        l, r = 0, 0
        ret = 0
        while r < len(s):
            c = s[r]
            if c in d:
                d[c] += 1
            elif c not in d and len(d) < k:
                d[c] = 1
            else:
                while len(d) >= k:
                    d[s[l]] -= 1
                    if d[s[l]] == 0:
                        d.pop(s[l])
                    l += 1
                d[c] = 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret
