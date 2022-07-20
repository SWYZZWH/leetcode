# 2272. Substring With Largest Variance

# The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
#
# Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
#
# A substring is a contiguous sequence of characters within a string.
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of lowercase English letters.
import math


class Solution:
    # do it in O(n^2 * 26), cause time exceeding
    # def largestVariance(self, s: str) -> int:
    #     ret = 0
    #     if len(s) == 1 or len(s) == 2:
    #         return 0
    #     for i in range(len(s)):
    #         buckets = {}
    #         curMax, curMin = -1, math.inf
    #         curMaxKey, curMinKey = None, None
    #         for j in range(i, len(s)):
    #             if s[j] not in buckets:
    #                 buckets[s[j]] = 1
    #             else:
    #                 buckets[s[j]] += 1
    #             if (buckets[s[j]] > curMax or s[j] == curMaxKey) or (s[j] == curMinKey or buckets[s[j]] < curMin):
    #                 if buckets[s[j]] > curMax or s[j] == curMaxKey:
    #                     curMax = buckets[s[j]]
    #                     curMaxKey = s[j]
    #                 else:
    #                     curMin = buckets[s[j]]
    #                     curMinKey = s[j]
    #                 if curMaxKey != curMinKey:
    #                     ret = max(ret, curMax - curMin)
    #     return ret

    # for each character pair, calculate the max diff
    def largestVariance(self, s: str) -> int:
        if len(s) == 1 or len(s) == 2:
            return 0
        ret = 0
        # d = [-1] * 26
        # for i in range(26):
        #     d[i] = 0
        d = {}

        for k in range(len(s)):
            if s[k] not in d:
                d[s[k]] = 1
            else:
                d[s[k]] += 1
            # if d[ord(s[k])] == -1:
            #     d[ord(s[k])] = 1
            # else:
            #     d[ord(s[k]) - ord('a')] += 1
            for c1 in d.keys():
                for c2 in d.keys():
                    if c1 != c2:
                        val1, val2 = d[c1] - d[c2]
                        ret = max(ret, val1 - val2) if val1 > val2 else max(ret, val2 - val1)
        return ret


