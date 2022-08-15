import math
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        path1 = set()
        dist1 = dict()
        # from node 1 to all nodes
        n1 = node1
        l1 = 0
        while n1 != -1 and n1 not in path1:
            path1.add(n1)
            dist1[n1] = l1
            l1 += 1
            n1 = edges[n1]

        path2 = set()
        dist2 = dict()
        # from node 1 to all nodes
        n2 = node2
        l2 = 0
        while n2 != -1 and n2 not in path2:
            path2.add(n2)
            dist2[n2] = l2
            l2 += 1
            n2 = edges[n2]

        common_dist = math.inf
        idx = -1
        for k, v1 in dist1.items():
            if k not in dist2:
                continue
            if max(v1, dist2[k]) <= common_dist:
                if max(v1, dist2[k]) != common_dist or idx == -1 or k < idx:
                    idx = k
                common_dist = min(max(v1, dist2[k]), common_dist)

        return idx
