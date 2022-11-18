# https://leetcode.com/problems/find-the-k-sum-of-an-array/
# https://leetcode.com/discuss/interview-question/1895396/amazon-sde-new-grad-oa-k-most-popular-combos
import heapq
from typing import List

class Solution:
    # another BFS
    # level 0 : [1]
    # level 1: [2] [1,2] # take or not take 2
    # level 3:[3] [2,3] [1,3] [1,2,3] # first take 3, then decide whether keep 3 or not
    # level 4:[4] [3,4] [2,4] [2,3,4] [1,4] [1,3,4] [1,2,4] [1,2,3,4]
    # another simple solution:
    # if k < 2 ** i:
    # put all 2 ** i elements in the heap and pop the kth
    def kSum(self, nums: List[int], k: int) -> int:
        ini = sum([num for num in nums if num > 0])
        nums = sorted([num if num > 0 else - num for num in nums])
        if k == 1:
            return ini
        h = [(nums[0], 0)]
        index = 1
        while h:
            e = heapq.heappop(h)
            index += 1
            if index == k:
                return ini - e[0]
            if e[1] + 1 < len(nums):
                heapq.heappush(h, (e[0] + nums[e[1] + 1], e[1] + 1))
                heapq.heappush(h, (e[0] + nums[e[1] + 1] - nums[e[1]], e[1] + 1))
        return -1

