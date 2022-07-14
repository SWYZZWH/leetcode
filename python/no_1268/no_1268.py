# 1268
# You are given an array of strings products and a string searchWord.
#
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
#
# Return a list of lists of the suggested products after each character of searchWord is typed.
from typing import List


# dictionary tree
class DictTreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ret = []
        dt = DictTreeNode()
        for prod in products:
            p = dt
            for i in range(len(prod)):
                if p.children[ord(prod[i]) - ord('a')] is None:
                    p.children[ord(prod[i]) - ord('a')] = DictTreeNode()
                p = p.children[ord(prod[i]) - ord('a')]
            p.isWord = True

        for i in range(len(searchWord)):
            ret.append(self.searchPrefix(dt, searchWord[:i + 1]))

        return ret

    # search tree and find 3 common prefix word

    def searchPrefix(self, root: DictTreeNode, prefix: str) -> List[str]:
        p = root
        ret = []
        for i in range(len(prefix)):
            if p.children[ord(prefix[i]) - ord('a')] is None:
                return []
            p = p.children[ord(prefix[i]) - ord('a')]
        for s in self.searchAll(p):
            ret.append(prefix + s)
        return ret[:3]

    def searchAll(self, root: DictTreeNode) -> List[str]:
        if root is None:
            return []
        ret = []
        if root.isWord:
            ret.append("")
        for i in range(26):
            if root.children[i] is not None:
                subs = self.searchAll(root.children[i])
                if len(subs) == 0:
                    ret.append(chr(i + ord('a')))
                for s in subs:
                    ret.append(chr(i + ord('a')) + s)
        return ret


#     def suggestedProducts(self, A, word):
#         A.sort()
#         res, prefix, i = [], '', 0
#         for c in word:
#             prefix += c
#             i = bisect.bisect_left(A, prefix, i)
#             res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
#         return res