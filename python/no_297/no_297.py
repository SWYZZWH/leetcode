# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the same or
# another computer environment.
#
#  Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work. You
# just need to ensure that a binary tree can be serialized to a string and this
# string can be deserialized to the original tree structure.
#
#  Clarification: The input/output format is the same as how LeetCode
# serializes a binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
#
#
#  Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
#
#  Example 2:
#
#
# Input: root = []
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 10⁴].
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics String Tree Depth-First Search Breadth-First Search Design
# Binary Tree 👍 7276 👎 273


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


# simplest way: serialize to pre-order + "|" + mid-order and deserialize from two strings
# leetcode way: BFS
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        q = collections.deque()
        q.append(root)

        while len(q) != 0:
            tmp_queue = collections.deque()
            has_next_level = False
            while len(q) != 0:
                n = q.popleft()
                if n is None:
                    ret.append("null")
                    continue
                ret.append(str(n.val))
                if n.left is not None or n.right is not None:
                    has_next_level = True
                tmp_queue.append(n.left)
                tmp_queue.append(n.right)
            if not has_next_level:
                break
            q = tmp_queue

        return "[" + ",".join(ret) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        q = data[1:-1].split(",")
        if len(q) == 0 or q[0] == "null":
            return None
        root = TreeNode(int(q[0]))

        # can be replaced by a queue
        node_lst = [None for i in range(len(q))]
        node_lst[0] = root

        p_idx, child_idx = 0, 1
        while True:
            while p_idx < len(q) and q[p_idx] == "null": p_idx += 1
            if p_idx == len(q):
                break
            p = node_lst[p_idx]
            left, right = None, None
            if child_idx < len(q) and q[child_idx] != "null":
                left = TreeNode(int(q[child_idx]))
                node_lst[child_idx] = left
            child_idx += 1
            if child_idx < len(q) and q[child_idx] != "null":
                right = TreeNode(int(q[child_idx]))
                node_lst[child_idx] = right
            child_idx += 1
            p.left, p.right = left, right
            p_idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
