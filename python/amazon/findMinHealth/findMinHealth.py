# https://leetcode.com/discuss/interview-question/1789737/amazon-OA
# sum(power) - min(armor, max(power)) + 1a
import heapq
from typing import List


class Solution:
    # TLE...
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        visited = set([(i - 1, i) for i in range(1, len(nums))])
        h = [(abs(nums[i] - nums[i - 1]), i - 1, i) for i in range(1, len(nums))]
        heapq.heapify(h)

        # print(nums)
        i = 0
        while h:
            e = heapq.heappop(h)
            visited.add((e[1], e[2]))
            i += 1
            if i == k:
                return e[0]
            if e[1] - 1 >= 0 and (e[1] - 1, e[2]) not in visited:
                heapq.heappush(h, (abs(nums[e[1] - 1] - nums[e[1]]) + e[0], e[1] - 1, e[2]))

        return -1



