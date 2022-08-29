# should use two pointers...
from typing import List


class SparseVector:
    # compress the sparse vector
    def __init__(self, nums: List[int]):
        self.m = {}
        for i, num in enumerate(nums):
            self.m[i] = num

    # time complexity should be O(K), where K is number of 1's
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.m) > len(vec.m):
            return vec.dotProduct(self)
        ret = 0
        for idx, num1 in self.m.items():
            if idx in vec.m:
                ret += num1 * vec.m[idx]
        return ret

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
