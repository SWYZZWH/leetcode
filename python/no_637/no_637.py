# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import Optional, List


class Solution:
    # simple BFS
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        if root is None:
            return ret
        q = collections.deque([root])

        while q:
            tmp = collections.deque()
            cur_level_sum = 0
            cur_level_cnt = 0
            while q:
                e = q.pop()
                cur_level_sum += e.val
                cur_level_cnt += 1
                if e.left:
                    tmp.append(e.left)
                if e.right:
                    tmp.append(e.right)
            if cur_level_cnt > 0:
                ret.append(cur_level_sum / cur_level_cnt)
            q = tmp

        return ret
