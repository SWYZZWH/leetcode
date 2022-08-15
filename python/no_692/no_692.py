import heapq
from typing import List

from sortedcontainers import SortedDict


# how to customized heap order
class TopWord:

    def __init__(self, freq: int, word: str):
        self.freq = freq
        self.word = word

    def __lt__(self, other: 'TopWord'):
        if self.freq != other.freq:
            return lt(self.freq, other.freq)
        else:
            # opposite
            return lt(other.word, self.word)


# python heap is a minimum heap
# always keeps larger ones
# if we want to keep small ones, like lexicographical smaller strings, we reverse the order of string
# to keep k
class Solution:
    # sorted dict: red-black tree
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.defaultdict(int)
        for word in words:
            d[word] += 1

        h = []
        heapq.heapify(h)
        for key, value in d.items():
            heapq.heappush(h, TopWord(value, key))
            if len(h) > k:
                heapq.heappop(h)

        ret = []
        for i in range(k):
            ret.append(heapq.heappop(h).word)

        return ret[::-1]
