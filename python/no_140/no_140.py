import collections
from typing import List


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Solution:
    # Trie Tree
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # build trie tree
        root = TrieNode()
        for w in wordDict:
            p = root
            for c in w:
                p = p.children[c]
            p.is_word = True

        ret = []

        def find_word(i: int, prefix: List[str]):
            if i == len(s):
                ret.append(" ".join(prefix))
                return

            p = root
            j = i
            while j != len(s) and s[j] in p.children:
                p = p.children[s[j]]
                j += 1
                if p.is_word:
                    find_word(j, prefix + [s[i:j]])

            return

        find_word(0, [])
        return ret