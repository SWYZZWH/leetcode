import sortedcontainers


class ListNode:

    def __init__(self, val: int, prev: "ListNode" = None, next: "ListNode" = None):
        self.val = val
        self.prev = prev
        self.next = next


class MaxStack:

    def __init__(self):
        self.sd = sortedcontainers.SortedDict()
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        newNode = ListNode(x, None, None)
        prev = self.tail.prev
        prev.next = newNode
        newNode.prev = prev
        self.tail.prev = newNode
        newNode.next = self.tail
        if x not in self.sd:
            self.sd[x] = [newNode]
        else:
            self.sd[x].append(newNode)

    def pop(self) -> int:
        cur = self.tail.prev
        val = cur.val
        prev = cur.prev
        prev.next = self.tail
        self.tail.prev = prev

        if len(self.sd[val]) == 1:
            self.sd.pop(val)
        else:
            self.sd[val] = self.sd[val][:-1]

        return cur.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        return self.sd.keys()[-1]

    def popMax(self) -> int:
        val = self.sd.keys()[-1]
        node = self.sd[val][-1]

        if len(self.sd[val]) == 1:
            self.sd.pop(val)
        else:
            self.sd[val] = self.sd[val][:-1]

        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        return val

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()