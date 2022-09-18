class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(n: Optional[TreeNode]):
            if n is None:
                return ""
            ret = str(n.val)
            left = preorder(n.left)
            right = preorder(n.right)
            if left and right:
                ret += "("+ left + ")"
                ret += "("+ right + ")"
            elif left:
                ret += "("+ left + ")"
            elif right:
                ret += "()"
                ret += "("+ right + ")"
            return ret
        return preorder(root)