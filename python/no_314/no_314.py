# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    # BFS can reach O(N)
    # one thing to notice is the column number of every node is continuously
    # which means there is no void in [left_border, right_border]
    # and BFS keeps left to right order for nodes in each row
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # simply remember the column number and row number
        ret = []
        if root is None:
            return ret

        d = collections.defaultdict(list)

        q = collections.deque()
        q.append((0, 0, root))

        l_border, r_border = 0, 0
        while q:
            r, c, node = q.popleft()
            d[c].append(node.val)
            l_border = min(c, l_border)
            r_border = max(c, r_border)
            if node.left:
                q.append((r + 1, c - 1, node.left))
            if node.right:
                q.append((r + 1, c + 1, node.right))

        for i in range(l_border, r_border + 1):
            ret.append(d[i])

        return ret
