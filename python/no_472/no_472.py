# Given an array of strings words (without duplicates), return all the
# concatenated words in the given list of words.
#
#  A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
#
#
#  Example 1:
#
#
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog",
# "hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
#  Example 2:
#
#
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
#
#
#
#  Constraints:
#
#
#  1 <= words.length <= 10⁴
#  1 <= words[i].length <= 30
#  words[i] consists of only lowercase English letters.
#  All the strings of words are unique.
#  1 <= sum(words[i].length) <= 10⁵
#
#
#  Related Topics Array String Dynamic Programming Depth-First Search Trie 👍 20
# 98 👎 229


# leetcode submit region begin(Prohibit modification and deletion)
import sortedcontainers


class Solution:

    def find(self, d, word, start) -> bool:
        l = len(word)
        if start == l:
            return True
        res_len = l - start

        if start != 0 and res_len in d and word[start:] in d[res_len]:
            return True

        idx = d.bisect_left(res_len)
        for i in reversed(range(0, idx)):
            length = d.keys()[i]
            if word[start:start + length] not in d[length]:
                continue
            if self.find(d, word, start + length):
                if l - start - length != 0 and l - start - length not in d:
                    d[l - start - length] = set()
                d[l - start - length].add(word[start + length:])
                return True

        return False

    # group by length
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = sortedcontainers.SortedDict()
        for word in words:
            if len(word) not in d:
                d[len(word)] = set()
            d[len(word)].add(word)

        ret = []
        for word in words:
            if self.find(d, word, 0):
                ret.append(word)

        return ret

# recursive way, super clean
# class Solution(object):
#     def findAllConcatenatedWordsInADict(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         d = set(words)
#
#         def dfs(word):
#             for i in range(1, len(word)):
#                 prefix = word[:i]
#                 suffix = word[i:]
#
#                 if prefix in d and suffix in d:
#                     return True
#                 if prefix in d and dfs(suffix):
#                     return True
#                 if suffix in d and dfs(prefix):
#                     return True
#
#             return False
#
#         res = []
#         for word in words:
#             if dfs(word):
#                 res.append(word)
#
#         return res
# leetcode submit region end(Prohibit modification and deletion)
