class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        MOD = 10 ** 9  + 7
        for i in range(1, n + 1):
            l = i.bit_length()
            res %= MOD
            res <<= l
            res += i
        return res % MOD