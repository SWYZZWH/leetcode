import collections


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # build tree from reversed
        t = collections.defaultdict(list)
        ret = []

        for i in range(len(pid)):
            t[ppid[i]].append(pid[i])

        # kill use BFS
        #         q = collections.deque()
        #         q.append(kill)

        #         while q:
        #             p = q.popleft()
        #             ret.append(p)
        #             for child in t[p]:
        #                 q.append(child)

        # kill use DFS
        def dfs(root: int):
            ret.append(root)
            for child in t[root]:
                dfs(child)

        dfs(kill)
        return ret
