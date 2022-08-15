# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1: get the length first, then two pointer, one is ahead of the other by len // 2
    # Solution 2: two pointers, quick and slow, quick move 2 steps each time
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        quick, slow = head, head

        while quick is not None and quick.next is not None:
            quick = quick.next.next
            slow = slow.next

        return slow
