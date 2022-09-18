import collections
from typing import List


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)

    def add_word(self, word: str):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True


class Solution:
    # Trie optimization
    # key is we gonna store the words in dict to the Trie reversely
    # for dp[i], let j = i initial, and we start to look up s[j: i] in the Trie
    # if we find an end of word, we update dp[i] with dp[j]
    # we continouly travsing the Trie until the s[j] is not in Trie
    # so the time complexity should be O(n * max length of word in wordDict)
    # but it still require sum of length of words in wordDict to build a Trie structure
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            root.add_word(reversed(word))

        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            cur = root
            for j in reversed(range(1, i + 1)):
                if s[j - 1] not in cur.children:
                    break
                cur = cur.children[s[j - 1]]
                if cur.is_word and dp[j - 1]:
                    dp[i] = True
                    break

        return dp[-1]