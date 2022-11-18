import collections
from typing import List


class Solution:
    # exactly k -> at most k
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(k: int) -> int:
            if k == 0:
                return 0
            n = len(nums)
            s = collections.defaultdict(int)
            j = 0
            res = 0
            for i in range(n):
                s[nums[i]] += 1
                while len(s) > k:
                    s[nums[j]] -= 1
                    if s[nums[j]] == 0:
                        s.pop(nums[j])
                    j += 1
                res += i - j + 1
            return res

        return at_most_k(k) - at_most_k(k - 1)
