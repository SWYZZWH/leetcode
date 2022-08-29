# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # naive idea is BFS, which leads to O(n) time complexity
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(root, 1)])
        ret = 0
        while q:
            tmp = collections.deque()
            l_most = -1
            r_most = -1
            while q:
                node, no = q.popleft()
                if l_most == -1:
                    l_most = no
                    r_most = no
                else:
                    l_most = min(l_most, no)
                    r_most = max(r_most, no)
                if node.left:
                    tmp.append((node.left, 2 * no))
                if node.right:
                    tmp.append((node.right, 2 * no + 1))
            ret = max(ret, r_most - l_most + 1)
            q = tmp

        return ret
