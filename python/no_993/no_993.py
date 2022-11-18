# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if x == root.val or y == root.val:
            return False

        def find(node: Optional[TreeNode], n: int, cur_depth: int, p: Optional[TreeNode]) -> (int, int):
            if node == None:
                return (-1, -1)
            if node.val == n:
                return (cur_depth, p.val)

            l_depth, l_p = find(node.left, n, cur_depth + 1, node)
            if l_depth != -1:
                return (l_depth, l_p)
            r_depth, r_p = find(node.right, n, cur_depth + 1, node)
            if r_depth != -1:
                return (r_depth, r_p)

            return (-1, -1)

        d1, p1 = find(root, x, 0, None)
        d2, p2 = find(root, y, 0, None)
        return d1 == d2 and p1 != p2