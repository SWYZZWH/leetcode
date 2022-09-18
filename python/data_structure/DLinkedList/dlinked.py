class DLinkedNode:

    def __init__(self, val: int = 0, prev: "DLinkedNode" = None, nxt: "DLinkedNode" = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

    def __str__(self) -> str:
        return "val {}".format(self.val)


class DLinkedList:

    def __init__(self):
        self.head = DLinkedNode()
        self.tail = self.head

    def __len__(self) -> int:
        return 0

    def append(self, n: DLinkedNode):
        if n is None:
            return
        self.tail.nxt = n
        n.prev = self.tail
        self.tail = n

    def pop(self, n: DLinkedNode):
        prev = n.prev
        nxt = n.nxt
        prev.nxt = nxt
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev

    def popright(self):
        self.pop(self.tail)

    def popleft(self):
        n = self.head.nxt
        if not n:
            return
        self.pop(n)

    def __str__(self):
        cur = self.head.nxt
        i = 0
        ret = "List:\n"
        while cur is not None:
            ret += "\tnode {}: {}\n".format(i, cur)
            i += 1
            cur = cur.nxt

        return ret
