# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# don't do that in a real practice, it's stupid
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        pre = None
        while p.next:
            if not pre:
                pre = node
            else:
                pre = p
            p.val = p.next.val
            p = p.next
        pre.next = None
