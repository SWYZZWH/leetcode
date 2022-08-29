import collections
from typing import List


class Solution:
    # classic topological sort
    # topological is implemented by BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cnt = [0 for i in range(numCourses)]
        G = [set() for i in range(numCourses)]
        for p in prerequisites:
            cnt[p[1]] += 1
            G[p[0]].add(p[1])

        q = [i for i in range(numCourses) if cnt[i] == 0]
        for idx in q:
            for j in G[idx]:
                cnt[j] -= 1
                if cnt[j] == 0:
                    q.append(j)

        return len(q) == numCourses
