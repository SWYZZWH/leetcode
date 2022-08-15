# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def dfs(n: Optional[TreeNode]):
            if n is None:
                return

            if n.left is None and n.right is None:
                return

            if n.left is not None and n.right is None:
                ret.append(n.left.val)

            if n.right is not None and n.left is None:
                ret.append(n.right.val)

            dfs(n.left)
            dfs(n.right)

        dfs(root)

        return ret
