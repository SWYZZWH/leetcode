import collections
from typing import List


class Solution:
    # topological sort
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        G = collections.defaultdict(set)
        for edge in edges:
            G[edge[0]].add(edge[1])
            G[edge[1]].add(edge[0])

        q = collections.deque([i for i, nei in G.items() if len(nei) == 1])
        visited = 0
        while n - visited > 2:
            tmp = collections.deque()
            while q:
                node = q.popleft()
                visited += 1
                p = list(G[node])[0]
                G[p].remove(node)
                if len(G[p]) == 1: # len method should be O(1)
                    tmp.append(p)
            q = tmp

        return list(q)
