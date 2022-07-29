# Given two non-negative integers low and high. Return the count of odd numbers
# between low and high (inclusive).
#
#
#  Example 1:
#
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
#
#  Example 2:
#
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
#
#  Constraints:
#
#
#  0 <= low <= high <= 10^9
#
#
#  Related Topics Math 👍 883 👎 65


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # nothing to say...
    def countOdds(self, low: int, high: int) -> int:
        left_odd = low % 2 == 0
        right_odd = high % 2 == 0
        ret = 0
        if left_odd and right_odd:
            high = high - 1
        if not left_odd and not right_odd:
            ret += 1
            high = high - 1
        return ret + (high - low + 1) // 2
# leetcode submit region end(Prohibit modification and deletion)
