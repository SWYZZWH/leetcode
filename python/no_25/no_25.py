# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        virtual_head = ListNode(-1, head)
        # find the length of the list firstly
        p = virtual_head
        l = -1
        while p:
            l += 1
            p = p.next

        times = l // k

        p, q = virtual_head, head
        for i in range(times):
            # q walks k steps
            # during the walk, we reverse the connections between neighbors
            last = p
            start = q
            for j in range(k):
                nxt = q.next
                if j != 0:
                    q.next = last
                last = q
                q = nxt
            start.next = q
            p.next = last
            p = start

        return virtual_head.next
