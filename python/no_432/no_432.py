# 432. All O`one Data Structure

# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.
#
# Implement the AllOne class:
#
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity

from collections import deque


class AllOne:
    # hash map for search key in O(1)
    # cause value of key can only change by 1 each time
    # use dequeue to sort values
    # dequeue.head() always return maximum; dequeue.tail() always return minimum
    # when we inc some key, we find the key in dequeue and compare with the node before, if val + 1 < val_before,
    # insert a new node; else, move current node to before; modify the hashmap pointer; remove node if needed
    # always implement a double linked list, we can use sentinel to simplify code

    class Node:
        def __init__(self, next, before, val: int):
            self.next = next
            self.before = before
            self.val = val
            self.rev_idx = {}

        def add_new_key(self, key: str):
            self.rev_idx[key] = True

        def remove_key(self, key: str):
            self.rev_idx.pop(key)

        def get_random_key(self) -> str:
            k, v = self.rev_idx.popitem()
            self.add_new_key(k)
            return k

        def is_empty(self) -> bool:
            return len(self.rev_idx) == 0

        def insert_after(self, new_node):
            n = self.next
            new_node.before = self
            self.next = new_node
            new_node.next = n
            n.before = new_node

        def delete_self(self):
            b, n = self.before, self.next
            b.next = n
            n.before = b

    def __init__(self):
        self.head = self.Node(None, None, -1)  # sentinel
        self.end = self.Node(None, None, -1)  # sentinel
        self.head.next = self.end
        self.end.before = self.head
        self.d = {}

    def inc(self, key: str) -> None:
        if key not in self.d:
            if self.end.before.val != 1:
                new_node = self.Node(None, None, 1)
                new_node.add_new_key(key)
                self.end.before.insert_after(new_node)
                self.d[key] = new_node
            else:
                self.end.before.add_new_key(key)
                self.d[key] = self.end.before
        else:
            cur_node = self.d[key]
            cur_before = cur_node.before
            if cur_before.val != cur_node.val + 1:
                new_node = self.Node(None, None, cur_node.val + 1)
                new_node.add_new_key(key)
                cur_before.insert_after(new_node)
                self.d[key] = new_node
            else:
                cur_before.add_new_key(key)
                self.d[key] = cur_before
            cur_node.remove_key(key)
            if cur_node.is_empty():
                cur_node.delete_self()

    def dec(self, key: str) -> None:
        cur_node = self.d[key]
        next = cur_node.next
        if cur_node.val == 1:
            pass
        elif next.val != cur_node.val - 1:
            new_node = self.Node(None, None, cur_node.val - 1)
            new_node.add_new_key(key)
            cur_node.insert_after(new_node)
            self.d[key] = new_node
        else:
            next.add_new_key(key)
            self.d[key] = next
        cur_node.remove_key(key)
        if cur_node.is_empty():
            cur_node.delete_self()

    def getMaxKey(self) -> str:
        if self.head.next == self.end:
            return ""
        return self.head.next.get_random_key()

    def getMinKey(self) -> str:
        if self.head.next == self.end:
            return ""
        return self.end.before.get_random_key()

# if key not in self.d:
#     if self.end is None:
#         self.head = self.end = self.Node(None, None, 1, key)
#     else:
#         if self.end.val > 1:
#             new_node = self.Node(None, self.end, 1, key)
#             self.end.next = new_node
#             self.end = new_node
#         else:
#             self.end.add_new_key(key)
#     self.d[key] = self.end
# else:
#     cur_node = self.d[key]
#     if cur_node == self.head:
#         # update head
#         new_node = self.Node(None, None, cur_node.val + 1, key)
#         self.head.remove_key(key)
#         if self.head.is_empty():
#             # remove old head
#             if self.head == self.end:
#                 self.head = self.end = new_node
#             else:
#                 cur_next = self.head.next
#                 cur_next.before = new_node
#                 new_node.next = cur_next
#         self.head = new_node
#         self.d[key] = new_node
#     else:
#         p = cur_node.before
#         # may be remove tail
#         if p.val == cur_node.val + 1:

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
