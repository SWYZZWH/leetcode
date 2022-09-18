import functools


class Solution:
    @functools.lru_cache
    def minJumps(self, arr: List[int]) -> int:
        m = collections.defaultdict(set)
        for i, num in enumerate(arr):
            m[num].add(i)

        starts = set([0])
        ends = set([len(arr) - 1])
        visited = set()
        visited_v = set()
        steps = 0

        while starts and ends:
            if len(ends) < len(starts):
                starts, ends = ends, starts

            nxt = set()
            for idx in starts:
                if idx < 0 or idx >= len(arr):
                    continue
                if idx in ends:
                    return steps
                visited.add(idx)
                if arr[idx] not in visited_v:
                    for i in m[arr[idx]]:
                        if i not in visited:
                            nxt.add(i)
                    visited_v.add(arr[idx])
                if idx - 1 not in visited:
                    nxt.add(idx - 1)
                if idx + 1 not in visited:
                    nxt.add(idx + 1)
            steps += 1
            starts = nxt

        return -1
