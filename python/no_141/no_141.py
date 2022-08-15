# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # simple version of no_142
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        quick, slow = head, head
        while quick is not None and quick.next is not None:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                return True

        return False
