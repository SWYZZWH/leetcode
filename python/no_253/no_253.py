from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timestamps = []
        for i in intervals:
            timestamps.append((i[0], 0))
            timestamps.append((i[1], -1))

        timestamps.sort()
        res = 0
        cur = 0
        for ts in timestamps:
            if ts[1] == 0:
                cur += 1
            if ts[1] == -1:
                cur -= 1
            res = max(res, cur)

        return res