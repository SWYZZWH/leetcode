from typing import List


class Solution:
    # same as no_6134, with a path set record the node we have visited
    # for each node, with a dict d {idx: dist}, and the circle length is d[i1] - d[i2]
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        n = len(edges)

        ret = -1
        for i in range(n):
            d = {}
            node = i
            l = 0
            while node != -1 and node not in visited:
                d[node] = l
                l += 1
                visited.add(node)
                node = edges[node]
            if node in d:
                ret = max(ret, l - d[node])

        return ret
