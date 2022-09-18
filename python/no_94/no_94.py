# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        # push elements in the stack if the cur node has left node
        # pop out one element from the stack and add it to the ret array
        # push the right child of cur node if any, and return to step 1

        #        1
        #       2
        #      3
        #     4
        #

        if not root:
            return ret

        first = collections.deque([root])
        second = collections.deque()

        while first or second:
            if first:
                node = first.pop()
                if node.left:
                    first.append(node.left)
                second.append(node)
            else:
                node = second.pop()
                ret.append(node.val)
                if node.right:
                    first.append(node.right)

        return ret