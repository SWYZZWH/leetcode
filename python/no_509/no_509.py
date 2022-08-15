class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    # top-down dp
    def fib(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]