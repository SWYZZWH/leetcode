# We have n jobs, where every job is scheduled to be done from startTime[i] to
# endTime[i], obtaining a profit of profit[i].
#
#  You're given the startTime, endTime and profit arrays, return the maximum
# profit you can take such that there are no two jobs in the subset with overlapping
# time range.
#
#  If you choose a job that ends at time X you will be able to start another
# job that starts at time X.
#
#
#  Example 1:
#
#
#
#
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
#
#  Example 2:
#
#
#
#
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70
# ,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
#
#
#  Example 3:
#
#
#
#
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
#
#
#  Constraints:
#
#
#  1 <= startTime.length == endTime.length == profit.length <= 5 * 10⁴
#  1 <= startTime[i] < endTime[i] <= 10⁹
#  1 <= profit[i] <= 10⁴
#
#
#  Related Topics Array Binary Search Dynamic Programming Sorting 👍 3506 👎 38


# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class Solution:
    # the priority queue method(from left to right, maintains interval chains) is beautiful

    # from back to the front, insert one job into dp array each time according to the order of startTime
    # dp[t] means from start time: t to the end, the max possible profit we can gain
    # binary search the endTime(t_end) in all startTimes in dp array (right border) dp[t_end], if can't find any, dp[t_end] should be 0
    # record cur_max, and calculate max every time we insert a job, the dp[t_start] will be max(cur_max, dp[t_end])
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sorted by start time
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[0])
        startTime, endTime, profit = list(zip(*jobs))

        n, dp, cur_max = len(startTime), {}, 0
        for i in reversed(range(0, n)):
            last_max = 0
            idx = bisect.bisect_right(startTime, endTime[i] - 1, i + 1, n)
            if idx != len(startTime):
                last_max = dp[startTime[idx]]
            cur_max = max(cur_max, last_max + profit[i])
            dp[startTime[i]] = cur_max
        return dp[startTime[0]]
# leetcode submit region end(Prohibit modification and deletion)
