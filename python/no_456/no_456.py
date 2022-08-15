# Given an array of n integers nums, a 132 pattern is a subsequence of three
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] <
# nums[j].
#
#  Return true if there is a 132 pattern in nums, otherwise, return false.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#
#
#  Example 2:
#
#
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
#
#  Example 3:
#
#
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3,
#  0] and [-1, 2, 0].
#
#
#
#  Constraints:
#
#
#  n == nums.length
#  1 <= n <= 2 * 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#
#
#  Related Topics Array Binary Search Stack Monotonic Stack Ordered Set 👍 4884
# 👎 277


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    # Solution1: find all the raising interval, search num in the rest of nums which value is in this interval,
    #       however, the complexity will be O(n ^ 2)
    # Solution2: mono-stack: the intuition is not all 3s are useful
    # Solution3: one pass mono-stack
    def find132pattern(self, nums: List[int]) -> bool:
        min_arr = []  # for 1
        cur_min = math.inf
        for i in range(len(nums)):
            cur_min = min(cur_min, nums[i])
            min_arr.append(cur_min)
        stk = collections.deque()  # for 3
        for i in reversed(range(len(nums))):
            if nums[i] <= min_arr[i]:
                continue
            while stk and min_arr[i] >= stk[-1]:
                stk.pop()
            if stk and stk[-1] < nums[i]:
                return True
            stk.append(nums[i])

        return False

# leetcode submit region end(Prohibit modification and deletion)
