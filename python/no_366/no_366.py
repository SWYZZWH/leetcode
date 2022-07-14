# 366. Find Leaves of Binary Tree

# Given the root of a binary tree, collect a tree's nodes as if you were doing this:
#
# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.

# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # another solution: first get all height 0 nodes, then the height 1 nodes...
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # d = {}
        ret = []
        if root is None:
            return ret

        # visit tree find each p for each node, also init ret
        leaves = []
        self.dfs(root, None, leaves)
        while len(leaves) != 0:
            ret.append([leave.val for leave in leaves])
            newLeaves = []
            while len(leaves) != 0:
                leave = leaves.pop()
                p = leave.p
                if p is not None:
                    if leave == p.left:
                        p.left = None
                    if leave == p.right:
                        p.right = None
                    if p.left is None and p.right is None:
                        newLeaves.append(p)
            leaves = newLeaves
        return ret

    def dfs(self, root: TreeNode, p: Optional[TreeNode], ret: List[int]):
        if root is None:
            return

        root.p = p
        if root.left is None and root.right is None:
            ret.append(root.val)
            return

        if root.right is None:
            self.dfs(root.left, root, ret)

        if root.left is None:
            self.dfs(root.right, root, ret)
