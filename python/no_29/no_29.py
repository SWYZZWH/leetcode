from bisect import bisect


class Solution:
    # basic idea is using add/subtract instead of multiplication
    # however, this can be accelerated by exponential
    def divide(self, dividend: int, divisor: int) -> int:
        dd, ds = abs(dividend), abs(divisor)
        cache = [ds for i in range(32)]
        for i in range(1, len(cache)):
            cache[i] = cache[i - 1] + cache[i - 1]

        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        ret = 0
        while dd >= ds:
            idx = bisect.bisect_right(cache, dd) - 1
            ret += 1 << idx if idx >= 0 else 0
            dd -= cache[idx]
        ret = min(ret, (1 << 31) - 1) if not neg else max(- ret, - 1 << 31)
        return ret
