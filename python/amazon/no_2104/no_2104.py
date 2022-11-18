import collections
import math
from typing import List


class Solution:
    # at index i, check the last smaller value, check the last biger
    # nums = [4,-2,-3,4,1]
    # idx 0 max_stk = [(4, 0)], pre_sum = 0, sum += 4 * (0 - -1), pre_sum = sum
    # idx 1 max_stk = [(4, 0), (-2, 1)], pre_sum = 4, sum += -2 * (1 - 0) + 4 * (0 - --1), pre_sum = 4 + -2 = 2
    # idx 2 max_stk = [(4, 0), (-2, 1), (-3, 2)], sum += 4 * (0 - -1) + -2 * (1 - 0) + - 3 * (2 - 1)  pre_sum = -1
    # idx 2 max_stk = [(4, 0), (1, 3)], pre_sum = -2 - -2 * (1 - 0) - -3 * (2- 1) = -1 + 2 + 3 = 4, sum -= 4 + 1 *(3 - 0), pre_sum = sum  = 4
    # idx 3 max_stk = [(4, 3)] sum += 4 * (3 - -1)
    # idx 4 max_stk = [(4, 3), (1, 4)]

    # check lee215's solution
    def subArrayRanges(self, nums: List[int]) -> int:
        max_stk, min_stk = collections.deque([(math.inf, -1)]), collections.deque([(-math.inf, -1)])
        ret = 0
        pre_max_sum = 0
        pre_min_sum = 0
        for i, num in enumerate(nums):
            while max_stk and num > max_stk[-1][0]:
                e = max_stk.pop()
                pre_max_sum -= e[0] * (e[1] - max_stk[-1][1])
            pre_max_sum = pre_max_sum + num * (i - max_stk[-1][1])
            max_stk.append((num, i))
            while min_stk and num < min_stk[-1][0]:
                e = min_stk.pop()
                pre_min_sum -= e[0] * (e[1] - min_stk[-1][1])
            pre_min_sum = pre_min_sum + num * (i - min_stk[-1][1])
            min_stk.append((num, i))
            ret += pre_max_sum - pre_min_sum

        return ret