"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# clearify the condition and design test cases
# [2] [1] will lead to infinite loop and stack overflow
# we should build nodes first and connect them after wards
# propose a solution & show it works & complexity
# dfs, by the way bfs also works
class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = {}

        def build_graph(node: 'Node'):
            if node in visited:
                return
            new_node = Node(node.val, [])
            visited[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    build_graph(neighbor)
                new_node.neighbors.append(visited[neighbor.val])

        build_graph(node)
        return visited[1]
