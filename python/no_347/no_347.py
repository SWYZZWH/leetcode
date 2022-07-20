# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
import heapq
from collections import Counter
from typing import List

# topK means quick_select
# bucket sort might be a good idea, just build a bucket size len(nums)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # transfer to set and heapify
        h = []
        for k, v in freq.items():
            heapq.heappush(h, (v, k))
        return [pair[1] for pair in heapq.nlargest(k, h)]


if __name__ == "__main__":
    s = Solution()
    s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
