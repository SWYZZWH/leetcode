# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ret = [0]

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            res = 1
            l = dfs(root.left)
            r = dfs(root.right)
            ret[0] = max(ret[0], max(l, r))

            if root.left and root.val == root.left.val - 1:
                res = max(res, l + 1)
            if root.right and root.val == root.right.val - 1:
                res = max(res, r + 1)

            ret[0] = max(ret[0], res)
            return res

        dfs(root)
        return ret[0]
