# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
#  Return the sum of the three integers.
#
#  You may assume that each input would have exactly one solution.
#
#
#  Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#  Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
#
#
#
#  Constraints:
#
#
#  3 <= nums.length <= 1000
#  -1000 <= nums[i] <= 1000
#  -10⁴ <= target <= 10⁴
#
#
#  Related Topics Array Two Pointers Sorting 👍 6437 👎 330


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     # sort first
#     # for each index, calculate res = target - nums[i]
#     # use two pointers, search minimum difference in nums[i+1:]
#
#     # another way is binary search
#     # find two num and binary search the third
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         diff = math.inf
#         ret = target
#         nums.sort()
#
#         for i in range(len(nums) - 2):
#             res = target - nums[i]
#             j, k = i + 1, len(nums) - 1
#             while j != k:
#                 if nums[j] + nums[k] == res:
#                     return target
#                 if abs(res - nums[j] - nums[k]) < diff:
#                     diff = abs(res - nums[j] - nums[k])
#                     ret = nums[i] + nums[j] + nums[k]
#                 if nums[j] + nums[k] < res:
#                     j += 1
#                 else:
#                     k -= 1
#
#         return ret

class Solution:
    # sort first
    # for each index, calculate res = target - nums[i]
    # use two pointers, search minimum difference in nums[i+1:]

    # another way is binary search
    # find two num and binary search the third
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = math.inf
        ret = target
        nums = sorted(nums)

        for i in range(len(nums) - 2):

            # optimization 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            res = target - nums[i]
            j, k = i + 1, len(nums) - 1

            # very important optimization
            if nums[i] + nums[k - 1] + nums[k] <= target:
                j = k - 1
            elif nums[i] + nums[j] + nums[j + 1] >= target:
                k = j + 1

            while j != k:
                if nums[j] + nums[k] == res:
                    return target
                if abs(res - nums[j] - nums[k]) < diff:
                    diff = abs(res - nums[j] - nums[k])
                    ret = nums[i] + nums[j] + nums[k]
                if nums[j] + nums[k] < res:
                    j += 1
                else:
                    k -= 1

        return ret
#
# class Solution:
#     # sort first
#     # for each index, calculate res = target - nums[i]
#     # use two pointers, search minimum difference in nums[i+1:]
#
#     # another way is binary search
#     # find two num and binary search the third
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         diff = math.inf
#         ret = target
#         nums = sorted(nums)
#
#         for i in range(len(nums) - 2):
#             res = target - nums[i]
#             j, k = i + 1, len(nums) - 1
#             while j != k:
#                 if nums[j] + nums[k] == res:
#                     return target
#                 if abs(res - nums[j] - nums[k]) < diff:
#                     diff = abs(res - nums[j] - nums[k])
#                     ret = nums[i] + nums[j] + nums[k]
#                 if nums[j] + nums[k] < res:
#                     j += 1
#                 else:
#                     k -= 1
#
#         return ret


# leetcode submit region end(Prohibit modification and deletion)
