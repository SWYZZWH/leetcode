# Given an array intervals where intervals[i] = [li, ri] represent the interval
# [li, ri), remove all intervals that are covered by another interval in the list.
#
#
#  The interval [a, b) is covered by the interval [c, d) if and only if c <= a
# and b <= d.
#
#  Return the number of remaining intervals.
#
#
#  Example 1:
#
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#
#
#  Example 2:
#
#
# Input: intervals = [[1,4],[2,3]]
# Output: 1
#
#
#
#  Constraints:
#
#
#  1 <= intervals.length <= 1000
#  intervals[i].length == 2
#  0 <= li < ri <= 10⁵
#  All the given intervals are unique.
#
#
#  Related Topics Array Sorting 👍 1926 👎 46


# leetcode submit region begin(Prohibit modification and deletion)
from operator import itemgetter
from typing import List


class Solution:
    # don't know if this can be solved in linear time
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=itemgetter(0))
        ret = 0
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] == cur_interval[0] and intervals[i][1] >= cur_interval[1]:
                ret += 1
                cur_interval = intervals[i]
            elif intervals[i][0] <= cur_interval[1] and intervals[i][1] <= cur_interval[1]:
                ret += 1
            else:
                cur_interval = intervals[i]
        return len(intervals) - ret
# leetcode submit region end(Prohibit modification and deletion)
