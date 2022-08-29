import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        ret = 0

        # build stop info
        stop_info = collections.defaultdict(set)
        for route, stops in enumerate(routes):
            for stop in stops:
                stop_info[stop].add(route)

        visited_route = set()
        q = collections.deque([source])
        visited_stop = {source}

        while q:
            tmp = collections.deque()
            while q:
                stop = q.pop()
                if stop == target:
                    return ret
                for route in stop_info[stop]:
                    if route in visited_route:
                        continue
                    for s in routes[route]:
                        if s not in visited_stop:
                            tmp.append(s)
                            visited_stop.add(s)
                    visited_route.add(route)
            q = tmp
            ret += 1

        return -1
