# Definition for singly-linked list.
from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # priority queue solution: O(nlogk), 0(k), we can maintain a heap with size k
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        h = []
        for i in range(k):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        ret = ListNode(-1, None)
        p = ret
        while h:
            e = heapq.heappop(h)
            new_node = ListNode(e[0], None)
            p.next = new_node
            p = p.next
            if lists[e[1]]:
                heapq.heappush(h, (lists[e[1]].val, e[1]))
                lists[e[1]] = lists[e[1]].next

        return ret.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # divide and conquer will reduce the
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not lists:
            return None

        def merge2Lists(l1: Optional[ListNode], l2: Optional[ListNode]):
            if not l2:
                return l1

            p1, p2 = ListNode(-1, l1), ListNode(-1, l2)
            cur1, cur2 = p1, p2
            while cur1.next and cur2.next:
                if cur1.next.val <= cur2.next.val:
                    cur1 = cur1.next
                    continue
                else:
                    tmp = cur2.next.next
                    cur2.next.next = cur1.next
                    cur1.next = cur2.next
                    cur2.next = tmp
                    cur1 = cur1.next

            if cur2.next:
                cur1.next = cur2.next

            return p1.next

        interval = 1
        while interval < n:
            i = 0
            while i < n:
                lists[i] = merge2Lists(lists[i], lists[i + interval] if i + interval < n else None)
                i += 2 * interval
            interval *= 2

        return lists[0]




