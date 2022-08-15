# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes (i.e.,
# only nodes themselves may be changed.)
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
#  Example 2:
#
#
# Input: head = []
# Output: []
#
#
#  Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 100].
#  0 <= Node.val <= 100
#
#
#  Related Topics Linked List Recursion 👍 7621 👎 315


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# two pointer each time
# add virtual head to simplify code
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = virtual_head = ListNode(-1, head)
        while p.next is not None and p.next.next is not None:
            n1, n2, after = p.next, p.next.next, p.next.next.next
            n2.next, n1.next, p.next, p = n1, after, n2, n1
        return virtual_head.next
# leetcode submit region end(Prohibit modification and deletion)
