from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # just like no_410 and no_1011
        # the only diffience is they find min(max()), we find max(min())
        # sweetness = [- sweet for sweet in sweetness]
        l, r = min(sweetness), 10000000
        while l < r:
            mid = (l + r + 1) // 2
            cur = 0
            offer = 0
            for sweet in sweetness:
                cur += sweet
                if cur >= mid:
                    offer += 1
                    cur = 0
            if offer < k + 1:
                r = mid - 1
            else:
                # offer >= k is acceptable
                # we want to find the maximum
                l = mid
        return l
