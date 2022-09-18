import collections


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)
        # self.cache = collections.defaultdict(dict)

    def add_word(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def search_word(self, word: str, i: int) -> bool:
        # if i in self.cache[word]:
        #     return True
        cur = self
        for j in range(i, len(word)):
            if word[j] == ".":
                for v in cur.children.values():
                    if v.search_word(word, j + 1):
                        # self.cache[word][i] = True
                        return True
                return False
            else:
                if word[j] not in cur.children:
                    return False
                cur = cur.children[word[j]]

        # if cur.is_word:
        #     self.cache[word][i] = True
        #     return True
        return cur.is_word


class WordDictionary:

    def __init__(self):
        self.max_len = 0
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.add_word(word)
        self.max_len = max(self.max_len, len(word)) # opt1, simple but effective

    def search(self, word: str) -> bool:
        if len(word) > self.max_len:
            return False
        return self.root.search_word(word, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)