from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        return [[x, y] for i in intervals for (x, y) in [(i[0], min(toBeRemoved[0], i[1])), (max(toBeRemoved[1], i[0]), i[1])] if x < y]