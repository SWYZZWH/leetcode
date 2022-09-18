# usually, we will consider use a heap
# for O(1) complexity, we have to maintain a linked list
# the list may work cause each function results in user counter changing by one
# there is a map: key -> Node
# for each node, we should maintain a list/set to maintain key with the same freq
# when tie, the behavior of LFU go back to LRU, thus, we can simply use a deque
# the least recent use key must be at the head of the deque
import collections


class Pair:

    def __init__(self, node, k=-1, v=-1, prev=None, nxt=None):
        self.node = node
        self.k = k
        self.v = v
        self.prev = prev
        self.nxt = nxt


# actually we can maintain a min_freq
# so we don't have to maintain a deque for pair
# a map key: freq, value: Pair will do
class Node:

    def __init__(self, no: int, prev=None, nxt=None):
        self.no = no
        self.head = Pair(self)
        self.tail = self.head
        self.prev = prev
        self.nxt = nxt


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0)
        self.m = collections.defaultdict(Pair)

    def __update(self, k: int, v: int):
        if k not in self.m:
            return

        p = self.m[k]
        node = p.node

        # remove pair from node
        prev_pair = p.prev
        nxt_pair = p.nxt
        prev_pair.nxt = nxt_pair
        if nxt_pair:
            nxt_pair.prev = prev_pair
        else:
            node.tail = prev_pair

        nxt_node = node.nxt
        if nxt_node is None or nxt_node.no != node.no + 1:
            nxt_node = Node(node.no + 1, node, node.nxt)
            if node.nxt:
                node.nxt.prev = nxt_node
            node.nxt = nxt_node

        new_pair = Pair(nxt_node, k, v)
        if nxt_node.head != nxt_node.tail:
            new_pair.prev = nxt_node.tail
            nxt_node.tail.nxt = new_pair
            nxt_node.tail = new_pair
        else:
            nxt_node.head.nxt = new_pair
            nxt_node.tail = new_pair
            new_pair.prev = nxt_node.head

        # remove node if neccessary
        if node.tail == node.head:
            node.prev.nxt = node.nxt
            if node.nxt:
                node.nxt.prev = node.prev
        self.m[k] = new_pair

    def __is_full(self) -> bool:
        return self.cap == len(self.m)

    def __insert(self, k: int, v: int):
        if k in self.m:
            return

        if self.__is_full():
            self.__pop()
            if self.__is_full():
                return

        node = self.head.nxt
        if self.head.nxt is None or self.head.nxt.no > 1:
            node = Node(1, self.head, self.head.nxt)
            if self.head.nxt:
                self.head.nxt.prev = node
            self.head.nxt = node

        new_pair = Pair(node, k, v)
        if node.head != node.tail:
            new_pair.prev = node.tail
            node.tail.nxt = new_pair
            node.tail = new_pair
        else:
            node.head.nxt = new_pair
            node.tail = new_pair
            new_pair.prev = node.head

        self.m[k] = new_pair

    def __pop(self):
        if len(self.m) < self.cap:
            return

        if len(self.m) == 0:
            return

        cur_node = self.head.nxt
        cur_pair = cur_node.head.nxt
        cur_node.head.nxt = cur_pair.nxt
        if cur_node.tail == cur_pair:
            cur_node.tail = cur_node.head
        if cur_pair.nxt:
            cur_pair.nxt.prev = cur_node.head
        self.m.pop(cur_pair.k)

        if cur_node.head == cur_node.tail:
            cur_node.prev.nxt = cur_node.nxt
            if cur_node.nxt:
                cur_node.nxt.prev = cur_node.prev

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        ret = self.m[key]
        self.__update(key, ret.v)
        return ret.v

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.__update(key, value)
        else:
            self.__insert(key, value)

    def __print(self):
        n = self.head.nxt
        while n:
            print("node no:", n.no)
            p = n.head.nxt
            while p:
                print(p.k, p.v)
                p = p.nxt
            print("tail", n.tail.k, n.tail.v)
            n = n.nxt

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
