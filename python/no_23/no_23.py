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

