import collections

from sortedcontainers import SortedList


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        return sum(freq[1] * (i // 9 + 1) for i, freq in enumerate(collections.Counter(s).most_common()))

# class Solution:
#     def minimumKeypresses(self, s: str) -> int:
#         c = collections.Counter(s)
#         sl = SortedList()
#         for freq in c.values():
#             sl.add(-freq)
#
#         res = 0
#         for i, freq in enumerate(sl):
#             res += (- freq) * (i // 9 + 1)
#         return res
