from typing import List


class Solution:
    # two pointers
    # one pass solution opt 1
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ret = 0
        while l != r:
            ret = max(ret, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                j = l
                while height[j] <= height[l] and j != r:  # opt 2
                    j += 1
                l = j
            else:
                j = r
                while height[j] <= height[r] and j != l:
                    j -= 1
                r = j

        return ret
