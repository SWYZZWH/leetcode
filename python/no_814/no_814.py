# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]) -> bool:
            if root is None:
                return True

            should_prune = True
            if root.val == 1:
                should_prune = False

            if dfs(root.left):
                root.left = None
            else:
                should_prune = False

            if dfs(root.right):
                root.right = None
            else:
                should_prune = False

            return should_prune

        return root if not dfs(root) else None
