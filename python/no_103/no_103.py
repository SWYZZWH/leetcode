# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # just modify the standard BFS a little...
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ret = []
        # use stack, and change left and right each time
        q = collections.deque([root])
        left_to_right = True
        while q:
            tmp = collections.deque()
            tmp_ret = []
            while q:
                node = q.pop()
                if not node:
                    continue
                tmp_ret.append(node.val)
                if left_to_right:
                    tmp.append(node.left)
                    tmp.append(node.right)
                else:
                    tmp.append(node.right)
                    tmp.append(node.left)
            if tmp_ret:
                ret.append(tmp_ret)
            left_to_right = False if left_to_right else True
            q = tmp

        return ret
