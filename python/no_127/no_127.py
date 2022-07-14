# 127. Word Ladder
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Constraints:
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
from collections import deque
from typing import List


class Solution:
    # same string can't be used twice, cause if s1 -> s2 -> s3 -> s2 -> s4 == s1 -> s2 -> s4
    # use BFS
    # main point is find neighbors quickly
    # get a set like: "dog" -> "*og" "d*g" "do*" will be faster
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque()
        q.append(beginWord)
        wordList.remove(beginWord)
        ret = 0
        while q.__len__() != 0:
            ret += 1
            tmpQ = deque()
            while q.__len__() != 0:
                word = q.pop()
                if word == endWord:
                    return ret
                for i in word:
                    for c in range(ord('a'), ord('z') + 1):
                        newStr = word[:i] + chr(c) + word[i + 1:]
                        if newStr in wordList:
                            tmpQ.append(newStr)
                            wordList.remove(newStr)
            q = tmpQ
        return -1
