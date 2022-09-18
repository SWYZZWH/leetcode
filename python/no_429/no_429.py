"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = []

        q = collections.deque([root])
        while q:
            tmp = collections.deque()
            row = []
            while q:
                cur = q.popleft()
                if cur:
                    row.append(cur.val)
                    for c in cur.children:
                        tmp.append(c)
            if row:
                ret.append(row)
            q = tmp

        return ret
