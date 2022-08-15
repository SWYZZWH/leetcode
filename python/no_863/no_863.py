from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # double recursive
    # we can also mark every parent of TreeNode (O(N) and the input is modified)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        ret = set()

        def dfs(root: TreeNode, depth: int):
            if root is None:
                return

            if depth == 0:
                ret.add(root.val)

            dfs(root.left, depth - 1)
            dfs(root.right, depth - 1)

        # find the target and all of its parent
        def find(root: TreeNode):
            if root is None:
                return False, 0

            if root is target:
                dfs(root, k)
                return True, k

            f, res = find(root.left)
            if f:
                if res - 1 == 0:
                    ret.add(root.val)
                dfs(root.right, res - 2)
                return True, res - 1

            f, res = find(root.right)
            if f:
                if res - 1 == 0:
                    ret.add(root.val)
                dfs(root.left, res - 2)
                return True, res - 1

            return False, 0

        find(root)
        return list(ret)
