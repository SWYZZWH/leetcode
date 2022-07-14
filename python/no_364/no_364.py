# 364. Nested List Weight Sum II

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
#
# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.
#
# The weight of an integer is maxDepth - (the depth of the integer) + 1.
#
# Return the sum of each integer in nestedList multiplied by its weight.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import math
from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


# two pass dfs
# class Solution:
#     maxDepth = 0
#
#     # notice: [[]] depth is 1!
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         self.maxDepth = 1
#         ret = 0
#         infos = self.rec(nestedList, 1)
#         l = self.maxDepth
#         for info in infos:
#             ret += (self.maxDepth - info[1] + 1) * info[0]
#         return ret
#
#     def rec(self, nestedList: List[NestedInteger], curDepth: int) -> List:
#         lst = []
#         if nestedList is None or len(nestedList) == 0:
#             return lst
#         self.maxDepth = max(self.maxDepth, curDepth)
#         for node in nestedList:
#             if node.isInteger():
#                 lst.append([node.getInteger(), curDepth])
#             else:
#                 lst += self.rec(node.getList(), curDepth + 1)
#         return lst

# one pass solution
# math
# (maxDepth - (the depth of the integer) + 1) * value[i]
# (maxDepth + 1) * sum(value) - depth[i] * value[i]

class Solution:

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.maxDepth = 1
        self.curSum = 0
        self.depthSum = 0
        self.rec(nestedList, 1)
        return (self.maxDepth + 1) * self.curSum - self.depthSum

    def rec(self, nestedList: List[NestedInteger], curDepth: int):
        if nestedList is None or len(nestedList) == 0:
            return
        self.maxDepth = max(self.maxDepth, curDepth)
        for node in nestedList:
            if node.isInteger():
                self.depthSum += curDepth * node.getInteger()
                self.curSum += node.getInteger()
            else:
                self.rec(node.getList(), curDepth + 1)
