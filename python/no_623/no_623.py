# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth <= 0:
            return root

        virtual_root = TreeNode(-1, root, None)
        q = collections.deque([(virtual_root, None, True)])
        cur_depth = 0
        while q:
            tmp = collections.deque()
            while q:
                cur_node, parent, is_left = q.popleft()
                if cur_node:
                    tmp.append((cur_node.left, cur_node, True))
                    tmp.append((cur_node.right, cur_node, False))
            cur_depth += 1
            q = tmp
            if cur_depth == depth:
                while q:
                    cur_node, parent, is_left = q.popleft()
                    new_node = TreeNode(val, None, None)
                    if is_left:
                        new_node.left = cur_node
                        parent.left = new_node
                    else:
                        new_node.right = cur_node
                        parent.right = new_node
                break
        return virtual_root.left
