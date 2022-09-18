import heapq
from typing import List


class Solution:
    # k-way merge sort
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        candidates = [0 for i in range(min(k, m))]
        h = [(nums1[i] + nums2[0], i, 0) for i in range(len(candidates))]
        heapq.heapify(h)
        ret = []

        while h:
            e = heapq.heappop(h)
            ret.append([nums1[e[1]], nums2[e[2]]])
            if len(ret) == k:
                return ret
            candidates[e[1]] += 1
            if candidates[e[1]] < n:
                heapq.heappush(h, (nums1[e[1]] + nums2[candidates[e[1]]], e[1], candidates[e[1]]))

        return ret[:k]
