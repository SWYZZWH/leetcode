# 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Constraints:
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104

class Solution:
    # naive way is O(n), however, n can be so large
    # use a cache and solve the problem recursively
    # def __init__(self):
    #     self.cache = {0: 1.0}
    #
    # def myPow(self, x: float, n: int) -> float:
    #     if n in self.cache:
    #         return self.cache[n]
    #
    #     ret = 0
    #     if n == 1:
    #         ret = x
    #     elif n == -1:
    #         ret = 1 / x
    #     else:
    #         ret = self.myPow(x, n // 2) * self.myPow(x, n - n // 2)
    #
    #     self.cache[n] = ret
    #     return ret

    # however, the space complexity is O(logN)
    # to achieve O(1) space complexity, we can't solve it recursively
    # let's represent the n in 2-bit: 11011
    # then we add x^(2*i) if n[i] == 1
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        neg = n < 0
        if neg:
            n = -n

        res = x
        ret = 1
        if n % 2 == 1:
            ret *= res
        n = n // 2

        while n:
            res = res * res
            if n % 2 == 1:
                ret *= res
            n = n // 2

        return ret if not neg else 1 / ret

