# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:
#
# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# Return true if and only if all roads from source lead to destination.

from typing import List, Dict


class Solution:
    # Solution1(wrong) : reverse all edges, check all nodes that can be reached by destination, there shouldn't be any nodes left.

    # def rec(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    #     outgoings = {}
    #     for edge in edges:
    #         if edge[1] not in outgoings:
    #             outgoings[edge[1]] = [edge[0]]
    #         else:
    #             outgoings[edge[1]].append(edge[0])
    #
    #     q = [destination]
    #     not_visited = set([i for i in range(n)])
    #     while len(q) != 0:
    #         node = q.pop()
    #         if node not in not_visited:
    #             continue
    #         not_visited.remove(node)
    #         if node not in outgoings:
    #             continue
    #         next_nodes = outgoings[node]
    #         if node in next_nodes:
    #             return False
    #         for nn in next_nodes:
    #             q.append(nn)

    # common method: from edges list to edges array
    # def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    #     reverse = [[edge[1], edge[1]] for edge in edges]
    #     return self.rec(n, edges, source, destination) and self.rec(n, reverse, destination, source)

    def dfs(self, source: int, outgoings: Dict, destination: int, visited: Dict) -> bool:
        if source not in outgoings:
            return source == destination
        next_nodes = outgoings[source]
        for node in next_nodes:
            if visited[node]:
                return False
            visited[node] = True
            self.dfs(node, outgoings, destination, visited)
            visited[node] = False

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        outgoings = {}
        for edge in edges:
            if edge[1] not in outgoings:
                outgoings[edge[0]] = [edge[1]]
            else:
                outgoings[edge[0]].append(edge[1])
        visited = {i: False for i in range(n)}
        return self.dfs(source, outgoings, destination, visited)
