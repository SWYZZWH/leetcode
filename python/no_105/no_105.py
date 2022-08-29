# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # classic of the classic
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # better do it recursively
        if len(preorder) == 0:
            return None
        mid = 0
        while inorder[mid] != preorder[0]:
            mid += 1
        return TreeNode(preorder[0], self.buildTree(preorder[1:1 + mid], inorder[:mid]), self.buildTree(preorder[mid + 1:], inorder[mid + 1:]))