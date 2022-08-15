import functools


class Solution:
    # simple fibnacci
    # def __init__(self):
    #     self.cache = {0: 0, 1: 1}

    @functools.cache
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
