# word search

# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
from typing import List


class Solution:
    # still BFS / DFS
    # notice: this problem is more difficult than no_79, cause the words collection may be large, and we can't simply return after find any word
    #         another aspect is multiple words can be searched in one round
    # two ways to improve:  build a Trie Tree / HashMap for quick search prefix and return false immediately
    #                       clearing word in Trie after it has been found (necessary)

    # or use Trie Tree
    # class TrieNode {
    #     TrieNode[] next = new TrieNode[26];
    #     String word;
    # }
    # store entire word only at the end

    class State:
        def __init__(self, is_word: bool):
            self.is_word = is_word
            self.count = 1

    def recollect(self, prefix_dict, word):
        for i in range(len(word)):
            s = prefix_dict[word[:i + 1]]
            if s.is_word:
                s.is_word = False
            s.count -= 1
            if s.count == 0:
                prefix_dict.pop(word[:i + 1])

    def dfs(self, board: List[List[str]], visited: List[List[bool]], prefix_dict, prefix, all_lst: List[str], i: int, j: int):
        m, n = len(board), len(board[0])
        if i >= m or i < 0 or j >= n or j < 0:
            return
        if visited[i][j]:
            return
        visited[i][j] = True
        cur_str = prefix + board[i][j]
        if cur_str in prefix_dict:
            state = prefix_dict[cur_str]
            if state.is_word:
                all_lst.append(cur_str)
                self.recollect(prefix_dict, cur_str)
            self.dfs(board, visited, prefix_dict, cur_str, all_lst, i + 1, j)
            self.dfs(board, visited, prefix_dict, cur_str, all_lst, i - 1, j)
            self.dfs(board, visited, prefix_dict, cur_str, all_lst, i, j + 1)
            self.dfs(board, visited, prefix_dict, cur_str, all_lst, i, j - 1)

        visited[i][j] = False
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        prefix = {}
        for word in words:
            for i in range(len(word) - 1):
                if word[:i + 1] not in prefix:
                    prefix[word[:i + 1]] = self.State(False)
                else:
                    prefix[word[:i + 1]].count += 1
            if word in prefix:
                prefix[word].is_word = True
                prefix[word].count += 1
            else:
                prefix[word] = self.State(True)

        visited = [[False for i in range(n)] for j in range(m)]
        ret = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, visited, prefix, "", ret, i, j)
        return ret
