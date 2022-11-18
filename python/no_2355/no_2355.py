import collections
from typing import List


class Solution:
    # mono stack
    # consider of the constraints:
    # each element inside of the books is a rule: all the elements on the left of i should be at most books[i] - 1, books[i] - 2...
    # the key is which rule is governing at any position
    # go from left to right, if the current rule is strict than the rules before, then the former rules are useless
    # else, the current rule is useless for elements before, but it may be useful for rules on the right, so we keep it
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        res = books[0]
        q = collections.deque([(books[0], 0, books[0])])
        for i in range(1, n):
            while q and books[i] < q[-1][0] + i - q[-1][1]:
                q.pop()
            cur = 0
            last_idx = -1
            if q:
                last_idx = q[-1][1]
                cur += q[-1][2]
            left = max(books[i] + last_idx - i + 1, 0)
            cur += (books[i] + left) * (books[i] - left + 1) // 2
            res = max(res, cur)
            q.append((books[i], i, cur))

        return res
