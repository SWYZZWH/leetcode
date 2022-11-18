# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def rec(root: Optional[TreeNode], no: int):
            if root is None:
                return 0
            if root.left == None and root.right == None:
                return no

            l, r = root.left, root.right
            ll_h, lr_h, rl_h, rr_h = 0, 0, 0, 0
            p = l
            while p:
                p = p.left
                ll_h += 1
            p = r
            while p:
                p = p.left
                rl_h += 1

            if ll_h > rl_h:
                return rec(root.left, 2 * no)

            return rec(root.right, 2 * no + 1)

        return rec(root, 1)