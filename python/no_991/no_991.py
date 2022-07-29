# There is a broken calculator that has the integer startValue on its display
# initially. In one operation, you can:
#
#
#  multiply the number on display by 2, or
#  subtract 1 from the number on display.
#
#
#  Given two integers startValue and target, return the minimum number of
# operations needed to display target on the calculator.
#
#
#  Example 1:
#
#
# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
#
#
#  Example 2:
#
#
# Input: startValue = 5, target = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
#
#
#  Example 3:
#
#
# Input: startValue = 3, target = 10
# Output: 3
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
#
#
#
#  Constraints:
#
#
#  1 <= startValue, target <= 10⁹
#
#
#  Related Topics Math Greedy 👍 2325 👎 195


# leetcode submit region begin(Prohibit modification and deletion)
# greedy! actually is obvious case target can be 10^9
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target <= startValue:
            return startValue - target
        skip = 0
        while True:
            last = target
            target = (target + 1) // 2
            skip += 1 + (last % 2 != 0)
            if target <= startValue < last:
                return skip + startValue - target
# leetcode submit region end(Prohibit modification and deletion)
