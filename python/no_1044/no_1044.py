from functools import reduce
from typing import List


class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def rabin_karp(nums: List[int], L: int) -> int:
            if L > len(nums):
                return -1
            MOD = 2 ** 63 - 1
            base = 26
            h = (reduce(lambda x, y: x * base + y, nums[:L])) % MOD
            s = {h}
            aL = pow(base, L, MOD)
            for i in range(1, len(nums) - L + 1):
                h = (h * base - aL * nums[i - 1] + nums[i + L - 1]) % MOD
                if h in s:
                    return i
                s.add(h)
            return -1

        nums = [ord(s[i]) - ord("a") for i in range(len(s))]
        l, r = 1, len(s)
        max_len = 0
        idx = -1
        while l < r:
            mid = (l + r) // 2
            i = rabin_karp(nums, mid)
            if i == -1:
                r = mid
            else:
                if mid > max_len:
                    max_len = mid
                    idx = i
                l = mid + 1

        return "" if idx == -1 else s[idx: idx + max_len]