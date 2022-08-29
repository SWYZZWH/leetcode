# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
import collections
from typing import List


class Solution:
    # count sort to improve performance: for string only contains specific characters
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     d = {}
    #     for s in strs:
    #         s_sort = sorted(s)
    #         if s_sort not in d:
    #             d[s_sort] = [s]
    #         else:
    #             d[s_sort].append(s)
    #     ret = []
    #     for v in d.values():
    #         ret.append(v)
    #     return ret

    # counting sort NK
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            count = [0 for i in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(s)

        ret = []
        for v in d.values():
            ret.append(v)
        return ret
