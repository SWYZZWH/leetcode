# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # prefix sum
    # for pre-order dfs, every time in the loop there is a chain O(logn)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        ret = [0]

        def dfs(root: Optional[TreeNode], prefix_sum: int):
            if root is None:
                return

            cur_sum = prefix_sum + root.val
            if cur_sum - targetSum in d:
                ret[0] += d[cur_sum - targetSum]

            d[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            d[cur_sum] -= 1

        dfs(root, 0)
        return ret[0]
