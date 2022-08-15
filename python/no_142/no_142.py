# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # classic problem
    # the math proof is kinda complicated
    # the conclusion is:
    # first we use quick&slow pointers
    # when they meet, we create a new slow pointer start from the head
    # when the new pointer meets the slow one, we find where the circle start
    # if any None pointer occurs in the whole procedure, we return None
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        quick, slow = head, head

        while quick is not None and quick.next is not None:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                break

        if quick is None or quick.next is None:
            return None
        p = head

        while slow is not None and p is not None and slow != p:
            p = p.next
            slow = slow.next

        if slow is None or p is None:
            return None

        return p
