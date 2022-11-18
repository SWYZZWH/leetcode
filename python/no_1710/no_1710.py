import heapq
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        h = [[-box[1], box[0]] for box in boxTypes]
        heapq.heapify(h)
        res = 0
        while h and truckSize:
            box = heapq.heappop(h)
            if box[1] > truckSize:
                res += truckSize * (-box[0])
                return res
            truckSize -= box[1]
            res += box[1] * (- box[0])
        return res