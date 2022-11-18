import collections
import math

# monotonic stack
class StockSpanner:

    def __init__(self):
        self.stk = collections.deque([(math.inf, 0)])
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while self.stk and self.stk[-1][0] <= price:
            self.stk.pop()

        res = self.day - self.stk[-1][1]
        self.stk.append((price, self.day))
        return res
