"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import functools


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node: 'Optional[Node]', parent: 'Optional[Node]'):
            if node is None:
                return

            dfs(node.left, node)
            if not parent:
                node.next = None
            elif node == parent.left:
                node.next = parent.right
            else:
                if not parent.next:
                    node.next = None
                else:
                    node.next = parent.next.left
            dfs(node.right, node)

        dfs(root, None)
        return root
