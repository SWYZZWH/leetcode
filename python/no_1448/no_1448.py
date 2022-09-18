# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # we simply dfs from the root, preorder visit the tree
    # maintain a current maximum value
    def goodNodes(self, root: TreeNode) -> int:
        ret = [0]

        def dfs(root: TreeNode, cur_max: int):
            if root is None:
                return

            if root.val >= cur_max:
                ret[0] += 1

            dfs(root.left, max(cur_max, root.val))
            dfs(root.right, max(cur_max, root.val))

        dfs(root, -math.inf)
        return ret[0]
