import collections
from typing import List


class Solution:
    # use array instead of dict will reduce the constant of time complexity when comparing two dict
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        if len(p) > len(s):
            return ret

        p_freq = collections.Counter(p)
        s_freq = collections.Counter(s[0: len(p)])

        if s_freq == p_freq:
            ret.append(0)

        for i in range(len(p), len(s)):
            remove_idx = i - len(p)
            s_freq[s[remove_idx]] -= 1
            if s_freq[s[remove_idx]] == 0:
                s_freq.pop(s[remove_idx])
            if s[i] not in s_freq:
                s_freq[s[i]] = 1
            else:
                s_freq[s[i]] += 1
            if s_freq == p_freq:
                ret.append(remove_idx + 1)

        return ret
