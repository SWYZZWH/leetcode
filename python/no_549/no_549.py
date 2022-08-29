# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs
    # calculate and save longest consecutive path in subtree
    # return max length of consecutive path of which end is root
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ret = [0]

        def dfs(root: Optional[TreeNode]) -> (int, int):
            if root is None:
                return 0, 0

            # inc/dec means from bottom to up, the relationship of elements
            max_len_inc, max_len_dec = 1, 1
            l_inc, l_dec = dfs(root.left)
            r_inc, r_dec = dfs(root.right)

            if root.left and root.val == root.left.val + 1:
                max_len_inc = max(max_len_inc, 1 + l_inc)

            if root.left and root.val == root.left.val - 1:
                max_len_dec = max(max_len_dec, 1 + l_dec)

            if root.right and root.val == root.right.val + 1:
                max_len_inc = max(max_len_inc, 1 + r_inc)

            if root.right and root.val == root.right.val - 1:
                max_len_dec = max(max_len_dec, 1 + r_dec)

            ret[0] = max(max_len_inc, ret[0])
            ret[0] = max(max_len_dec, ret[0])

            # update ret in this subtree
            if root.left and root.right and root.left.val + 1 == root.val and root.right.val == root.val + 1:
                ret[0] = max(ret[0], l_inc + 1 + r_dec)

            if root.left and root.right and root.left.val - 1 == root.val and root.right.val == root.val - 1:
                ret[0] = max(ret[0], l_dec + 1 + r_inc)

            return max_len_inc, max_len_dec

        dfs(root)
        return ret[0]
