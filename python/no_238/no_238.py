# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#  You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
#  Example 1:
#  Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
#  Example 2:
#  Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
#  Constraints:
#
#
#  2 <= nums.length <= 10⁵
#  -30 <= nums[i] <= 30
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
#  Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#  Related Topics Array Prefix Sum 👍 13543 👎 780


# leetcode submit region begin(Prohibit modification and deletion)

# the only thing to be consider is how to handle zero
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_mul = 1
        find_zero = False
        for i in nums:
            if i == 0:
                if find_zero:
                    return [0 for i in nums]
                find_zero = True
                continue
            all_mul *= i
        if find_zero:
            return [all_mul if i == 0 else 0 for i in nums]
        return [all_mul // i for i in nums]
# leetcode submit region end(Prohibit modification and deletion)
