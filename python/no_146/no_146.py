# hashmap + double linked list
class ListNode:

    def __init__(self, key: int, val: int, nxt: "ListNode", prev: "ListNode"):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}
        self.lst = ListNode(-1, - 1, None, None)  # virtual head
        self.tail = self.lst

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self.update(key, self.m[key].val)
        return self.m[key].val

    def is_full(self) -> bool:
        return self.cap == len(self.m)

    def evict(self):
        if self.cap == 0:
            return

        if not self.is_full():
            return

        nxt_nxt = self.lst.nxt.nxt
        to_remove = self.lst.nxt
        self.m.pop(to_remove.key)
        self.lst.nxt = nxt_nxt
        if nxt_nxt:
            nxt_nxt.prev = self.lst

        if to_remove == self.tail:
            self.tail = self.lst

    def update(self, key: int, val: int):
        if key not in self.m:
            return

        to_move = self.m[key]
        to_move.val = val
        prev = to_move.prev
        nxt = to_move.nxt
        if to_move == self.tail:
            return
        self.tail.nxt = to_move
        to_move.prev = self.tail
        self.tail = to_move
        prev.nxt = nxt
        if nxt:
            nxt.prev = prev

    def append(self, key: int, val: int):
        if key in self.m:
            return

        new_node = ListNode(key, val, None, None)
        self.m[key] = new_node

        self.tail.nxt = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.update(key, value)
        else:
            if self.is_full():
                self.evict()
            self.append(key, value)
        # print(self.m)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)