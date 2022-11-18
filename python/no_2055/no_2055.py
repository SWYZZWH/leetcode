from bisect import bisect
from typing import List


# binary seach
# prefix sum

def platesBetweenCandles(self, s, queries):
    A = [i for i, c in enumerate(s) if c == '|']
    res = []
    for a, b in queries:
        i = bisect.bisect_left(A, a)
        j = bisect.bisect(A, b) - 1
        res.append((A[j] - A[i]) - (j - i) if i < j else 0) # way around to calculate the res instead of storing prefix_sum
    return res

# class Solution:
#     def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
#         n = len(s)
#         l = []
#         candles = [idx for idx in range(n) if s[idx] == "|"]
#         prefix_sum = [0 for i in range(len(candles))]
#         j = 0
#         total = 0
#         for i in range(n):
#             if s[i] == "*":
#                 total += 1
#             else:
#                 prefix_sum[j] = total
#                 j += 1
#
#         res = []
#         for q in queries:
#             left = bisect.bisect_left(candles, q[0])
#             right = bisect.bisect_right(candles, q[1])
#             if right == left:
#                 res.append(0)
#             else:
#                 res.append(prefix_sum[right - 1] - prefix_sum[left])
#
#         return res