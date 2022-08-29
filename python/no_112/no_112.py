# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    # simple dfs
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], target: int) -> bool:
            if root is None:
                return False
            if root.left is None and root.right is None:
                return root.val == target
            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)

        return dfs(root, targetSum)
