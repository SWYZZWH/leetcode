# 362. Design Hit Counter

# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
#
# Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.
#
# Implement the HitCounter class:
#
# HitCounter() Initializes the object of the hit counter system.
# void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
# int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

# Constraints:
#
# 1 <= timestamp <= 2 * 109
# All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# At most 300 calls will be made to hit and getHits.

# basic idea is use binary search, which will cost O(MlogN) time and O(N) space
# however, if the hits each seconds go huge, we can use a sumArray to store total hits till this second. which is (timestamp, freq)
import bisect


# better use queue
class HitCounter:

    def __init__(self):
        # 0 ts, 1 freq
        self.sum_arr = []
        self.cur_sum = 0

    def hit(self, timestamp: int) -> None:
        if len(self.sum_arr) == 0 or self.sum_arr[-1][0] != timestamp:
            self.sum_arr.append((timestamp, 1 if len(self.sum_arr) == 0 else self.sum_arr[-1][1] + 1))
        else:
            self.sum_arr[-1] = (timestamp, self.sum_arr[-1][1] + 1)

    def getHits(self, timestamp: int) -> int:
        idx = bisect.bisect_left(self.sum_arr, timestamp - 300)
        last_sum = 0
        if idx != 0 or self.sum_arr[idx][0] == timestamp - 300:
            last_sum = self.sum_arr[idx][1]
        return self.sum_arr[-1][1] - last_sum

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
