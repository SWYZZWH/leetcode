# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the last node
        if head is None:
            return head
        p = head
        pp = None
        l = 1
        while p.next:
            l += 1
            pp = p
            p = p.next

        if k % l == 0:
            return head
        k = l - k % l

        q = head
        while k - 1:
            k -= 1
            q = q.next

        ret = q.next
        q.next = None
        p.next = head

        return ret
