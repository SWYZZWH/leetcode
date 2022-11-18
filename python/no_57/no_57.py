from bisect import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        marks = [t for i in intervals for t in i]
        l = bisect.bisect_left(marks, newInterval[0])
        start = l // 2
        r = bisect.bisect_right(marks, newInterval[1])
        end = (r - 1) // 2

        if start < len(intervals):
            newInterval[0] = min(newInterval[0], intervals[start][0])
        if 0 <= end < len(intervals):
            newInterval[1] = max(newInterval[1], intervals[end][1])
        return intervals[:start] + [newInterval] + intervals[end + 1:]
