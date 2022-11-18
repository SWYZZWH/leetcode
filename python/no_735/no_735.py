import collections
from typing import List


class Solution:
    # stack is more elegant
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ll = collections.deque()
        lr = collections.deque()
        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                cur = asteroids[i]
                while lr and cur + lr[-1] < 0:
                    lr.pop()
                if lr and lr[-1] + cur == 0:
                    lr.pop()
                elif not lr:
                    ll.append(cur)
            else:
                lr.append(asteroids[i])

        return list(ll + lr)