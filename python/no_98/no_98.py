# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # dfs with optimization
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return vals: isValid, left most, right most
        # opt 1: multiple return value
        def dfs(root: Optional[TreeNode]) -> (bool, int, int):
            if root is None:
                return True, 2 ** 31, -2 ** 31 - 1

            ok_l, ll, lr = dfs(root.left)
            if not ok_l or lr >= root.val:  # opt 2, cut dfs tree
                return False, 0, 0

            ok_r, rl, rr = dfs(root.right)
            if not ok_r or root.val >= rl:
                return False, 0, 0

            return True, min(ll, root.val), max(rr, root.val)

        return dfs(root)[0]
