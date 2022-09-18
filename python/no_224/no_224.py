# https://leetcode.com/problems/basic-calculator/discuss/2017431/Stop-hating-parsing-problems-and-start-having-fun
import collections
from typing import List


def check_circle(n: int, edges: List[List[int]]) -> bool:
    G = collections.defaultdict(set)
    for edge in edges:
        G[edge[0]].add(edge[1])
        G[edge[1]].add(edge[0])

    visited = set()

    def dfs(cur: int, parent: int) -> bool:
        if cur in visited:
            return True

        visited.add(cur)
        for neighbor in G[cur]:
            if neighbor == parent:
                continue
            if dfs(neighbor, cur):
                return True

        return False

    for i in range(n):
        if i in visited:
            continue
        if dfs(i, i):
            return True

    return False


if __name__ == "__main__":
    print(check_circle(3, [[0, 1], [0, 2], [1, 3]]))
