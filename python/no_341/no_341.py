# 341. Flatten Nested List Iterator

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
#
# Implement the NestedIterator class:
#
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:
#
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# from no_364.no_364 import NestedInteger
import collections


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    # the para of constructor should be NestedInteger... LOL
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.lst = nestedList
        self.stk = collections.deque()
        if len(nestedList) != 0:
            self.stk.append([nestedList[0], 0])
        self.next_next = self.find_next()

    def next(self) -> int:
        next = self.next_next
        self.next_next = self.find_next()
        return next

    def find_next(self) -> int:
        while True:
            res = -1_000_000_00
            while len(self.stk) != 0:
                node, idx = self.stk.pop()
                if node.isInteger():
                    return node.getInteger()
                if idx == len(node.getList()):
                    continue
                next_int = node.getList()[idx]
                self.stk.append([node, idx + 1])
                self.stk.append([next_int, 0])
            if res != -1_000_000_00:
                return res
            self.idx += 1
            if self.idx >= len(self.lst):
                break
            self.stk.append([self.lst[self.idx], 0])

        return -1_000_000_00

    def hasNext(self) -> bool:
        return self.next_next != -1_000_000_00
