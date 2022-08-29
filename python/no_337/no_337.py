# Definition for a binary tree node.
from typing import Optional


# Under what cases we must use tree dp?

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# simple recursive problem
# time complexity is O(n)
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> (int, int):
            # if root is None:
            #     return 0, 0
            stole = root.val
            l_s, l_ns = 0, 0
            r_s, r_ns = 0, 0
            if root.left:
                l_s, l_ns = dfs(root.left)
            if root.right:
                r_s, r_ns = dfs(root.right)
            s = root.val + l_ns + r_ns
            ns = max(max(l_ns + r_ns, l_s + r_ns), max(l_s + r_s, l_ns + r_s))

            return s, ns

        return max(dfs(root))
