import collections
from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        def split_num(num: int) -> List[int]:
            q = collections.deque()
            while num:
                q.appendleft(num % 10)
                num //= 10
            return list(q)

        def build_num(lst: List[int]) -> int:
            res = 0
            for i in range(len(lst)):
                res *= 10
                res += lst[i]
            return res

        lst = split_num(num)
        for i in range(len(lst) - 1):
            max_idx = i
            for j in range(i + 1, len(lst)):
                if lst[j] >= lst[max_idx]:
                    max_idx = j
            if max_idx != i and lst[max_idx] != lst[i]:
                lst[max_idx], lst[i] = lst[i], lst[max_idx]
                return build_num(lst)

        return num