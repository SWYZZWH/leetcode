# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        if length == 1:
            return None
        mid = length // 2
        pre = None
        p = head
        while mid:
            pre = p
            p = p.next
            mid -= 1
        pre.next = p.next
        return head
