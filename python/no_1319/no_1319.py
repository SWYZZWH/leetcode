from typing import List


# simple Union Find
class Solution:
    class UnionFind:

        def __init__(self, n: int):
            self.uf = [i for i in range(n)]

        def union(self, i: int, j: int):
            i_p, j_p = self.find(i), self.find(j)
            self.uf[j_p] = i_p

        def find(self, i: int) -> int:
            while self.uf[i] != i:
                self.uf[i] = self.uf[self.uf[i]]
                i = self.uf[i]
            return i

    # description sucks
    # count connected components by union find
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        uf = self.UnionFind(n)
        for conn in connections:
            uf.union(conn[0], conn[1])

        visited = set()
        for i in range(n):
            p = uf.find(i)
            if p not in visited:
                visited.add(p)

        return len(visited) - 1

