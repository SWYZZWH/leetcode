import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        q = collections.deque(sorted(tokens))
        scores = 0
        while q:
            while q and power >= q[0]:
                p = q.popleft()
                power -= p
                scores += 1
            if len(q) <= 2 or scores == 0:
                return scores
            p = q.pop()
            scores -= 1
            power += p
        return scores