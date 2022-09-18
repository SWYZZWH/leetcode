# so delete any idx in an array can be implemented as O(1)
from random import random


class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.cur_len = 0
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.elements.append(val)
        self.index_map[val] = self.cur_len
        self.cur_len += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        idx = self.index_map[val]
        if idx != self.cur_len - 1:
            self.elements[-1], self.elements[idx] = self.elements[idx], self.elements[-1]
            self.index_map[self.elements[idx]] = idx
        self.index_map.pop(self.elements[-1])
        self.elements.pop()
        self.cur_len -= 1
        return True

    def getRandom(self) -> int:
        return self.elements[random.randint(0, self.cur_len - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()