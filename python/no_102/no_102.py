# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iteration solution use queue
    # dfs is also okay
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if root is None:
            return ret
        q = collections.deque()
        q.append(root)
        while q:
            tmp = collections.deque()
            ret.append([nn.val for nn in q])
            while q:
                n = q.popleft()
                if n.left is not None:
                    tmp.append(n.left)
                if n.right is not None:
                    tmp.append(n.right)
            q = tmp

        return ret
