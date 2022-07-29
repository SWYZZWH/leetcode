# 239. Sliding Window Maximum
import math
from collections import deque
from typing import List

from sortedcontainers import SortedDict


# class Solution:
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.

# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

# Solution 1 : use sortedMap(RB Tree), time complexity is O(n log n + k log k)
# Solution 2 : monotonous stack/queue
# Solution 3 : like no_42, get the maximum from left and from right, the brilliant part is: divide nums into small groups (size k)

# def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#     n = len(nums)
#     d = SortedDict()
#     ret = math.inf
#     for i in range(0, k):
#         if nums[i] in d:
#             d.update({nums[i]: d[nums[i]] + 1})
#         else:
#             d.setdefault(nums[i], 1)
#     ret_lst = [min(ret, max(nums[0: k]))]
#     for i in range(0, n - k):
#         # remove nums[i]
#         if d[nums[i]] == 1:
#             d.pop(nums[i])
#         else:
#             d.update({nums[i]: d[nums[i] - 1]})
#         # append nums[i + k]
#         if nums[i + k] in d:
#             d.update({nums[i + k]: d[nums[i + k]] + 1})
#         else:
#             d.setdefault(nums[i + k], 1)
#         ret_lst.append(d.peekitem(-1)[0])
#     return ret_lst


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output
