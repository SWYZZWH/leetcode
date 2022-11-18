# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# tree dp
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @functools.cache
        def dfs(cur: Optional[TreeNode], is_cur_covered: bool, is_put: bool) -> int:
            if cur is None:
                return 0
            res = 1 + dfs(cur.left, True, False) + dfs(cur.right, True, False)
            if is_put:
                return res
            if is_cur_covered:
                return min(res, dfs(cur.left, False, False) + dfs(cur.right, False, False))
            else:
                if cur.left:
                    res = min(res, dfs(cur.left, False, True) + dfs(cur.right, False, False))
                if cur.right:
                    res = min(res, dfs(cur.left, False, False) + dfs(cur.right, False, True))
            return res
        return dfs(root, False, False)