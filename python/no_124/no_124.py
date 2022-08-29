# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = [-math.inf]  # global maximum path length

        # one path that root included, but also root is one end of the path
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            l = dfs(root.left)  # maximum path in left subtree, root.left must be one end of the path
            r = dfs(root.right)  # maximum path in right subtree, root.right must be one end of the path

            max_sum = root.val
            res = root.val
            if l > 0:
                if l >= r:
                    res += l
                max_sum += l

            if r > 0:
                if r > l:
                    res += r
                max_sum += r

            ret[0] = max(ret[0], max_sum)
            return res

        dfs(root)
        return ret[0]
