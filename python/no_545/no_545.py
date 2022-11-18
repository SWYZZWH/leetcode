# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


# BFS is not okay!!
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def is_leaf(node: Optional[TreeNode]) -> bool:
            return not node.left and not node.right

        # must do dfs
        def dfs(node: Optional[TreeNode], is_left: bool, is_border: bool) -> List[int]:
            if not node:
                return []

            if is_leaf(node):
                return [node.val]

            cur, l, r = [node.val] if is_border else [], [], []
            l = dfs(node.left, is_left, is_border and (is_left or not node.right))
            r = dfs(node.right, is_left, is_border and (not is_left or not node.left))
            if is_left:
                return cur + l + r
            else:
                return l + r + cur

        return [root.val] + dfs(root.left, True, True) + dfs(root.right, False, True)
