from functools import reduce
from typing import List


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        def rabin_karp(L: int, nums: List[int]) -> bool:
            if L >= len(nums):
                return False
            MOD = 2 ** 63 - 1
            base = 26
            aL = pow(base, L)
            h = reduce(lambda x, y: x * base + y, nums[:L]) % MOD
            seen = {h}
            for i in range(1, len(nums) - L + 1):
                h = (h * base - aL * nums[i - 1] + nums[i + L - 1]) % MOD
                if h in seen:
                    return True
                seen.add(h)

            return False

        nums = [ord(s[i]) - ord("a") for i in range(len(s))]
        l, r = 1, len(s)
        while l < r:
            mid = (l + r) // 2
            if rabin_karp(mid, nums):
                l = mid + 1
            else:
                r = mid

        return l - 1
