# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stk = collections.deque([(root, 0)])
        ret = []

        while stk:
            node = stk.pop()
            if node[1] == 0:
                stk.append((node[0], 1))
                if node[0].right:
                    stk.append((node[0].right, 0))
                if node[0].left:
                    stk.append((node[0].left, 0))
            else:
                ret.append(node[0].val)

        return ret