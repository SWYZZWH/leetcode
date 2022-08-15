"""
# Definition for a Node.

"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # just the same as preorder visit of binary tree
    def __init__(self):
        self.ret = []

    def dfs(self, root: 'Node'):
        if root is None:
            return

        self.ret.append(root.val)

        for child in root.children:
            self.dfs(child)

    def preorder(self, root: 'Node') -> List[int]:
        self.dfs(root)
        return self.ret
