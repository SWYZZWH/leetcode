# 973. K Closest Points to Origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points

        dist = [(point[0] * point[0] + point[1] * point[1], i) for i, point in enumerate(points)]
        heapq.heapify(dist)

        return [points[d[1]] for d in heapq.nsmallest(k, dist)]
