# k-sum:
# complexity: O(N ** (k/2))
# cut into two parts, build a hashmap for first, and search while visit the other part
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = collections.defaultdict(int)
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                s = nums1[i] + nums2[j]
                d[s] += 1

        ret = 0
        for i in range(n):
            for j in range(n):
                ret += d[-nums3[i] - nums4[j]]

        return ret
