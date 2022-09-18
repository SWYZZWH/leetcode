# https://oi-wiki.org/graph/cut/
import collections
from typing import List


class Solution:

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        G = collections.defaultdict(set)
        for conn in connections:
            G[conn[0]].add(conn[1])
            G[conn[1]].add(conn[0])

        low = [0 for i in range(n)]
        dfs_cnt = [0 for i in range(n)]
        dfs_clock = [0]
        bridge_set = set()

        # pre_order for dfs_cnt and post_order for low
        def cut_edge(cur: int, pa: int):
            dfs_clock[0] += 1
            low[cur] = dfs_cnt[cur] = dfs_clock[0]
            for child in G[cur]:
                if dfs_cnt[child] == 0:
                    cut_edge(child, cur)
                    low[cur] = min(low[cur], low[child])
                    if low[child] > dfs_cnt[cur]:
                        bridge_set.add((min(child, cur), max(cur, child)))
                else:
                    if dfs_cnt[child] < dfs_cnt[cur] and child != pa:
                        low[cur] = min(low[cur], dfs_cnt[child])

        cut_edge(0, 0)

        ret = []
        for b in bridge_set:
            ret.append([b[0], b[1]])
        return ret
