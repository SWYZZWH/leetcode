from bisect import bisect
from random import random
from typing import List


# actually there is o(1) solution which is awesome
# https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation
class Solution:

    def __init__(self, w: List[int]):
        self.w = [w[0]]
        for weight in w[1:]:
            self.w.append(self.w[-1] + weight)

    def pickIndex(self) -> int:
        i = random.randint(0, self.w[-1] - 1)
        idx = bisect.bisect_right(self.w, i)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
