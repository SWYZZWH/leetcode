import math
from typing import List

# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
# hash on tree nodes

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_finish(k: int) -> bool:
            hours_need = 0
            for p in piles:
                hours_need += math.ceil(p / k)
                if hours_need > h:
                    return False

            return True

        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1

        return l