# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        neg = x < 0
        x = abs(x)
        while True:
            if self.check_overflow(ret, x % 10, True, neg):
                return 0
            ret += x % 10
            x //= 10
            if x == 0:
                break
            if self.check_overflow(ret, -1, False, neg):
                return 0
            ret *= 10
        return ret if not neg else -ret

    def check_overflow(self, num: int, adder: int, is_add: bool, neg: bool) -> bool:
        limit = 0
        if neg:
            limit = (1 << 31)
        else:
            limit = (1 << 30) + ((1 << 30) - 1)

        if is_add:
            if limit - adder < num:
                return True
            return False

        if limit / 10 < num:
            return True
        return False
