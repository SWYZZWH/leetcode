# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p, _ = self._serialize(root)

    def next(self) -> int:
        val = self.p.val
        self.p = self.p.right
        return val

    def hasNext(self) -> bool:
        return self.p is not None

    def _serialize(self, root: Optional[TreeNode]) -> (Optional[TreeNode], Optional[TreeNode]):
        if root is None:
            return None, None
        ll, lr, rl, rr = root, None, None, root
        if root.left:
            ll, lr = self._serialize(root.left)
        if root.right:
            rl, rr = self._serialize(root.right)

        root.left = lr
        root.right = rl
        if lr:
            lr.right = root
        if rl:
            rl.left = root
        return ll, rr


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = collections.deque([(root, 1)])

    def next(self) -> int:
        while True:
            node, flag = self.stk.pop()
            if flag == 2:
                return node.val
            if node.right:
                self.stk.append((node.right, 1))
            self.stk.append((node, 2))
            if node.left:
                self.stk.append((node.left, 1))

    def hasNext(self) -> bool:
        return len(self.stk) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()