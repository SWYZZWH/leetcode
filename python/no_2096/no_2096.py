# 2096. Step-By-Step Directions From a Binary Tree Node to Another


# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.

# first: find common parent
# then: from source -> common parent parent -> dest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:

    def searchForNodeByVal(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.left is not None:
            root.left.p = root
            left = self.searchForNodeByVal(root.left, val)
            if left is not None:
                return left
        if root.right is not None:
            root.right.p = root
            right = self.searchForNodeByVal(root.right, val)
            if right is not None:
                return right
        return None

    def findCommonParent(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> (Optional[TreeNode], int, List[int]):
        if a is None or b is None:
            return None
        a_parents, b_parents = [], []
        p = a
        while p is not None:
            a_parents.append(p)
            p = p.p
        p = b
        while p is not None:
            b_parents.append(p)
            p = p.p

        a_ret = 0
        for p in a_parents:
            if p.val in (p.val for p in b_parents):
                return p, a_ret, b_parents
            a_ret += 1

        return None, None, None

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        root.p = None
        start, dest = self.searchForNodeByVal(root, startValue), self.searchForNodeByVal(root, destValue)
        p, start_parents, dest_parents = self.findCommonParent(start, dest)
        ret = "U" * start_parents

        i = len(dest_parents) - 1
        pp = dest_parents[i]
        while pp != p:
            i -= 1
            pp = dest_parents[i]

        for pp in reversed(dest_parents[:i + 1]):
            if p == pp:
                continue
            if p.left is not None and pp.val == p.left.val:
                p = p.left
                ret += "L"
            else:
                p = p.right
                ret += "R"
            if pp.val == destValue:
                return ret
        return ret
