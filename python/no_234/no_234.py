# Given the head of a singly linked list, return true if it is a palindrome.
#
#
#  Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
#  Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [1, 10⁵].
#  0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in
# O(n) time and
# O(1) space?
#
#  Related Topics Linked List Two Pointers Stack Recursion 👍 10013 👎 609


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first, we find the node in middle
        # reverse list after middle
        node_cnt = 0
        p = head
        while p is not None:
            p = p.next
            node_cnt += 1

        if node_cnt == 1:
            return True

        mid = (node_cnt + 1) // 2
        p = head
        # prev = p
        for i in range(mid):
            # prev = p
            p = p.next

        next = p.next
        p.next = None
        while next is not None:
            nn = next.next
            next.next = p
            p = next
            next = nn

        p1, p2 = head, p
        while p1 is not None and p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

# leetcode submit region end(Prohibit modification and deletion)
