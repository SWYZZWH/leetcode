# You are given a list of songs where the iᵗʰ song has a duration of time[i]
# seconds.
#
#  Return the number of pairs of songs for which their total duration in
# seconds is divisible by 60. Formally, we want the number of indices i, j such that i <
# j with (time[i] + time[j]) % 60 == 0.
#
#
#  Example 1:
#
#
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
#
#
#  Example 2:
#
#
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
#
#
#
#  Constraints:
#
#
#  1 <= time.length <= 6 * 10⁴
#  1 <= time[i] <= 500
#
#
#  Related Topics Array Hash Table Counting 👍 3299 👎 128


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    # just two-sum (take mod first)
    # remove pair: re
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        c = collections.Counter(time)
        ret = 0
        for t in time:
            if (60 - t) % 60 in c:
                ret += c[(60 - t) % 60]
                if t == (60 - t) % 60:
                    ret -= 1
        return ret // 2

# leetcode submit region end(Prohibit modification and deletion)
