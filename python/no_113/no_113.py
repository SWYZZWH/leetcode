# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []

        def dfs(prefix: List[int], root: Optional[TreeNode], t: int):
            if root is None:
                return
            # if root.left is None and root.right is None and root.val == t:
            #     ret.append(prefix + [root.val])
            # dfs(prefix + [root.val], root.left, t - root.val)
            # dfs(prefix + [root.val], root.right, t - root.val)

            prefix.append(root.val)
            if root.left is None and root.right is None and root.val == t:
                ret.append(prefix.copy())  # back-tracking optimization
            dfs(prefix, root.left, t - root.val)
            dfs(prefix, root.right, t - root.val)
            prefix.pop(-1)

        dfs([], root, targetSum)
        return ret
